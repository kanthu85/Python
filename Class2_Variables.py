#variable is a container(box) we put our value
x=3
y=4
print(x+y)
print(x+5)
print(y-2)
#_+5 is working in command prompt(here _ is to fetch previous statement output as input to immediat next statement)
#print(_+5)
# working with string variables
str="string"
#print(str +5) #TypeError: can only concatenate str (not "int") to str
print(str+'5') #now both str and 5 are strings(encoading in quots is considered as string)
Firstname ="sreekanth Reddy"
print(Firstname+" Lakkireddy")
Lastname=" LakkiReddy"
print(Firstname+Lastname)

#String is a collection of characters, there is no char datatype in Python
fullName =Firstname+Lastname
print(fullName[0]) #string index start from 0
lst =[i for i in fullName] #print Full name as list
print(lst)
for i in fullName: #Iterate string
    print(i)
#print(fullName[50]) #IndexError: string index out of range(through error if excceds index range)
#slicing on string [start:stop:step] (eg:[0:(n-1): skipcount after printchar])
#step negative means start is -1(it will reverse string)
slic=fullName[:50] #we can avoid above out of range index by slicing
print(slic)

#working on Slicing
string="Welcome"
print(string[0:2]) #In slicing end index will not include(#output we 
print(string[0:2:2]) #output w
print(string[0:3:2]) #output wc
print(string[::-1]) #output emocleW
print(string[:-1])#putput: welcom
print(string[-1:])#output: e
print(string[-1:-5:-1])#output: emoc
print(string[-1:-5:-2])#output: eo
print(string[:-5:-2])#output: eo
print(string[:-5:])#output: we

#Try to append/replace string chars From 'YOU' to 'MY' we will get error "object does not support item assignment"
#strings in python is immutable(we can not change/modify string value)
immuteString ='YouTube'
#immuteString[0:1]='My' #TypeError: 'str' object does not support item assignment
#but to print we use slicing and add string before and after.
print('My'+immuteString[3:7]) #output: MyTube

#String Length -The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#Check String -To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#---------------Continue With String Methods in Next Class------------