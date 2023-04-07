# list stores heterogeneous data
number = [23,35,56,123,57,2,5,9]
friends = ["chetan", "jasleen", "madhav","madhav","madhav","madhav","sudhamshu","pranav","bhargav","manohar","karthik"]
# print(friends[2])  # accessing elements
# print(friends)  # printing the whole list
# print(friends[-1])  # negative indexing
# print(friends[2:])
# print(friends[2:6])
# friends[0] = "Anoushka"
print(friends)

friends.append("Bhavya")
print(friends)
friends.insert(1,"spandana")
print(friends)
friends.remove("Bhavya")
print(friends)
friends.pop()
print(friends)
print(friends.index("madhav"))
print(friends.count("madhav"))

number.sort()
print(number)

friends.sort()
print(friends)

number.reverse()
print(number)

friends2 = friends.copy()
print(friends2)