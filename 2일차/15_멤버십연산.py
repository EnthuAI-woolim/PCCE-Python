# 멤버십(Membership) 연산
# 특정 원소가 해당 컨테이너에 속하나요? -> True or False
# in, not in

# 1. 리스트에서의 사용
numbers = [1, 2, 3, 4, 5]
print(1 in numbers)  # True
print(0 not in numbers)  # True

# 2. 문자열에서의 사용
word = "python"
print("p" in word)  # True
print("j" not in word)  # True

# 3. 실 사용 예시
names = ["kyle", "alex", "justin", "harry"]

if "haley" in names:
    print("멤버입니다.")
else:
    print("멤버가 아닙니다.")