# 파이썬의 딕셔너리 데이터 타입이 가진 메서드를 연습하고자 한다.

data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}
# 1. data가 가진 모든 키와 벨류 목록을 출력한다.

# 2. data가 가진 벨류 목록들만 모아서 출력한다.

# 3. data에서 'without' 키가 가진 value를 출력한다.
    # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.

# 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.

# 5. 변경된 data를 출력한다.

print(data.items())
print(data.values())
data.setdefault('without', 'unknown')
print(data['without'])
data.update(plus_data)
print(data)