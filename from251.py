#251 - pass

"""
클래스, 객체, 인스턴스에 대해 설명해봅시다.
"""

#252 - x

# class Human:

class Human:
    pass

#253 - o 
areum = Human()

#254 - x 
class Human:
    print("응애응애")

areum = Human()

# 😶 그냥 Human()만 하면 응애응애-라고는 나오는데 <__main__.Human at 0x1f05113c2e0> 가 같이 나옴

#255 - x ⭐️

# class Human(name, age, gender):

class Human:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("아름", 25, "여자")
print(areum.name)
    
#256 - o

areum = Human("조아름", 25, "여자")
print(areum.name)
print(areum.age)
print(areum.gender)

#257 - x 🙀 엉망으로 생각하여... 기록을 남김

# class Human():
#     def who():
#         print 

# # 출력
# areum = Human()


# 2번째 시도. x 🙀 -------------------------------

# class Human():
#     __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def who(self):
#         print("name{}, age{}, gender{}.format(self.name, self.age, self.gender)")

# areum = Human()
# areum.who()

# 3번째 시도----------------------------------------

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self): #😶 self 잊으면 안돼! 
        print("이름:{}. 나이:{}, 성별:{}".format(self.name, self.age, self.gender))

areum = Human("조아름", 25, "여자")
areum.who()

#258 - x

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print("이름:{}, 나이:{}, 성별:{}".format(self.name, self.age, self.gender))

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("모름", 0, "모름")
areum.who() # 이름:모름, 나이:0, 성별:모름

areum.setInfo("아름", 25, "여자")
areum.who() #이름:아름, 나이:25, 성별:여자

#259 - x 소멸자 : 객체가 소멸할 때 호출됨

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print("이름:{}, 나이:{}, 성별:{}".format(self.name, self.age, self.gender))

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#260 - x 😶 이유를 모르겠당...

#261 - o 

class Stock:
    pass

#262 - o 

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

삼성 = Stock("삼성전자", "005930")      
print(삼성.name)

#263 - o

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

a = Stock(None, None)
print(a.name) # None

a.set_name("삼성전자")
print(a.name) # 삼성전자

#264 -x 

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

a = Stock(None, None) 
# 괄호 안에 주지 않으면 
# -> __init__() missing 2 required positional arguments: 'name' and 'code'
a.set_code("005930")
print(a.code)

#265 - x ⭐️ 

# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code

#     def get_name(self, name):
#         print(self.name)

#     def get_code(self, code):
#         print(self.code)

# 삼성 = Stock("삼성전자", "005930")
# 삼성.get_name("삼성전자")
# 삼성.get_code("005930")

#----------------------------------

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code
        
삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)
print(삼성.get_name())
print(삼성.get_code())

#266 - o

class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

#267 - o

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)

#268 - o

class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, 배당수익률):
        self.배당수익률 = 배당수익률

#269 - o

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
삼성.set_per(12.75)

print(삼성.per)

#270 - x 

# 삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# 현대 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
# LG = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

# list = [] 

# list.append(삼성, 현대, LG) 
# 🙀 TypeError: list.append() takes exactly one argument (3 given)

# for i in list:
#     print(i.code, i.per)

list = [] 

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

list.append(삼성)
list.append(현대)
list.append(LG)

for i in list:
    print(i.code, i.per)

#271 - x 😶zfill 함수는 굳이 왜 다시 해주는거지?

# class Account:
#     def __init__(self, 예금주, 초기잔액):
#         self.예금주 = "SC은행"
#         self.초기잔액 = 

"""
randint()함수는 지정된 범위 사이에서 임의의 정수를 생성하는 데 사용
시작 및 끝 위치는 매개 변수로 함수에 전달


x = 2
print(str(x).zfill(2))
# 02

print(str(x).zfill(3))
# 002

"""

import random

class Account:
    def __init__(self, name, 초기잔액):
        self.name = name
        self.초기잔액 = 초기잔액
        self.banck = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0, 999999)

        self.account = num1 + '-' + num2 + '' +num3

은행 = Account()
print(은행.account)

# 🙀 이렇게만 하면 잘못한 점 
# 1) TypeError: __init__() missing 2 required positional arguments: 'name' and '초기잔액'
# 2) TypeError: unsupported operand type(s) for +: 'int' and 'str'

# -----------------------------------------------------

class Account:
    def __init__(self, name, 초기잔액):
        self.name = name
        self.초기잔액 = 초기잔액
        self.banck = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0, 999999)

        num1 = str(num1)
        num2 = str(num2)
        num3 = str(num3)

        self.account = num1 + '-' + num2 + '-' +num3

은행 = Account(None, None)
print(은행.account)

#272 - x

class Account:

    account_count = 0

    def __init__(self, name, 초기잔액):
        self.name = name
        self.초기잔액 = 초기잔액
        self.banck = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0, 999999)

        num1 = str(num1)
        num2 = str(num2)
        num3 = str(num3)

        self.account = num1 + '-' + num2 + '-' +num3

        # account_count +=1 😶 이러면 왜 안되지
        Account.account_count +=1

# 😶 출력에서 이렇게 접근하는거. 객체로 접근해도 나오는데... 위에는 왜 꼭 저렇게 접근해야하는지

kim = Account("김민수", 100)
print(Account.account_count)
lee = Account("이민수", 100)
print(Account.account_count)

#273 -x 😶 cls (class method)

class Account:

    account_count = 0 

    def __init__(self, name, 초기잔액):
        self.name = name
        self.초기잔액 = 초기잔액
        self.banck = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0, 999999)

        num1 = str(num1)
        num2 = str(num2)
        num3 = str(num3)

        self.account = num1 + '-' + num2 + '-' +num3

        Account.account_count +=1

    def get_account_num(self):
        print(Account.account_count)



#274


#275


#276


#277


#278


#279


#280

