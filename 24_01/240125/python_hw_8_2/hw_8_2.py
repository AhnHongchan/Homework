# 아래 함수를 수정하시오.
def check_number(num):
    try:
        if int(num) > 0:
            print('양수입니다.')
        elif int(num) == 0:
            print('0입니다.')
        elif int(num) < 0:
            print('음수입니다.')
    except:
        print('잘못된 입력입니다..')
        print('다시 시도하세요')

num = input('숫자를 입력하세요: ')
check_number(num)
