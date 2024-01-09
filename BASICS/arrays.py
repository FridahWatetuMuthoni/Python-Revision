users = ["Dave","John", "Sara"]

#Checking if a value is in a list

if 'Dave' in users:
    print("Dave is in the data list")
else:
    print("Dave is not in the data list")

data = ["Dave", 42, True,"Dave","John", "Sara"]

print(data[-1])
print(data[-2])
print(data.index('Sara'))
print(len(data))

users.append("Elsa")
users.extend(['Robert','Jimmy', 'Jason'])
print(users)

users.insert(0, "Bob")
print(users)

users.remove('Bob')
print(users)

deleted_user = users.pop()
print(deleted_user)

#emptying a list
data.clear()
