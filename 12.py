from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# 웹 드라이버 실행
driver = webdriver.Chrome()
지역명 = '응암동'
url = f'https://map.naver.com/p/search/{지역명}%20스터디카페?c=12.00,0,0,0,dh'
driver.get(url)
time.sleep(5)

try:
    # **1. searchIframe으로 전환**
    driver.switch_to.frame('searchIframe')

    # **2. iframe 안쪽 클릭 (활성화)**
    driver.find_element(By.CSS_SELECTOR, 'div.Ryr1F').click()

    # **3. 스크롤 전 리스트 개수 확인**
    prev_count = len(driver.find_elements(By.CSS_SELECTOR, 'li.VLTHu'))
    print(prev_count)
    while True:
        # **4. PAGE_DOWN 키로 스크롤 수행**
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
        time.sleep(2)  # 페이지 로딩 대기

        # **5. 스크롤 후 리스트 개수 확인**
        new_count = len(driver.find_elements(By.CSS_SELECTOR, 'li.VLTHu'))
        print(f"📜 스크롤 후 리스트 개수: {new_count}")

        # **6. 리스트 변화가 없으면 종료**
        if new_count == prev_count:
            print("🚫 더 이상 새로운 리스트가 없습니다. 스크롤 종료!")
            break

        # 개수 갱신
        prev_count = new_count

    # **7. 최종 결과 출력**
    cafes = driver.find_elements(By.CSS_SELECTOR, 'li.VLTHu')
    print(f"\n🎯 최종 스터디카페 개수: {len(cafes)}")
    name_case = []
    location_case = []
    for idx, cafe in enumerate(cafes, start=1):
        name = cafe.find_element(By.CSS_SELECTOR, 'span.YwYLL').text
        location = cafe.find_element(By.CSS_SELECTOR, 'span.Pb4bU').text
        name_case.append(name)
        location_case.append(location)
except Exception as e:
    print(f"❌ 오류 발생: {e}")

finally:
    driver.quit()


print(name_case)
print(location_case)

data = pd.DataFrame({"studycafename":name_case,"lcation":location_case})

data.to_csv(f'은평구{지역명}스터디카페.csv', index=False, encoding='utf-8-sig')