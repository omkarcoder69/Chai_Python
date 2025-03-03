# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

userPassword = input("Enter your password")
if len(userPassword)<=6:
    print("password is weak")
elif len(userPassword)>=6 and  len(userPassword)<=10:
    print("password is medium")
elif len(userPassword)>=10:
    print("password is strong")
else:
    print("Enter proper choice")