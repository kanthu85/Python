'''A Python dictionary is a collection of key-value pairs where each key must be unique.
 Think of it like a real-world dictionary where each word (key) has a definition (value).'''
'''Dictionaries are:

1.Unordered (in Python versions before 3.7)
2.Ordered (from Python 3.7 onwards)
3.Mutable (can be changed)
4.Indexed by keys, not positions'''

'''Creating a Python Dictionary
Method 1: Using Curly Braces {}
Method 2: Using the dict() Constructor
Method 3: Using Dictionary Comprehension(for,dictionary from two lists using zip)'''

# Empty dictionary
my_dict_braces = {}
my_dict_constructor = dict()
# Dictionary with initial values
customer = {'name': 'John Smith','age': 35,'city': 'New York','is_active': True}
print(customer)
# Dictionary from sequence of key-value pairs
customer = dict([('name', 'John Smith'),('age', 35),('city', 'New York'),('is_active', True)])
print(customer)

# Create a dictionary of squares
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create a dictionary from two lists
cities = ['New York', 'Los Angeles', 'Chicago']
populations = [8804190, 3898747, 2746388]
#from 2 lists using zip of two lists through for loop
city_pops = {city: pop for city, pop in zip(cities, populations)}
print(city_pops)  # Output: {'New York': 8804190, 'Los Angeles': 3898747, 'Chicago': 2746388}

#from 2 lists using dict and zip of two lists 
fromtlists=dict(zip(cities, populations))
print(fromtlists)

#Accessing Dictionary Values
#1. Using Square Brackets []
#2. Using get() Method (The get() method is safer because it returns None (or a default value) if the key doesn’t exist:)

customer = {'name': 'John Smith','age': 35,'city': 'New York','is_active': True}
# Access a value
print(customer['name'])  # Output: John Smith
print(customer.get('name'))
# This will raise KeyError if the key doesn't exist
# print(customer['email'])  # KeyError: 'email'
# Using get() with a non-existent key
print(customer.get('email'))  # Output: None
print(customer.get('email', 'Not Found') ) # KeyError: 'email'

#Modifying Dictionaries
#1.Adding or Updating Items
#2.Using update() Method
customer_AddUpdate = {'name': 'John Smith', 'age': 35}
print('initial dict',customer_AddUpdate)
# Add a new key-value pair
customer_AddUpdate['city'] = 'New York'
print('Adding Item to dict',customer_AddUpdate)
# Update an existing value
customer_AddUpdate['age'] = 36
print('updating Item value in dict',customer_AddUpdate) # Output: {'name': 'John Smith', 'age': 36, 'city': 'New York'}

'''Using update() Method
The update() method adds multiple key-value pairs at once with comma seperated:'''

customer = {'name': 'John Smith', 'age': 35}
# Update with multiple key-value pairs
customer.update({'city': 'New York', 'email': 'john@example.com', 'age': 36})
print(customer)  # Output: {'name': 'John Smith', 'age': 36, 'city': 'New York', 'email': 'john@example.com'}

#Removing Items
#Using Pop()- Remove a specific item and return its value
customer = {'name': 'John Smith', 'age': 36, 'city': 'New York', 'email': 'john@example.com'}
age = customer.pop('age')
print(age)  # Output: 36
print(customer)  # Output: {'name': 'John Smith', 'city': 'New York', 'email': 'john@example.com'}

#Remove and return the last inserted item (Python 3.7+)
last_item = customer.popitem()
print(last_item)  # Output: ('email', 'john@example.com')
print(customer)  # Output: {'name': 'John Smith', 'city': 'New York'}

# Delete a specific item
del customer['city']
print(customer)  # Output: {'name': 'John Smith'}

# Clear all items
customer.clear()
print(customer)  # Output: {}


#Dictionary Methods - keys(), values(), and items()
product = {'name': 'Laptop','price': 999.99,'brand': 'TechPro','in_stock': True}

# Get all keys
print(list(product.keys()))  # Output: ['name', 'price', 'brand', 'in_stock']

# Get all values
print(list(product.values()))  # Output: ['Laptop', 999.99, 'TechPro', True]

# Get all key-value pairs as tuples
print(list(product.items()))  
# Output: [('name', 'Laptop'), ('price', 999.99), ('brand', 'TechPro'), ('in_stock', True)]


