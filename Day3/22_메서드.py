# 자주 사용하는 메서드

# 1. 리스트 메서드
# 1-1. sort
numbers = [30, 10, 50, 40, 20]
numbers.sort()
print(numbers)  # [10, 20, 30, 40, 50]

# sorted vs sort
# sorted는 원본을 변경하지 않는 함수이고
numbers = [30, 10, 50, 40, 20]
sorted_numbers = sorted(numbers)

print(numbers)  # [30, 10, 50, 40, 20]
print(sorted_numbers)  # [10, 20, 30, 40, 50]

# .sort 는 원본을 변경하는 메서드이다.
numbers = [30, 10, 50, 40, 20]
numbers.sort()

print(numbers)  # [10, 20, 30, 40, 50]


# 1-2. count
numbers = [1, 1, 2, 2, 2, 3, 4, 5]
print(numbers.count(2))  # 3

"""
numbers = [1, 1, 2, 2, 2, 3, 4, 5]
result = 0
wanted = 2

for number in numbers:
    if number == wanted:
        result += 1

print(result)  # 3
"""

# 1-3. index
numbers = [1, 2, 2, 3, 4]
print(numbers.index(1))  # 0
print(numbers.index(2))  # 1
# print(numbers.index(5))  # ValueError: 5 is not in list

# 1-4. extend
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7]

numbers1.extend(numbers2)

print(numbers1)  # [1, 2, 3, 4, 5, 6, 7]

for number in numbers2:
    numbers1.append(number)


# 2. 문자열
# 2-1. split (문자열을 구분자를 통해 나눠서 리스트로 저장)
word = "kyle alex justin haley" # -> ["kyle", "alex", "justin", "haley"]
names = word.split()
print(names)  # ['kyle', 'alex', 'justin', 'haley']


word = "kyle,alex,justin,haley"
names = word.split(",")
print(names)  # ['kyle', 'alex', 'justin', 'haley']

# 2-2. find, index
word = "hello"
print(word.find("e"))  # 1
print(word.find("p"))  # -1

print(word.index("e"))  # 1
# print(word.index("p"))  # ValueError: substring not found

# 2-3. count
word = "hello"
print(word.count("l"))  # 2

# 2-4. replace
word = "hello"
new_word = word.replace("h", "H")  # old -> new

print(word)  # hello 
print(new_word)  # Hello

# replace를 이용해서 문자를 삭제하는 것도 가능하다.
word = "hello"
new_word = word.replace("l", "")  # "l" -> ""
print(new_word)  # heo

# replace는 여러 문자열도 바꿀 수 있다.
word = "hello"
new_word = word.replace("llo", "rs")  # "llo" -> "rs"
print(new_word)  # hers

# 2-5. join (문자열 리스트를 특정 구분자를 통해 하나의 문자열로 묶어주기)
words = ["hello", "python", "!"]  # -> "hello python !"
result = " ".join(words)
print(result)  # hello python !

result = ",".join(words)
print(result)  # hello,python,!

result = "".join(words)
print(result)  # hellopython!

"""
hello
python
!
"""

for word in words:
    print(word)

print("\n".join(words))  # "hello\npython\n!"