# coding: UTF-8

#True or False

sales = [50,100,80,45]
#sales.reverse()
#print(sales)

d= "2016/10/11"
#print(d.split("/"))
a = ["a","b","c"]
#print("-".join(a))
#a = (2,5,8)
#print(len(a))
#print(a*3)
#b =list(a)
#print(b)

a = set([1,2,3,4])
b =set([3,4,5])
print( a^b)

sales = {"taguchi":200, "fkoji":300, "dot":500}
sales["fkoji"]=800
print(sales)
print("taguchi" in sales)
print(sales.keys())
print(sales.values())
print(sales.items())
