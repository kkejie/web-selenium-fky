# coding=utf-8

str = "521,25,2.03"
by = ''
value = ''
value2 = ''
if "," not in str:
    by = ""
    value = str
elif len(str.split(",")) == 2:
    by = str.split(",")[0]
    value = str.split(",")[1]
else:
    by = str.split(",")[0]
    value = str.split(",")[1]
    value2 = str.split(",")[2]

strr = by + value + value2

print(by)
print(value)
print(float(strr))
print(len(str.split(",")))