import os
import requests, zipfile, io
import sqlite3
import pandas as pd
import numpy as np
import seqlog
import logging
from io import BytesIO


# Create connection to seqlog and logger_name
seqlog.log_to_seq(
    server_url="http://localhost:5341/",
    level=logging.INFO,
    batch_size=1,
    auto_flush_timeout=1,  # seconds
    override_root_logger=True
)

logger = logging.getLogger(__name__)

# merge the two CSV files from url and create binary file to use for SQL database - seems that this is not possible since kaagle doesnt allow for direct zip link
url = "https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store/download" \
          "?datasetVersionNumber=8"

r = requests.get(url)
buf1 = BytesIO(r.content)
df_files = []
with zipfile.ZipFile(buf1, 'r') as f:
    for name in f.namelist():
        if name.endswith('.csv'):
            with f.open(name) as zd:
                dataframe = pd.read_csv(zd)
                df_files.append(dataframe)

df = pd.concat(df_files)
np.asarray(df.values).tofile('data_binary.dat')



# Create SQL database if not exist, extract the data from the path and load it to the database
con = sqlite3.connect('ecom_database.db')


