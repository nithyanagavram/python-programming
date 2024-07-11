import random

def generate_password(length, complexity):
    if complexity == "low":
        characters = "abcdefghijklmnopqrstuvwxyz"
    elif complexity == "medium":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif complexity == "high":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    else:
        return "Invalid complexity level"

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


password = generate_password(10, "medium")
print(password)
