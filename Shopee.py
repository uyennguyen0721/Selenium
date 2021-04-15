from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="venv/chromedriver.exe")
driver.get("https://shopee.vn/APPLE-col.678255")


urls = driver.find_elements_by_css_selector(".shopee-search-item-result__item > a")[:5]
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

    comments = driver.find_elements_by_class_name("shopee-product-rating__content")
    for comment in comments:
        print(comment.text)


driver.quit()
