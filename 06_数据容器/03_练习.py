age_list = [21, 25, 21, 23, 22, 20]

age_list.append(31)
print(age_list)

new_list = [29, 33, 30]
age_list.extend(new_list)
print(age_list)

print(age_list[0])
print(age_list[-1])
print(age_list.index(31))
