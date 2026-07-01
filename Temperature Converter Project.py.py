#TEMPERATURE CONVERTER PROJECT
print("Hello Welcome To Temperature Converter Project")
print("/Menu")
print("(1)Celsius into Fahrenheit")
print("(2)Fahrenheit into Celsius")
print("(3)Celsius into Kelvin")
print("(4)Kelvin into Celsius")
print("(5)Exit")
# first we will ask about input from user
user_choice=int(input("choose any option between 1,2,3,4, 5:"))

if user_choice not in[1,2,3,4,5]:
    print("Invalid choice chose between the available options ")

elif user_choice==1:
    # here we will take input from user in differnt temperatures
    temp=int(input("Enter the temperature in Celcius:"))
    converted_temp=(temp *9/5)+32
    print(f"{temp}C)={converted_temp}F")
elif user_choice==2:
    temp=int(input("Enter the temperature in Farheniet:"))
    converted_temp=(temp -32)*5/9
    print(f"{temp} F)={converted_temp}C")
elif user_choice==3:
    temp=int(input("Enter the temperature in Celcius:"))
    converted_temp=(temp+273.15)
    print(f"{temp}C)={converted_temp}K")
elif user_choice==4:
    temp=int(input("Enter the temperature in Kelvin:"))
    converted_temp=(temp-273.15)
    print(f"{temp}K)={converted_temp}C")
elif user_choice==5:
    print("Exit bro tata by by")
use_again=input("do you want to convert again(yes/no):").lower()
if use_again!= "yes":
    print("Thanks for using temperature converter")

