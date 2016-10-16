#!/usr/bin/python3

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


display=Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Firefox()

def attendance(sub):
    if sub=='BET':
        print ("Current attendance: "+driver.find_element_by_id("cc_ListAttendanceSummary_attendancePercentage_4").text+"%")
        tot=driver.find_element_by_id("cc_ListAttendanceSummary_attendanceTaken_4").text
        att=driver.find_element_by_id("cc_ListAttendanceSummary_classesAttended_4").text
    elif sub=='PSUC':
        print ("Current attendance: "+driver.find_element_by_id("cc_ListAttendanceSummary_attendancePercentage_5").text+"%")
        tot=driver.find_element_by_id("cc_ListAttendanceSummary_attendanceTaken_5").text
        att=driver.find_element_by_id("cc_ListAttendanceSummary_classesAttended_5").text
    elif sub=='MATHS':
        print ("Current attendance: "+driver.find_element_by_id("cc_ListAttendanceSummary_attendancePercentage_1").text+"%")
        tot=driver.find_element_by_id("cc_ListAttendanceSummary_attendanceTaken_1").text
        att=driver.find_element_by_id("cc_ListAttendanceSummary_classesAttended_1").text
    elif sub=='CHEM':
        print ("Current attendance: "+driver.find_element_by_id("cc_ListAttendanceSummary_attendancePercentage_2").text+"%")
        tot=driver.find_element_by_id("cc_ListAttendanceSummary_attendanceTaken_2").text
        att=driver.find_element_by_id("cc_ListAttendanceSummary_classesAttended_2").text
    elif sub=='BIO':
        print ("Current attendance: "+driver.find_element_by_id("cc_ListAttendanceSummary_attendancePercentage_3").text+"%")
        tot=driver.find_element_by_id("cc_ListAttendanceSummary_attendanceTaken_3").text
        att=driver.find_element_by_id("cc_ListAttendanceSummary_classesAttended_3").text
    elif sub=='EVS':
        print ("Current attendance: "+driver.find_element_by_id("cc_ListAttendanceSummary_attendancePercentage_6").text+"%")
        tot=driver.find_element_by_id("cc_ListAttendanceSummary_attendanceTaken_6").text
        att=driver.find_element_by_id("cc_ListAttendanceSummary_classesAttended_6").text
    else:
        return 0


    print("If you bunk your next class, your attendance will be: " + str(round((int(att)/(int(tot)+1)*100))))
    print("If you attend next class, your attendance will be: "+ str(round((int(att)+1)/(int(tot)+1)*100)))


def loginInfo(mode):
    file=open("Creds.txt",'w+')
    #file.seek(0)
    if os.path.getsize('Creds.txt')==0:
        #file.seek(0)
        file.write(input("DOB (YYYY-MM-DD): ")+"\n")
        file.write(input("Registration Number: "))
        #file.truncate()
    elif mode==1:
        os.remove("Creds.txt")
        file=open("Creds.txt",'w+')
        file.write(input("DOB (YYYY-MM-DD): ")+"\n")
        file.write(input("Registration Number: "))

    file.seek(0)   
    creds = file.readlines()
    file.close()
    
    return creds



def login(creds):
    driver.get("http://websismit.manipal.edu/websis/control/main")
    driver.find_element_by_id("idValue").send_keys(creds[1])
    driver.find_element_by_id("birthDate_i18n").send_keys(creds[0])
    #driver.find_element_by_id("birthDate_i18n").send_keys(Keys.RETURN)

    driver.get("http://websismit.manipal.edu/websis/control/StudentAcademicProfile")
  
    sub="woof"

    while sub!="EXIT":
        sub = input("Subject: ")
        if sub=="EXIT":
            break
        elif sub=="NEW":
            creds=loginInfo(1)
            driver.find_element_by_id("header-bar-logout").click()
            driver.find_element_by_id("idValue").send_keys(creds[1])
            driver.find_element_by_id("birthDate_i18n").send_keys(creds[0])
            driver.get("http://websismit.manipal.edu/websis/control/StudentAcademicProfile")

        attendance(sub)
    driver.close()

def main():
    creds=loginInfo(0)
    login(creds)

main()
