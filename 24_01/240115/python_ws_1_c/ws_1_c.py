password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# 아래에 코드를 작성하시오.
lst = list(password)
first_char = ''.join(lst[28:36])
second_word = ''.join(lst[113:118])
third_word = ''.join(lst[68:65:-1])
fourth_word = ''.join(lst[325:321:-1])
fifth_word = ''.join(lst[365:371])

print(f'{first_char}{second_word} {third_word} {fourth_word} "{fifth_word}".')