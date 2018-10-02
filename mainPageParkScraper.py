
from bs4 import BeautifulSoup
#from urllib.request import urlopen
#import ssl


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Create chrome browser object
driver = webdriver.Chrome('/Users/NicoleFetsch/Downloads/chromedriver')
driver.get('https://www.reservecalifornia.com/CaliforniaWebHome/')

"""
# Attempts to connect to reservecalifornia.com 5 times
for i in range(1):
    try:
        driver.get('https://www.reservecalifornia.com/CaliforniaWebHome/')
    except:
        print("No Such Element Found")
        driver.quit()
"""

# Park, Stay length and date arrived
park = "Limekiln SP"
stayLength = "2"
date = "01/11/2019"

# Navigating main Reserve CA webpage
def main_ReserveCA (_park, _stayLength, _date):
    form_stayLength = driver.find_element_by_name("ctl00$ctl00$mainContent$ddlHomeNights")
    form_arrivalDate = driver.find_element_by_name("ctl00$ctl00$mainContent$txtArrivalDate")
    form_parkName = driver.find_element_by_name("ctl00$ctl00$mainContent$txtSearchparkautocomplete")

    form_stayLength.send_keys(_stayLength)
    form_arrivalDate.send_keys(_date)
    driver.find_element_by_name("ctl00$ctl00$mainContent$txtSearchparkautocomplete").click()
    form_parkName.send_keys(_park)

    time.sleep(1) #wait for autocomplete box to appear
    form_parkName.send_keys(Keys.ARROW_DOWN)
    form_parkName.send_keys(Keys.RETURN)

    driver.find_element_by_class_name("home_go_btn").click()
    time.sleep(5) #wait for the next page to load



main_ReserveCA(park, stayLength, date)
# Goes to Ocean Camp (sites 1-12) availability page
try:
    driver.find_element_by_css_selector("div[class='newdata_right placedata-title-right small_success']").click()
except:
    driver.find_element_by_css_selector("div[class='newdata_right placedata-title-right small_danger']").click()

# Selenium hands the page source to Beautiful Soup
soup = BeautifulSoup(driver.page_source, features="html.parser")
week_day_long = soup.findAll("th", {"class":"week_text"} )
week_day_short = week_day_long[0:7]

print(week_day_short)

### Pryce's code ####

weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for bs_str in week_day_short:
    for day in weekdays:
        result = bs_str.find(day)

print('Printing result..')
print(result)

### End pryces code ###



def find_Week_Order(week):
    week_final = []
    for i in week:
        x = i[-8:-5]
    return week_final.append(x)

find_Week_Order(week_day_short)

print(week_order)
print(find_Week_Order(week_day_short))

time.sleep(5)
driver.quit()

"""
list_table = []
        for i in table:
            list_table.append(str(i))
"""







"""
#form_parkName = driver.find_element_by_name("ctl00$ctl00$mainContent$txtSearchparkautocomplete")

time.sleep(3)
"""
#driver.quit()


#form_stayLength = driver.find_element_by_name("ctl000$ctl00$mainContent$ddlHomeNights")
#form_go_Button = driver.find_element_by_name("ctl00$ctl00$mainContent$btnSearch")

"""
#creating a custom ssl context without SSL certification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
"""

"""
driver = webdriver.Chrome()
driver.get("https://www.reservecalifornia.com/CaliforniaWebHome/")
print(driver.page_source)
"""
""""
parkName_form = driver.find_element_by_name("ctl00$ctl00$mainContent$hdnSearchPlaceName")
arrivalDate_form = driver.find_element_by_name("ctl00$ctl00$mainContent$txtArrivalDate")
stayLength_form = driver.find_element_by_name("ctl000$ctl00$mainContent$ddlHomeNights")
go_Button = driver.find_element_by_name("ctl00$ctl00$mainContent$btnSearch")


arrivalDate_form.send_keys("09/28/2018")
stayLength_form.send_keys("2")
go
"""

"""
html = urlopen("https://www.reservecalifornia.com/CaliforniaWebHome/", context=ctx)
bsObj = BeautifulSoup(html, features="html.parser");
main_search_table = bsObj.findAll("div", {"class":"banner_search_box_main"})
print(main_search_table)
"""
"""
with urllib.request.urlopen(url_string, context=ctx) as u, \
        open(file_name, 'wb') as f:
    f.write(u.read())
"""
#from urllib.error import HTTPError

#html = urllib.request.urlopen("google.com")




"""
for child in bsObj.find("div", {"class":"banner_search_box_main"}):
    print(child)
    
#html = urlopen("https://www.reserveamerica.com/camping/nehalem-bay-state-park/r/campgroundDetails.do?contractCode=OR&parkId=402191")

"""

"""
try:
    #html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
    #html = urlopen("https://www.reservecalifornia.com/CaliforniaWebHome/")
    html = urlopen("https://docs.python.org/3/library/urllib.requestttt")
except HTTPError as e:
    print(e)
    #Start "Plan B" send email/text saying script failed
"""
