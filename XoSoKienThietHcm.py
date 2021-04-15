from selenium import webdriver

driver = webdriver.Chrome(executable_path="venv/chromedriver.exe")
driver.get("https://www.xskthcm.com/")


row = driver.find_elements_by_xpath('''//*[@id="jslidernews3"]/div[1]/div/ul/li[1]/div/table/tbody/tr''')

kq = {}
for i in row:
    giai = i.find_element_by_css_selector(" td:nth-child(1)").text
    so = i.find_element_by_css_selector(" td:nth-child(2)").text

    kq[giai] = {"so": so}

input = input("Nhap xo so:").strip(' ')

flag = False

for k, v in kq.items():
    if input in v["so"].split(' - '):
        print("Ban da trung: %s" % k)
        flag = True
        break

if not flag:
    print("Chuc may man lan sau")

driver.quit()