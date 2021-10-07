class Data:
    def __init__(self, userdata):
        self.userdata = Data.validdata(userdata)

    @classmethod
    def strinint(cls, userdata):
        return [int(i) for i in userdata.split('-')]

    @staticmethod
    def validdata(userdata):
        valdat = Data.strinint(userdata)
        if valdat[1] > 12:
            print("Месяц указан не верно")
            return None
        elif valdat[2] < 1000:
            print("Давненько это было!")
            return userdata



data1 = Data("1-22-2000")
print(data1.userdata)
data2 = Data("1-12-200")
print(data2.userdata)
