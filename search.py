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


def search(url):
    count = 0
    extension_path = "/home/sakib/metamask-10.3.0-an+fx.xpi"
    # driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
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


    time.sleep(3)
    try:

        button = driver.find_element(By.CSS_SELECTOR, "button.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.kmCSYg.gIDfxn")

        button.click()
        time.sleep(20)
        # button = driver.find_element(By.CSS_SELECTOR, "button.UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0.btgkrL.Blockreact__Block-sc-1xf18x6-0.Flexreact__Flex-sc-1twd32i-0.Itemreact__ItemBase-sc-1idymv7-0.dBFmez.jYqxGr.glymPt")
        # button.click()

        button = driver.find_element(By.CSS_SELECTOR,
                                 "button.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.kmCSYg.gIDfxn")
        button.click()

        input = driver.find_element(By.XPATH,"/html/body/div[11]/div/div/div/section/div[1]/div/div[2]/div/div[1]/input").send_keys('0.1')
        input = driver.find_element(By.XPATH,"/html/body/div[11]/div/div/div/section/div[2]/div[2]/div[1]/div/input").send_keys('Custom date')
        button2 = driver.find_element(By.XPATH,"/html/body/div[11]/div/div/div/section/div[2]/div[2]/div[2]/div/input").send_keys("13:40")
        checkbox = driver.find_element(By.ID,"tos").click()
    except:
        pass

    for i in url:
        # if count > 2:
        #     count = 0
        #     driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
        #     driver.switch_to.window(driver.window_handles[1])
        # else:
        driver.execute_script(f"window.open('about:blank', 'tab{str(i)}');")
        driver.switch_to.window(f'tab{str(i)}')
        count +=1
        driver.get(i)

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
            button = driver.find_element(By.CSS_SELECTOR,
                                     "button.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.kmCSYg.gIDfxn")
            button.click()

            input = driver.find_element(By.XPATH,
                                    "/html/body/div[11]/div/div/div/section/div[1]/div/div[2]/div/div[1]/input").send_keys(
                '0.1')
            input = driver.find_element(By.XPATH,
                                    "/html/body/div[11]/div/div/div/section/div[2]/div[2]/div[1]/div/input").send_keys(
                'Custom date')
            button2 = driver.find_element(By.XPATH,
                                      "/html/body/div[11]/div/div/div/section/div[2]/div[2]/div[2]/div/input").send_keys(
                "13:40")
            checkbox = driver.find_element(By.ID, "tos").click()

        except:
            pass



    # input.submit()




    # except:
    #     pass
    # driver.close()
