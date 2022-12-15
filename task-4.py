#Problem 4----------------------------------------------------------------------------------------------------------------
'''The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
If the fruit exists print('That fruit already exist in the list')'''
#Solution -----------------------------------------------------------------------------------------------------------------

fruits = ['banana', 'orange', 'mango', 'lemon']
customer=input("Enter A Fruit Name :")
if customer.lower() in fruits:
    print ("That fruit already exist in the list")
elif customer.lower()  not in fruits:
    fruits.insert(0,customer)
    print (fruits)