import random

class ParentClass:
    def foo(self):
        print("ParentClass")

class ChildClass1(ParentClass):
    def foo(self):
        print("ChildClass1")

class ChildClass2(ParentClass):
    def foo(self):
        print("ChildClass2")
        
        
objects = []

for i in range(500):
    if random.randint(0, 1):
        obj = ChildClass2()
    else:
        obj = ChildClass1()
    objects.append(obj)
    
for obj in objects:
    obj.foo()