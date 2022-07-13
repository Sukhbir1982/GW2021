johnsFollowers = {"kia","sim","leo","mike","dave"}
fionnasFollowers = {"john","kia","lee","ana","mike","dave"}

#Mutual friends/followers
mutualFollowers = johnsFollowers.intersection(fionnasFollowers)

print("JOHN")
print(johnsFollowers,len(johnsFollowers))

print("FIONNA")
print(fionnasFollowers,len(fionnasFollowers))

print("MUTUAL")
print(mutualFollowers,len(mutualFollowers))
