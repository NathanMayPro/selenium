import time
import getpass
import argparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from playsound import playsound


def check_exists_by_xpath(xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return None
    return element


def check_exists_by_css(selector):
    try:
        element = driver.find_element_by_css_selector(selector)
    except NoSuchElementException:
        return None
    return element


def connect_to_facebook(driver, args, strpswd):
    driver.get('https://www.facebook.com/')
    driver.implicitly_wait(2)
    driver.find_element_by_xpath(
        '//*[@data-cookiebanner="accept_button"]').click()
    mail = check_exists_by_xpath('//*[@id="email"]')
    passwd = check_exists_by_xpath('//*[@id="pass"]')
    mail.send_keys(args.email)
    passwd.send_keys(strpswd)
    connectbutton = driver.find_element_by_name('login').click()
    return driver


def connect_to_ticketswap(driver, args, strpswd):
    driver.get('https://www.ticketswap.fr')
    login = check_exists_by_xpath("//button[contains(text(),'Connecte-toi')]")

    # if login:
    #     login.click()
    #     time.sleep(2)
    #     facebookclick = check_exists_by_xpath(
    #         "//button[contains(text(),'Se connecter avec Facebook')]")
    #     print(facebookclick)
    #     facebookclick.click()

    # time.sleep(10)
    # login = check_exists_by_xpath("//button[contains(text(),'Connecte-toi')]")
    # if not login:
    #     print("Login success")
    #     return True
    # else:
    #     print("ERROR: Can't connect, retry")
    #     return False


def checktickt(driver, link):
    end = False
    counter = 0

    while not end:
        print(1)
        driver.get(link)
        driver.execute_script("window.scrollTo(0, 400)")
        dispo = check_exists_by_xpath("//*[text()='Available']")
        if dispo:
            print(2)
            a = check_exists_by_xpath(
                "//*[contains(@data-testid,'available-tickets-list')]/li[1]/a")
            driver.get(a.get_attribute("href"))
            driver.find_element_by_xpath("//*[text()='Buy ticket']").click()
            driver.find_element_by_xpath(
                "//*[text()='Continue with Facebook']").click()
            #playsound('Panda Dub - smile is the key.mp3')

            end = True

    # driver.get('https://www.ticketswap.fr/cart')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email', metavar='e',
                        help='facebook email')
    parser.add_argument('link', metavar='l',
                        help='ticketswap link')
    parser.add_argument('strpswd', metavar='p', help="Facebook password:")
    args = parser.parse_args()
    strpswd = args.strpswd
    # Optional argument, if not specified will search path.
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome("./chromedriver", options=options)
    #newdriver = webdriver.Chrome("./chromedriver", options=options)
    connect_to_facebook(driver, args, strpswd)
    connect = False
    # while not connect:
    #connect = connect_to_ticketswap(driver, args, strpswd)
    # time.sleep(2)
    driver.get("https://ticketswap.fr")
    # # driver.find_element_by_xpath("//*[text()='Accept']").click()
    # time.sleep(2)
    # driver.find_element_by_id('language').click()
    #driver.find_element_by_css_selector("button.css-y0bopz e12hwzh00")
    #driver.find_element_by_xpath("css-y0bopz e12hwzh00").click()
    # driver.find_element_by_class_name('css-1e3iek1').click()
    # driver.find_element_by_class_name('css-1e3iek1').click()
    # driver.find_element_by_class_name('css-1e3iek1').click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[text()='Connectez-vous']").click()
    # driver.find_element_by_xpath(
    #     "//*[text()='Se connecter avec Facebook']").click()
    # time.sleep(2)
    # driver.get(args.link)
    # driver.find_element_by_xpath("//*[text()='Changer la langue']").click()
    # driver.find_element_by_xpath("//*[text()='Accepter']").click()
    # time.sleep(2)
    # driver.find_element_by_xpath(
    #   "/html/body/div[1]/div[2]/div[4]/div/ul/li[1]/a/div").click()
    checktickt(driver, args.link)

    # newdriver.find_element_by_xpath(
    #     '//*[@data-cookiebanner="accept_button"]').click()
    # driver.switch_to_alert()
    # print(driver.window_handles)

    # # Switch to new window
    # # driver.switch_to.window(driver.window_handles[-1])
    # driver.find_element_by_xpath(
    #     '//*[@data-cookiebanner="accept_button"]').click()
    # mail = check_exists_by_xpath('//*[@id="email"]')
    # passwd = check_exists_by_xpath('//*[@id="pass"]')
    # mail.send_keys(args.email)
    # passwd.send_keys(strpswd)
    # connectbutton = driver.find_element_by_name('login').click()

    #login = check_exists_by_xpath("//button[contains(text(),'Connecte-toi')]")
    #checktickt(driver, args.link)
