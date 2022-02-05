'''class Human:
    age = 10
    height = 150
    weight = 50
    def say_hello(self):
        print('Hello!')
        print('I am a human')

    def say_good_bye(self):
        print('See you!')

John = Human()
Frank = Human()
print(John.age, Frank.age)
print(John.height)
print(Frank.weight)
John.say_hello()
Frank.say_good_bye()'''

'''age = 100
name = 'Inginirum'
nums = [10,20,30]

print(type(age))
print(type(name))
print(type(nums))'''

'''class Hero:
    def hit(self):
        print('HIT!')

    def jump(self):
        print("I'm jumping!")

Arnold = Hero()
Arnold.jump()'''

'''class Human:
    def __init__(self,age,name,height):
        self.age = age
        self.name = name
        self.height = height
        print('I was born here! My name is', name)

    def say_hello_to(self,name_to):
        print('Hello,', name_to)

    def tell_about_yourself(self):
        print('Hello, my name is', self.age)
        print('I am', self.age, 'y o')

    def happy_birthday(self):
        print('Today is my birthday!')
        self.age +=1

print('MICHAEL')
Michael = Human(16, 'Michael', 171)
print(Michael.age)
Michael.happy_birthday()
print(Michael.age)

print('KUSHYAN')
Kushyan = Human(15, 'Kushyan', 154)
Kushyan.say_hello_to('Erik')'''

'''class Car:
    def sound(self):
        print('beep')

    def long_sound(self):
        print('beep-beep')

BMW = Car()

BMW.sound()
BMW.long_sound()'''

class Button:
    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks +=1

    def reset(self):
        self.clicks = 0

    def click_count(self):
        print(self.clicks)


a = Button()
a.click()
a.click()
a.click()
a.reset()
a.click()
a.click_count()

