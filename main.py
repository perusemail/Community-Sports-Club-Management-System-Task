import random


class Person():
    def __init__(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number
    
    def set_details(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number
        
    def get_details(self):
        print("Name:",self.name,"\nAge:",self.age,"\nContact number",self.contact_number)

class Member(Person):
    def __init__(self,name,age,contact_number,membership_id,sport,performance_scores):
        super().__init__(name,age,contact_number)
        self.id = id
        self.sport = sport
        self.membership_id = membership_id
        self.performance_scores = performance_scores
        self.average_score = 0
    
    def set_member_details(self, membership_id, sport):
        self.membership_id = id
        self.sport = sport
    
    def add_performance_score(self, score):
        self.performance_scores.append(score)
    def calculate_average_score(self):
        if len(self.performance_scores)>0:
            x = 0
            t = 0
            for counter in self.performance_scores:
                x += counter
                t += 1
            self.average_score = x/t
        else:
            self.average_score = 0

    def get_member_summary(self):
        print("Name:",self.name,"\nAge:",self.age,"\nContact number:",self.contact_number,"\nMembership id:",self.membership_id,"\nSport:",self.sport,"\nPerformance scores:",self.performance_scores,"\nAverage_score:",self.average_score)

class Coach(Person):
    def __init__(self, name, age, contact_number,coach_id,specialisation,salary,):
        super().__init__(name,age,contact_number)
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []

    def set_coach_details(self, coach_id, specialisation, salary):
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary

    def assign_mentee(self,member):
        self.mentees.append(member)
        print("Coach",self.name,"is now mentoring",member,"in",member.sport)
    
    def get_mentees(self):
        return self.mentees
    
    def increase_salary(self, percentage):
        self.salary = self.salary * (1+(percentage/100))
        print("New salary:",self.salary)


    class Staff(Person):
        def __init__(self, name, age, contact_number,staff_id,position,years_of_service):
            super().__init__(name.age.contact_number)
            self.staff_id = staff_id
            self.position = position
            self.years_of_service = years_of_service
            

member1 = Member("John",10,"1234567890","m1234","Football",[1,2,3,4,5,6])
member1.calculate_average_score()
member1.get_member_summary()