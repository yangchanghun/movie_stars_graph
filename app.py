from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from multiprocessing.pool import ThreadPool
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%A4%91%EC%9D%B8+%EC%98%81%ED%99%94"
driver.get(url)

time.sleep(2)
태그정보 = 'div.card_item'
group = driver.find_elements(By.CSS_SELECTOR,태그정보)

총영화이름 = []
총평점 = []




"""def attendance(i):
    총관객수 = []

    # 현재페이지영화이름= []
    # 관객수 정보 담기
    # multi =ThreadPool(12)
    try:
        # 요소가 클릭 가능할 때까지 대기
        url = i
        driver = webdriver.Chrome()
        driver.get(url)

        time.sleep(2)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.item_link'))
        )

    # href 속성 가져오기
        element.click()
        time.sleep(2)
        숫자 = driver.find_elements(By.CSS_SELECTOR, 'span.this_text_bold')
        단위 = driver.find_elements(By.CSS_SELECTOR, 'span.this_text_normal')
        print(f"{숫자[2].text},{단위[1].text}, url:{url}")


    except Exception as e:
        print(f"오류 url:{url}")
"""

#처음 페이지 크롤링



for i in group:
    이름정보 = 'a.this_text'
    별점정보 = 'span.num'
    영화이름 = i.find_element(By.CSS_SELECTOR, 이름정보)

    총영화이름.append(영화이름.text)
    try:
        영화별점 = i.find_element(By.CSS_SELECTOR, 별점정보)
        총평점.append(영화별점.text)
    except:
        총평점.append(0)


클릭태그 = driver.find_element(By.CSS_SELECTOR,'a.pg_next')
try:
    while 클릭태그:
        클릭태그.click()
        time.sleep(4)
        태그정보 = 'div.card_item'
        group = driver.find_elements(By.CSS_SELECTOR,태그정보)
        for i in group:
            이름정보 = 'a.this_text'
            별점정보 = 'span.num'
            영화이름 = i.find_element(By.CSS_SELECTOR, 이름정보)
            총영화이름.append(영화이름.text)
            try:
                영화별점 = i.find_element(By.CSS_SELECTOR, 별점정보)
                총평점.append(영화별점.text)
            except:
                총평점.append(0)

except:
    print("이제 클릭 할거 없음")



import pandas as pd

데이터 = pd.DataFrame({
    '영화이름': 총영화이름,
    '평점': 총평점
})


데이터.to_csv('자자.csv', index=False, encoding='utf-8-sig')
