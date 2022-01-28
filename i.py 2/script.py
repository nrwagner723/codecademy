class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  
  def getName(self):
    return self.name

  def getLevel(self):
    return self.level

  def getnumberOfStudents(self):
    return self.numberOfStudents

  def setnumberOfStudents (self, newNumberOfStudents):
    self.newNumberOfStudents = newNumberOfStudents

  def __repr__(self):
    return (f'A {self.level} school named {self.name} with {self.numberOfStudents} students. ')

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getpickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + 'The pickup policy is {pickupPolicy}'.format(pickupPolicy = self.pickupPolicy)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams

  def getsportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentReprP = super().__repr__()
    return parentReprP + 'The sports teams are {sportsTeams}'.format(sportsTeams = self.sportsTeams)

mySchool = School('Codecademy', 'high', 20)
print(mySchool)
# print(mySchool.getName())
# print(mySchool.getLevel())
mySchool.setnumberOfStudents(50)
# print(mySchool.getnumberOfStudents())

myPrimarySchool = PrimarySchool('Codecademy', 100, 'Allowed')
# print(myPrimarySchool.getpickupPolicy)
print(myPrimarySchool)

myHighSchool = HighSchool('Codecademy', 1000, 'Soccer and Tennis')
# print(myHighSchool.getsportsTeams())
print(myHighSchool)
