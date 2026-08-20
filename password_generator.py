import random
import string

print("🔐 مولد كلمة السر القوية")

length = int(input("عايزة كلمة السر كام حرف؟ "))

letters = string.ascii_letters  # a-z A-Z
numbers = string.digits         # 0-9
symbols = string.punctuation    # !@#$%

all_chars = letters + numbers + symbols

password = ""
for i in range(length):
    password += random.choice(all_chars)

print(f"كلمة السر بتاعتك هي: {password}")
print("اوعي تنسيها 😂")
