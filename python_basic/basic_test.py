import json
dict1 = {'zhangfei':1, "liubei":2, "guanyu": 4, "zhaoyun":3}
myjson = json.dumps(dict1)
mydict = json.loads(myjson)

import random
list_1 = list(range(1,10))
random.shuffle(list_1)
print(list_1)

class A(object):
    def funcA(self):
        print("this is func A")
    
class B(A):
    def funcA_inB(self):
        super(B,self).funcA()
    
    def funcC(self):
        print("this is func C")
        
ins = B()

ins.funcA_inB()
ins.funcC()
    

a = A()
b = B()
print(f"isinstance: {isinstance(a,A)}")
print(f"isinstance: {isinstance(b,A)}")
print(f"type func is : {type(a)==A}")
print(f"type func is : {type(b)==A}")


# # 元类的创建
# class MyMetaClass(type):
#     def __new__(cls,name,bases,attrs):
#         # 修改类的属性和方法
#         attrs["__str__"] == lambda self: "This is a class created by MyMetaClass"
#         # 添加新的属性和方法
#         attrs["new_method"] = lambda self:"this is a new method"
#         # 控制类的继承关系
#         if name == "MyClass":
#             bases += (BaseClass,)
#         return super().__new__(cls,name,bases,attrs)

# class MyClass(object,metaclass = MyMetaClass):
#     pass
# print(MyClass())
# # 输出：This is a class created by MyMetaClass
# obj = MyClass()
# obj.new_method()

print("all",all([1,2,0,3,4]))
print("any",any([1,2,0,3,4]))

def reverse_int(x):
    if not isinstance(x,int):
        return False
    if -10 < x < 10:
        return x
    tmp = str(x)
    if tmp[0] != "-":
        tmp = tmp[::-1]
        return int(tmp)
    else:
        tmp = tmp[1:][::-1]
        x = int(tmp)
        return  -x

res = reverse_int(-23782)


def sum(*arg):
    def inner_sum():
        tmp = 0
        for i in arg:
            tmp += i
        return tmp
    return inner_sum


# mysum = sum(2,4,6)
# print(mysum)
# res1 = mysum()
# print(res1)
def my_dec(func):
    def wrapper(*args,**kwargs):
        print("Befor callign function")
        result = func(*args,**kwargs)
        print("After calling funciton")
        return result
    return wrapper

@my_dec
def my_function(x):
    return x + 1

res2 = my_function(32)
print(res2)

'''
判断两个json格式的数据是否相等
'''
file_text2 = '{"name":"john","age":22,"sex":"woman","address":"USA"}'
file_text1 = '{"name":"john","age":22,"sex":"man","address":"USA"}'
dict1 = json.loads(file_text1)
dict2 = json.loads(file_text2)
for s1, s2 in zip(sorted(dict1), sorted(dict2)):
    print(s1,s2)
    if str(dict1[s1]) != str(dict2[s2]):
        print(s1 + ":" + dict1[s1] + "!=" + s2 + ":" + dict2[s2])
# sex:man!=sex:woman

# 主动抛出异常
# def test_raise(n):
#     if not isinstance(n,int):
#         raise Exception("n is not an integer")
#     else:
#         print("good")
# test_raise(8.9)


# def test_Assert(n):
#     assert n == 2, "n is not 2"
#     print("n is 2")
# test_Assert(8.9)

import datetime
def dayofyear():
    '''
    year，day,month都是数字！ 很关键
    :return:
    '''
    year = datetime.datetime.today().year
    month = datetime.datetime.today().month
    day = datetime.datetime.today().day
    dayofyear = year + month + day
    print(dayofyear)
    print(year)
dayofyear()

