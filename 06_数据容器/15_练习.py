money_dict = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    }, "周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    }, "林俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    }, "张学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    }, "刘德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}
print(f"全体员工当前信息如下:{money_dict}")

for name in money_dict:
    if money_dict[name]["级别"] == 1:
        employee_dict = money_dict[name]
        employee_dict["级别"] = 2
        employee_dict["工资"] += 1000
        money_dict[name] = employee_dict

print(f"员工级别为1的员工升职加薪,操作后:{money_dict}")
