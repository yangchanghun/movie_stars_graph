from selenium import webdriver
from selenium.webdriver.common.by import By

# 드라이버 실행
driver = webdriver.Chrome()
url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bkEw&pkid=68&os=35481329&qvt=0&query=%EB%BD%80%EB%A1%9C%EB%A1%9C%20%EA%B7%B9%EC%9E%A5%ED%8C%90%20%EB%B0%94%EB%8B%B7%EC%86%8D%20%EB%8C%80%EB%AA%A8%ED%97%98%20%EC%A0%95%EB%B3%B4'
driver.get(url)

# 41과 만명 요소 찾기
try:
    숫자 = driver.find_elements(By.CSS_SELECTOR, 'span.this_text_bold')
    단위 = driver.find_elements(By.CSS_SELECTOR, 'span.this_text_normal')

    print(숫자[2].text)
    print(단위[1].text)
except Exception as e:
    print(f"오류 발생: {e}")

driver.quit()
