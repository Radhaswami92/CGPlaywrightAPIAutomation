class Parent:
    def greet(self):
        print("Hello I am from greet from parent")
    def only_greet(self):
        print("I am a method belongs to Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello I am greet from child")



obj = Child()
obj.greet()
obj.only_greet()

