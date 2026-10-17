#child -> age < 13
#teenager -> age 13 - 19
#adult -> 20 - 59
#senior -> 60+

from collections import Counter

def age_group_categorization(age):
    if age < 13:
        print("Child")
    elif age >= 13 and age < 20:
        print("Teenager")
    elif age >= 20 and age < 60:
        print("Adult")
    else:
        print("Senior")

# age_group_categorization(11)

# =======================================================


str1 = "vivek@"

str1_obj = {}

for i in range(0,len(str1)):
    if str1_obj.get(str1[i]):
        str1_obj[str1[i]] = str1_obj[str1[i]] + 1
    else:
        str1_obj[str1[i]] = 1

# print(str1_obj)

# print(Counter(str1))

# =======================================================


for i in range(len(str1) - 1, -1, -1):
    print(str1[i])

rev = ""
for char in str1:
    rev = char + rev

print(rev)

# =============================
