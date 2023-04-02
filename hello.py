# PYTHON LISTS:   (LISTS are mutable  --- can be edited once created on the other hand tuples are immutable)

cars = ["audi", "GTR" , "porche" , "ferrari" , "dodge" , "benz"]

me = cars[0]

print(me)

#length of the list printed :
print(len(cars))

# inserting to a list;

cars.insert(2,"Jaguar")

print(cars)

#apending to a list: --> will be done at the last:

cars.append("JEEP")
print(cars)

# concatinating two list:

colour_list = ["blue" , "pink" , "red" ,"yellow" ,"orange"]

x = colour_list + cars

print(x)

# deleting from the end of a LIST;

cars.pop(-1)

print(cars)