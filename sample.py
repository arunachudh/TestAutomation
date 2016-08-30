from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    

    # create a new Firefox session
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.maximize_window()
     
    # navigate to the application home page
    driver.get("http://www.google.com")
     
    # get the search textbox
    search_field = driver.find_element_by_id("lst-ib")
    
    search_field.clear()
     
    # enter search keyword and submit
    search_field.send_keys("Selenium WebDriver Interview questions")
    search_field.submit()
    driver.implicitly_wait(5)
    

     
    # close the browser window
    driver.quit()


main()
