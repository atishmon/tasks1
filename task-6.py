#Problem 6----------------------------------------------------------------------------------------------------------------

'''sets it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24]

Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set'''
#Solution -----------------------------------------------------------------------------------------------------------------
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = (19, 22, 24, 20, 25, 26)
B = (19, 22, 20, 25, 26, 24, 28, 27)
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Finding the length of the set it_companies with the help of len() funtion.
print (len(it_companies))
#Adding 'Twitter' to it_companies
it_companies.update({"Twitter"})
print (it_companies)
#Removing one of the companies from the set it_companies.
it_companies.remove("Google")
print (it_companies)
#Join A and B
C=A+B
print (C)
# i am making two new  dictionary a,b  
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}

#Find A intersection B
#intersection occur in the dictionary not in the tuples.
print(a.intersection(b))
#Is A subset of B
print('A is subset of B:', a.issubset(b))
#Are A and B disjoint sets
# checks if set A and set B are disjoint
print(a.isdisjoint(b))
#Join A with B and B with A.
C=A+B
print(C)
#What is the symmetric difference between A and B.
symmetry = a.symmetric_difference(b)
print (symmetry)
#Delete the sets completely
del a 
del b 
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
umar=set(age)
print("Set of uniqueNames:",umar)