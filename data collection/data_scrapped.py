import olx_scrapper as olx
import pandas as pd 

path = "C:\\Users\\Wasim\\Desktop\\Data_science_Projects\\datascience_salary\\data collection\\chromedriver.exe"
rows=1000
df=olx.get_information(path,4,5) #4 states

df.to_csv('olx_rent_data.csv', index = False)
