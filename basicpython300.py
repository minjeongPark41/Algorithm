#221 - o
def print_reverse(str):
    print(str[::-1])

#222 - x 

# def print_score(list):
#     for i in list:
# print(sum(i)/len(list))

def print_score(list):
    print(sum(list)/len(list))

#223 - o 
def print_even(list):
    for i in list:
        if i%2==0:
            print(i)

#224 - x 
# def print_keys(dic):
#     dic.keys() -> 이러면 dict_keys(['이름', '나이', '성별'])

def print_keys(dic):
    for i in dic.keys():
        print(i)

#225 - o
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dict, date):
    print(dict[date])


#226 - x

"""
0:4
5:9
10:14
15: .... 
"""

# def print_5xn(string):
#     for i in range(len(string)):
#         # 만약 이러면 0부터 

def print_5xn(string):
    for i in range(int((len(string)/5))):
        print(string[i*5:i*5+5])

# TypeError: 'float' object cannot be interpreted as an integer -> int화

#227 - x 

"""
0:2
3:5
6:9
"""

# def print_mxn(string, num):
#     chunk = int(len(string)/num) # 🧚‍♂️ TypeError: 'int' object is not iterable
#     for i in chunk:
#         print(string[num*i:num*i+num])

def print_mxn(string, num):
    chunk = int(len(string)/num)
    for i in range(chunk+1):
        print(string[num*i:num*i+num])

#228 - o 

def calc_monthly_salary(annual_salary):
    print(int(annual_salary/12))

# 답지에서는 return. 

#229 - o

#230 - o

#231 -x 
"""
함수 내부에서 사용한 변수는 함수 밖에서는 접근이 불가능
함수 내부에서 계산한 값을 전달하기 위해서는 return을 사용해야 함

"""

#232 - x

# def make_url(address):
#     return("www.", address, ".com") # 이러면 ('www.', 'naver', '.com')

def make_url(address):
    url = "www." + address + ".com"
    return url 

#233 - o 
def make_list(str):
    return(list(str))

# 2번째 방법
def make_list(str):
    list = []
    for i in str:
        list.append(i)
    return(list)

#234 - o 

def pickup_even(list):
    new_list = []
    for i in list:
        if i%2 == 0:
            new_list.append(i)
    return new_list
    
#235 - o

def convert_int(str_number):
    str_number = str_number.replace(",","")
    return(int(str_number))

#236 - o 

#237 - o 

#238 - o 

#239 - o 

#240 - o

"""
함수1(12)
-> 함수0(14)
-> 28
"""



