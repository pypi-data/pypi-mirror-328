import argparse
import pandas as pd
import numpy as np
import json
import os
import sqlite3
import sys
import shutil
import git
import re
import logging
import requests
from pathlib import Path
from urllib.parse import urlparse, urlunparse

from acmc import trud, omop, parse

# setup logging
import acmc.logging_config as lc
logger = lc.setup_logger()

pd.set_option("mode.chained_assignment", None)

PHEN_DIR = 'phen'
DEFAULT_PHEN_PATH = Path('build') / PHEN_DIR

CODES_DIR = 'codes'
MAP_DIR = 'map'
CONCEPT_SET_DIR = 'concept-set'
DEFAULT_PHEN_DIR_LIST = [CODES_DIR, MAP_DIR, CONCEPT_SET_DIR]

CONFIG_FILE = 'config.json'
REPORT_FILE = 'report.md'

DEFAULT_GIT_BRANCH = 'main'

SPLIT_COL_ACTION = "split_col"
CODES_COL_ACTION = "codes_col"
DIVIDE_COL_ACTION = "divide_col"
COL_ACTIONS = [SPLIT_COL_ACTION, CODES_COL_ACTION, DIVIDE_COL_ACTION]

class PhenValidationException(Exception):
	"""Custom exception class raised when validation errors in phenotype configuration file"""		
	def __init__(self, message, validation_errors=None):
		super().__init__(message)
		self.validation_errors = validation_errors

def construct_git_url(remote_url):
	"""Constructs a git url for github or gitlab including a PAT token environment variable"""			
	# check the url
	parsed_url = urlparse(remote_url)

	# if github in the URL otherwise assume it's gitlab, if we want to use others such as codeberg we'd
	# need to update this function if the URL scheme is different.
	if "github.com" in parsed_url.netloc:
		# get GitHub PAT from environment variable
		auth = os.getenv("ACMC_GITHUB_PAT")
		if not auth:
			raise ValueError("GitHub PAT not found. Set the ACMC_GITHUB_PAT environment variable.")			
	else:
		# get GitLab PAT from environment variable
		auth = os.getenv("ACMC_GITLAB_PAT")
		if not auth:
			raise ValueError("GitLab PAT not found. Set the ACMC_GITLAB_PAT environment variable.")				
		auth = f"oauth2:{auth}"
	
	# Construct the new URL with credentials
	new_netloc = f"{auth}@{parsed_url.netloc}"
	return urlunparse((parsed_url.scheme, new_netloc, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))

def create_empty_git_dir(path):
	"""Creates a directory with a .gitkeep file so that it's tracked in git"""		
	path.mkdir(exist_ok=True)
	keep_path = path / '.gitkeep'
	keep_path.touch(exist_ok=True)

