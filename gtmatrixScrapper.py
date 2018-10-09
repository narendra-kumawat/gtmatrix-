from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException
import sys
import convertTocsv as conv
import url as l
# import urlList as url

user="shubhamchand0103@gmail.com"
password="shubhamchand0103"
url="http://www.datamintelligence.com"
country=[1,3,4,5,6]

driver=webdriver.Chrome('/home/gopal_admin/Music/chromedriver')
driver.get("https://gtmetrix.com")

def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except ElementNotVisibleException:
        return False
    except NoSuchElementException:
        return False
    return True

def check_exists_by_css_selector(driver,css_selector):
    try:
        driver.find_element_by_css_selector(css_selector)
    except ElementNotVisibleException:
        return False
    except NoSuchElementException:
        return False
    return True

def checkExistenceByXpath(xpath):
    found=False
    while(found==False):
        found=check_exists_by_xpath(driver,xpath)
    if(found==True):
        return True

def checkExistenceByCSSSelector(css_selector):
    found=False
    while(found==False):
        found=check_exists_by_css_selector(driver,css_selector)
    return True  

def fetchReport(pageSpeedfile,ySlowfile):        
    if(checkExistenceByXpath('/html/body/div[1]/main/article/div[2]/div[1]/div/div[1]/span/span')):
        pageSpeedScore=driver.find_element_by_xpath('/html/body/div[1]/main/article/div[2]/div[1]/div/div[1]/span/span')    
        print(pageSpeedScore.text)
        putdataintofile("w",pageSpeedScore)
        ySlow=driver.find_element_by_xpath('/html/body/div[1]/main/article/div[2]/div[1]/div/div[2]/span/span')
        print(ySlow.text)
        putdataintofile("a",ySlow)
        fullyLoadedTime=driver.find_element_by_xpath('/html/body/div[1]/main/article/div[2]/div[2]/div/div[1]/span')
        print(fullyLoadedTime.text)
        putdataintofile("a",fullyLoadedTime)
        totalPageSize=driver.find_element_by_xpath('/html/body/div[1]/main/article/div[2]/div[2]/div/div[2]/span')
        print(totalPageSize.text)
        putdataintofile("a",totalPageSize)
        request=driver.find_element_by_xpath('/html/body/div[1]/main/article/div[2]/div[2]/div/div[3]/span')
        print(request.text)
        putdataintofile("a",request)
        table=driver.find_element_by_xpath('//*[@id="pagespeed"]/div/div[1]/table')
        with open(pageSpeedfile,'w') as f:
            f.write(table.text)
        print(table.text)
        driver.find_element_by_xpath('/html/body/div[1]/main/article/div[3]/ul/li[2]/a').click() 
        ySlow=driver.find_element_by_xpath('//*[@id="yslow"]/div/div[1]/table')
        with open(ySlowfile,'w') as f:
            f.write(ySlow.text)
        print("-----------")
        print(ySlow.text)
           

def processData(url):
    if(checkExistenceByXpath('/html/body/div[1]/main/article/form/div[1]/div[1]/div/input')):         
        for i in country:
            for x in range(i):                
                driver.find_element_by_xpath('//*[@id="af-info-region"]').click()
            driver.find_element_by_xpath('/html/body/div[1]/main/article/form/div[1]/div[1]/div/input').send_keys(url)    
            driver.find_element_by_xpath('/html/body/div[1]/main/article/form/div[1]/div[2]/button').click()
            pageSpeedfile="./files/PageSpeed"+str(i)+".txt"
            ySlowfile="./files/YSlow"+str(i)+".txt"
            print(pageSpeedfile,ySlowfile)
            fetchReport(pageSpeedfile,ySlowfile)

            conv.dataStructure(url)

            driver.find_element_by_xpath('/html/body/div[1]/header/div/nav/ul/li[1]/a/i').click()
            time.sleep(3)
            

def putdataintofile(mode,obj):
    with open("./files/data.txt",mode) as f:
        f.write(obj.text+"\n")


driver.find_element_by_xpath('//*[@id="user-nav-login"]/a').click()

if(checkExistenceByXpath('//*[@id="li-email"]')):
    driver.find_element_by_xpath('//*[@id="li-email"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="li-password"]').send_keys(password) 
    driver.find_element_by_xpath('//*[@id="menu-site-nav"]/div[2]/div[1]/form/div[4]/button').click()

# urlList=[
#     "https://www.datamintelligence.com/research-report/active-pharmaceutical-ingredients-market/",
#     "https://www.datamintelligence.com/research-report/asia-pacific-adhesives-sealants-market/",
#     "https://www.datamintelligence.com/research-report/aqua-feed-market/",
#     "https://www.datamintelligence.com/research-report/asia-compound-feed-market/",
#     "https://www.datamintelligence.com/research-report/ancient-grains-market/",
#     "https://www.datamintelligence.com/research-report/alcoholic-beverages-market/",    
#     ]

if __name__=="__main__":
    for url in l.urlList:
        processData(url)
        # sys.exit()
  




   
