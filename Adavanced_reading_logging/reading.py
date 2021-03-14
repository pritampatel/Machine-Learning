import pandas as pd
import numpy as np
import os
import logging
import datetime

start_time = datetime.datetime.now()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

Formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
file_handler = logging.FileHandler('logfile.log')
file_handler.setFormatter(Formatter)

logger.addHandler(file_handler)
path = 'C:\\Users\\Pritam\\Desktop\\Machine-Learning\\Adavanced_reading_logging\\churn_data.csv'
try:
    logger.info(f'Reading the file from path {path}')
    df = pd.read_csv(path)

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    logger.info('Succesfully Read the File!!')
    print(df.head(3))

total_time_taken = datetime.datetime.now()-start_time
print(
    f'Succesfully Read the File in {total_time_taken.total_seconds()} Seconds')
logger.info(f'Executed in {total_time_taken.total_seconds()} Seconds')
