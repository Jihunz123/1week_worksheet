
# 문자열 메서드 Count

text = "Hello, World!"
count = text.count("l")
print(count) # 3

# 문자열 메서드 find

text = "Hello, World!"
position = text.find("World")
print(position) # 7

# 문자열 메서드 index

text = "Hello, World!"
try:
    position = text.index("World")
    print(position)
except ValueError:
    print("찾는 문자열이 없습니다.")
    
# 문자열 메서드 join

fruits = ["apple", "banana", "cherry"]
joined_fruits = ", ".join(fruits)
print(joined_fruits) 

#문자열 메서드 upper, lower

text = "Hello, World!"
uppercase_text = text.upper()
print(uppercase_text)

lowercase_text = text.lower()
print(lowercase_text)

#문자열 메서드 replace

text = "Hello, World!"
replaced_text = text.replace("World", "Python")
print(replaced_text)

#문자열 메서드 split

text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)

#문자열 메서드 len

numbers = [1,2,3,4,5]
print(len(numbers))

#문자열 메서드 del

numbers = [1,2,3,4,5]
del numbers[2]
print(numbers)

#문자열 메서드 append

numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)

#문자열 메서드 sort
numbers = [3,2,4,1,5]
numbers.sort()
print(numbers)

#문자열 메서드 reverse
numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)

#문자열 메서드 index
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana'))

#문자열 메서드 insert
numbers = [1,2,3,4,5]
numbers.insert(2, 10)
print(numbers)

#문자열 메서드 remove
numbers = [1,2,3,4,5]
numbers.remove(3)
print(numbers)

#리스트 메서드 pop
numbers = [1,2,3,4,5]
numbers.pop(3)
print(numbers)

#리스트 메서드 count
numbers = [1,2,3,3,4,5]
print(numbers.count(3))

#리스트 메서드 extend
numbers = [1,2,3]
numbers.extend([4,5,6])
print(numbers)

#리스트 메서드+=
numbers = [1,2,3]
numbers += [4,5,6]
print(numbers)

#딕셔너리 메서드 딕셔너리 초기화

empty_dict = {}

my_dict = {"apple":1, "banana":2, "orange":3}

print(my_dict)

#딕셔너리 메서드 딕셔너리 쌍 추가

my_dict = {"apple":1, "banana": 2, "orange":3}

my_dict["grape"] = 4
print(my_dict)

#딕셔너리 메서드 del

my_dict = {'apple': 1, "banana":2, "orange": 3}

del my_dict["apple"]
print(my_dict)

#딕셔너리 메서드 Key -> Value

my_dict = {"apple": 1, "banana":2, "orange":3}

print(my_dict["banana"])

#딕셔너리 메서드 keys

my_dict = {"apple":1, "banana":2, "orange":3}

key_list = list(my_dict.keys())
print(key_list)

#딕셔너리 메서드 values
my_dict = {"apple":1, "banana":2, "orange": 3}

value_list = list(my_dict, values())
print(value_list)

#딕셔너리 메서드 items
person = {'name': 'Jihun', 'age':30, 'gender': 'male'}

items = person.items()
print(items)

#딕셔너리 메서드 clear
person = {'name': 'Jihun', 'age':30, 'gender': 'male'}

person.clear()
print(person)
#딕셔너리 메서드 get
person = {'name': 'Jihun', 'age':30, 'gender':'male'}

name = person.get('name')
print(name)

#딕셔너리 메서드 in
person = {'name': 'Jihun', 'age':30, 'gender': 'male'}

print('name' in person)
print('email' in person)