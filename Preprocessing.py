import pandas as pd

data = pd.read_csv('은평구스터디카페_통합.csv')

data.drop(columns=['동'], inplace=True)

print(data.groupby(data['lcation']).count())

# 중복 데이터 제거
data.drop_duplicates(subset=['studycafename', 'lcation'], keep='first', inplace=True)
# 'lcation' 열 기준으로 정렬하고 상위 10개만 출력
data.to_csv('중복제거후.csv',index=False, encoding='utf-8-sig')

