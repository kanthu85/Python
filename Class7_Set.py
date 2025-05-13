'''A set in Python is a collection of distinct hashable objects. 
Unlike lists or tuples, sets are unordered and do not index elements. 
This makes them perfect for membership testing and eliminating duplicate entries.'''

'''Creating a Set:
You can create a set in Python using curly braces {} or the set() function:
'''
# Using curly braces
fruits = {'apple', 'banana', 'cherry'}

# Using the set() function
numbers = set([1, 2, 3, 4, 5])

# Creating an empty set
# Note: {} creates an empty dictionary, not a set
empty_set = set()
print(type(empty_set))

'''Set Properties
Sets in Python have several key properties:

1.Unordered: Elements in a set have no specific order
2.Unique Elements: Duplicates are automatically removed
3.Mutable: You can add or remove elements
4.Hashable Elements: Set elements must be immutable (strings, numbers, tuples)'''
'''Method	Description
    1.add()	Adds an element to the set
    2.clear()	Removes all elements from the set
    3.copy()	Returns a copy of the set
    4.difference()	Returns the difference of two or more sets
    5.discard()	Removes the specified element
    6.intersection()	Returns the intersection of two sets
    7.isdisjoint()	Returns True if two sets have no intersection
    8.issubset()	Returns True if another set contains this set
    9.issuperset()	Returns True if this set contains another set
    10.pop()	Removes and returns an arbitrary element
    11.remove()	Removes the specified element
    12.union()	Returns the union of sets
    13.update()	Updates the set with elements from another set'''
#Adding Elements
fruits = {'apple', 'banana', 'cherry'}
print('Initial set:',fruits)
fruits.add('orange')  # Add a single element
print('add element to set:',fruits)
fruits.update(['mango', 'grapes'])  # Add multiple elements
print('Updated/added list to set:',fruits)
#Removing Elements
fruits = {'apple', 'banana', 'cherry'}
print('Initial set:',fruits)
fruits.remove('banana')  # Raises error if element doesn't exist
print('removed item from set:',fruits)
fruits.discard('mango')  # No error if element doesn't exist
print('try to remove not available item item from set with discard method to avoid error :',fruits)
popped_item = fruits.pop()  # Removes and returns an arbitrary element
print(popped_item)
fruits_copy =set()
fruits_copy =fruits.copy()
print('fruits copy set: ',fruits_copy)
fruits_copy.clear()  # Removes all elements
print(fruits_copy)


'''Mathematical Set Operations
Python sets support mathematical set operations:'''

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (all elements from both sets)
union_set = set1 | set2  # or set1.union(set2)
print(union_set)

# Intersection (elements common to both sets)
intersection_set = set1 & set2  # or set1.intersection(set2)
print(intersection_set)

# Difference (elements in set1 but not in set2)
difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)

superset = {"f", "e", "d", "c", "b", "a"}
subset= {"a", "b", "c"}

print('superset check:',superset.issuperset(subset))
print('subset check:',subset.issubset(superset))

disjoint_distinct1 = {"f", "e", "d"}
subsdisjoint_distinct2= {"a", "b", "c"}
print('disjoint check:',disjoint_distinct1.isdisjoint(subsdisjoint_distinct2))
# Symmetric difference (elements in either set, but not in both)
symmetric_difference = set1 ^ set2  # or set1.symmetric_difference(set2)
print(symmetric_difference)
'''Set Comprehensions
Like list comprehensions, Python allows set comprehensions:'''

# Square of numbers from 0 to 9
squares = {x**2 for x in range(10)}
print(squares)
# Even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)

#Common Applications of Sets
#1.Removing duplicates from a sequence
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(list_with_duplicates))
print(unique_items)

#2.Membership testing (faster than lists for large collections)
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)  # True
#3.Finding unique elements in multiple collections
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
unique_to_list1 = set(list1) - set(list2)  # {1, 2}
print(unique_to_list1)
#Frozen Sets- Python also provides immutable sets called frozen sets:

frozen = frozenset([1, 2, 3, 4])
# frozen.add(5)  # This will raise an error



'''SET Best Practices
1.Use sets when order doesn’t matter, but uniqueness does
2.Prefer sets over lists for membership testing with large collections
3.Use frozen sets when you need an immutable set (like dictionary keys)
4.Remember that sets can only contain hashable elements'''