'''setdefault() Method
The setdefault() method returns the value of a key if it exists. If not, it inserts the key with a specified value and returns that value:'''

customer = {'name': 'John Smith', 'city': 'New York'}

# Get existing value
nameval = customer.setdefault('name', 'Unknown')
print(nameval)  # Output: John Smith

# Set default for non-existent key
email = customer.setdefault('email', 'no-email@example.com')
print(email)  # Output: no-email@example.com
print(customer)  
# Output: {'name': 'John Smith', 'city': 'New York', 'email': 'no-email@example.com'}

'''Dictionary Comprehension with Conditionals
We can use conditionals in dictionary comprehensions for more advanced filtering:
'''
prices = {'apple': 1.2, 'banana': 0.5, 'orange': 0.8, 'grapes': 2.5, 'watermelon': 5.0}

# Create dictionary of fruits that cost less than $1
affordable_fruits = {fruit: price for fruit, price in prices.items() if price < 1}
print(affordable_fruits)  # Output: {'banana': 0.5, 'orange': 0.8}

# Create dictionary with applied discount for expensive fruits
discounted_prices = {fruit: (price * 0.8 if price > 2 else price) 
                     for fruit, price in prices.items()}
print(discounted_prices)  # Output: {'apple': 1.2, 'banana': 0.5, 'orange': 0.8, 'grapes': 2.0, 'watermelon': 4.0}

'''Nested Dictionaries
Dictionaries can contain other dictionaries as values, allowing for complex data structures:'''

employees = {
    'E001': {
        'name': 'John Smith',
        'department': 'Sales',
        'salary': 65000,
        'contact': {
            'email': 'john@example.com',
            'phone': '555-1234'
        }
    },
    'E002': {
        'name': 'Lisa Johnson',
        'department': 'Marketing',
        'salary': 70000,
        'contact': {
            'email': 'lisa@example.com',
            'phone': '555-5678'
        }
    }
}

# Accessing nested values
print(employees['E001']['name'])  # Output: John Smith
print(employees['E002']['contact']['email'])  # Output: lisa@example.com

# Modifying nested values
employees['E001']['salary'] = 68000
employees['E002']['contact']['phone'] = '555-9999'

print(employees['E001']['salary'])  # Output: 68000
print(employees['E002']['contact']['phone'])  # Output: 555-9999

'''Dictionary with Multiple Values per Key
Sometimes we need to store multiple values for a single key. There are several ways to achieve this:'''

#Using Lists as Values
student_courses = {
    'John': ['Math', 'Physics', 'Computer Science'],
    'Lisa': ['History', 'English', 'Art'],
    'Mike': ['Biology', 'Chemistry']
}

# Adding a new course for John
student_courses['John'].append('Economics')
print(student_courses['John'])  # Output: ['Math', 'Physics', 'Computer Science', 'Economics']

# Adding a new student
student_courses['Sarah'] = ['Geography', 'Spanish']
print(student_courses)

'''Using Tuples as Values
If you don’t need to modify the values, tuples can be more efficient:'''

# Store multiple phone numbers
contacts = {
    'John': ('555-1234', '555-5678'),
    'Lisa': ('555-8765',),
    'Mike': ('555-4321', '555-8765', '555-9999')
}

# Access first phone number
print(contacts['John'][0])  # Output: 555-1234

'''Using Dictionaries as Values
For more structured data:'''

customers = {
    'C001': {
        'name': 'John Smith',
        'purchases': ['Laptop', 'Mouse', 'Keyboard'],
        'total_spent': 1250.75
    },
    'C002': {
        'name': 'Lisa Johnson',
        'purchases': ['Phone', 'Headphones'],
        'total_spent': 950.25
    }
}

# Add a new purchase for John
customers['C001']['purchases'].append('Monitor')
customers['C001']['total_spent'] += 299.99

print(customers['C001'])
'''Dictionary Counting and Frequency Analysis
Dictionaries are excellent for counting occurrences:'''

# Count word frequency in a text
text = "how much wood would a woodchuck chuck if a woodchuck could chuck wood"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# Output: {'how': 1, 'much': 1, 'wood': 2, 'would': 1, 'a': 2, 'woodchuck': 2, 'chuck': 2, 'if': 1, 'could': 1}

