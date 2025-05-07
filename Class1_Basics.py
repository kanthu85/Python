print(2+3)#add 2 numbers
print(9-8)#substract 2 numbers
print(4*6)#multiple 2 numbers
print(0/4)#divide 2 numbers
print(5/2) #divide 2 numbers with quitient as float output: 2.5
print(5//2) #divide 2 numbers as integer as output:2--this is called integer division or floor division
print(5%2) #divide 2 numbers with remainder as output:1
print(6+9-10)#math calculation BODMOS
print(8+2*3)#math calculation BODMOS
print((8+2)*3)#math calculation BODMOS
print(2*2*2) #same number repeated calculation
print(2**3) #same number repeated calculation with power of

#working with strings
print('sreekanth')
print("sreekanth's Laptop")
print('Sreekanth "Laptop"')
print("Sreekanth's \"Laptop\"")
print('C:\docs\naresh') #\n is escape character so, c:/docs and aresh in 2 lines
#This way, the backslashes are not interpreted as escape characters, and the string is printed exactly as it is. used for "paths"
print(r'C:\docs\naresh')
print(r"Sreekanth's \"Laptop\"") 
raw_string = r"This is a raw string with a newline character: \n and a tab character: \t"
print(raw_string)
#print string Multiple times
print('sreekanth '*10)
#print with comma seperated (string  and calculation in print)
sum =3+4
print("sum of 3+4 is ",sum)
#print with input value input is always a string so, converting x,y to integer.
x=int(input("enter X value:"))
y=int(input("enter y value:"))
#using formated string literals(f-strings)
print("sum of {1} and {0} is:".format(y,x), x+y) 
print(f"sum of {x} and {y} is:", x+y)
