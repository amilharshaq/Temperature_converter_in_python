choice = int(input("Enter 1 to covert CELSIUS TO FAHRENHEIT\n"      
               "      2 to CONVERT FAHRENHEIT TO CELSIUS \n "
               "     3 to CONVERT CELSIUS TO KELVIN \n "
               "     4 to CONVERT KELVIN TO CELSIUS \n "
               "     5 to CONVERT FAHRENHEIT TO KELVIN \n "
               "     6 to CONVERT KELVIN TO FAHRENHEIT  \n "
               "Enter the value :"))

if choice==2 or choice==5 :
    temp = float(input("Enter temperature in Fahrenheit :"))
elif choice==1 or choice==3 :
    temp = float(input("Enter temperature in Celsius :"))
elif choice==4 or choice==6 :
    temp = float(input("Enter temperature in Kelvin :"))    
else :
    print("please check the number you enterd")

def to_fahrenheit1() :
    fahrenheit = (temp*1.8)+32 
    print("Temperature in fahrenheit =",fahrenheit,"°F")

def to_celsius1() :
    celsius = (temp - 32) * .5556
    print("Temperature in celsius =",celsius,"°c")

def to_kelvin1() :
    Kelvin = temp + 273.15
    print("Temperature in kelvin =",Kelvin,"K")

def to_celsius2() :
    celsius2 = temp - 273.15  
    print("Temperature in celsius =",celsius2,"°c")   

def to_kelvin2() :
    kelvin2 = (temp - 32) * (5/9) + 273.15
    print("Temperature in kelvin =",kelvin2,"°c")  

def to_fahrenheit2() :
    fahrenheit2 = (temp - 273.15)*(9/5) + 32
    print("Temperature in fahrenheit =",fahrenheit2,"°c")  

def convert():
    if choice==1:
        to_celsius1()
    elif choice==2 :   
        to_fahrenheit1()  
    elif choice==3 :
        to_kelvin1() 
    elif choice==4 :
        to_celsius2()
    elif choice==5 :
        to_kelvin2()
    elif choice==6 :
        to_fahrenheit2()                    

convert()