'''This technique, known as frequency analysis, is incredibly useful for data processing tasks.

Finding the Most Common Items
We can use dictionaries to find the most common items:'''

# Find the most common word
most_common_word = max(word_count.items(), key=lambda x: x[1])
print(f"Most common word: {most_common_word[0]} (appears {most_common_word[1]} times)")
# Output: Most common word: wood (appears 2 times) - or any other word with count 2
'''Using Counter from Collections
The collections module provides a specialized Counter class that makes frequency counting even easier:'''

from collections import Counter

# Same text as before
text = "how much wood would a woodchuck chuck if a woodchuck could chuck wood"
words = text.split()

# Count word frequency using Counter
word_count = Counter(words)
print(word_count)
# Output: Counter({'wood': 2, 'a': 2, 'woodchuck': 2, 'chuck': 2, 'how': 1, 'much': 1, 'would': 1, 'if': 1, 'could': 1})

# Find most common words
most_common = word_count.most_common(3)
print(most_common)  # Output: [('wood', 2), ('a', 2), ('woodchuck', 2)] - order may vary
'''Dictionary Performance and Memory Usage
One of the reasons I love dictionaries is their performance. Looking up values by key is extremely fast (O(1) on average), making them perfect for large datasets.

Here’s an example where I compare list search vs. dictionary lookup for finding sales data:'''

import time

# Create test data - 10,000 products
product_ids = list(range(10000))
sales_amounts = [i * 10 for i in range(10000)]

# Create list of tuples (slower to search)
sales_list = list(zip(product_ids, sales_amounts))

# Create dictionary (faster to search)
sales_dict = dict(zip(product_ids, sales_amounts))

# Search in list - O(n) time complexity
start_time = time.time()
for _ in range(1000):
    product_id = 9876  # Product near the end of the list
    for item in sales_list:
        if item[0] == product_id:
            sale_amount = item[1]
            break
list_time = time.time() - start_time

# Search in dictionary - O(1) time complexity
start_time = time.time()
for _ in range(1000):
    product_id = 9876
    sale_amount = sales_dict[product_id]
dict_time = time.time() - start_time

print(f"List search time: {list_time:.6f} seconds")
print(f"Dictionary lookup time: {dict_time:.6f} seconds")
print(f"Dictionary is {list_time/dict_time:.1f}x faster")

'''Practical Applications of Dictionaries
Over my years of Python development, I’ve used dictionaries in countless applications. Here are some real-world examples:'''

#1. Configuration Settings
app_config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'username': 'admin',
        'password': 'secure_password',
        'database_name': 'product_db'
    },
    'api': {
        'base_url': 'https://api.example.com',
        'version': 'v2',
        'timeout': 30,
        'retry_limit': 3
    },
    'logging': {
        'level': 'INFO',
        'file_path': '/var/log/app.log',
        'rotation': '1 day'
    }
}

# Access configuration values
db_host = app_config['database']['host']
api_timeout = app_config['api']['timeout']

#2. Data Processing and Transformation
# Process customer orders
orders = [
    {'customer_id': 'C001', 'product': 'Laptop', 'amount': 999.99},
    {'customer_id': 'C002', 'product': 'Phone', 'amount': 699.99},
    {'customer_id': 'C001', 'product': 'Headphones', 'amount': 149.99},
    {'customer_id': 'C003', 'product': 'Tablet', 'amount': 349.99},
    {'customer_id': 'C002', 'product': 'Case', 'amount': 29.99}
]

# Calculate total spending per customer
customer_totals = {}
for order in orders:
    customer_id = order['customer_id']
    amount = order['amount']
    customer_totals[customer_id] = customer_totals.get(customer_id, 0) + amount

print(customer_totals)
# Output: {'C001': 1149.98, 'C002': 729.98, 'C003': 349.99}

#3. Caching and Memoization
# Using a dictionary as a cache for expensive function calls
fibonacci_cache = {}

def fibonacci(n):
    # Check if value exists in cache
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # Calculate the nth term
    if n <= 1:
        value = n
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    
    # Cache the result and return
    fibonacci_cache[n] = value
    return value

# Calculate first 20 Fibonacci numbers
for i in range(20):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

#4. Implementing a Simple Database
# Simple in-memory database using dictionaries
users_db = {}

