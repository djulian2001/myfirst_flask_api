

class Student(object):
  """docstring for Student"""
  def __init__(self, name, age, school):
    # super(Student, self).__init__()
    self.name = name
    self.age = age
    self.school = school
    
  def average(self):
    pass

  # Student is passed in, not the instance of the class
  @classmethod
  def go_to_school(cls):
    print("I'm going to school.")
    # print("I'm going to school at {}.".format(cls.school()))
    print("I'm a {}".format(cls.__name__))

  # another decarator
  @staticmethod
  def bring_paper():
    print("You bet, we bring paper!")

  @classmethod
  def friend(cls, name, school, age=20, *args, **kwargs):
    return cls(name, age, school, *args, **kwargs)
  

class WorkingStudent(Student):
  """docstring for WorkingStudent"""
  def __init__(self, name, age, school, salary=11.00, job_title="grunt"):
  # def __init__(self, *args, salary=11.50, job_title='grunt', **kwargs):
    super().__init__(name, age, school)
    self.salary = salary
    self.job_title = job_title

  # @classmethod
  # def friend(cls, *args, **kwargs):
  #   return super().friend(*args, **kwargs)

  def school(self):
    return str(super().school)


def main():
  worker = WorkingStudent('Ann', 18, 'asu', salary=20.00)
  friend = worker.friend(age=23, name='Peter', school=worker.school)

  worker.bring_paper()
  worker.go_to_school()

  print(friend.salary)

  student = Student('Bobby',28, 'Colins College')
  s_friend = student.friend('Tammy', 'ASU', 22)

  print(s_friend.name,s_friend.age,s_friend.school)
  # print(friend.name,friend.age,friend.school,friend.job_title)
  print(friend.name)
  


if __name__ == "__main__":
  main()