# Exercise 1
import torch
import torch.nn as nn
from soft_max_and_sm_stable_class import Softmax, SoftmaxStable
from ward_class import Ward, Teacher, Student, Doctor
from stack_class import MyStack
from queue_class import MyQueue

# Question 1
data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
# print(output)


# Question 2
data = torch . Tensor([5, 2, 4])
my_softmax = Softmax()
output = my_softmax(data)
# print(output)


# Question 3
data = torch . Tensor([1, 2, 300000000])
my_softmax = Softmax()
output = my_softmax(data)
# print(output)


# Question 4
data = torch . Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
# print(output)


# Question 5
student1 = Student(name="studentZ2023", yob=2011, grade="6")
assert student1.yob == 2011
# student1.describe()


# Question 6
teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
assert teacher1.yob == 1991
# teacher1.describe()


# Question 7
doctor1 = Doctor(name="doctorZ2023", yob=1981, specialist="Endocrinologists")
assert doctor1.yob == 1981
# doctor1.describe()


# Question 8
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
# print(ward1.count_doctor())


# Question 9
stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
# print(stack1.is_full())


# Question 10
stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
# print(stack1.top())


# Question 11
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
# print(queue1.is_full())


# Question 12
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
# print(queue1.front())
