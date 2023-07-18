import re

# s = "itheima1 @@python2 !!666 ##itcast3 PYTHON SPARK"
#
# result = re.findall(r'[A-z]', s)  # 字符串前带上r的标记, 表示字符串中转义字符无效,就是普通字符的意思
# print(result)

# 匹配账号,只能由字母和数字组成,长度限制6-10位
# r = '^a-zA-Z0-9]{6,10}$'
# s = '1234567_'
# print(re.findall(r, s))

# 匹配QQ号, 要求纯数字,长度5-11,第一位不为0
r = '^[1-9][0-9]{4,10}$'
s = '123489122'
print(re.findall(r, s))

# 匹配邮箱地址,只允许qq,163,gmail 这三种邮箱
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = 'a.b.c.e.f.g@qq.com.a.z.g.c.d'

print(re.match(r, s))
