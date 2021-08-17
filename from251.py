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

#258

#259

#260

