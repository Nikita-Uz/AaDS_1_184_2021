n = int(input())
array = input()

str_list = array.split(" ")
res = []

for item in str_list:
    res.append(int(item))

print(res)

def Func(list_):
    list_.sort()
    new_list = set(list_)
    new_list = tuple(new_list)
    return new_list
    
 

print(Func(res))