def init(phen_dir, remote_url):
	"""Initial phenotype directory as git repo with standard structure"""	
	logger.info(f"Initialising Phenotype in directory: {phen_dir}")
	phen_path = Path(phen_dir)

	# check if directory already exists and ask user if they want to recreate it
	configure = False
	if phen_path.exists() and phen_path.is_dir():  # Check if it exists and is a directory
		user_input = input(f"The phen directory '{phen_path}' already exists. Do you want to reinitialise? (yes/no): ").strip().lower()
		if user_input in ['yes', 'y']:
			shutil.rmtree(phen_path)  
			configure = True;
		else:
			logger.info("Phen directory was not recreated.")
	else:
		configure=True

	if not configure:
		logger.info(f"Exiting, phenotype not initiatised")
		return

	# Initialise repo from local or remote
	repo = None
	# if remote then clone the repo otherwise init a local repo	
	if remote_url != None:
		# add PAT token to the URL
		git_url = construct_git_url(remote_url)

		# clone the repo
		repo = git.cmd.Git()
		repo.clone(git_url, phen_path)	
		# open repo
		repo = git.Repo(phen_path)
		
		# check if there are any commits (new repo has no commits)
		if len(repo.branches) == 0 or repo.head.is_detached:  # Handle detached HEAD (e.g., after init)
			logger.debug("The phen repository has no commits yet.")
			commit_count = 0
		else:
			# Get the total number of commits in the default branch
			commit_count = sum(1 for _ in repo.iter_commits())
			logger.debug(f"Repo has previous commits: {commit_count}")
	else:
		# local repo, create the directories and init
		phen_path.mkdir(parents=True, exist_ok=True) 
		logger.debug(f"Phen directory '{phen_path}' has been created.")
		repo = git.Repo.init(phen_path)
		commit_count = 0

	# initialise empty repos
	if commit_count == 0:
		# create initial commit
		initial_file_path = phen_path / "README.md"
		with open(initial_file_path, "w") as file:
			file.write("# Initial commit\nThis is the first commit in the phen repository.\n")
		repo.index.add([initial_file_path])
		repo.index.commit("Initial commit")
		commit_count = 1

	# Checkout the phens default branch, creating it if it does not exist
	if DEFAULT_GIT_BRANCH in repo.branches:
		main_branch = repo.heads[DEFAULT_GIT_BRANCH]
		main_branch.checkout()
	else:
		main_branch = repo.create_head(DEFAULT_GIT_BRANCH)
		main_branch.checkout()
		
	# if the phen path does not contain the config file then initialise the phen type
	config_path = phen_path / CONFIG_FILE
	if config_path.exists():
		logger.debug(f"Phenotype configuration files already exist")		
		return
		
	logger.info("Creating phen directory structure and config files")
	for d in DEFAULT_PHEN_DIR_LIST:
		create_empty_git_dir(phen_path / d)
	
	# set initial version based on the number of commits in the repo, depending on how the repo was created
	# e.g., with a README.md, then there will be some initial commits before the phen config is added
	next_commit_count =  commit_count + 1
	initial_version = f"v1.0.{next_commit_count}"			
	
	# create empty phen config file
	config = {
		"concept_sets": {
			"version": initial_version,
			"omop": {
				"vocabulary_id": "",
				"vocabulary_name": "",
				"vocabulary_reference": ""
			},
			"concept_set": [
			]
		},
		"codes": [
		]
	}
	config_path = phen_path / CONFIG_FILE
	with open(config_path, "w", encoding="utf-8") as f:
		json.dump(config, f, indent=4) 
		
	# add to git repo and commit
	for d in DEFAULT_PHEN_DIR_LIST:
		repo.git.add(phen_path / d)			
	repo.git.add(all=True)		
	repo.index.commit("initialised the phen git repo.")			
		
	logger.info(f"Phenotype initialised successfully")
	
