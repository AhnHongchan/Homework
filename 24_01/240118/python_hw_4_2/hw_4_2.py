list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

all_books = True
for book in rental_list:
    if book in list_of_book:
        continue
    else:
        print(f'{book}은/는 보유하고 있지 않습니다.')
        all_books = False
        break
if all_books:
    print('모든 도서는 대여 가능한 상태입니다.')
