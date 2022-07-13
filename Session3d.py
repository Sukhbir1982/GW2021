#Multi Value Container
#Dictionary in Python also known as Map
#Stores Data as Key Value Pair

restaurant = {
    "name":"Gopal Sweets",
    "reviews":4.3,
    "Categories":["Mithai","Indian","Bakery","Fast Food"],
    "time_to_deliver":41,
    "promocode":"CRAVINGS",
    1:"1356"
}

"""print(restaurant)
print(type(restaurant))
print(len(restaurant)) # is number of keys in dictionary
"""
#We can have any type of key or any type of value
#Homo or Hetero

dish1 = {
    "name":"Gujiya",
    "price":125
}
dish2 = {
    "name":"Khoya Burfi",
    "price":150
}
dish3 = {
    "name":"Milk Cake",
    "price":200
}
dishes = [dish1, dish2, dish3]

#Adding Key Later and its a key containing list of dictionaries
restaurant["dishes"] = dishes

print(restaurant)

#Assignment : Replicate any of the Amazon web page with products