def validate(phen_dir):
	"""Validates the phenotype directory is a git repo with standard structure"""		
	logger.info(f"Validating phenotype: {phen_dir}")
	phen_path = Path(phen_dir)
	if not phen_path.is_dir():
		raise NotADirectoryError(f"Error: '{phen_path}' is not a directory") 
	
	config_path = phen_path / CONFIG_FILE
	if not config_path.is_file():
		raise FileNotFoundError(f"Error: phen configuration file '{config_path}' does not exist.")    	
	
	codes_path = phen_path / CODES_DIR
	if not codes_path.is_dir():  
		raise FileNotFoundError(f"Error: source codes directory {source_codes_dir} does not exist.")
	
	# Calidate the directory is a git repo
	try:
		git.Repo(phen_path)
	except (git.exc.InvalidGitRepositoryError, git.exc.NoSuchPathError):
		raise Exception(f"Phen directory {phen_path} is not a git repo")

	# Load configuration File
	if config_path.suffix == ".json":
		mapping = json.load(open(config_path, "rb"))
	else:
		raise Exception(f"Unsupported configuration filetype: {str(config_path.resolve())}")

	# initiatise 
	validation_errors = []
	concept_sets = mapping["concept_sets"]
	concept_codes = mapping["codes"]
	code_types = parse.CodeTypeParser().code_types
	
    # check the version number is of the format vn.n.n
	match = re.match(r"v(\d+\.\d+\.\d+)", concept_sets['version'])
	if not match:
		validation_errors.append(f"Invalid version format in configuration file: {concept_sets['version']}")

	# create a list of all the concept set names defined in the concept set configuration
	concept_set_names = []	
	for item in concept_sets['concept_set']:
		if item['concept_set_name'] in concept_set_names:
			validation_errors.append(f"Duplicate concept set defined in concept sets {item['concept_set_name'] }")
		else:
			concept_set_names.append(item['concept_set_name'])

	# check codes definition
	concept_set_mapping_names = []
	for item in concept_codes:
		
		required_keys = {"folder", "files"}
		if required_keys.issubset(item.keys()):		
			# check concept codes path is a directory
			concept_code_dir_path = codes_path / item['folder']
			if not concept_code_dir_path.is_dir():
				validation_errors.append(f"Folder directory {str(concept_code_dir_path.resolve())} is not a directory")
				
			for file in item["files"]:			
				# check concepte code file exists
				concept_code_file_path = concept_code_dir_path / file['file']
				if not concept_code_file_path.exists():
					validation_errors.append(f"Coding file {str(concept_code_file_path.resolve())} does not exist")
					
				# check concepte code file is not empty
				concept_code_file_path = concept_code_dir_path / file['file']
				if concept_code_file_path.stat().st_size == 0:
						validation_errors.append(f"Coding file {str(concept_code_file_path.resolve())} is an empty file")

				# check columns section exists
				if "columns" not in file:
						validation_errors.append(f"Columns not defined for {concept_code_file_path}")
					
				# check columns specified are a supported medical coding type
				for column in file['columns']:
					if column not in code_types and column != 'metadata':
						validation_errors.append(f"Column type {column} for file {concept_code_file_path} is not supported")
	
				# check the actions are supported
				if 'actions' in file:
					for action in file['actions']:
						if action not in COL_ACTIONS:
							validation_errors.append(f"Action {action} is not supported")
	
				# check concept_set defined for the mapping
				for concept_set_mapping in file['concept_set']:
					# store the concept set names found for later set operations
					if concept_set_mapping not in concept_set_mapping_names:
						concept_set_mapping_names.append(concept_set_mapping)
		else:
			validation_errors.append(f"Missing required elements {required_keys} in codes {item}")
	# create sets to perform set operations on the lists of concept set names
	concept_set_names_set = set(concept_set_names)
	concept_set_mapping_names_set = set(concept_set_mapping_names)

	# check all concept sets in the summary section have at least one code mapping 
	concept_set_no_codes = list(concept_set_names_set - concept_set_mapping_names_set)
	if len(concept_set_no_codes) > 0:
		validation_errors.append(f"Concept sets do not exist in codes {concept_set_no_codes}")
	
	# check all concept sets included in the code mapping are defined in the summary concept_set section
	codes_no_concept_set = list(concept_set_mapping_names_set - concept_set_names_set)
	if len(codes_no_concept_set) > 0:
		validation_errors.append(f"Concept sets mapped in codes do not exist in the concept sets: {codes_no_concept_set}")
		
	if len(validation_errors) > 0:
		logger.error(validation_errors)
		raise PhenValidationException(f"Configuration file {str(config_path.resolve())} failed validation",
									  validation_errors)

	logger.info(f"Phenotype validated successfully")

def read_table_file(path, excel_sheet=None):
    """
    Load Code List File
    """
    if path.suffix == ".csv":
        df = pd.read_csv(path, dtype=str)
    elif path.suffix == ".xlsx":
        if excel_sheet:
            df = pd.read_excel(path, sheet_name=excel_sheet, dtype=str)
        else:
            df = pd.read_excel(path, dtype=str)
    elif path.suffix == ".dta":
        df = pd.read_stata(path, dtype=str)
    else:
        raise Exception(f"Unsupported filetype provided for source file {path.suffix}")
		
    return df

def process_actions(df, file):
	# Perform Structural Changes to file before preprocessing
	logger.debug("Processing file structural actions")
	if ("actions" in file and "split_col" in file["actions"] and "codes_col" in file["actions"]):
		split_col = file["actions"]["split_col"]
		codes_col = file["actions"]["codes_col"]
		logger.debug("Action: Splitting", split_col, "column into:", df[split_col].unique(),)
		codes = df[codes_col]
		oh = pd.get_dummies(df[split_col], dtype=bool)  # one hot encode
		oh = oh.where((oh != True), codes, axis=0)  # fill in 1s with codes
		oh[oh == False] = np.nan  # replace 0s with None
		df = pd.concat([df, oh], axis=1)  # merge in new columns

	return df

