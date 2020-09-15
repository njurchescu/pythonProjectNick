lucky_numbers = [4, 23, 42, 16, 8]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

# friends.extend(luck_numbers)  # appends lucky_numbers at the end of friends
friends.append("Creed")  # adds a new element at the end of the list
friends.insert(1, "Kelly")  # adds new element at specific index
# friends.remove("Jim")  # removes "Jim" element
# friends.clear()  # removes all the elements
friends.pop()  # removes the last element in the list (Creed)
# print(friends.index(42))  # prints index of specific element
friends.sort()  # alphabetically order
lucky_numbers.sort()
lucky_numbers.reverse()  # reverses the order of the list
# print(friends.count("Jim"))  # counts number of times Jim appears

friends2 = friends.copy()  # makes a copy of the exact same list
print(friends)
print(lucky_numbers)

