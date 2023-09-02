stack_l = [0]
input_l = []
sr_dict = {"id0": "S5", "id4": "S5", "id6": "S5", "id7": "S5","+1": "S6", "+2": "R2", "+3": "R4", "+5": "R6","+8": "S6", "+9": "R1", "+10": "R3", "+11": "R5","*2": "S7","*3": "R4", "*5": "R6", "*9": "S7", "*10": "R3", "*11": "R5","(0": "S4", "(4": "S4", "(6": "S4", "(7": "S4",")2": "R2", ")3": "R4", ")5": "R6", ")8": "S11", ")9": "R1", ")10": "R3", ")11": "R5", "$1": "accept", "$2": "R2", "$3": "R4", "$5": "R6", "$9": "R1", "$10": "R3", "$11": "R5", "E0": "1", "E4": "8","T0": "2", "T4": "2", "T6": "9","F0": "3", "F4": "3", "F6": "3", "F7": "10"}
input_i = input()
for i in input_i:
    if i == 'i': input_l.append('id')
    elif i == 'd':continue
    else:input_l.append(i)
input_l.append('$')
input_l.reverse()
def find_index(liste,harf):
    liste.reverse()
    index=liste.index(harf)
    liste.reverse()
    return (-(index+1))
def R(x):
    if x == '1':
        index_i = find_index(stack_l,'E')
        del stack_l[index_i::]
        stack_l.append('E')
    elif x == '2':
        index_i = find_index(stack_l, 'T')
        del stack_l[index_i::]
        stack_l.append('E')
    elif x == '3':
        index_i = find_index(stack_l, 'T')
        del stack_l[index_i::]
        stack_l.append('T')
    elif x == '4':
        index_i = find_index(stack_l, 'F')
        del stack_l[index_i::]
        stack_l.append('T')
    elif x == '5':
        index_i = find_index(stack_l, '(')
        del stack_l[index_i::]
        stack_l.append('F')
    elif x == '6':
        index_i = find_index(stack_l, 'id')
        del stack_l[index_i::]
        stack_l.append('F')
    stack_l.append(sr_dict.get("{}{}".format(stack_l[-1], stack_l[-2])))
def S(x):
    stack_l.append(input_l[-1])
    stack_l.append(x)
    input_l.pop()
stack_l.append(input_l[-1])
stack_l.append(sr_dict.get("{}{}".format(stack_l[-1], stack_l[0]))[-1])
del input_l[-1]
flag = True
while flag:
    x =sr_dict.get("{}{}".format(input_l[-1], stack_l[-1]))
    try:
        if x.startswith('S'):
            if len(x)==3:
                S(x[-1]+x[-2])
            else:
                S(x[-1])
        elif x.startswith('R'):
            R(x[-1])
        elif x == "accept":
            print("VALID string entered. ACCEPTED!")
            flag= False
    except:
        print("INVALID string entered. SYNTAX ERROR!")
        flag = False