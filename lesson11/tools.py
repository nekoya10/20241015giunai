import random , csv

class BMI(): 
    def __init__(self,name:str,height:int,weight:int): 
        self.name = name
        self.height = height
        self.weight = weight

    def get_bmi(self)->float:
        return round(self.weight / (self.height/100) ** 2,ndigits=2)
    
    def get_status(self)->str:  
        bmi = self.get_bmi()
        if bmi >=35:
            status = "您的體重:重度肥胖"
        elif bmi >= 30:
            status = "您的體重:中度肥胖"
        elif bmi >= 27:
            status = "您的體重:輕度肥胖"
        elif bmi >= 24:
            status = "您的體重:過重"
        elif bmi >= 18.5:
            status = "您的體重:正常範圍"
        else:
            status = "您的體重:體重過輕"
        return status


def get_name(nums:int=2)->list[str]: 
    with open('names.txt',mode='r',encoding='utf-8') as file:
            names_str = file.read()
    names = names_str.split()
    names = random.choices(names,k=nums)
    return  names
     
def generate_bmi(names:list[str])->list[BMI]: 
    students:list[BMI] = []
    for name in names:
        height = random.randint(140,190)
        weight = random.randint(50,110)
        student_STATUS = BMI(name, height, weight)
        students.append(student_STATUS) 
    return students