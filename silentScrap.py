from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import csv
import time

class MyBot:
    def __init__(self) :
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=self.options)

        # self.driver.get("https://google.com")
        # self.driver.get_screenshot_as_file("screenshot.png")
        # print(self.driver.title)

        # fetch all weight related questions and answers
        search = "weight"

        options = webdriver.ChromeOptions()
        self.driver.get('https://www.google.com')
        self.driver.find_element(By.NAME,"q").send_keys(search + Keys.ENTER)

        limit = 5 # no of questions to be fetched
        counter = 1
        qno=1
        header = ["question","answer"]
        data = []
        while counter <= limit:
            qq=aa=""
            try:
                question = self.driver.find_element(By.CSS_SELECTOR, 'div[jsname="N760b"] > div:nth-child(' + str(counter) + ')')
                qq=question.text
                if search not in qq:  # this is just to ignore UN RELATED questions
                    counter+=1        # the keyword must be in questions 
                    continue
            except NoSuchElementException:
                counter +=1
                continue
            print (qno, question.text) 
            #driver.implicitly_wait(60) # wait after each click
            # wait for 1 seconds
            time.sleep(1)
            question.click()
            
            try:
                answer = question.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div > div > span:nth-child(1) > span')
            except NoSuchElementException:
                answer = ""
            if answer == '':
                print ('different format')
                aa=""
            else:
                print (answer.text)
                aa = answer.text
            print ('-------------------------------------')
            counter += 1
            qno +=1
            row = [qq, aa]
            data.append(row)
        with open('q.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

MyBot()


