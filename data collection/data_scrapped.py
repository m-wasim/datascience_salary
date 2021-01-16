import olx_scrapper as olx
import pandas as pd 

path = "C:\\Users\\Wasim\\Desktop\\Data_science_Projects\\datascience_salary\\data collection\\chromedriver.exe"
rows=1000
df=olx.get_information(path,7,4)

df.to_csv('olx_rent_data.csv', index = False)