def add_user(user_id, name, email, age):
    users_db[user_id] = {
        'name': name,
        'email': email,
        'age': age,
        'created_at': time.time()
    }
    return f"User {name} added successfully"

def get_user(user_id):
    return users_db.get(user_id, "User not found")

def update_user(user_id, **kwargs):
    if user_id in users_db:
        users_db[user_id].update(kwargs)
        return f"User {user_id} updated successfully"
    return "User not found"

def delete_user(user_id):
    if user_id in users_db:
        del users_db[user_id]
        return f"User {user_id} deleted successfully"
    return "User not found"

# Usage example
add_user("U001", "John Smith", "john@example.com", 35)
add_user("U002", "Lisa Johnson", "lisa@example.com", 28)
print(get_user("U001"))
update_user("U001", email="john.smith@example.com", age=36)
print(get_user("U001"))

#Counting Frequencies Using Dictionaries
#Counting the frequencies of items in collections is one of the most common use cases for dictionaries. Let’s explore this further:

# Analyzing US state populations (sample data)
states = ['California', 'Texas', 'Florida', 'New York', 'Texas', 'Florida', 
          'California', 'Texas', 'Georgia', 'California', 'Washington']

# Count occurrences using a dictionary
state_counts = {}
for state in states:
    if state in state_counts:
        state_counts[state] += 1
    else:
        state_counts[state] = 1

print(state_counts)
# Output: {'California': 3, 'Texas': 3, 'Florida': 2, 'New York': 1, 'Georgia': 1, 'Washington': 1}

# More elegantly with get() method
state_counts = {}
for state in states:
    state_counts[state] = state_counts.get(state, 0) + 1

print(state_counts)

'''Working with JSON and Dictionaries
Python dictionaries are closely related to JSON, making them perfect for web applications:'''


import json

# Dictionary representing data for a weather API
weather_data = {
    'location': {
        'city': 'New York',
        'state': 'NY',
        'country': 'USA',
        'coordinates': {
            'latitude': 40.7128,
            'longitude': -74.0060
        }
    },
    'current': {
        'temperature': 72.5,
        'feels_like': 74.2,
        'humidity': 65,
        'wind_speed': 10.4,
        'conditions': 'Partly Cloudy'
    },
    'forecast': [
        {'day': 'Monday', 'high': 75, 'low': 65, 'conditions': 'Sunny'},
        {'day': 'Tuesday', 'high': 80, 'low': 68, 'conditions': 'Clear'},
        {'day': 'Wednesday', 'high': 77, 'low': 66, 'conditions': 'Partly Cloudy'}
    ]
}

# Convert dictionary to JSON string
json_data = json.dumps(weather_data, indent=4)
print(json_data)

# Convert JSON string back to dictionary
parsed_data = json.loads(json_data)
print(parsed_data['location']['city'])  # Output: New York
print(parsed_data['forecast'][1]['high'])  # Output: 80

'''Advanced Dictionary Techniques
Dictionary Union (Python 3.9+)
In Python 3.9 and later, you can use the | operator to merge dictionaries:'''

# Base product information
product = {
    'id': 'P001',
    'name': 'Smartphone',
    'price': 799.99
}

# Additional product details
details = {
    'brand': 'TechX',
    'model': 'X20',
    'color': 'Midnight Blue'
}

# Merge dictionaries with |
complete_product = product | details
print(complete_product)
# Output: {'id': 'P001', 'name': 'Smartphone', 'price': 799.99, 'brand': 'TechX', 'model': 'X20', 'color': 'Midnight Blue'}

# Update and merge with |=
product |= details
print(product)
# Output: {'id': 'P001', 'name': 'Smartphone', 'price': 799.99, 'brand': 'TechX', 'model': 'X20', 'color': 'Midnight Blue'}
#Using defaultdict
#The defaultdict from the collections module creates dictionaries with default values for missing keys:

from collections import defaultdict

# Using defaultdict with int as default factory
word_count = defaultdict(int)
for word in "how much wood would a woodchuck chuck".split():
    word_count[word] += 1  # No need to check if key exists

