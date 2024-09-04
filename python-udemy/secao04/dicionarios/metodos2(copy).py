import copy

d1 = {
    'c1':1,
    'c2':2,
    'c3': [9,8,7,6]
}


#shallow copy copy(d1)
# deep copy  deepcopy(d1)
# both using copy.xxx
d2 = copy.deepcopy(d1)  
d2['c1'] = 5 #ligados
d2['c3'][-1] = 0 #  A lista é alterada mesmo quando o copy() é usado


print(f'd1 = {d1}')
print(f'd2 = {d2}')