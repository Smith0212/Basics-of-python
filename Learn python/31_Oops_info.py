class programer :
    compny = "microsoft"

    def __init__(self, name, salary, post) :
        self.name = name
        self.salary = salary
        self.post = post

    def info(self):
        print(f"The name of the {self.compny} programer is {self.name} \nthe salary is {self.salary} and \nthe post is {self.post}\n ")

smith = programer("Smith","120k","linkedin")
saurav = programer("Saurav","100k","skype")

smith.info()
saurav.info()