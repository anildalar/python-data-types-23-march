from string import Template

# range(start(O), stop(C), step(0))


students = ["Nandini","Sofiya","Avadhi"] #list


print(students)

for student in students:
    #print(f"Hello {student}") # String Interpolation 1  f-string technique
    #print("Hello %s"%(student )) # String Interpolation 2 % formating tech
    #print("Hello {}".format(student)) # String Interpolation 3 str.format()
    # create the object from the class
    name = student
    new = Template('Hello $name')
    print(new.substitute(name= name))

    #print("Hello {}".format(student)) # String Interpolation 3 str.format()

#for x in range(4,6):
   # print(x);