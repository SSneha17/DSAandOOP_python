from abc import abstractmethod


class Student:
    def __init__(self, name, marks):
        print("Invoked during object creation")
        self.name = name
        self.marks = marks

    def getAverageScore(self):
        sum = 0
        l = len(self.marks)
        for x in self.marks:
            sum+=x;
        return round(sum/l, 2);
    def getDegree(self):
        return "High School"
       


''' Class level methods are Static methods. They use @static decorator'''
@staticmethod
def Greet():
    print("Hello from Student Class level Static method")


#Inheritance
class Masters(Student):
    def getDegree(self):
        return "Masters Degree"
        
    def getAverageScore(self):
        return super().getAverageScore()
    

#Run time polymorphism
def getHighestDegree(person):
    person.getDegree()


#abstraction
class Vehicle():
    def type(self):
        pass
class Ford(Vehicle):
    def type(self):
        print("Sedan")

class GMC(Vehicle):
    def type(self):
        print("SUV")

#Interface
class Specifics():
    @abstractmethod
    def getMileage(self):
        ...

class VehiclaSpecifics(Vehicle, Specifics):
    def getMileage(self):
        print("60 miles per hour")





if __name__ == "__main__":
    
    s1= Student('Jia', [15,25,25])
    avg = s1.getAverageScore()
    print (avg)
    #print (s1.getDegree())

    Greet()

    m1 = Masters('Sam',[25,30,26])
    print(m1.getAverageScore())
    #print(m1.getDegree())

    print(f"Sam's degress is:\t", (m1.getDegree()))


    ford = Ford()
    ford.type()

    gmc = GMC()
    gmc.type()

    audi = VehiclaSpecifics()
    audi.getMileage()


    a = [1, 2, 3] 
    a.append([4, 5]) 
    print(len(a)) 
    print(a)
    b=a
    a+=[6,8]
    print(b)
    

    