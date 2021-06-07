from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=92000000&keywords=able%20seaman&location=Worldwide"
LOGIN = "LOGIN"
PASSWORD = "PASWORD"
P_NUMBER = "1231234567"

driver = webdriver.Chrome(executable_path="D:\pythonProject\othersoft\chromedriver.exe")

driver.get(URL)
login_button = driver.find_element_by_css_selector("a.nav__button-secondary")
login_button.click()
time.sleep(1)

username = driver.find_element_by_css_selector("input#username")
username.send_keys(LOGIN)
password = driver.find_element_by_css_selector("input#password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
# submit_button = driver.find_element_by_css_selector("button.btn__primary--large")
# submit_button.click()
time.sleep(4)

all_jobs_list = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in all_jobs_list:
    print("---------------click job")
    print(job.text)
    time.sleep(1)
    job.click()
    time.sleep(3)
    try:
        job_apply_button = driver.find_element_by_css_selector(".jobs-apply-button")
        print(job_apply_button.text)
        job_apply_button.click()

        time.sleep(1)
        input_phone_number = driver.find_element_by_class_name("fb-single-line-text__input")
        input_phone_number.clear()
        input_phone_number.send_keys(P_NUMBER)

        time.sleep(1)
        next_button = driver.find_element_by_css_selector("footer button")
        if next_button.get_attribute("data-control-name") != "submit_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            print(close_button.get_attribute("id"))
            close_button.click()
            time.sleep(1)
            confirm_buttons = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")
            confirm_buttons[1].click()
            print("app skipped (next)")
            continue
        else:
            print(next_button.text)
            next_button.click()
            time.sleep(1)
            close_button = driver.find_element_by_class_name(".artdeco-modal__dismiss")
            close_button.click()

    except NoSuchElementException:
        print("no app button")

    time.sleep(5)
