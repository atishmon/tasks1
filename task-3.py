#Problem 3----------------------------------------------------------------------------------------------------------------
'''
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, 
the season is Autumn. December, January or February, the season is Winter. March,
 April or May, the season is Spring June, July or August, the season is Summer'''
#Solution -----------------------------------------------------------------------------------------------------------------
#Autumn=["September","October","November"]
#Winter=["December","January","February"]
#Spring=["March","April", "May"]
#Summer= ["july","august"]
print("To Know About The Season Name...")
a=(input("Enter The Month Name (e.g. January, February etc.) : "))
if a.lower() in ["september","october","november"]:
    print ("Season Is Autumn")
elif a.lower() in ["december","january","february"]:
    print ("Season Is Winter")
elif a.lower() in ["March","April", "May"]:
    print ("Season Is Spring")
elif a.lower() in ["july","august"]:
    print ("Season Is Summer")
else:
    print ("Please Enter A Valid Name Of Month")