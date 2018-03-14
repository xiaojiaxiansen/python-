'''
station = ["dali","hainan","chengdu","guangdong","shijiazhuang"]
print(station)
print("~"*20)

#使用sorted按字母顺序相反的顺序打印列表 （不会）

print(sorted(station))
print(station)
print("~"*20)

station.reverse()
print(station)
print("~"*20)

station.reverse()
print(station)
print("~"*20)

station.sort()
print(station)
print("~"*20)

station.sort(reverse=True)
print(station)
print("~"*20)
'''


list = ["china","japan","america","canada","indea","faguo","eluosi"]
'''
print(list)
print("@"*40)
#添加元素
list.append("hanguo")
print(list)

print("@"*40)
list.insert(4,"chaoxian")
print(list)
print("@"*40)
#修改元素
list[1] = "malaixiya"
print(list)
print("@"*40)
#删除元素
del list[4]
print(list)
print("@"*40)

list.pop()
print(list)

print("@"*40)
list.pop(3)
print(list)

print("@"*40)
list.remove("malaixiya")
print(list)
#排序

print("@"*40)
#list.sort()
#print(list)

#print("@"*40)
#list.sort(reverse = True)
#print(list)

print(sorted(list))

print("@"*40)
list.reverse()
print(list)

print("@"*40)
print(len(list))
'''

print("The first three items in the list are:")
print(list[0:3])
print("Three items from the middle of the list are:")
print(list[2:5])

print("The last three items in the list are:")
print(list[-3:])
