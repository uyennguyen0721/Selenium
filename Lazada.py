from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="venv/chromedriver.exe")
driver.get("https://www.lazada.vn/dien-thoai-di-dong/?spm=a2o4n.home.cate_1.1.47ee6afecemFB7")

driver.execute_script("window.scroll(0, 1200)")
time.sleep(1)

urls = driver.find_elements_by_css_selector(".cRjKsc > a")[:5]
urls = [url.get_attribute("href") for url in urls]

for url in urls:
    print("=== ", url)
    driver.get(url)

    driver.execute_script("window.scroll(0, 1200)")
    time.sleep(1)

    driver.execute_script("window.scroll(0, 2000)")
    time.sleep(1)

    driver.execute_script("window.scroll(0, 3000)")
    time.sleep(1)

    driver.execute_script("window.scroll(0, 4000)")
    time.sleep(1)

    driver.execute_script("window.scroll(0, 5000)")
    time.sleep(1)

    driver.execute_script("window.scroll(0, 6000)")
    time.sleep(1)

    driver.execute_script("window.scroll(0, 7000)")
    time.sleep(1)

    driver.execute_script("window.scroll(0, 8000)")
    time.sleep(1)

    comments = driver.find_elements_by_class_name("content")
    for comment in comments:
        print(comment.text)

driver.quit()
