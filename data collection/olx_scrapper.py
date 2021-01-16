from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
from tqdm import tqdm

def get_information(pathofdriver,n_loads,n_states):
    brave_path = r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    url='https://www.olx.in/for-rent-houses-apartments_c1723?filter=type_eq_rent-apartments_and_floors_and_houses'
    path=pathofdriver
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.get(url)
    
    time.sleep(10)

    listofitems=[]

    for state in range(1,n_states+1):
        driver.find_element_by_xpath('//*[@id="container"]/main/div/div/section/div/div/div[5]/div[1]/div/div[2]/div[3]/ul/li/ul/li['+str(state)+']/a').click()
        time.sleep(10)

        #for LOAD MORE of houses
        
        time.sleep(10)
        s=42
        no_loads=n_loads
        for load in range(0,no_loads):
            listoflinks=[]
            productInfoList=driver.find_elements_by_class_name('EIR5N')
            for el in productInfoList:
                try:
                    ppp1=el.find_element_by_tag_name('a')
                    listoflinks.append(ppp1.get_property('href'))
                except NoSuchElementException:
                    print("Scraping terminated ..")
            driver.find_element_by_xpath('//*[@id="container"]/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li['+str(s)+']/div/button/span').click()
            time.sleep(5)
            print(load+1)
            s=s+40
        driver.execute_script("scrollBy(0,-50000);")
        driver.find_element_by_xpath('//*[@id="container"]/main/div/div/section/div/div/div[5]/div[1]/div/div[2]/div[3]/ul/li/a/div/div[2]').click()
        time.sleep(5)
        listofitems.extend(listoflinks)
    
    overallinfo=[]
    for i in tqdm(listofitems):
        driver.get(i)
        try:
            types=driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[1]/div/span[2]').text
            bed=driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[2]/div/span[2]').text
            bath=driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[3]/div/span[2]').text
            fur=driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[4]/div/span[2]').text
            area=driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[7]/div/span[2]').text
            face=driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[13]/div/span[2]').text
            floors=driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[10]/div/span[2]').text
            ment=driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[9]/div/span[2]').text
            price=driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div/div[5]/div[1]/div/section/span[1]').text
        except NoSuchElementException:
            types = -1
            bed = -1
            bath = -1
            fur = -1
            area = -1
            face = -1
            floors= -1
            ment=-1
            price=-1
            
        tempJ={'Type':types,'bedroom':bed,'bathroom':bath,'furnishing':fur,'Carpet Area (ft²)':area,'Maintenance (Monthly)':ment,'facing':face,'Total floor':floors,'Rent':price}
        overallinfo.append(tempJ) 

    return pd.DataFrame(overallinfo) 
     #df.to_csv(r'C:\Users\Wasim\Desktop\Data_science_Projects\datascience_salary\data collection\olx_rent_data.csv', index = False) 







