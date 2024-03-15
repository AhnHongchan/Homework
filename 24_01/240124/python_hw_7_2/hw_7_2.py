# 주어진 문자열을 반복 출력하는 StringRepeater 클래스를 작성하시오.
# 클래스에는 반복 횟수와 ㅁ누자열을 인자로 받아 문자열을 반복 출력하는 repeat_string 메서드가 포함되어야 한다.

class StringRepeater:
    def repeat_string(self, num, string):
        for i in range(num):
            print(string)


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
