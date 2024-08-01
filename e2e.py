from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import os


app_url = "http://127.0.0.1:5000"


def test_scores_service(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        web_score = driver.find_element(By.ID, "score")
        score = web_score.text

        if 0 < int(score) < 1000:
            return True
        else:
            print("Test failed!")
            return False

    except WebDriverException as e:
        print("Test failed due to website connection issue.")
        return False



def main_function():
    if test_scores_service(app_url) == True:
        print("Test successful!")
        os._exit(0)
    else:
        print("Test failed!")
        os._exit(1)


main_function()




