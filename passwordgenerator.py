import string
import random


upper = string.ascii_uppercase

lower = string.ascii_lowercase

punct = string.punctuation

digit = string.digits


elements = list()  #creting empty lists


elements.extend(upper)
elements.extend(lower)
elements.extend(punct)
elements.extend(digit)


random.shuffle(elements)

try: 
    user_ip = int(input("Enter the length of password required : "))

    print("The password is : \n", "".join(elements[0 : user_ip]))

    

except ValueError as e:
    print("You have an value error", e)