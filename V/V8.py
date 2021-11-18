class Student:
    def __init__(self, name, surname, mark):
        self.name = name
        self.surname = surname
        self.mark = mark

    def __str__(self):
        return str(self.__dict__)


st1 = Student("John", "Thomson", 2)
st2 = Student("Tom", "Thomson", 3)
st3 = Student("Nikki", "Thomson", 5)
min_grade = st3.mark
trash = None

if st1.mark > st2.mark:
    trash = st2
elif st1.mark < st2.mark:
    trash = st1

if trash.mark > st3.mark:
    trash = st3
else:
    print(trash.name)
