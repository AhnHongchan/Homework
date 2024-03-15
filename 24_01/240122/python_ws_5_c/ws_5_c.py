def restructure_word(word, arr):
    for i in word:
        if i.isdecimal() == True:
            for j in range(int(i)):
                arr.pop()
        else:
            arr.remove(i)
    return arr

        





original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
arr.extend(list(original_word))
print(arr) # ['코', '딩', ' ', '공', '부', '는', 'ㄴ', ' ', '1', '일', 'ㄹ', ' ', '1', '커', 'ㅓ', '밋', 'ㅅ', ' ', '@', '@', '@', '#', '^', '(', ')', '#', '_', '+', '!', '&', '~', ':', '"']


result = restructure_word(word, arr)
print(result)

final = ''.join(result)
print(final)