#variant 36
from math import pow
from time import perf_counter
from itertools import filterfalse
import mmm
def decorator(func):
    def wrapper(data):
        try:
            t_start = perf_counter() #TODO: comment this line
            max_num, closest_char = func(data)
            all_time = perf_counter() - t_start
            nums = [x for x in data if isinstance(x,float)] # get all numbers in list
            chars = [y for y in data if isinstance(y,str)] # get all chars in list
            if nums: # check if there are numbers in list
                min_num = min(nums) # get min number in list,               !!!math is used
                min_num = pow(min_num, 2) # get square of min number
                print(f"Минимальное из чисел в строке в квадрате: {min_num:.7f}")
            if chars: # check if there are chars in list
                count = chars.count(chars[2]) # get count of third char in list
                print(f"Количество повторений третьего символа в строке: {count}")
            if max_num: # check if there is a max number in list
                print(f"Максимальное из чисел в строке: {max_num}")
            else:
                print("В списке нет чисел")
            if closest_char: # check if there is a closest char in list
                print(f"Ближайший сивол к концу: {closest_char}")
            else:
                print("В списке нет символов")
            print(f"Время выполнения: {all_time:.10f} секунд")
            print(f"Рандомное значение 1: {mmm.gen_1()}")
            print(f"Рандомное значение 2: {mmm.gen_2():.2f}")
            return max_num, closest_char
        except Exception as e:
            print("Error: " + str(e))
    return wrapper

def check_input(dataStr):
    dataStr = str(dataStr)
    allowed_symdols = ("BCDFGHJKLMNPQRSTVWXZ")
    if not dataStr: raise Exception("Empty input")
    else:
        if '.' in dataStr: # check if number is float
            try:
                num = float(dataStr) # try to convert to float
                if num < 0: # check if number is negative
                    return num
                else:
                    raise Exception("Not negative number")
            except ValueError: 
                raise Exception("Wrong symbols in number")
        else:
            data = filterfalse(lambda data : not(len(data) == 1 and data in allowed_symdols), dataStr) # filtering input with allowed symbols
            return list(data)

@decorator
def counter(dataList):
    allowed_symdols = ("BCDFGHJKLMNPQRSTVWXZ")
    if not isinstance(dataList,list): # check if input is a list
        raise Exception("Wrong type of function formal argument")
    nums = [x for x in dataList if isinstance(x,float)] # get all numbers in list
    chars = [y for y in dataList if isinstance(y,str)] # get all characters in list
    if not nums: # check if input is not containing numbers
        max_num = False
    else:
        max_num = max(nums) # get max number in list
    if not chars: # check if input is not containing characters
        closest_char = False
    else:
        closest_char = min(chars, key=lambda x: abs(allowed_symdols.find(x) - len(allowed_symdols))) # get closest character to the end of alphabet
    return max_num, closest_char

#main
dataList = [] 
help(mmm)
intList = [mmm.gen_1() for _ in range(10)]
floatList = [mmm.gen_2() for _ in range(10)]
print(intList)
print(floatList)
intList = list(map(check_input, intList))
floatList = list(map(check_input, floatList))
print(intList)
print(floatList)
while True:
    data = input("Enter your data, plaese (or 'end' for finish): ")
    
    if data.lower() == "end":
        print("Finished!")
        break
    else:
        try:
            data = check_input(data)
            print(data)
            dataList.append(data)
        except Exception as e:
            print("Error: " + str(e))
counter(dataList)