# Perform QA Checks on columns individually and append to df
def preprocess_codes(df, file, target_code_type=None, codes_file=None):
	""" Parses each column individually - Order and length will not be preserved! """
	out = pd.DataFrame([])  # create output df to append to
	code_errors = [] # list of errors from processing

	meta_columns = []  # meta columns to keep with codes
	if "actions" in file and "divide_col" in file["actions"]:
		meta_columns += [file["actions"]["divide_col"]]
	# TODO: enable metacolumns to be outputted - problem with map_file appending
	if "metadata" in file["columns"]:
		meta_columns += file["columns"]["metadata"]

	metadata_df = df[meta_columns]
	
	# Preprocess codes
	code_types = parse.CodeTypeParser().code_types
	for code_type_name, code_type_parser in code_types.items():
		if code_type_name in file['columns']:
			logger.info(f"Processing {code_type_name} codes...")
			
			# get code types
			codes = df[file['columns'][code_type_name]].dropna()
			codes = codes.astype(str)  # convert to string
			codes = codes.str.strip()  # remove excess spaces	

			# process codes, validating them using parser and returning the errors
			codes, errors = code_type_parser.process(codes, codes_file)  
			if len(errors) > 0:
				code_errors.extend(errors)
				logger.warning(f"Codes validation failed with {len(errors)} errors")
				
			# add metadata columns
			out = pd.concat([out, pd.DataFrame({code_type_name: codes}).join(metadata_df)], ignore_index=True)
				
	return out, meta_columns, code_errors

# Translate Df with multiple codes into single code type Series
def translate_codes(df, target_code_type):
	codes = pd.Series([], dtype=str)

	# Convert codes to target type
	logger.info(f"Converting to target code type {target_code_type}")
	for col_name in df.columns:
		# if target code type is the same as thet source code type, no translation, just appending source as target
		if col_name == target_code_type:
			logger.debug(f"Target code type {target_code_type} has source code types {len(df)}, copying rather than translating")
			codes = pd.concat([codes, df[target_code_type]])
		else:
			filename = f"{col_name}_to_{target_code_type}.parquet"
			map_path = trud.TRUD_PROCESSED_DIR / filename
			if map_path.exists():
				col = df[col_name]
				df_map = pd.read_parquet(map_path)
				# merge on corresponding codes and take target column
				translated = pd.merge(col, df_map, how="left")[target_code_type]  
				# TODO: BUG mask does not match column
				codes = pd.concat([codes, translated])  # merge to output
			else:
				logger.warning(f"No mapping from {col_name} to {target_code_type}, file {str(map_path.resolve())} does not exist")
			
	return codes

# Append file's codes to output Df with concept
def map_file(df, target_code_type, out, concepts, meta_columns=[]):
	# seperate out meta_columns
	metadata_df = df[meta_columns]
	df = df.drop(columns=meta_columns)

	# translate codes
	codes = translate_codes(df, target_code_type)
	codes = codes.dropna()  # delete NaNs
	
	# Append to output if translated 
	if len(codes) > 0:
		codes = pd.DataFrame({"CONCEPT": codes})
		codes = codes.join(metadata_df)
		for concept in concepts:
			codes["CONCEPT_SET"] = np.repeat(concept.strip(), len(codes))
			out = pd.concat([out, codes])
	else:
		logger.debug(f"No codes converted with target code type {target_code_type}")
	
	return out

def sql_row_exist(conn, table, column, value):
    # Execute and check if a result exists
    cur = conn.cursor()
    query = f"SELECT 1 FROM {table} WHERE {column} = ? LIMIT 1;"
    cur.execute(query, (value,))
    exists = cur.fetchone() is not None

    return exists

def write_code_errors(code_errors, code_errors_path):
	err_df = pd.DataFrame([
		{"CONCEPT": ", ".join(err.codes[~err.mask].tolist()),
		 "VOCABULARY": err.code_type,
		 "SOURCE": err.codes_file,
		 "CAUSE": err.message} for err in code_errors])

	err_df = err_df.drop_duplicates()  # Remove Duplicates from Error file
	err_df = err_df.sort_values(by=["SOURCE", "VOCABULARY", "CONCEPT"])	
	err_df.to_csv(code_errors_path, index=False, mode="w")

