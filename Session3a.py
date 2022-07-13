followers = ["John", "Jennie", "Fionna", "Dave", "Kia"]
print(followers, type(followers), len(followers))

#Update id of a follower
followers[0] = "John.Watson"
print(followers, type(followers), len(followers))

#Delete a follower from a list
del followers[3]
print(followers, type(followers), len(followers))

#Add new follower
followers.append("Harry")
followers.append("George")
followers.append("Kim")
print(followers, type(followers), len(followers))