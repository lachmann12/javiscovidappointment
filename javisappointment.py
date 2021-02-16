# for this to work the selenium driver has to be downloaded and added to the path
# this is for people with preexisting conditions
# the software will fill in the information automatically and retry the website until it finds 
# new appointments, it then requires additional manual input

from selenium import webdriver
from playsound import playsound

browser = webdriver.Firefox()

browser.get('https://am-i-eligible.covid19vaccine.health.ny.gov/Public/providers')

label = "Get Started";
button = browser.find_elements_by_class_name("ux-btn-primary")[0]
button.click()

# change birthdate
bday = browser.find_element_by_xpath('//input[@placeholder="MM/DD/YYYY"]')
bday.send_keys("05291987")

# this will select female. Modifications are required for male
gender = browser.find_element_by_id("gender_group_1")
gender.click()

work = browser.find_element_by_id("nyworker_0")
work.click()

resident = browser.find_element_by_id("nyresident_0")
resident.click()

# change zip code (this might change the order of vaccination sites)
zip = browser.find_element_by_id("zip")
zip.send_keys("10014")

ucon = browser.find_element_by_id("underlyingCondition_0")
ucon.click()

uconc = browser.find_element_by_id("underlyingConditionConfirm_0")
uconc.click()

consent = browser.find_elements_by_xpath('//input')[-1]
consent.click()

button = browser.find_elements_by_class_name("ux-btn-primary")[0]
button.click()

time.sleep(2)

button = browser.find_elements_by_class_name("ux-btn-primary")[-1]
button.click()

# this is not ideal, if the loading page is too slow it can trigger an alarm
while True:
   schedule = browser.find_element_by_partial_link_text("Schedule your vaccine")
   schedule.click()
   chwd = browser.window_handles
   browser.switch_to.window(chwd[-1])
   time.sleep(4)
   if browser.page_source.find("No Appointments Available") == -1:
       print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
       print("ok appointments are ready at Javis")
       # choose your own sound file to play
       playsound('dixie-horn_daniel-simion.mp3')
       break
   else:
       browser.close()
       browser.switch_to.window(chwd[0])


