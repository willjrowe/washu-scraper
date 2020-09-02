from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
from datetime import datetime
now = datetime.now()
print("Start time")
print(now)
args = sys.argv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://courses.wustl.edu/Semester/Listing.aspx")

# link = driver.find_element_by_link_text(args[1]) #Engineering
# mainDiv = driver.find_element_by_class_name("CenteredContent")
# link.click()

# <a id="Body_repSchools_lnkSchool_5" class="ControlLink" href="javascript:__doPostBack('ctl00$Body$repSchools$ctl05$lnkSchool','')" style="font-weight:normal;">Engineering</a>

# try:
#     element = WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.LINK_TEXT,args[2]))
#     )
#     element.click()
# except:
#     driver.quit()
# try:
#     element = WebDriverWait(driver,10).until(
#     EC.presence_of_element_located((By.ID,"divSelectRowE8113111E"))
#     )
#     print("found")
# except:
#     print("not found")
#     driver.quit()
# listOfThings = driver.find_elements(By.CSS_SELECTOR,("[crs='131']"))
departmentTable = driver.find_element_by_id("Body_dlDepartments")
listOfDepartments = departmentTable.find_elements_by_tag_name("a")
luvList = []
classCount=0
for ele in listOfDepartments:
    luvList.append(ele.text)
departmentCount=len(listOfDepartments)
for thing in luvList:
    if (thing!="All Departments(All)"):
        print(thing)
        link = driver.find_element_by_link_text(thing)
        link.click()
        time.sleep(9)
        try:
            element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"Body_oCourseList_viewSelect"))
            )
        except:
            driver.quit()
        testObj = driver.find_element_by_id("Body_oCourseList_tabSelect")
        classList = driver.find_elements_by_css_selector("div[class^='Crs']")
        classCount+=len(classList)
        # testList = testObj.find_elements(By.CSS_SELECTOR,("[style='font-weight: bold; text-align:left;']"))
        for classObj in classList:
            titleInfo = classObj.find_element_by_tag_name('table')
            # titleInfo = classObj.find_element_by_css_selector("[style='margin-top:-10px;']")
            topLevel = titleInfo.find_elements(By.CSS_SELECTOR,("a[style*='text-align:left;']"))
            for topObj in topLevel:
                print(topObj.text)
            descLevel = classObj.find_element_by_css_selector("div[class*='DivDetail']")
            actualDesc = descLevel.find_element_by_css_selector("a[style='text-align:left;'")
            print(actualDesc.get_attribute('textContent'))
            attribList = descLevel.find_elements_by_css_selector("a[class^='CrsAttr']")
            for attrib in attribList:
                print(attrib.get_attribute('textContent'))
            instrType = descLevel.find_element_by_css_selector("td[style='width:30%;']")
            actualInstr = instrType.find_element_by_tag_name('a')
            print(actualInstr.get_attribute('textContent'))
            gradeOption = descLevel.find_element_by_class_name("GradeOptionLink")
            print(gradeOption.get_attribute('textContent'))
            freqType = descLevel.find_element_by_css_selector("td[style='width:44%;vertical-align:top;']")
            actualFreq = freqType.find_element_by_tag_name('a')
            print(actualFreq.get_attribute('textContent'))
            resultTab = classObj.find_element_by_class_name("ResultTable")
            sections = resultTab.find_elements(By.CSS_SELECTOR,("tr[id*='tr']"))
            for section in sections:
                sectionContent = section.find_elements(By.CSS_SELECTOR,("td[class*='ItemRow']"))
                for cont in sectionContent:
                    print(cont.text)

print("end time")            
done = datetime.now()
print(done)
print("time elapsed")
print(done-now)
print("departments scanned")
print(departmentCount)
print("classes scanned")
print(classCount)
    # swag = thing.find_element_by_tag_name("tr")
    # print(swag.text)
    # search = driver.find_element_by_id("Body_txtSearchKeyword")
# search.send_keys("test")

