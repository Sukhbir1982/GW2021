"""
i = 0
print("While Loop")
while i <= 10:
    print("i is:",i)
    i += 2 # increment i by 1

# No do-while loop in Python
print("For Loop")
#for i in range(1, 11):
for i in range(1, 11, 2):
    print("i is:",i)

# Nested Loops
print("Nested Loop")
for i in range(1, 6): # i: 1, 2, 3, 4, 5
    print(">> i is:",i)

    for j in range(1, 4): # j: 1, 2, 3
        print(j, end=" ")
    print()
"""
# Break and Continue
"""print("BREAK")
my_floor = int(input("Enter Floor:"))
total_floors = 10
start = 1
for floor in range(start, total_floors+1):
    print("Floor Number:", floor)
    if floor == my_floor:
        print("~~~~~~~~~~~~~~~~")
        print("My Floor Arrived:", my_floor)
        print("~~~~~~~~~~~~~~~~")
        break # Terminates the Loop
"""
print("CONTINUE")
for i in range(1, 11):
    if i <=5:
        continue
#    print("i is:", i)
    print("{} * {} = {}".format(5, i, (5*i)))

# Assignment:
# 1. Explore if we have labels in python in loops
# 2. Write Reverse Loops | From 10 to 1
# 3. Very Closely observe how elevator works and write all those features in code
# 4. Write a real time use case for continue keyword