#problem 1 ----------------------------------------------------------------------------------------------------------------------------
'''Declare an empty list
Declare a list with more than 5 items
Find the length of your list
Get the first item, the middle item and the last item of the list
Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
Print the list using print()
Print the number of companies in the list
Print the first, middle and last company
Print the list after modifying one of the companies
Add an IT company to it_companies
Insert an IT company in the middle of the companies list
Change one of the it_companies names to uppercase (IBM excluded!)
Join the it_companies with a string '#;  '
Check if a certain company exists in the it_companies list.
Sort the list using sort() method
Reverse the list in descending order using reverse() method
Slice out the first 3 companies from the list
Slice out the last 3 companies from the list
Slice out the middle IT company or companies from the list
Remove the first IT company from the list
Remove the middle IT company or companies from the list
Remove the last IT company from the list
Remove all IT companies from the list
Destroy the IT companies list
Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express']'''
#Solution ------------------------------------------------------------------------------------------------------------------------------
a1=[]#1 empty list
a=["Bohemia",169,140,33,34.3,54,420]#2 second list with more then 5 elements
print (len(a))#3printing the lenth of the list in int value
print(a[-1],a[0])#4.1printing first and the last value of the list
#4.2finding the middle value of the list and then printing the value.
l=len(a)
mid=int((l-0)/2)
print(mid)
print(a[mid])
#5declaring the list named mixed_data_types 
mixed_data_types=["Atish",27,5.6,"unmarried","delhi"]
#6declaring the list named it_companies
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print (it_companies)#7printing the list.
print (len(it_companies))#8printing the number of companies.
print(it_companies[0],it_companies[-1],it_companies[3]) #9printing first ,mid  and the last value of the list.
it_companies.append("smartcoderz")
print (it_companies)#10printing the list
it_companies.append("company.Inc")
print (it_companies)#11printing the list
it_companies.insert(5,"Atish")#12inserting the value at any position in the list.
print (it_companies)#13printing the list.
print (it_companies[3].upper())#14converthing one the the IT company name in the upper case.
#15join the it_companies with a string "#"
for i in it_companies :
    print ("#",i)#this will show the list in vertical way.
  #  print ("#",i,end='')# another way to show list in a single line
#finding if the company exist or not.
a2=input("Enter the company name : ")
if a2 in it_companies:
    print("company exist in our list")
else:
    print("not exist ! ")
# sorting the list in accending order.
it_companies.sort()
print (it_companies)
# sorting the list in the desending order.
it_companies.reverse()
#Sliceing out the list jumps 3 index at a time continue till END of the list.for eg:- list[1,2,3,4,5,6,7,8,9,10,11,12]
#output of this list will be list=[1,4,7,10].
print (it_companies)
print(it_companies[::3])
#Slice out the first 3 companies from the list.
print(it_companies)
print(it_companies[0:3])
#Slice out the last 3 companies from the list.
print(it_companies[7:10])
#Slice out the middle companies from the list.
print (it_companies[4:6])
#Remove the first IT company from the list.
it_companies.pop(0)
print (it_companies)
#Remove the middle IT company or companies from the list.
it_companies.pop(4)
print (it_companies)
#Remove the last IT company from the list.
it_companies.pop(-1)
print (it_companies)
#Removing all the left companies name from the list.
it_companies.clear()
print(it_companies)
#destroying the it_companies list.
del it_companies
#here i am to trying to print the list name  that recently have been deleted in the last code.
try:
  print (it_companies)
except:
  print ("name it_companies is not defined")

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express',]
front_end.extend(back_end)
print(front_end)
