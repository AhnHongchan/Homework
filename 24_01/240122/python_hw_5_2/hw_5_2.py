# 주어진 문자열에서 특정 문자의 개수를 세는 count_character 함수를 작성하시오.
# 문자열과 대상 문자를 인자로 받아 개수를 반환해야 한다.
def count_character(stc, char):
    stc_count = stc.count(char)

    return stc_count
    


result = count_character("Hello, World!", "o")
print(result)  # 2
