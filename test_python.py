list1 = [1,2,3,[7,8]]
list2 = list1.copy()
# list1 = [1,2,3,4,5,6,7,8]
print("list1: ",list1)
print("list2: ",list2)
#
list1[3][0] = 9
list1[2] = 9

print("list1: ",list1)
print("list2: ",list2)



def get_lines():
    l = []
    with open('file.txt','rb') as f:
        data = f.readlines(60000)
    l.append(data)
    yield l
