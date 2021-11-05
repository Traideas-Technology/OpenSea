from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
# driver.send_keys(Keys.CONTROL + 'T')

# options = Options()
# options.headless = True
from datetime import datetime
import json


def data_parser():
    now = datetime.now()
    f = open('data.json', )
    data = json.load(f)
    HH = int(data['time']["HH"])
    mm = int(data['time']["mm"])
    cHH = int(now.strftime("%H"))
    cmm = int(now.strftime("%M"))
    HH = HH+cHH
    mm = mm+cmm
    dict = {"time": f"{HH}:{mm}", "amount": data['weth']}
    return dict


def search(url):
    data = data_parser()
    count = 0
    extension_path = "/home/sakib/Desktop/Projects/opensea/metamask-10.3.0-an+fx.xpi"
    driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
    driver.install_addon(extension_path, temporary=True)
    driver.get("about:support")
    time.sleep(40)
# except:
#     driver = webdriver.Firefox(options=options, executable_path="geckodriver")
#     pass

# url = input("Enter URL: ")
#     url = "https://opensea.io/assets?search[query]=galaxy%20fight%20club"

    driver.get(url[0])


    time.sleep(10)
    try:

        button = driver.find_element(By.CSS_SELECTOR, "button.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.kmCSYg.gIDfxn")

        button.click()
        time.sleep(20)
        # button = driver.find_element(By.CSS_SELECTOR, "button.UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0.btgkrL.Blockreact__Block-sc-1xf18x6-0.Flexreact__Flex-sc-1twd32i-0.Itemreact__ItemBase-sc-1idymv7-0.dBFmez.jYqxGr.glymPt")
        # button.click()

        button = driver.find_element(By.CSS_SELECTOR,
                                 "button.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.kmCSYg.gIDfxn")
        button.click()

        input = driver.find_element(By.XPATH,"/html/body/div[11]/div/div/div/section/div[1]/div/div[2]/div/div[1]/input").send_keys(data['amount'])
        input = driver.find_element(By.XPATH,"/html/body/div[11]/div/div/div/section/div[2]/div[2]/div[1]/div/input").send_keys('Custom date')
        button2 = driver.find_element(By.XPATH,"/html/body/div[11]/div/div/div/section/div[2]/div[2]/div[2]/div/input").send_keys(data['time'])
        checkbox = driver.find_element(By.ID,"tos").click()
    except:
        pass
    length = url.__len__()
    for i in range(length):
        if count > 2:
            count = 0
            driver.switch_to.new_window()
            # driver.switch_to.window(driver.window_handles[1])
        # else:
        driver.execute_script(f"window.open('about:blank', 'tab{str(i)}');")
        driver.switch_to.window(f'tab{str(i)}')
        count +=1
        driver.get(url[i])

        # time.sleep(3)
        # try:
        # button = driver.find_element(By.CSS_SELECTOR,
        #                              "button.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.kmCSYg.gIDfxn")
        #
        # button.click()
        time.sleep(1)
        # button = driver.find_element(By.CSS_SELECTOR, "button.UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0.btgkrL.Blockreact__Block-sc-1xf18x6-0.Flexreact__Flex-sc-1twd32i-0.Itemreact__ItemBase-sc-1idymv7-0.dBFmez.jYqxGr.glymPt")
        # button.click()
        try:
            try:
                button = driver.find_element(By.CSS_SELECTOR,
                                     "button.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.kmCSYg.gIDfxn")
                button.click()
            except:
                print("Make Offer could not be clicked")
            try:
                input = driver.find_element(By.XPATH,
                                    "/html/body/div[11]/div/div/div/section/div[1]/div/div[2]/div/div[1]/input").send_keys(
                data['amount'])
                input = driver.find_element(By.XPATH,
                                    "/html/body/div[11]/div/div/div/section/div[2]/div[2]/div[1]/div/input").click()
            except:
                print("Amount is not properly set")

            buttonList = driver.find_element(By.CSS_SELECTOR, 'div.tippy-content')
            try:
                custom_date = buttonList.find_element(By.XPATH, "//button[contains(., 'Custom date')]").click()
            except:
                print("custom date not selected")
            # button2 = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div/section/div[2]/div[2]/div[2]/div/input").send_keys(data['time'])
            try:
                checkbox = driver.find_element(By.ID, "tos").click()
            except:
                print("Check box is not clicked")

            try:
                make_offer = driver.find_element(By.CSS_SELECTOR, "button.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.bhqEJb.fzwDgL").click()
            except:
                print("Make Offer button is not clicked")

        except:
            pass
