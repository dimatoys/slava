## This is an Animal class inheriting default object
class Animal(object):
    def __init__(self, name):
        self.name = name

## This is a Dog class inheriting Animal class (IS-A)
class Dog(Animal):
    def __init__(self, name):
        ## Property of the Dog class / Dog object (HAS-A)
        self.name = name

## Cat class inheriting Animal class (IS-A)
class Cat(Animal):
    def __init__(self, name):
        ## Property of the Cat class / Cat object (HAS-A)
        self.name = name

## Person class inheriting default object (IS-A)
class Person(object):
    def __init__(self, name):
        ## Property of Person object (HAS-A)
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee class inheriting Person class (IS-A)
class Employee(Person):
    def __init__(self, name, salary):
        ## Create an object of Parent class of Employee, i.e. 
        ## Person and call it's initializer
        super(Employee, self).__init__(name)
        ## Property of employee class
        self.salary = salary

## Fish class which inherites object
class Fish(object):
    def __init__(self,name):
        self.name = name
## Salmon class inheriting Fish
class Salmon(Fish):
    def __init__(self,name):
        self.name = name
## Halibut inheriting Fish
class Halibut(Fish):
    def __init__(self,name):
        super(Halibut,self).__init__(name)
## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mery has-a pet satan
mary.pet = satan

print(mary.name, ' has a ', mary.pet.name)

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a pet rover
frank.pet = rover

## flipper is a Fish
flipper = Fish("Flipper")

## crouse is a Salmon
crouse = Salmon("Crouse")

## harry is a Halibut
harry = Halibut("Harry")

john = Employee('John', 1000000)
david = Employee('David', 12345678)
john.pet = crouse
david.pet = harry

print(john.name)
print(john.pet.name)
print(david.name)
print(david.pet.name)