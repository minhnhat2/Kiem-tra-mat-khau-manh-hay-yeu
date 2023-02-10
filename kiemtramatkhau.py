import random

def suggest_password(password):  
    uppers = [c for c in password if c.isupper()]
    lowers = [c for c in password if c.islower()]
    digits = [c for c in password if c.isdigit()]
    specials = [c for c in password if not c.isalnum()]

    new_password = ""
    for _ in range(len(password)):
        char_group = random.choice([uppers, lowers, digits, specials])
        if char_group:
            new_password += random.choice(char_group)
        else:
            new_password += random.choice(uppers + lowers + digits + specials)

    return new_password

def check_password_strength(password):
    n = len(password)
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    normal_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    
    for i in range(n):
        if password[i] not in normal_chars:
            has_special = True
        if password[i].islower():
            has_lower = True
        if password[i].isdigit():
            has_digit = True
        if password[i].isupper():
            has_upper = True
        
    print("Mật khẩu của bạn là ", end="")
    if (has_lower and has_upper and has_digit and has_special and n >= 8):
        print("mạnh")
    elif ((has_lower or has_upper) and has_digit and n >= 6):
        print("trung bình")
    else:
        print("yếu")
        print("Đề xuất mật khẩu mới:", suggest_password(password))

if __name__ == "__main__":
    password = input("Nhập mật khẩu của bạn: ")
    check_password_strength(password)
