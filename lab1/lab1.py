# 1. NUMERIC

print("NUMERIC")

print(type(1))
print(type(-10))
print(type(0))
print(type(0.0))
print(type(2.2))
print(type(4E2))

# Arithmetic
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 ** 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)

# Basic Functions
print(pow(5, 2))
print(abs(-50))
print(round(5.46))
print(round(5.468, 2))
print(bin(512))
print(hex(512))

# Converting Strings to Numbers

print("\nCONVERT STRING TO NUMBER")

age = input("How old are you? ")
age = int(age)

pi = input("What is the value of pi? ")
pi = float(pi)

print("Age:", age)
print("Pi:", pi)

# 2. STRINGS

print("\nSTRINGS")

print(type("Hellooo"))

print("I'm thirsty")
print("I'm thirsty")
print("\n")
print("\t")

name = "John Doe"

print(name[2])
print(name[:])
print(name[1:])
print(name[:1])
print(name[-1])
print(name[::-1])
print(name[0:7:2])

print("Hi there " + "Timmy")
print("*" * 10)

print(len("turtle"))

# String methods
print(" I am alone ".strip())
print("On an island".strip('d'))
print("but life is good!".split())
print("Help me".replace("me", "you"))
print("Need to make fire".startswith("Need"))
print("and cook rice".endswith("rice"))
print("bye bye".index("e"))
print("still there?".upper())
print("HELLO!".lower())
print("ok, I am done.".capitalize())
print("oh hi there".find("i"))
print("oh hi there".count("e"))

# String Formatting

print("\nSTRING FORMATTING")

name1 = "Andrei"
name2 = "Sunny"

print(f"Hello there {name1} and {name2}")
print("Hello there {} and {}".format(name1, name2))
print("Hello there %s and %s" % (name1, name2))

# Palindrome Check

print("\nPALINDROME CHECK")

word = "reviver"

p = bool(word.find(word[::-1]) + 1)

print("Is palindrome:", p)

# 3. BOOLEAN

print("\n BOOLEAN")

print(bool(True))
print(bool(False))

print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(set()))

# 4. LIST

print("\nLIST")

my_list = [1, 2, '3', True]

print(len(my_list))
print(my_list.index('3'))
print(my_list.count(2))

print(my_list[3])
print(my_list[1:])
print(my_list[:1])
print(my_list[-1])
print(my_list[::-1])
print(my_list[0:3:2])

# Add to List

print("\nADD TO LIST")

print(my_list * 2)
print(my_list + [100])

my_list.append(100)
print(my_list)

my_list.extend([200, 300])
print(my_list)

my_list.insert(2, "!!!")
print(my_list)

# Copy a List

print("\nCOPY LIST")

basket = ["apples", "pears", "oranges"]

new_basket = basket.copy()
new_basket2 = basket[:]

print(new_basket)
print(new_basket2)

# Remove from List

print("\nREMOVE FROM LIST")

numbers = [1, 2, 3]

numbers.pop()
print(numbers)

numbers.pop(1)
print(numbers)

numbers = [1, 2, 3]
numbers.remove(2)
print(numbers)

numbers.clear()
print(numbers)

# Ordering Lists

print("\nORDERING LIST")

numbers = [1, 2, 5, 3]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers = [1, 2, 5, 3]
numbers.reverse()
print(numbers)

print(sorted([1, 2, 5, 3]))

print(list(reversed([1, 2, 5, 3])))

# Useful operations

print("\nUSEFUL OPERATIONS")

print(1 in [1, 2, 5, 3])
print(min([1, 2, 3, 4, 5]))
print(max([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5]))

# Get First and Last element

print("\nFIRST AND LAST ELEMENT")

mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]

first, *x, last = mList

print("First:", first)
print("Last:", last)

# DICTIONARY

print("\nDICTIONARY")

my_dict = {
    "name": "John Doe",
    "age": 25,
    "magic_power": False
}

print(my_dict["name"])
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))
print(list(my_dict.items()))

my_dict["favorite_snack"] = "Grapes"
print(my_dict)

print(my_dict.get("age"))
print(my_dict.get("ages", 0))

del my_dict["name"]
print(my_dict)

# TUPLE

print("\nTUPLE")

my_tuple = ("apple", "grapes", "mango", "grapes")

print(len(my_tuple))
print(my_tuple[2])
print(my_tuple[-1])

print(my_tuple.index("grapes"))
print(my_tuple.count("grapes"))

# SET

print("\nSET")

my_set = set()

my_set.add(1)
my_set.add(100)
my_set.add(100)

print(my_set)

new_list = [1,2,3,3,4,4,5,6]
print(set(new_list))

my_set.remove(100)
my_set.discard(100)

my_set.clear()

new_set = {1,2,3}.copy()
print(new_set)

# Set Operations

print("\nSET OPERATIONS")

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))

# Frozen Set

print("\nFROZENSET")

frozen = frozenset([1,2,3])
print(frozen)

# NONE

print("\nNONE")

a = None
print(type(a))

# EXTRA EXAMPLES

print("\nEXTRA EXAMPLES")

# Even or odd
number = 10

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")


# Reverse string
text = "Python"

reversed_text = text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)


# Sum of list
numbers = [10, 20, 30, 40]

total = sum(numbers)

print("Sum:", total)


# Min and max
numbers = [3, 7, 2, 9, 5]

print("Min:", min(numbers))
print("Max:", max(numbers))


# Remove duplicates
numbers = [1,2,2,3,4,4,5]

unique_numbers = list(set(numbers))

print("Unique numbers:", unique_numbers)


# Count letters
text = "banana"

print("Number of 'a':", text.count("a"))


# Range example
numbers = list(range(1, 11))

print("Numbers:", numbers)


# Check element in list
numbers = [1,2,3,4,5]

print(3 in numbers)
print(10 in numbers)