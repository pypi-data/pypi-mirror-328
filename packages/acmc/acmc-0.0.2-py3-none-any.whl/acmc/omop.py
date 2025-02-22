import os
import argparse
import sqlite3
import pandas as pd
import json
import logging
from pathlib import Path

from acmc import logging_config

# setup logging
logger = logging_config.setup_logger()

OMOP_DB_DIR = Path('./build/omop')
OMOP_DB_PATH = OMOP_DB_DIR / 'omop_54.sqlite'
VERSION_FILE = 'omop_version.json'
VERSION_PATH = OMOP_DB_DIR / VERSION_FILE

vocabularies = {
	"source": "OHDSI Athena", 
	"url": "https://athena.ohdsi.org/vocabulary/list",
	"version": "",
	"vocabularies": [
		{ "id": 1, "name": "SNOMED"},
		{ "id": 2, "name": "ICD9CM"},
		{ "id": 17, "name": "Readv2"},
		{ "id": 21, "name": "ATC"},
		{ "id": 55, "name": "OPCS4"},
		{ "id": 57, "name": "HES Specialty"},
		{ "id": 70, "name": "ICD10CM"},
		{ "id": 75, "name": "dm+d"},
		{ "id": 144, "name": "UK Biobank"},
		{ "id": 154, "name": "NHS Ethnic Category"},
		{ "id": 155, "name": "NHS Place of Service"}
	],
	"model": []
}

#Populate SQLite3 Database with default OMOP CONCEPTS 
def install (omop_install_folder, version, db_path=OMOP_DB_PATH):
	"""Installs the OMOP release csv files in a file-based sql database"""
	logger.info(f"Installing OMOP database from {omop_install_folder}")
	
	# check folder for omop install files is a directory
	omop_install_path = Path(omop_install_folder) 
	if not omop_install_path.is_dir():
		raise NotADirectoryError(f"Error: '{omop_install_path}' for OMOP installation files is not a directory")    
	
	# check codes directory exists and if not create it
	if not OMOP_DB_DIR.exists():  
		OMOP_DB_DIR.mkdir(parents=True)
		logger.debug(f"OMOP directory '{OMOP_DB_DIR}' created.")    

	# connect to database, if it does not exist it will be created
	conn = sqlite3.connect(OMOP_DB_PATH)    
	# Iterate through files in the folder
	for filename in os.listdir(omop_install_folder):
		if filename.endswith(".csv"):  # Check if the file is a CSV
			file_path = os.path.join(omop_install_folder, filename)
			try:
				logger.info(f"Reading table: {file_path}")
				# read the CSV file with the specified delimiter
				df = pd.read_csv(file_path, delimiter="\t", low_memory=False)
				table_name = os.path.splitext(os.path.basename(file_path))[0] #Get name of file
			
				# export Table to sqlite db
				df.to_sql(table_name, conn, if_exists='replace', index=False)
				
				# add to the metadata
				vocabularies["model"].append(filename)
			except Exception as e:
				raise Exception(f"Error reading file {file_path}: {e}")
	conn.close()

	# write version file
	write_version_file(version)

	logger.info(f"OMOP installation completed")

def write_version_file(version):
	"""Writes the OMOP vocaburaries and version to a file"""		
	vocabularies['version'] = version
	with open(VERSION_PATH, "w", encoding="utf-8") as f:
		json.dump(vocabularies, f, indent=4) 
		
def clear(db_path):
	"""Clears the OMOP sql database"""			
	logger.info(f"Clearing OMOP data from database")
	omop_db_path = Path(db_path)
	if not omop_db_path.is_file():  
		raise FileNotFoundError(f"Error: OMOP DB file '{omop_db_path}' does not exist.")
	conn = sqlite3.connect(db_path)
	cur = conn.cursor()
	cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
	
	# Fetch and print table names
	tables = cur.fetchall()
	logger.debug("Tables in database:", [table[0] for table in tables])

	#cur.execute("DROP TABLE CONCEPT_SET;")
	#cur.execute("DROP TABLE CONCEPT_SET_ITEM;")

	conn.close()
	logger.info(f"OMOP database cleared")
	
def delete(db_path):
	"""Deletes the OMOP sql database"""
	logger.info(f"Deleting OMOP database")
	omop_db_path = Path(db_path)
	if not omop_db_path.is_file():  
		raise FileNotFoundError(f"Error: OMOP DB file '{omop_db_path}' does not exist.")    
		
	omop_db_path.unlink()
	logger.info(f"OMOP database deleted")
	
