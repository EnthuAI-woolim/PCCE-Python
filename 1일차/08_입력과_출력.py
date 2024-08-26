# 1. 입력
#word = int(input()) # 무조건 문자열로 받는다!
#print(word)
#print(type(word))

# 2. 출력
name1 = "kyle"
name2 = "alex"
name3 = "harry"

# 2-1. 아래로 출력
print(name1)
print() # 공백을 출력
print(name2)

# 2-2. 옆으로 출력
print(name1, name2, name3)

# 2-3. end 옵션
print(name1, end=" ")
print(name2, end=" ")
print(name3)

# 2-4. sep 옵션
print(name1, name2, name3, sep="$$")