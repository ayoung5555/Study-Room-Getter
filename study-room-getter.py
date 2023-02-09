import pytest                                                                                   #
import time                                                                                     #
import json                                                                                     #
from selenium import webdriver                                                                  #
from selenium.webdriver.chrome.options import Options                                           #
from selenium.webdriver.common.by import By                                                     #
from selenium.webdriver.common.action_chains import ActionChains                                #
from selenium.webdriver.support import expected_conditions                                      #
from selenium.webdriver.support.wait import WebDriverWait                                       #
from selenium.webdriver.common.keys import Keys                                                 #
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities                  #
driver = webdriver.Chrome()                                                                     #
vars = {}                                                                                       #
time.sleep(0.5)                                                                                 #
# ==================== DO NOT CHANGE ANYTHING ABOVE THIS LINE ===================================

# UM login info (do not upload since this is plaintext)
uniqname = "CHANGE THIS"
UMpassword = "CHANGE THIS"
# optional: change the booking name for your study room
groupName = "study"
# list url for exact study room you want
# Ex. https://umich.libcal.com/r/accessible/availability?lid=2761&zone=1609&gid=5040&capacity=1&space=22737
desired_room = "CHANGE THIS"
# optional: time to wait for DUO push confirmation. Default is 1 minute
login_wait_time = 1
# optional: time to wait for page to load. Default is 0.25 seconds
loadtime = 0.25


# ===================== DO NOT CHANGE ANYTHING BELOW THIS LINE ==================================
driver.get(desired_room)                                                                        #
driver.set_window_size(1278, 1391)                                                              #
driver.find_element(By.ID, "date").click()                                                      #
dropdown = driver.find_element(By.ID, "date")                                                   #
                                                                                                #
# optional: change the amount of days in advance to book a room. Default is 7 days (value of 8) #
# note that index below does not start at 0, it starts at 1                                     #
dropdown.find_element(By.CSS_SELECTOR, "*:nth-child(8)").click()                                #
                                                                                                #
driver.find_element(By.ID, "s-lc-submit-filters").click()                                       #
# ==================== DO NOT CHANGE ANYTHING ABOVE THIS LINE ===================================

# CHANGE THIS TO THE DESIRED TIME SLOT(s) YOU WANT
# uncomment the lines below to select the time slot you want

driver.find_element(By.XPATH, "//label[contains(.,\'8:00am - 8:30am\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'8:30am - 9:00am\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'9:00am - 9:30am\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'9:30am - 10:00am\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'10:00am - 10:30am\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'10:30am - 11:00am\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'11:00am - 11:30am\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'11:30am - 12:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'12:00pm - 12:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'12:30pm - 1:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'1:00pm - 1:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'1:30pm - 2:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'2:00pm - 2:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'2:30pm - 3:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'3:00pm - 3:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'3:30pm - 4:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'4:00pm - 4:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'4:30pm - 5:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'5:00pm - 5:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'5:30pm - 6:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'6:00pm - 6:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'6:30pm - 7:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'7:00pm - 7:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'7:30pm - 8:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'8:00pm - 8:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'8:30pm - 9:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'9:00pm - 9:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'9:30pm - 10:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'10:00pm - 10:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'10:30pm - 11:00pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'11:00pm - 11:30pm\')]").click()
# driver.find_element(By.XPATH, "//label[contains(.,\'11:30pm - 12:00am\')]").click()


# ===================== DO NOT CHANGE ANYTHING BELOW THIS LINE ==================================
driver.find_element(By.ID, "s-lc-submit-times").click()                                         #
element = driver.find_element(By.ID, "s-lc-submit-times")                                       #
actions = ActionChains(driver)                                                                  #
actions.move_to_element(element).perform()                                                      #
element = driver.find_element(By.CSS_SELECTOR, "body")                                          #
actions = ActionChains(driver)                                                                  #
actions.move_to_element(element).perform()                                                      #
# =========== LOGIN ===========                                                                 #
driver.find_element(By.ID, "login").send_keys(uniqname)                                         #
driver.find_element(By.ID, "password").send_keys(UMpassword)                                    #
time.sleep(loadtime)                                                                            #
driver.find_element(By.ID, "loginSubmit").click()                                               #
url = driver.current_url                                                                        #
timesecs = login_wait_time * 60                                                                 #
WebDriverWait(driver, timesecs).until(lambda driver: driver.current_url != url)                 #
time.sleep(loadtime)                                                                            #
# ========= END LOGIN =========                                                                 #
driver.find_element(By.ID, "nick").click()                                                      #
driver.find_element(By.ID, "nick").send_keys(groupName)                                         #
driver.find_element(By.CSS_SELECTOR, ".checkbox:nth-child(1) input").click()                    #
driver.find_element(By.ID, "s-lc-eq-bform-submit").click()                                      #
element = driver.find_element(By.ID, "s-lc-eq-bform-submit")                                    #
actions = ActionChains(driver)                                                                  #
actions.move_to_element(element).perform()                                                      #
element = driver.find_element(By.CSS_SELECTOR, "body")                                          #
actions = ActionChains(driver)                                                                  #
actions.move_to_element(element).perform()                                                      #
driver.quit()                                                                                   #
# ==================== DO NOT CHANGE ANYTHING ABOVE THIS LINE ===================================