def table_exists(cursor, table_name):
	# Query to check if the table exists
	cursor.execute(
		"""
		SELECT name
		FROM sqlite_master
		WHERE type='table' AND name=?
		""",
		(table_name,)
	)

	# Fetch the result
	result = cursor.fetchone()
	
	return result is not None

def vocab_exists(cursor, vocab_id):
	# Query to check if the table exists
	cursor.execute(
		"""
		SELECT vocabulary_id 
		FROM VOCABULARY
		WHERE vocabulary_id=?
		""",
		(vocab_id,)
	)
	
	# Fetch the result
	result = cursor.fetchone()
	
	return result is not None

def setup(db_path, vocab_id, vocab_version, vocab_name, vocab_reference):
    #Setup SQLite3 Database for OMOP    
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    #Check if DB populated with necessary VOCABULARY
    if not table_exists(cur, "VOCABULARY"):
        raise Exception(f"Error {db_path} is not yet populated with OMOP VOCABULARY. Please download from https://athena.ohdsi.org/.") 
    
    #Check if Vocabulary already exists 
    elif not omop_vocab_exists(cur, vocab_id):
        #Create VOCABULARY
        df_test = pd.DataFrame([{
            "vocabulary_id": vocab_id,
            "vocabulary_name": vocab_name,
            "vocabulary_reference": vocab_reference,
            "vocabulary_version": vocab_version,
            # "vocabulary_concept_id": 0,
        }])
        df_test.to_sql("VOCABULARY", conn, if_exists='append', index=False)
    
    #Check if CONCEPT_SET table exists
    if not table_exists(cur, "CONCEPT_SET"):
        cur.execute("""
        CREATE TABLE CONCEPT_SET (
            concept_set_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each concept set
            atlas_id INTEGER,                                -- Unique identifier generated by ATLAS
            concept_set_name TEXT,                           -- Optional name for the concept set
            concept_set_description TEXT,                    -- Optional description for the concept set
            vocabulary_id TEXT NOT NULL,                     -- Foreign key to VOCABULARY table
            FOREIGN KEY (vocabulary_id) REFERENCES VOCABULARY(vocabulary_id)
        );""")
    
    #Check if CONCEPT_SET_ITEM table exists
    if not table_exists(cur, "CONCEPT_SET_ITEM"):
        cur.execute("""
        CREATE TABLE CONCEPT_SET_ITEM (
            concept_set_item_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each mapping
            concept_set_id INTEGER NOT NULL,                      -- Foreign key to CONCEPT_SET table
            concept_id INTEGER NOT NULL,                          -- Foreign key to CONCEPT table
            FOREIGN KEY (concept_set_id) REFERENCES CONCEPT_SET(concept_set_id),
            FOREIGN KEY (concept_id) REFERENCES CONCEPT(concept_id)
        );""")

    conn.close()

def publish_concept_sets(out, db_path, vocab_output, vocab_type, output_version):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    for concept_set_name, grp in out.groupby("CONCEPT_SET"):		
        #Create Concept_Set
        if not sql_row_exist(conn, "CONCEPT_SET", "concept_set_name", concept_set_name):
            cur.execute(f"INSERT INTO CONCEPT_SET (concept_set_name, vocabulary_id) VALUES ('{concept_set_name}', 'MELDB');")
        else:
            logger.debug("concept_set", concept_set_name, "already exists")
            #TODO: ask to remove old concept_set?
        
        #Get Concept_set_Id
        query = "SELECT concept_set_id FROM CONCEPT_SET WHERE concept_set_name = ? AND vocabulary_id = ?;"
        cur.execute(query, (concept_set_name, vocab_output, ))    
        concept_set_id = cur.fetchone()[0]
        
        #Get corresponing Concept_id (OMOP) for each Concept_code (e.g. SNOMED)
        concept_codes = "'"+"', '".join(list(grp["CONCEPT"].astype(str)))+"'"
        query = f"SELECT concept_id FROM CONCEPT WHERE vocabulary_id = ? AND concept_code IN ({concept_codes});"
        cur.execute(query, (vocab_type, ))
        df_out = pd.DataFrame(cur.fetchall(), columns=["concept_id"])
        
        if not len(grp) == len(df_out):
            logger.error("ERROR: Some", vocab_type, "Codes do not exist in OMOP Database")
        
        #Create Concept_set_item
        df_out["concept_set_id"] = concept_set_id
        df_out.to_sql("CONCEPT_SET_ITEM", conn, if_exists='append', index=False)

    conn.close()
