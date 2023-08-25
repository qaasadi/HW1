class School:
    def __init__(self,name,gender,minAge,maxAge):
        self.name=name
        self.gender=gender
        self.minAge=minAge
        self.maxAge=maxAge

class Student:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def SelectSchool(self,schoolList):
        OK=0
        for obj in schoolList:
            if self.gender==obj.gender and self.age >= obj.minAge and self.age <= obj.maxAge:
                print(f"{self.name}:{obj.name} School")
                OK=1
        if OK !=1 :
                print(f"Sorry, we can't find a suitable school for {self.name} in this city!")



#School Data
schoolList=[]
schoolList.append(School("TALASH",'male',7,12))
schoolList.append(School("ENGHELAB",'male',7,12))
schoolList.append(School('MAREFAT',"male",13,15))
schoolList.append(School('AYANDEH',"male",16,18))
schoolList.append(School('KOSAR',"female",7,12))
schoolList.append(School('NIKAN',"female",13,15))


#Student Data
studentList=[]
studentList.append(Student("Ali","male",6))
studentList.append(Student("Amir","male",8))
studentList.append(Student("Masoud","male",12))
studentList.append(Student("Arman","male",11))
studentList.append(Student("Mehrdad","male",7))
studentList.append(Student("Omid","male",18))
studentList.append(Student("Sajjad","male",18))
studentList.append(Student("Ehsan","male",18))
studentList.append(Student("Reza","male",18))
studentList.append(Student("Kia","male",18))
studentList.append(Student("Setareh","female",8))
studentList.append(Student("Fatemeh","female",6))
studentList.append(Student("Negar","female",10))
studentList.append(Student("Nasrin","female",11))
studentList.append(Student("Kiana","female",18))
studentList.append(Student("Samaneh","female",8))
studentList.append(Student("Nafiseh","female",15))
studentList.append(Student("Narges","female",10))
studentList.append(Student("Arezoo","female",11))
studentList.append(Student("Reyhaneh","female",18))

print('------------------------------------------------------------------')
for obj in studentList:
    obj.SelectSchool(schoolList)
print('------------------------------------------------------------------')





     
    