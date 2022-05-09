class Student:
    def __init__(self, name, payment, marks, subjects):
        self.nameStudent = name
        self.pay = payment
        self.marksStudent = marks
        self.subject = subjects

    def __str__(self):
        return f'Students name: {self.nameStudent} '

    def __add__(self, other):
        if isinstance(other, Student):
            return self.pay + other.pay
        elif isinstance(other, (int, float)):
            return other + self.pay

    def __radd__(self, other):
        return self.pay + other

    def __iadd__(self, other):
        self.pay = self + other
        return self.pay

    def __sub__(self, other):
        return self.pay - other

    def __rsub__(self, other):
        return self.pay - other

    def __isub__(self, other):
        self.pay = self - other
        return self.pay

    def __truediv__(self, other):
        if isinstance(other, Student):
            return self.pay / other.pay

    def __rtruediv__(self, other):
        return self.pay / other

    def __itruediv__(self, other):
        self.pay = self / other
        return self.pay

    def __mul__(self, other):
        return self.pay * other

    def __imul__(self, other):
        self.pay = self * other
        return self.pay

    def __rmul__(self, other):
        return self.pay * other

    def __pow__(self, power, modulo=None):
        return self.pay ** power

    def __ipow__(self, other):
        self.pay = self ** other
        return self.pay

    def __rpow__(self, other):
        return self.pay ** other

    def __getitem__(self, item):
        return self.marksStudent[item]

    def __lt__(self, other):
        if self.marksStudent < other.marksStudent:
            return f'Student {other.nameStudent} has better marks'
        else:
            return f'Student {self.nameStudent} has better marks'

    def __gt__(self, other):
        if self.marksStudent > other.marksStudent:
            return f'Student {self.nameStudent} has better marks'
        else:
            return f'Student {other.nameStudent} has better marks'

    def __le__(self, other):
        if self.marksStudent <= other.marksStudent:
            return f'Student {other.nameStudent} has better marks or equal'
        else:
            return f'Student {self.nameStudent} has better marks or equal'

    def __ge__(self, other):
        if self.marksStudent >= other.marksStudent:
            return f'Student {self.nameStudent} has better marks or equal'
        else:
            return f'Student {other.nameStudent} has better marks or equal'

    def __eq__(self, other):
        if self.marksStudent == other.marksStudent:
            return f'Students have equal marks'
        else:
            return f'Students donot have equal marks'

 #   def __delitem__(self, key):
  #      print(f'Subject {self.marksStudent[key]} deleted')

  #  def __del__(self):
  #      print(f'Student {self.nameStudent} deleted')

    def __len__(self):
        return len(self.subject)

    def __call__(self, a, b):
        return (self.marksStudent + a + b)/3

    def __contains__(self, item):
        if item in self.subject:
            return True

        return False

    def display(self):
        print(f'Student: {self.nameStudent}'
              f'Payment: {self.pay}'
              f'Marks: {self.marksStudent}'
              f'Subjects: {self.subject}')

    def display_using_generator(self):
        pass

    #enumerate

def main():
    s1 = Student('Peter', 2000, 3, 'Physics')
    s2 = Student('Mary', 1000, 5, 'Math')

    print(s1)
    print(s1 + 1000)
    print(s2 - 1000)
    print(s1 * 3)
    print(s2 ** 2)
    print(s1 > s2)
    print(s1 == s2)
    print(s1 <= s2)
    print(len(s1))
    marks = s1(4, 3)
    print(marks)
    print(s1)
    name = 'Math'
    print(name in s1)
    print(name in s2)






if __name__ == '__main__':
    main()





