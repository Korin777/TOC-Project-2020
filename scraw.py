from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
import os
 

# options = Options()
# options.add_argument("--disable-notifications")
 
# chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
# chrome.get("https://www.facebook.com/")

# if __name__ == "__main__":    
#     options = Options()
#     options.add_argument("--disable-notifications")
#     url = 'https://accounts.pixiv.net/login?return_to=https%3A%2'+"F%"+"2Fwww.pixiv.net"+"%"+'2F&lang=zh_tw&source=pc&view_type=page'
#     driver = webdriver.Chrome('./chromedriver', chrome_options=options)
#     driver.get(url)
#     time.sleep(3)

#     input = driver.find_element_by_id("LoginComponent").find_elements_by_tag_name("input")
#     input[0].send_keys('k777k777tw123@gmail.com')
#     input[1].send_keys('ko95701ko')
#     input[1].submit()
#     time.sleep(8)
#     container = driver.find_element_by_class_name("gtm-toppage-thumbnail-illustration-recommend-works-zone")
#     picture = container.find_elements_by_tag_name("img")
#     picture_url = []
#     j = 0
#     for i in range(len(picture)):
#         if(picture[i].get_attribute("class") == "rp5asc-10 leQnFG"):
#             picture_url.append(picture[i].get_attribute("src"))
#             picture_url[j] = "https://i.pximg.net/img-master" + picture_url[j][picture_url[j].find("/img/"):picture_url[j].rfind("_p0_")] + "_p0_master1200.jpg"
#             print(picture_url[j])
#             j += 1
def get_pixiv_picture_url():   
    # options = Options()
    # options.add_argument("--disable-notifications")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless") #無頭模式
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    url = 'https://accounts.pixiv.net/login?return_to=https%3A%2'+"F%"+"2Fwww.pixiv.net"+"%"+'2F&lang=zh_tw&source=pc&view_type=page'
    # driver = webdriver.Chrome('./chromedriver', chrome_options=options)
    driver.get(url)
    time.sleep(3)

    input = driver.find_element_by_id("LoginComponent").find_elements_by_tag_name("input")
    input[0].send_keys('k777k777tw123@gmail.com')
    input[1].send_keys('ko95701ko')
    input[1].submit()
    time.sleep(8)
    container = driver.find_element_by_class_name("gtm-toppage-thumbnail-illustration-recommend-works-zone")
    picture = container.find_elements_by_tag_name("img")
    picture_url = []
    j = 0
    for i in range(len(picture)):
        if(picture[i].get_attribute("class") == "rp5asc-10 leQnFG"):
            picture_url.append(picture[i].get_attribute("src"))
            picture_url[j] = "https://i.pixiv.cat/img-master" + picture_url[j][picture_url[j].find("/img/"):picture_url[j].rfind("_p0_")] + "_p0_master1200.jpg"
            print(picture_url[j])
            j += 1
    return picture_url