from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from firebase import firebase
import sys
import time
from datetime import datetime
now = datetime.now()
print("Start time")
print(now)
args = sys.argv


firebase = firebase.FirebaseApplication("https://washu-scrape.firebaseio.com/",None)

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
listOfDepartmentElements = departmentTable.find_elements_by_tag_name("a")
listofDepartments = []
classCount=0
for department in listOfDepartmentElements:
    listofDepartments.append(department.text)
departmentCount=len(listofDepartments)
for department in listofDepartments:
    if (department=="BIOLOGY AND BIOMEDICAL SCIENCES(L41)"):
    # if (department!="All Departments(All)"):
        departmentLink = driver.find_element_by_link_text(department)
        departmentLink.click()
        time.sleep(11)
        try: #probably dont need this try and could by safe with time sleep only
            element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"Body_oCourseList_viewSelect"))
            )
        except:
            driver.quit()
        classList = driver.find_elements_by_css_selector("div[class^='Crs']")
        classCount+=len(classList)
        #add department to firebase here
        for classObj in classList:
            titleInfo = classObj.find_element_by_tag_name('table')
            topLevel = titleInfo.find_elements(By.CSS_SELECTOR,("a[style*='text-align:left;']"))
            #change this to explicitly define each
            courseNumber = topLevel[0].text
            courseName = topLevel[1].text
            courseUnits = topLevel[2].text
            # for topObj in topLevel:
                # print(topObj.text)
            descLevel = classObj.find_element_by_css_selector("div[class*='DivDetail']")
            actualDesc = descLevel.find_element_by_css_selector("a[style='text-align:left;'")
            actualDesc = actualDesc.get_attribute('textContent')
            attribList = descLevel.find_elements_by_css_selector("a[class^='CrsAttr']")
            #similar to topObh
            # for attrib in attribList:
                # print(attrib.get_attribute('textContent'))
            instrType = descLevel.find_element_by_css_selector("td[style='width:30%;']")
            actualInstr = instrType.find_element_by_tag_name('a')
            actualInstr = actualInstr.get_attribute('textContent')
            gradeOption = descLevel.find_element_by_class_name("GradeOptionLink")
            gradeOption = gradeOption.get_attribute('textContent')
            freqType = descLevel.find_element_by_css_selector("td[style='width:44%;vertical-align:top;']")
            actualFreq = freqType.find_element_by_tag_name('a')
            actualFreq = actualFreq.get_attribute('textContent')
            resultTab = classObj.find_element_by_class_name("ResultTable")
            sections = resultTab.find_elements(By.CSS_SELECTOR,("tr[id*='tr']"))
            sectionArray = []
            for section in sections:
                sectionContent = section.find_elements(By.CSS_SELECTOR,("td[class*='ItemRow']"))
                newSection = {
                    "Section" : sectionContent[0].text,
                    "Days" : sectionContent[1].text,
                    "Time" : sectionContent[2].text,
                    "Location" : sectionContent[3].text,
                    "Instructor" : sectionContent[4].text,
                    "Final" : sectionContent[5].text,
                    "Seats" : sectionContent[6].text,
                    "Enrolled" : sectionContent[7].text,
                    "Waitlist" : sectionContent[8].text
                }
                sectionArray.append(newSection)
            classData = {
                "Course Number" : courseNumber,
                "Course Name" : courseName,
                "Course Units" : courseUnits,
                "Course Description" : actualDesc,
                "Instruction Type" : actualInstr,
                "Grade Option" : gradeOption,
                "Frequency" : actualFreq,
                "Sections" : sectionArray
            }
            print(classData)
            # firebase.patch("/artsci/{}/{}".format(department,courseNumber),classData)

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

