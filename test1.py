from selenium import webdriver
from time import sleep
from datetime import datetime


# username = 'kevinkwendo95@gmail.com'
# password = 'Asila@1991'
username = 'jamesngari77@gmail.com'
password = 'Gianthorse2019'
url = 'https://timelog.gravitassolutionsltd.com/'

current_time = datetime.now()
time = current_time.strftime("%H:%M")
# time_hour = time.strftime()
day = current_time.isoweekday()

    # print("hello")
print(time)


driver = webdriver.Chrome('C:\\Users\\BackofficeTeam\\Downloads\\chromedriver')
driver.get(url)

driver.find_element_by_name('username').send_keys(username)
sleep(1)
driver.find_element_by_name('password').send_keys(password)
sleep(1)
driver.find_element_by_name('submit').click()
print('Logged in Successfully')

driver.find_element_by_class_name('icon-time').click()
sleep(1)
driver.find_element_by_name('punch_type').click()
sleep(1)
# clocking in

if day > 1 and day <= 4:
    if time  == "10:40":
        driver.find_element_by_xpath("//input[@value='in']").click()
        sleep(1)
        driver.find_element_by_xpath("//button[@id='punch_submit']").click()
        print('Clocked in Successfuly')
    elif time == "18:45":
        # clocking out
        driver.find_element_by_xpath("//input[@value='out']").click()
        sleep(1)
        driver.find_element_by_xpath("//button[@id='punch_submit']").click()
        print('Clocked in Successfuly')
    else:
        print('Stop right there and turn around!!!')
        exit()
elif day == 5:
    if time  == "8:50":
        driver.find_element_by_xpath("//input[@value='in']").click()
        sleep(1)
        driver.find_element_by_xpath("//button[@id='punch_submit']").click()
        print('Clocked in Successfuly')
        exit()
    elif time == "17:10":
        # clocking out
        driver.find_element_by_xpath("//input[@value='out']").click()
        sleep(1)
        driver.find_element_by_xpath("//button[@id='punch_submit']").click()
        print('Clocked in Successfuly')
        exit()
    else:
        print('Stop right there and turn around!!!')
        exit()
else:
    print('Its on a weekend, Enjoy')
    exit()

