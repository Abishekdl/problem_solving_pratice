class employee:
    def __init__(self,id,name,hours):
        self.id = id
        self.name = name
        self.hours = hours

    def work(self):
        print(f"Employee {self.name} working hours {self.hours}")

    def display(self):
        print("Employee Class")
        print(f"Employee id:{self.id} & Employee name:{self.name}")

class manager(employee):
    def __init__(self,id,name,hours,team_num,meetings):
        super().__init__(self,id,name)
        self.team_num = team_num
        self.meetings = meetings

    def meetings(self):
        print(f"Meeting number :{self.meetings} conducted by manager{self.name}")




    def display(self):
        super().display()
        print("Manager Class")
        print(f"Manager id: {self.id} Manager name:{self.name} \n"
        f"His team size:{self.team_num} meetings duration :{self.meetings}")


m = manager(1,"Abishek",4,100,5)
e = employee(2,"vp",8)

