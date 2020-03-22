from selenium import webdriver
# Option 1 - with ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options,  service_args=['--verbose', '--log-path=./chromedriver.log'])
# Option 2 - with pyvirtualdisplay
#from pyvirtualdisplay import Display 
#display = Display(visible=0, size=(1024, 768)) 
#display.start() 
#driver = webdriver.Chrome('/opt/lab/php-webapp/chromedriver', chrome_options=chrome_options,  service_args=['--verbose', '--log-path=/opt/chromedriver.log'])
# Log path added via service_args to see errors if something goes wrong (always a good idea - many of the errors I encountered were described in the logs)
# And now you can add your website / app testing functionality: 
#driver.get('https://python.org') 
#driver.get('http://34.93.0.46/')
print(driver.title)
# driver.click...
