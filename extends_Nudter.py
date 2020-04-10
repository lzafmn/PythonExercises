class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
class Nudter(Person):
    def __init__(self, age, name, nudtId):
        Person.__init__(self, age, name)
        self.Id = nudtId
    def getNudtId(self):
        return self.Id
    def setNudtId(self, Id):
        self.Id = Id
    def __lt__(self, other):
        try:
            return self.Id < other.Id
        except:
            try:
                return  self.Id < other
            except:
                raise TypeError('nudtId: Non_surported oerand type!')

class CollegeStudent(Nudter):
    pass
class Graduate(CollegeStudent):
    def __init__(self, age, name, nudtId, ocp):
        super().__init__( age, name, nudtId)
        self.ocp = ocp
    def getOccupation(self):
        return self.ocp
class UnderGraduate(CollegeStudent):
    def __init__(self, age, name, nudtId, classYear):
        super().__init__(age, name, nudtId)        
        self.classYear = classYear
    def getClass(self):
        return self.classYear

n1 = Nudter(20, 'zhangsan', 48)
g1 = Graduate(19, 'grad1', 23, 'developer')
u1 = UnderGraduate(19, 'ungrad1', 24, 'grade2')
g1.setNudtId(25)
print(g1.getNudtId())
print(g1 < u1)
print(n1 < g1)
##print('-----', super())
