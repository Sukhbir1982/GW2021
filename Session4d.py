restaurant1 = {
    "title" : "Nik Bakers",
    "timeToDeliver" : 60
}
restaurant2 = {
    "title" : "Just Laid Eggs",
    "timeToDeliver" : 50
}
restaurant3 = {
    "title" : "Gopal Sweets",
    "timeToDeliver" : 120
}
restaurant4 = {
    "title" : "Table By Basant",
    "timeToDeliver" : 30
}
restaurant5 = {
    "title" : "Ice Cream Studio",
    "timeToDeliver" : 45
}

# List of Dictionaries
# Indexes           0           1           2           3               4
restaurants = [restaurant1, restaurant2, restaurant3, restaurant4, restaurant5]
print("Restaurants:", restaurants)
"""
print(restaurants[0])
print(restaurants[1])
print(restaurants[2])
print(restaurants[3])
print(restaurants[4])
"""
 # i will vary from 0 to 4 i.e. i will become 0, 1, 2, 3 and 4
for i in range(0, 5):
#     print(restaurants[i])
    print(restaurants[i]['title'],"\t", restaurants[i]['timeToDeliver'] )
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Filter restaurants on the basis of time < 50 mins
print("Restaurants Delivery in less than 50 mins:")
for i in range(0, 5):
    if restaurants[i]['timeToDeliver'] <= 50:
        print(restaurants[i]['title'], "\t", restaurants[i]['timeToDeliver'])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
""" Assignment: COVID19 case study | https://data.covid19india.org/data.json

    covid19_punjab = {
			"active": 557,
			"confirmed": 599972,
			"deaths": 16344,
			"deltaconfirmed": "30",
			"deltadeaths": "2",
			"deltarecovered": "48",
			"lastupdatedtime": "13/08/2021 23:27:22",
			"migratedother": "0",
			"recovered": 583071,
			"state": "Punjab",
			"statecode": "PB",
			"statenotes": ""
		}
    Evaluate and give results;
    1. State with max deaths cases
    2. State with max active cases
    3. State with max confirmed cases
    4. State with max recovered cases
"""