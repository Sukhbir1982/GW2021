#Conditional Operators
# ==, !=, >, <, >=, <=

#Logical Operators
# and, or

#Membership Operators
# is, not is

cabFare = 100
wallet = 70
print("Can I Book the Cab:", (cabFare <= wallet))

username = "john@example.com"
password = "password123"
print("User Authenticaion 1:", username == "john@example.com")
print("User Authenticaion 2:", password == "password123")

print("User Authentication for Login:", username == "john@example.com" and password == "password123")

otp = 3027
user_otp = int(input("Enter The OTP: "))
print("OTP Matched:", otp == user_otp)

#Boolean or bool
isInternetOn = True
print("Can I login?", isInternetOn, type(isInternetOn))

print("====Membership====")
a = 10
print(a is 10)
print(a == 10)

name = "Fionna"
print(name == "Fionna")
print(name is "Fionna")
print(name is not "John")

# as of now is and == are performing same
# Assignment: Explore the difference between is and ==
# Hint: HashCodes :)

 