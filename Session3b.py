followers = {"John", "Jennie", "Fionna", "Dave", "Kia"}
print(followers, type(followers), len(followers))

#Set wont support duplicates
#Set add the data with hashing and hence we cannot see the output the way we added
#It shall come as per the buckets

#Add Data
followers.add("Fionna")
followers.add("George")
followers.add("Harry")
followers.add("Kia")
print(followers, type(followers), len(followers))

#Remove Data
followers.remove("Kia")
print(followers, type(followers), len(followers))

followers.add("Kia")
#followers[2].update("John.Watson")
print(followers, type(followers), len(followers))