def map(phen_dir, target_code_type):
	logger.info(f"Processing phenotype: {phen_dir}")
	logger.debug(f"Target coding format: {target_code_type}")	

	# Validate configuration
	validate(phen_dir)

	# initialise paths
	phen_path = Path(phen_dir)
	config_path = phen_path / CONFIG_FILE	
	codes_path = phen_path / CODES_DIR

	# load configuration
	config = json.load(open(config_path, "rb"))
	concept_sets = config["concept_sets"]
	codes = config["codes"]

	# Create output dataframe
	out = pd.DataFrame([]) 
	code_errors = []

	# Process each folder in codes section
	for folder in codes:
		for file in folder["files"]:
			logger.debug(f"--- {file['file']} ---")
			codes_file_path = codes_path / folder["folder"] / file["file"]

			# Load Code File
			if "excel_sheet" in file:
				df = read_table_file(path=codes_file_path, excel_sheet=file["excel_sheet"])
			else:
				df = read_table_file(path=codes_file_path)

			# process structural actions
			df = process_actions(df, file)

			# Preprocessing & Validation Checks		
			logger.debug("Processing and validating code formats")
			df, meta_columns, errors = preprocess_codes(
				df, 
				file, codes_file=str(codes_file_path.resolve()),
				target_code_type=target_code_type)

			logger.debug(f" Length of errors from preprocess {len(errors)}")
			if len(errors) > 0:
				code_errors.extend(errors)
			logger.debug(f" Length of code_errors {len(code_errors)}")

			# partition table by categorical column				
			if ("actions" in file and "divide_col" in file["actions"] and len(df) > 0):
				divide_col = file["actions"]["divide_col"]
				logger.debug("Action: Dividing Table by", divide_col, "column into: ", df[divide_col].unique(),)
				df = df.groupby(divide_col)			
			
			# Map to Concept/Phenotype	
			if len(df.index) != 0:			
				if ("concept_set" in file) and isinstance(df, pd.core.frame.DataFrame):					
					out = map_file(
						df,
						target_code_type,
						out,
						concepts=file["concept_set"],
						meta_columns=meta_columns)
				elif ("concept_set_categories" in file) and isinstance(df, pd.core.groupby.generic.DataFrameGroupBy):
					meta_columns.remove(divide_col)  # delete categorical column
					for cat, grp in df:
						if (cat in file["concept_set_categories"].keys()):  # check if category is mapped
							grp = grp.drop(columns=[divide_col])  # delete categorical column
							logger.debug("Category:", cat)
							out = map_file(
								grp,
								target_code_type,
								out,
								concepts=file["concept_set_categories"][cat],
								meta_columns=meta_columns,)
				else:
					raise AttributeError(f"File {file} has either no concept_set or conceot_set_categories or the instance of dataframe objectives associated is incorrect, concept_set must be a DataFrame, conceot_set_categories must be pd.core.groupby.generic.DataFrameGroupBy")
			else:
				logger.warning(f"File {file} has no output after preprocessing in config {str(config_path.resolve())}")

	if(len(code_errors) > 0):
		logger.error(f"The map processing has {len(code_errors)} errors")		
		error_filename = f"{target_code_type}-code-errors.csv"
		write_code_errors(code_errors, phen_path / MAP_DIR / error_filename)
	
	# Check there is output from processing
	if len(out.index) == 0:
		logger.error(f"No output after map processing")		
		raise Exception(f"No output after map processing, check config {str(config_path.resolve())}")

	# Final processing
	out = out.reset_index(drop=True)
	out = out.drop_duplicates(subset=["CONCEPT_SET", "CONCEPT"])
	out = out.sort_values(by=["CONCEPT_SET", "CONCEPT"])

	# Add concept set definition metadata
	concept_sets_df = pd.DataFrame(concept_sets["concept_set"])  # transform to dataframe
	if "metadata" in concept_sets_df.columns:
		concept_sets_df = concept_sets_df.join(pd.json_normalize(concept_sets_df["metadata"]))  # metadata to columns
		concept_sets_df = concept_sets_df.drop(columns=["metadata"])
	concept_sets_df = concept_sets_df.rename(columns={"concept_set_name": "CONCEPT_SET"})
	concept_sets_df = concept_sets_df.drop_duplicates()  # remove duplicates
	out = out.merge(concept_sets_df, how="left", on="CONCEPT_SET")  # merge with output

	# Save output to map directory
	output_filename = target_code_type + '.csv'
	map_path = phen_path / MAP_DIR / output_filename
	out.to_csv(map_path, index=False)
	logger.info(f"Saved mapped concepts to {str(map_path.resolve())}")	

	# save concept sets as separate files
	concept_set_path = phen_path / CONCEPT_SET_DIR / target_code_type
	
	# empty the concept-set directory if it exists but keep the .git file
	git_items = ['.git', '.gitkeep']
	if concept_set_path.exists():
		for item in concept_set_path.iterdir():
			if item not in git_items:
				item.unlink()
	else:
		concept_set_path.mkdir(parents=True, exist_ok=True)

	# write each concept as a separate file
	for name, concept in out.groupby("CONCEPT_SET"):
		concept = concept.sort_values(by="CONCEPT") #sort rows
		concept = concept.dropna(how='all', axis=1)  #remove empty cols
		concept = concept.reindex(sorted(concept.columns), axis=1) #sort cols alphabetically
		filename = f"{name}.csv"
		concept_path = concept_set_path / filename
		concept.to_csv(concept_path, index=False )

	# copy version files used for mapping to repo
	shutil.copy(trud.VERSION_PATH, phen_path / trud.VERSION_FILE)
	shutil.copy(omop.VERSION_PATH, phen_path / omop.VERSION_FILE)
	
	logger.info(f"Phenotype processed successfully")

