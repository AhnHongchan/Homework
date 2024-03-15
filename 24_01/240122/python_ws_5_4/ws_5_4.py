# 주어진 문자열에서 모든 단어의 첫 글자를 대문자로 변경하는 capitalize_words 함수를 작성하시오.
# 문자열을 인자로 받아 모든 단어의 첫 글자를 대문자로 변경한 문자열을 반환해야 한다.

def capitalize_words(text):
    ttl = text.title()
    return ttl


result = capitalize_words("hello, world!")
print(result)
