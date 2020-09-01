from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
args = sys.argv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://courses.wustl.edu/Semester/Listing.aspx")

link = driver.find_element_by_link_text(args[1]) #Engineering
link.click()

# <a id="Body_repSchools_lnkSchool_5" class="ControlLink" href="javascript:__doPostBack('ctl00$Body$repSchools$ctl05$lnkSchool','')" style="font-weight:normal;">Engineering</a>

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,args[2]))
    )
    element.click()
except:
    driver.quit()

# search = driver.find_element_by_id("Body_txtSearchKeyword")
# search.send_keys("test")

