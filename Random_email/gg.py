import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Load user data from CSV or any other source
user_data = pd.read_excel('C:\\Users\\Anuj\\projectyoube_video\\Random_email\\random_email_and_password.xlsx')


def login(username, password):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode for faster performance
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://cch247.helpersin.com/")  # Replace with the actual login URL

        username_field = driver.find_element(By.NAME, "email")  # Replace with actual name attribute
        password_field = driver.find_element(By.NAME, "password")  # Replace with actual name attribute

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)

    except Exception as e:
        print(f"Error logging in with {username}: {e}")
    finally:
        driver.quit()


def perform_logins(data):
    threads = []
    for index, row in data.iterrows():
        username = row['Email']
        password = row['Password']
        thread = threading.Thread(target=login, args=(username, password))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


perform_logins(user_data)
