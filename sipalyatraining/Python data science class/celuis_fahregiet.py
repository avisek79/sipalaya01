#Program to convert celcius to farenheit
class Conversion:
    def __init__(self,farenheit_value):
        self.fah=int(farenheit_value)

    def formula(self):
        self.celcius=(self.fah-32)/1.8

        print(f"celcius to fahrenheit : {self.celcius:.2f}")

fahren=input("enter the value to convert \"fahrenhiet\" to \"celcius\" :")
obj=Conversion(fahren)
obj.formula()


        
        
