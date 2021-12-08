
class Person:
  def __init__(self, fname, fage ):
    self.firstname = fname
    self.age =  fage

  def printname(self):
    print(self.firstname, self.age)



class Student(Person):
  def __init__(self, fname, fage):
    super().__init__(fname, fage)
    self.note = 20


mathis = Student("Mathis", 19)
theo = Person("Theo", 20)


mathis.printname()

theo.printname()


print(mathis.note)
print(theo.note)