print(dict(word_count))
# Output: {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 1, 'woodchuck': 1, 'chuck': 1}
'''The default dict in Python behaves almost exactly like a regular dictionary, but automatically assigns default values when accessing missing keys. This makes certain patterns much cleaner.

Using defaultdict with list
Another common use case is creating a dictionary where each value is a list:'''

# Group customers by state
customers = [
    ('John Smith', 'NY'),
    ('Lisa Johnson', 'CA'),
    ('Michael Brown', 'TX'),
    ('Sarah Davis', 'CA'),
    ('Robert Wilson', 'NY'),
    ('Jennifer Lee', 'TX'),
    ('David Garcia', 'FL')
]

# Without defaultdict (traditional approach)
customers_by_state = {}
for name, state in customers:
    if state not in customers_by_state:
        customers_by_state[state] = []
    customers_by_state[state].append(name)

# With defaultdict (cleaner approach)
customers_by_state = defaultdict(list)
for name, state in customers:
    customers_by_state[state].append(name)

print(dict(customers_by_state))
# Output: {'NY': ['John Smith', 'Robert Wilson'], 'CA': ['Lisa Johnson', 'Sarah Davis'], 'TX': ['Michael Brown', 'Jennifer Lee'], 'FL': ['David Garcia']}

'''Nested defaultdicts
You can even create nested defaultdicts for more complex data structures:'''

# Sales data by region, quarter, and product
sales = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

# Adding sales data
sales['West']['Q1']['Laptop'] += 50
sales['West']['Q1']['Phone'] += 100
sales['East']['Q1']['Laptop'] += 30
sales['West']['Q2']['Laptop'] += 45
sales['East']['Q2']['Phone'] += 75

# Accessing data (no KeyError even for new combinations)
print(sales['West']['Q1']['Laptop'])  # Output: 50
print(sales['South']['Q3']['Tablet'])  # Output: 0 (default value)

# Convert to regular dict for display
print(dict(sales))

'''Common Dictionary Patterns
Dictionary Sorting
Dictionaries in Python 3.7+ maintain insertion order, but sometimes we need to sort them:'''

# Sort dictionary by keys
product_prices = {
    'Laptop': 999.99,
    'Phone': 699.99,
    'Headphones': 149.99,
    'Tablet': 349.99,
    'Smartwatch': 249.99
}

# Sort by keys (alphabetical)
sorted_by_name = dict(sorted(product_prices.items()))
print(sorted_by_name)

# Sort by values (price)
sorted_by_price = dict(sorted(product_prices.items(), key=lambda item: item[1]))
print(sorted_by_price)

# Sort by values descending (highest price first)
sorted_by_price_desc = dict(sorted(product_prices.items(), 
                                  key=lambda item: item[1], 
                                  reverse=True))
print(sorted_by_price_desc)
'''Dictionary Filtering
Often, we need to filter dictionaries based on certain conditions:'''

sales_data = {
    'Laptop': 50,
    'Phone': 100,
    'Tablet': 30,
    'Desktop': 15,
    'Headphones': 150,
    'Keyboard': 75
}

# Filter items with sales >= 50 (traditional way)
high_volume_items = {}
for product, count in sales_data.items():
    if count >= 50:
        high_volume_items[product] = count

print(high_volume_items)
# Output: {'Laptop': 50, 'Phone': 100, 'Headphones': 150, 'Keyboard': 75}

# Dictionary comprehension way (more concise)
high_volume_items = {product: count for product, count in sales_data.items() if count >= 50}
print(high_volume_items)
'''Dictionary Transformation
Transforming dictionary values is another common operation:'''

prices = {
    'Laptop': 999.99,
    'Phone': 699.99,
    'Headphones': 149.99,
    'Tablet': 349.99
}

# Apply 10% discount to all products
discounted_prices = {product: price * 0.9 for product, price in prices.items()}
print(discounted_prices)

# Format prices as strings with $ symbol
formatted_prices = {product: f"${price:.2f}" for product, price in prices.items()}
print(formatted_prices)
# Output: {'Laptop': '$999.99', 'Phone': '$699.99', 'Headphones': '$149.99', 'Tablet': '$349.99'}

'''Dictionary Views and Iterating
Dictionary views (keys(), values(), and items()) provide dynamic views of dictionary contents:'''

inventory = {
    'Laptop': 25,
    'Phone': 50,
    'Tablet': 30
}