def publish(phen_dir):
	"""Publishes updates to the phenotype by commiting all changes to the repo directory"""		
	
	# Validate config
	validate(phen_dir)
	phen_path = Path(phen_dir)

	# load git repo and set the branch
	repo = git.Repo(phen_path)
	if DEFAULT_GIT_BRANCH in repo.branches:
		main_branch = repo.heads[DEFAULT_GIT_BRANCH]
		main_branch.checkout()
	else:
		raise AttributeError(f"Phen repo does not contain the default branch {DEFAULT_GIT_BRANCH}")	

	# check if any changes to publish
	if not repo.is_dirty() and not repo.untracked_files:
		logger.info("Nothing to publish, no changes to the repo")
		return
	 
	# get major version from configuration file
	config_path = phen_path / CONFIG_FILE
	config = json.load(open(config_path, "rb"))
	match = re.match(r"v(\d+\.\d+)", config['concept_sets']['version'])
	major_version = match.group(1)
	
	# get latest minor version from git commit count
	commit_count = len(list(repo.iter_commits("HEAD")))

	# set version and write to config file so consistent with repo version
	next_minor_version = commit_count + 1
	version = f"v{major_version}.{next_minor_version}"
	logger.info(f"New version: {version}")
	config['concept_sets']['version'] = version
	with open(config_path, "w", encoding="utf-8") as f:
		json.dump(config, f, indent=4)  	
		
	# Add and commit changes to repo
	commit_message = f"Committing updates to phenotype {phen_path}"
	repo.git.add('--all')
	repo.index.commit(commit_message)

	# Create and push the tag
	if version in repo.tags:
		raise Exception (f"Tag {version} already exists in repo {phen_path}")	
	repo.create_tag(version, message=f"Release {version}")
	logger.info(f"Created tag: {version}")

	# push to origin if a remote repo
	try:
		origin = repo.remotes.origin
		origin.push('main')
		origin.push(tags=True)
		logger.debug("Changes pushed to 'origin'.")
	except AttributeError:
		logger.debug("No remote named 'origin' found, local repo.")

	logger.info(f"Phenotype published successfully")

def copy(phen_dir, target_dir, version=None):
	"""Copys a phen repo at a specific tagged version into a target directory"""	

	# Validate
	validate(phen_dir)
	phen_path = Path(phen_dir)
	
	# Check target directory exists
	target_path = Path(target_dir)
	if not target_path.exists():
		raise FileNotFoundError(f"The target directory {target_path} does not exist")

	# Set copy directory
	if version:
		copy_path = target_path / version
	else:
		copy_path = target_path / 'latest'

	logger.info(f"Copying repo {phen_path} to {copy_path}")
	
	if not copy_path.exists():
		# If copy directory doesn't exist, clone the repo
		logger.debug(f"Cloning repo from {phen_path} into {copy_path}...")
		repo = git.Repo.clone_from(phen_path, copy_path)
	else:
		# If copy directory exists, open the repo
		logger.debug(f"Copy of repository already exists in {copy_path}. Opening the repo...")
		repo = git.Repo(copy_path)
	# Check out the latest commit or specified version
	if version:
		# Checkout a specific version (e.g., branch, tag, or commit hash)
		logger.info(f"Checking out version {version}...")
		repo.git.checkout(version)
	else:
		# Checkout the latest commit (HEAD)
		logger.info(f"Checking out the latest commit...")
		repo.git.checkout("HEAD")
	
	logger.debug(f"Copied {phen_path} {repo.head.commit.hexsha[:7]} in {copy_path}")

	logger.info(f"Phenotype copied successfully")

