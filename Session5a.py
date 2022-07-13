# MODEL
# Data Structure for Covid19 Cases
# For Data Please Refer: https://data.covid19india.org/data.json

# CONTROLLER | Logical Processing on Data
# Filtering
#      filter by shoe size
#      filter by shoe color[black and green]
#   Searching
#       To loop up for some item in collection
#   Sorting
#       may be ascending or descending based on an attribute

state1 = {
			"active": 3761,
			"confirmed": 72160,
			"deaths": 1235,
			"recovered": 67164,
			"state": "Meghalaya",
}
state2 = {
			"active": 8880,
			"confirmed": 48711,
			"deaths": 184,
			"recovered": 39647,
			"state": "Mizoram",
}
state3 = {
			"active": 1153,
			"confirmed": 29195,
			"deaths": 605,
			"recovered": 26601,
			"state": "Nagaland",
}
state4 = {
			"active": 9020,
			"confirmed": 995433,
			"deaths": 7006,
			"recovered": 979407,
			"state": "Odisha",
}
state5 = {
			"active": 892,
			"confirmed": 122331,
			"deaths": 1805,
			"recovered": 119634,
			"state": "Puducherry",
}
state6 = {
			"active": 557,
			"confirmed": 599972,
			"deaths": 16344,
			"recovered": 583071,
			"state": "Punjab",
}
state7 = {
			"active": 180,
			"confirmed": 953954,
			"deaths": 8954,
			"recovered": 944820,
			"state": "Rajasthan",
}
state8 = {
			"active": 2068,
			"confirmed": 28726,
			"deaths": 361,
			"recovered": 26018,
			"state": "Sikkim",
}
state9 = {
			"active": 1538,
			"confirmed": 81308,
			"deaths": 778,
			"recovered": 78929,
			"state": "Tripura",
}
state10 = {
			"active": 20370,
			"confirmed": 2590632,
			"deaths": 34547,
			"recovered": 2535715,
			"state": "Tamil Nadu",
}

# List of Dictionaries
india = [state1, state2, state3, state4, state5, state6, state7, state8, state9, state10]
print("Length of India is:", len(india))
print()
again_choice = "yes"
while again_choice == "yes":
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Press 1 for filtering COViD-19 Data with 2 filters")
    print("Press 2 for Search by State")
    print("Press 3 for Sorting the Cases with 1 filter")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    choice = int(input("What's Your Choice:"))

    if choice == 1:
        # 1. Filtering the data from Collection as expected by User
        filter1 = input("Please Enter 1st Filter from [active],[confirmed],[deaths],[recovered],[state]:")
        filter2 = input("Please Enter 2nd Filter from [active],[confirmed],[deaths],[recovered],[state]:")

        for i in range(0, len(india)):
            print("{} : {} \n{} : {}".format(filter1.upper(), india[i][filter1], filter2.upper(), india[i][filter2]))
            print("~~~~~~~~~~~~~~~~~~~")
            print()

    elif choice == 2:
        # 2. Searching from the Data | Linear Search
        state = input("Enter the name of state to search:")
        for i in range(0, len(india)):
            print("Matching {} with {}".format(state, india[i]["state"]))
            if state.lower() == india[i]["state"].lower():
                print("State {} found. Details are below:".format(state))
                print(india[i])
                break

    elif choice == 3:
        # 3. Sort the data | Buuble Sort on active cases field
        sort_filter = input("Enter Sorting Field [active],[confirmed],[deaths],[recovered]:")
        n = len(india)  # n is 9
        for i in range(0, n):  # 0, 1, 2, 3, 4
            # i = 0, j =[4], 0, 1, 2, 3
            # i = 1, j =[3], 0, 1, 2
            # i = 2, j =[2], 0, 1
            # i = 3, j =[1], 0
            # i = 4, j =[0]
            for j in range(0, n - i - 1):
                if india[j][sort_filter] > india[j + 1][sort_filter]:
                    # Swap the Elements
                    india[j][sort_filter], india[j + 1][sort_filter] = india[j + 1][sort_filter], india[j][sort_filter]
        print("Sorted as per {} cases:", format(sort_filter))
        for i in range(0, n):
            print("~~~~~~~~~~~~~~~~~~~")
            print("{} : {}\n{} : {}".format("State".upper(), india[i]["state"], sort_filter.upper(), india[i][sort_filter]))
    #       print("~~~~~~~~~~~~~~~~~~~")
            print()

    else:
        print("Not a valid choice")
    again_choice = input("Would you like to Again use the Program(yes/no):")
"""
# Assignment: Linear Search goes from 0 to n-1 for n elements and for last element it will take more time as n grows
#             Explore how Binary Search works
"""