# Get views
keys_view = inventory.keys()
values_view = inventory.values()
items_view = inventory.items()

print(keys_view)    # dict_keys(['Laptop', 'Phone', 'Tablet'])
print(values_view)  # dict_values([25, 50, 30])
print(items_view)   # dict_items([('Laptop', 25), ('Phone', 50), ('Tablet', 30)])

# Views are dynamic - they reflect dictionary changes
inventory['Headphones'] = 45
print(keys_view)    # dict_keys(['Laptop', 'Phone', 'Tablet', 'Headphones'])

# Common dictionary iteration patterns
# Iterating through keys (default behavior)
for product in inventory:
    print(product)

# Iterating through values
for quantity in inventory.values():
    print(quantity)

# Iterating through key-value pairs
for product, quantity in inventory.items():
    print(f"{product}: {quantity} units")
'''Dictionary Tricks for Data Analysis
As someone who frequently deals with data analysis, these dictionary tricks have proved invaluable:'''

#Grouping and Aggregating Data
# Sales transactions
transactions = [
    {"product": "Laptop", "price": 999.99, "region": "West"},
    {"product": "Phone", "price": 699.99, "region": "East"},
    {"product": "Laptop", "price": 1199.99, "region": "East"},
    {"product": "Headphones", "price": 149.99, "region": "West"},
    {"product": "Phone", "price": 599.99, "region": "West"},
    {"product": "Tablet", "price": 349.99, "region": "East"},
    {"product": "Laptop", "price": 899.99, "region": "West"}
]

# Group total sales by region
sales_by_region = {}
for t in transactions:
    region = t["region"]
    if region not in sales_by_region:
        sales_by_region[region] = 0
    sales_by_region[region] += t["price"]

print(sales_by_region)
# Output: {'West': 2649.96, 'East': 2249.97}

# Group sales by product type
sales_by_product = {}
for t in transactions:
    product = t["product"]
    if product not in sales_by_product:
        sales_by_product[product] = []
    sales_by_product[product].append(t["price"])

# Calculate average price per product
avg_price_by_product = {product: sum(prices)/len(prices) 
                        for product, prices in sales_by_product.items()}

print(avg_price_by_product)
# Output: {'Laptop': 1033.32, 'Phone': 649.99, 'Headphones': 149.99, 'Tablet': 349.99}
'''Dictionary Performance Optimization
Using dict.fromkeys()
When you need to create a dictionary with the same value for multiple keys:'''

# Initialize inventory with zero quantities (less efficient)
products = ["Laptop", "Phone", "Tablet", "Headphones", "Monitor", "Keyboard", "Mouse"]
inventory = {}
for product in products:
    inventory[product] = 0

# Better way using dict.fromkeys()
inventory = dict.fromkeys(products, 0)
print(inventory)
# Output: {'Laptop': 0, 'Phone': 0, 'Tablet': 0, 'Headphones': 0, 'Monitor': 0, 'Keyboard': 0, 'Mouse': 0}
'''Memory Efficiency with slots
For classes that will be instantiated many times, using __slots__ with dictionaries can save memory:'''

class ProductTraditional:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class ProductOptimized:
    __slots__ = ['id', 'name', 'price']
    
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

# The ProductOptimized class uses significantly less memory
# when you create thousands of instances
'''Dictionary Serialization and Storage
Dictionaries are easily serialized to various formats for storage or transmission:'''

import json
import pickle
import yaml  # requires PyYAML package

customer = {
    'id': 'C12345',
    'name': 'John Smith',
    'email': 'john@example.com',
    'orders': [
        {'order_id': 'O1', 'product': 'Laptop', 'amount': 999.99},
        {'order_id': 'O2', 'product': 'Headphones', 'amount': 149.99}
    ]
}

# JSON serialization
json_data = json.dumps(customer, indent=2)
with open('customer.json', 'w') as f:
    f.write(json_data)

# Pickle serialization (Python-specific binary format)
with open('customer.pickle', 'wb') as f:
    pickle.dump(customer, f)

# YAML serialization (requires PyYAML)
# with open('customer.yaml', 'w') as f:
#     yaml.dump(customer, f)

# Reading back
with open('customer.json', 'r') as f:
    loaded_customer = json.load(f)

print(loaded_customer['name'])  # Output: John Smith