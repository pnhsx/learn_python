str1 = "万过薪月,员序程马黑来,nohtyP学"

str2 = str1[::-1]

str3 = str1[::-1][9:14]
print(str3)

str4 = str1.split(",")[1].replace("来", "")[::-1]
print(str4)
