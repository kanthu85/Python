# to get type of variable use type() function.
x=10
print(type(x)) #output <class 'int'>

#-------------Data types ------------------

#1.Text Data Type ->string (Ex: str='Hello World' or str =str('1') or str ='1'

str = str('1') # or encode number in quote str ='1'
print(type(str))
str ='1' # or encode number in quote str ='1'
print(type(str))

#2.Numeric Types -> int(Ex:- x=5),float(Ex:- y=20.5), Complex(Ex:- z=1J)
x=5
print(type(x))
y=20.5
print(type(y))
z= 1J
print(type(z))

#3.Sequence Datatypes: -> list(EX:- lst=[1,2,3]), tuple(Ex:- tpl=(1,2,3)), Range(Ex:- rng=range(6))

lst=[1,2,3] # list is collection which is ordered and changable.Allows duplicate members
print(type(lst))
tpl=(1,2,3) #Tuple is acollection which is ordered and unchangable/immutable.Allows Duplicate Memnbers.Iteration is faster in tuple compared to list.
print(type(tpl))
rng= range(6) # The range() function in Python generates a sequence of numbers.
print(type(rng))
rng_list= [i for i in rng]
print(rng_list)
rng_sss= range(0,10,2)#range(start, stop, step): Generates a sequence starting from start, incrementing by step until it reaches (but does not include
print(type(rng_sss))
rng_sss_list = [i for i in rng_sss]
print(rng_sss_list)
#4.Mapping Types -> dictionary(EX:- dict={"Name":"Sreekanth","Job":"Data Engineer"})
Map_dict={"Name":"Sreekanth","Job":"Data Engineer"} #Dictionary is a collection which is ordered from python 3.7 version,all pervious versions unordered
print(type(Map_dict))

#5.Set Type ->set(Ex:- st={"apple","banana"} frozenset=({"apple","banana"})
#set is collection which is unordered and unchangable, but can remove and/or add irems.
#In Python, a frozenset is an immutable, unordered collection of unique elements. It is similar to a Python set, but once a frozenset is created, its elements cannot be changed (added or removed). This immutability makes frozenset objects hashable, meaning they can be used as keys in dictionaries or as elements of other sets. 
st={"apple","banana"}
print(type(st))
frozenset=({"apple","banana"}) # freeze set
#6.Boolean Type -> bool(Ex:- t=True, f =False)
t= True
print(type(t))
f= False
print(type(f))
#7.Binary Types -> (Bytes =b'Hello'), byteaeeay(Ex:- bytarray =bytearray(6),memoryview(Ex:- memryview =memoryview(b'5')))
Bytes =b'Hello'
print(type(Bytes))
bytarray =bytearray(6)
print(bytarray)
print(type(bytarray))
memryview =memoryview(b'5')
print(memryview)
print(type(memryview))
#8.NoneType: -> None(Ex:- n=None)
n=None
print(n)
print(type(n))


