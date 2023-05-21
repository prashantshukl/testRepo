from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.woccu.org/newsroom?gclid=CjwKCAjwue6hBhBVEiwA9YTx8GvQUIv5zRO_Wnd5d-XOvY2KRN_j2Ee2yekEHvD8hJKCQBHL35cV-BoCD9AQAvD_BwE"
path = "/home/prashant/Downloads/chromedriver/chromedriver"

service1 = Service(executable_path=path)
driver = webdriver.Chrome(service=service1)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="col-md-10"]')

for container in containers :
    headline =container.find_element(by="xpath", value='./h2').text
    content = container.find_element(by="xpath", value='./p[2]').text
    print(headline)
    print("")
    print(content)
    print("")
