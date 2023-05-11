import os
import requests, zipfile, io
import sqlite3
import pandas as pd
import seqlog
import logging

# Create connection to seqlog and logger_name
seqlog.log_to_seq(
    server_url="http://localhost:5341/",
    level=logging.INFO,
    batch_size=1,
    auto_flush_timeout=1,  # seconds
    override_root_logger=True
)

logger = logging.getLogger(__name__)

# Create path for data file, load and create data file if not exist
if not os.path.exists('../Data'):
    os.mkdir('../Data')

# Download data if it is unavailable and store as zip file
if 'e_com_behaviour_data.zip' not in os.listdir('../Data'):
    logger.info('Dataset loading.')
    url = r"https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store/download" \
          "?datasetVersionNumber=8"
    output = r'../Data/e_com_behaviour_data.zip'
    r = requests.get(url, allow_redirects=True)
    with open(output, 'wb') as f:
        f.write(r.content)
    logger.info('Loaded.')

data_path = "../Data/e_com_behaviour_data.zip"

# Create SQL database if not exist, extract the data from the path and load it to the database
con = sqlite3.connect('ecom_database.db')
zipfile.ZipFile.extractall(data_path)
