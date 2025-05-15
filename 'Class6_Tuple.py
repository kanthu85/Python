'Tuple is a collection which is ordered and unchangable.Allows duplicated.Iteration is faster in Tuple compared to List.'
'''Python Tuples	V/S  Python Lists
----------------------------------
Ordered	               | Ordered
Allows Duplicates      | Allows Duplicates
Indexable	           | Indexable
Heterogeneous	       | Heterogeneous
Immutable	           | Mutable'''

'''Ordered: Python tuples are an ordered collection of objects. This means that the order that the object has matters and will remain the same.
Indexable: You can access the items in a Python tuple using their index positions. Because tuples are ordered, the index remains the same.
Heterogeneous: Python tuples can contain different types of objects, including other tuples! For example, you can use tuples to store information about user information for a website, such as login, name, age, gender, etc.
Immutable: Python tuples are immutable, meaning that once they are created, they cannot be changed. This means that if you wanted to, say, sort a tuple, you’d need to create a new one.'''

'''Why Use Tuples Over Lists in Python
At this point, you might be wondering, “why even bother with tuples?”. There are two primary reasons for using tuples over lists:

Immutability: there may be times when you have some values that you simply don’t want to change (especially, accidentally). This is where tuples may are a better choice over lists.
Memory efficiency: Because Python tuples are immutable, they are significantly more memory-efficient. When a Python list is created, Python doesn’t know how much space to allocate for it in memory. Because of this, some space is reserved. Meanwhile, when a tuple is created, the exact size of that tuple is known!'''

# Your first tuple
data = ('welcome', 'to', 'MyWorld')
print(data)
print(type(data))
# Creating a tuple with a single item
data = ('Myworld')
print(data)
print(type(data))
# Creating a tuple with a single item
data = ('Myworld',)
print(data)
print(type(data))
# Creating a tuple with out brackets
data = 'Myworld',
print(data)
print(type(data))

#Accessing Items with Indexing
# Accessing items in a tuple with indexing
data = ('learn', 'python', 'with', 'MyWorld')
first_item = data[0]
print(first_item) # Returns: learn
# Accessing an item out of range
data = ('learn', 'python', 'with', 'MyWorld')
#print(data[4]) # Returns: IndexError: tuple index out of range
# Using negative indexing to access items
data = ('learn', 'python', 'with', 'MyWorld')
print(data[-1]) # Returns: datagy
# Slicing a tuple
data = ('learn', 'python', 'with', 'MYWorld')
print(data[0:2]) # Returns: ('learn', 'python')
# Slicing a tuple
print(data[:2]) # Returns: ('learn', 'python')

# Iterating over a Python tuple
data = ('learn', 'python', 'with', 'MYWorld')
for item in data:
    print(item)
# Trying to modify a tuple
data = ('learn', 'python', 'with', 'MYWorld')
#data[0] = 'hi'  # Returns: TypeError: 'tuple' object does not support item assignment

# Modifying a multable item in a tuple which is of type list[]
data = ('learning', 'python', 'with', 'datagy', 'is as easy as', [1,2])
print(data)
data[-1].append(3)
print(data)

# Concatenating two tuples
first_tuple = (1,2,3)
second_tuple = (4,5,6)
third_tuple = first_tuple + second_tuple

print(third_tuple) # Returns: (1, 2, 3, 4, 5, 6)

# Repeating a tuple in Python
a_tuple = (1,2,3)
print('First ID: ', id(a_tuple))
a_tuple *= 2
print('second ID: ', id(a_tuple))
print(a_tuple) # Returns: (1, 2, 3, 1, 2, 3)

'''note:
Something important to note here is that the code above makes it look like the tuple was mutated. 
However, the first instance of a_tuple was destroyed and a new one was created. 
You can verify this by using the id() function which returns the space in memory the object is using. Let’s confirm this now:
'''

#Python Tuple Methods(Count(), index())
# Counting items in a tuple
a_tuple = (1,2,3,4,1,2,1)
print(a_tuple.count(1)) # Returns: 3

# Finding the first index of an item in a tuple
a_tuple = (1,2,3,4,1,2,1)
print("The index position of 2 is: ", a_tuple.index(2)) # Returns: The index position of 2 is:  1

#You can delete a tuple using the `del` keyword.
a_tuple = (1,2,3)
del a_tuple
#print(a_tuple) # NameError: name 'a_tuple' is not defined.
