"""
Dictonaries are key, value pairs 
"""
band = {
    "vocals":"Plant",
    "guitar":"Page"
}
print(band)
print(len(band))

#Accessing items in a dict
print(band['vocals'])
print(band.get('guitar'))

#Listing all the keys
print(band.keys())

#Listing all the values
print(band.values())

#List of key/value pairs as tuples
print(band.items())

#verify a key exists
print("guitar" in band)
print("cow" in band)

#changing values
band["vocals"] = "Coverdale"
band.update({"bass":"JPJ"})
print(band)

#Remove items
print(band.pop('bass'))
print(band)

#Removing the last key/pair item added to the dictionary
print(band.popitem())
print(band)

#Deleting an item
band.update({"bass":"JPJ"})
band.update({"guitar":"Page"})
band.update({"drums":"Bonham"})

print(band)
del band["bass"]
print(band)

# clearing the dictionary
band.clear()
print(band)

# deleting the dictonary
del band

band = {
    "vocals":"Plant",
    "guitar":"Page",
    "guitar":"Page",
    "drums":"Bonham"
}

#Copying a dictionary
band2 = band.copy()
print(band2)
band2.update({"bass":"JPJ"})
print(band2)
