#lists is a collection of numbers,strings which is ordered and changable and allows duplicate members.
#Lists are mutable(we can change)
#we can retrive list value by using index [starts from 0]. If you provide index not in list range it will through error)Index out of range.
nums=[1,'sreekanth',80000,'Azure Engineer']
print('Record:'+ str(nums[0]) +'\n Name:'+ nums[1] +'\n Salary:'+ str(nums[2]) +'\n Designation:'+ nums[3])
#Nested list(list inside list)
nums=[1,2,3]
names=['sreekanth','pavan','kiran']
nestedlist=[nums,names]
print('Nested List: ',nestedlist) #output: [[1, 2, 3], ['sreekanth', 'pavan', 'kiran']]
print('Get Item from Nested list: ',nestedlist[1][1])#output: pavan(first bracked is nested list number, and second bracked is items in second list )
#working with list methods
'''1. Adding Elements
append(item): Adds an item to the end of the list.
extend(iterable): Extends the list by appending elements from another iterable (e.g., list, tuple).
insert(index, item): Inserts an item at a specified index.
2. Removing Elements
remove(item): Removes the first occurrence of the specified item.
pop(index): Removes and returns the item at the specified index (default is the last item).
clear(): Removes all elements from the list.
3. Searching and Counting
index(item, start, end): Returns the index of the first occurrence of the item (optional start and end specify a range).
count(item): Returns the number of occurrences of the specified item.
4. Sorting and Reversing
sort(key=None, reverse=False): Sorts the list in ascending order (can use a custom key and reverse the order).
reverse(): Reverses the elements of the list in place.
5. Copying
copy(): Returns a shallow copy of the list.
6. Other Utility Methods
len(list): Returns the number of elements in the list (not a method but a built-in function).
max(list): Returns the largest element in the list.
min(list): Returns the smallest element in the list.
sum(list): Returns the sum of all numeric elements in the list.'''
nums.append(4)
print('appended item 4 to list:', nums)
copylist=[]
copylist=nums.copy()
print('copylist:',copylist)
#nums.count()
print('number of times 2 occered in list: ',nums.count(2))#number of times 2 occered in list
a=[1,2,3]
b=[4,5]
a.extend(b)
a.extend([6,7,8,9])
print('Extended list: ',a)
print(nums.index(1))
nums.insert(0,6)
print('Inserted 6 at 0th index:',nums)
nums.pop()
print('pop/remove Last item from list: ',nums)
nums.remove(6)
print('remove item -6 from list: ',nums)
print('print list:',nums)
nums.reverse()
print('reverse list: ',nums)
nums.sort()
print('sort list: ',nums)
nums.clear()
print('emptying list by using clear: ',nums)
utilitylist =[1,2,3,4,5,6]
print('length of list: ',len(utilitylist))
print('min of list: ',min(utilitylist))
print('Max of list: ',max(utilitylist))
print('sum of list: ',sum(utilitylist))
