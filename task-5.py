#Problem 5----------------------------------------------------------------------------------------------------------------

'''Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary.
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries'''
#Solution -----------------------------------------------------------------------------------------------------------------
#Create an empty dictionary called dog.
dog={"name":"scooby","color":"brown","breed":"germenshepherd","age":"2yeaars" }
#Create an empty dictionary called student.
student={"first_name":"sachin","last_name":"panwar","gender":'male',"age":22,"marital status": "unmarried","country":"india","skill":"c,python"}
#Get the length of the student dictionary
print("total length of student dictionary ",len(student))
#Get the value of skills and check the data type, it should be a list
print(student["skill"])
print(type(student))
#Modify the skills values by adding one or two skills
student.update({'skill':"java, mysql, dbms"})
print (student)
#Get the dictionary keys as a list
print(student.keys())
#Get the dictionary values as a list.
print(student.values())
#Change the dictionary to a list of tuples using items() method
list=list(student.items())
print (list)
#Delete one of the items in the dictionary
student.pop("last_name")
print (student)
del dog #del dog simply deletes the dog dictionary.