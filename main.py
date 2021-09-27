from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
import time

if __name__ == "__main__":
    print(dir(webdriver))
    driver = webdriver.Chrome(
        "C:/Users/33610/Documents/Code/python/selenium/chromedriver_win32/chromedriver.exe")
    driver.get(
        "https://yurplan.com/event/This-is-Techno-Samedi-25-Septembre/72999?from=#/")
    time.sleep(1)
    driver.find_element_by_class_name(
        "c-btn.c-btn--primary.mt--s-3.u-display__b--s").click()
    # time.sleep()
    select = Select(driver.find_element_by_name(
        "typeTicket[204076]"))
    driver.find_element_by_name(
        "typeTicket[204076]").click()
    time.sleep(1)
    select.select_by_visible_text('2')
    time.sleep(1)

    driver.find_element_by_id(
        "booking-tickets").click()
    time.sleep(1)
    last_name = driver.find_element_by_name("ticketRegister[last_name]")
    last_name.send_keys("May")
    first_name = driver.find_element_by_name("ticketRegister[first_name]")
    first_name.send_keys("Nathan")
    email = driver.find_element_by_name("ticketRegister[email_address]")
    email.send_keys("Nathan.etu.univ@gmail.com")
    email_confirm = driver.find_element_by_name(
        "ticketRegister[email_address_confirm]")
    email_confirm.send_keys("Nathan.etu.univ@gmail.com")

    # ticketRegister[email_address]
    # ticketRegister[email_address_confirm]
