class Parrot:
    #class attribute
    species = "bird"
    count = 0
    # instance attribute
    def __init__(self,name,age):
        Parrot.count += 1
        self.name = name
        self.age = age
    @classmethod
    def count_ins(cls):
        return f"{cls.count}"
    def sing(self,song):
        return "{} sings {}".format(self.name,song)

obj = Parrot("Blu",10)
obj2 = Parrot("Bu",20)
print(Parrot.count_ins())
print(obj.sing(" 'Happy' "))
#access the class attributes
print("Blu is a {}".format(obj.__class__.species))
        
#access the instance attributes
print("{} is {} year old".format(obj.name, obj.age))