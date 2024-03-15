for tc in range(1, 11):
    length, password = input().split()
    length = int(length)
    new_password = []

    for number in password:
        if new_password:
            if number == new_password[-1]:
                new_password.pop()
            else:
                new_password.append(number)
        else:
            new_password.append(number)
    
    print(f"#{tc}", ''.join(new_password))