from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('/opt/lab/php-webapp/chromedriver', chrome_options=chrome_options,  service_args=['--verbose', '--log-path=/opt/chromedriver.log'])


driver.get('https://google.org')
print(driver.title)
