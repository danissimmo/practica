# importing pandas library
import pandas as pd

# reading the given csv file
# and creating dataframe
account = pd.read_csv("log.txt",
                      delimiter='	')
# store dataframe into csv file
account.to_csv('logi.csv',
               index=None)