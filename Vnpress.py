import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import datetime
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="venv/chromedriver.exe")
driver.get("https://vnexpress.net/chu-de/lai-suat-ngan-hang-3210")

row = WebDriverWait(driver=driver, timeout=530).until(
    ec.presence_of_all_elements_located((By.XPATH, '''//*[@id="box_ls_1"]/div[2]/div[1]/div/ul/li'''))
)

table = {}
for i in row:
    try:
        bank_name = i.find_element_by_css_selector("div:nth-child(1)").text
        one_month = float(i.find_element_by_css_selector("div:nth-child(2)").text.replace(",", "."))
        three_month = float(i.find_element_by_css_selector("div:nth-child(3)").text.replace(",", "."))
        six_month = float(i.find_element_by_css_selector("div:nth-child(4)").text.replace(",", "."))
        nine_month = float(i.find_element_by_css_selector("div:nth-child(5)").text.replace(",", "."))
        year = float(i.find_element_by_css_selector("div:nth-child(6)").text.replace(",", "."))
    except:
        continue
    table[bank_name] = {
        "1": one_month,
        "3": three_month,
        "6": six_month,
        "9": nine_month,
        "12": year
    }

for k, v in table.items():
    print("%s\t%f\t%f\t%f\t%f\t%f\t" % (k, v["1"], v["3"], v["6"], v["9"], v["12"] ))

ngan_hang = table["SCB"]
so_tien = float(input("Nhap so tien: "))
ky_han = (input("Nhap ky han: "))

if ky_han not in ["1", "3", "9", "6", "12"]:
    print("không có kỳ hạn")

ngay_dao_han = (input("Nhap ngay dao han: (dd-mm-yyyy)")).split("-")

def tinh_so_thang(ngay=ngay_dao_han):
    start_date = datetime.datetime.now()
    end_date = datetime.datetime(int(ngay[2]), int(ngay[1]), int(ngay[0]))
    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    return num_months

so_ky_han = math.floor(tinh_so_thang() / int(ky_han))
lai_suat = so_tien * ngan_hang[ky_han] * so_ky_han / 100

print("Lai suat %f, Tong tien nhan: %f" % (lai_suat, so_tien+lai_suat) )