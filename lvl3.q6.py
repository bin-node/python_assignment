class Animal:
    def sleep(self):
        print("I love to sleep whole time")
class Sound:
    def voice(self):
        print("I can sound, but can't sing")
class Dog(Animal, Sound):
    def eat(self):
        print("I love to eat all the time")
    def voice(self):
        super().voice()
    def sleep(self):
        super().sleep()



class Cat(Dog):
    def sleep(self):
        print("I can sleep 18 hours a day")





huskey = Dog()
huskey.sleep()
huskey.voice()

ragdall = Cat()

ragdall.sleep()
ragdall.eat()
ragdall.voice()