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

    # 😶출력 결과는 같게 나오긴하는데... 언제 cls를 쓸까 

    @classmethod
    def get_account_num(cls):
        print(cls.account_count) 

#274 - x

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

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, 입금):
        if 입금 >= 1:
            self.초기잔액 +=입금

#275 - x 

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

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, 입금):
        if 입금 >= 1:
            self.초기잔액 +=입금

    def withdraw(self, 출금):
        if 출금 < self.초기잔액:
            self.초기잔액 -=출금

    # 😶 withdraw 함수에서는 self가 붙었다는점 


#276 - x 

class Account:
    
    account_count = 0 

    def __init__(self, name, 초기잔액):
        self.name = name
        self.초기잔액 = 초기잔액
        self.bank = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0, 999999)

        num1 = str(num1)
        num2 = str(num2)
        num3 = str(num3)

        self.account = num1 + '-' + num2 + '-' +num3

        Account.account_count +=1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, 입금):
        if 입금 >= 1:
            self.초기잔액 +=입금

    def withdraw(self, 출금):
        if 출금 < self.초기잔액:
            self.초기잔액 -=출금

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주:", self.name)
        print("계좌번호:", self.account)
        print("잔고:", format(self.초기잔액, ','))


"""
cf) 1000단위마다 콤마 넣는법
number =  12345
number =  format(number, ',')

"""

#277 - x 

class Account:
    
    account_count = 0 

    def __init__(self, name, 초기잔액):

        self.deposit_count = 0 # 😶 왜 여기다가 두지? 

        self.name = name
        self.초기잔액 = 초기잔액
        self.bank = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0, 999999)

        num1 = str(num1)
        num2 = str(num2)
        num3 = str(num3)

        self.account = num1 + '-' + num2 + '-' +num3

        Account.account_count +=1

        # if Account.account_count == 5:
        #     self.초기잔액 = self.초기잔액*1.1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, 입금):
        if 입금 >= 1:
            self.초기잔액 +=입금

            self.deposit_count +=1
            if self.deposit_count % 5 == 0:
                self.초기잔액 = (self.초기잔액*1.01)

    def withdraw(self, 출금):
        if 출금 < self.초기잔액:
            self.초기잔액 -=출금

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주:", self.name)
        print("계좌번호:", self.account)
        print("잔고:", format(self.초기잔액, ','))

#278 - o

list = []

박 = Account("박", 1000)
석 = Account("석", 2000)
김 = Account("김", 3000)

list.append(박)
list.append(석)
list.append(김)


#279 - x 

for i in list:
    if i.초기잔액 > 1000000:
        # print(i.name)
        i.display_infor()

#280 - pass 

#281 - o

class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

#282 - x

# class 자전차(class 차):

class 자전차(차):
    pass

#283 - x 

class 자전차(차):
    def __init__ (self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

#284 - o 

class 자전차(차):
    def __init__ (self, 바퀴, 가격, 구동계):
        # self.바퀴 = 바퀴
        # self.가격 = 가격
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

bicycle = 자전차(2, 100, "시마노")
bicycle.구동계

#285 - x 

class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자동차(차):
    def __init (self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

    # def 정보(self, 바퀴, 가격):
    #     print("바퀴수", 바퀴)
    #     print("가격", 가격)

    #😶
    def 정보(self):
        print("바퀴수:", self.바퀴)
        print("가격", self.가격)

#286 - pass

#287 - pass 

#288 - pass 
 
#289 - pass 

#290 - pass 

#291 - pass ( 파일 쓰기 )

#292 - pass ( 파일 쓰기 ) 

#293 - pass ( 파일 쓰기 )

#294 - pass ( 파일 읽기 )

#295 - pass ( 파일 읽기 )

#296 - x 

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

#297 - x 

per = ["10.31", "", "8.00"]

# list = []

# for i in per:
#     float(i)
#     list.append(i)

list = [] 

for i in per:
    try:
        i = float(i)
    except:
        i = 0 
    list.append(i)

print(list)

#298 - x

try:
    a = 3/0
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")

#299 - x 

data = [1, 2, 3]

# try:
#     for i in range(5):
# except:
#     print("올바른 범위가 아닙니다.")

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)
        # 3,4 는 list index out of range

"""
try:
    실행코드
except 예외 as 변수:
    예외처리코드 
"""

#300

"""
try:
    실행 코드
except:
    예외가 발생했을 때 수행할 코드
else:
    예외가 발생하지 않았을 때 수행할 코드
finally:
    예외 발생 여부와 상관없이 항상 수행할 코드
"""

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(per))
    except:
        print(0)
    else:
        "예외 없음"
    finally:
        "항상 수행"