def diff(phen_dir, phen_old_dir):
	"""Compare the differences between two versions of a phenotype"""	
	
	# validate phenotype directories
	validate(phen_old_dir)	
	validate(phen_dir)

	old_phen_path = Path(phen_old_dir)	
	new_phen_path = Path(phen_dir)
	
	# Load report (FOR SOME REASON THIS WAS APPEND SO SET TO w for NOW)
	report_path = new_phen_path / REPORT_FILE
	if report_path.suffix == ".md":
		report = open(report_path, 'w')
		logger.debug(f"Writing to report file {str(report_path.resolve())}")
	else:
		raise ValueError(f"Unsupported filetype provided for report file {str(report_path.resolve())}")

	# Get maps files from phenotype 
	old_map_path = old_phen_path / MAP_DIR
	new_map_path = new_phen_path / MAP_DIR

	# List files from output directories
	old_output_files = [file.name for file in old_map_path.iterdir() if file.is_file() and not file.name.startswith('.')]
	new_output_files = [file.name for file in new_map_path.iterdir() if file.is_file() and not file.name.startswith('.')]

	# Convert the lists to sets for easy comparison
	old_output_set = set(old_output_files)
	new_output_set = set(new_output_files)
	
	# Outputs that are in old_output_set but not in new_output_set (removed files)
	removed_outputs = old_output_set - new_output_set
	# Outputs that are in new_output_set but not in old_output_set (added files)
	added_outputs = new_output_set - old_output_set
	# Outputs that are the intersection of old_output_set and new_output_set 
	common_outputs = old_output_set & new_output_set  
	
	# Write outputs report
	new_config_path = new_phen_path / CONFIG_FILE
	new_config = json.load(open(new_config_path, "rb"))
	report.write(f"\n\n# Report for version {new_config['concept_sets']['version']}\n\n")	
	report.write(f"- Removed outputs: {list(removed_outputs)}\n")
	report.write(f"- Added outputs: {list(added_outputs)}\n")
	report.write(f"- Common outputs: {list(common_outputs)}\n")

	report.write(f"\n\n## Compare concepts {str(old_phen_path.resolve())} to {str(new_phen_path.resolve())}\n\n")
	# Compare common outputs between versions
	for file in common_outputs:
		old_output = old_map_path / file
		new_output = new_map_path / file
		
		df1 = pd.read_csv(old_output)
		df1 = df1[["CONCEPT","CONCEPT_SET"]].groupby("CONCEPT_SET").count()
		df2 = pd.read_csv(new_output)
		df2 = df2[["CONCEPT","CONCEPT_SET"]].groupby("CONCEPT_SET").count()

		# Check for added and removed concepts
		report.write("- Removed concepts {}\n".format(list(set(df1.index) - set(df2.index))))
		report.write("- Added concepts {}\n".format(list(set(df2.index) - set(df1.index))))

		# Check for changed concepts 
		diff = df2 - df1 #diff in counts 
		diff = diff[(~(diff["CONCEPT"] == 0.0)) & diff["CONCEPT"].notna()] #get non-zero counts
		s = "\n"
		if len(diff.index) > 0:
			for concept, row in diff.iterrows():
				s += "\t - {} {}\n".format(concept, row["CONCEPT"])
			report.write(f"- Changed concepts {s}\n\n")
		else:
			report.write(f"- Changed concepts []\n\n")

	logger.info(f"Phenotypes diff'd successfully")

# Here's the atlas code that needs to go into anotehr function
#	if output_path == "atlas":
#		vocab_id = summary_config["omop"]["vocabulary_id"]
#		vocab_version = summary_config["version"]
#		vocab_name = summary_config["omop"]["vocabulary_name"]
#		vocab_reference = summary_config["omop"]["vocabulary_reference"]

		# Create New OMOP Vocabulary
#		omop_setup(OMOP_DB_PATH, vocab_id, vocab_version, vocab_name, vo#cab_reference)

		# Export to DB
#		omop_publish_concept_sets(out, 
#								  OMOP_DB_PATH,
#								  vocab_id,
#								  omop_vocab_types[target_code_type],
#								  vocab_version,)