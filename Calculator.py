
class Calculator:
    def __init__(self):
        print("                               Python Calculator                                ")
        print("---------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------")
        print("   NB: Seperate each value with a blank space and don't include the '=' sign,\n avoid adding a blank space before your question, press enter to get the answer. ")
        print("---------------------------------------------------------------------------------")
        print()

        self.get_question()

    def get_question(self):
        self.question = input("Enter your question (Enter 'exit' to quit) : ")

        if self.question == "exit" or self.question == "Exit" or self.question == "EXIT":
            print()
            print("_________________________________________________________________________________")
            print("                                    GoodBye                                      ")
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

            return 0
        
        else:
            values = self.question.split(" ")

            if len(values) < 3:
                print("Invalid!!")
                print()
                print()

                self.get_question()

            else:
                self.calculate_answer(values)
            
    def calculate_answer(self,values):
        value_1 = int(values[0])
        value_2 = int(values[2])
        operator = values[1]

        try:
            if operator == "+":
                answer = self.add(value_1,value_2)

            elif operator == "-":
                answer = self.minus(value_1,value_2)

            elif operator == "*":
                answer = self.multiply(value_1,value_2)

            elif operator == "/":
                answer = self.divide(value_1,value_2)

            elif operator == "%":
                answer = self.modulus(value_1,value_2)

            print(f"{self.question} = {answer}")
        
        except:
            print("Error!!")
            print()
            print()

        self.get_question()
    
    def add(self,x,y):
        return x + y
    
    def minus(self,x,y):
        return x - y
    
    def multiply(self,x,y):
        return x * y
    
    def divide(self,x,y):
        return x / y

    def modulus(self,x,y):
        return x % y
    
App = Calculator()