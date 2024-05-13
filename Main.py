import Question,Generator,Exitq
def Main():
    if Question.question(True,"Möchten sie eine bestimmte anzahl an Primzahlen wissen?") == True: 
        number = input("Wie viele Primzahlen wollen sie wissen?\n")
        print(Generator.primarynumberscontroller(True,number))
        Exitq.exitq(True)
        Main()
    if Question.question(True,"Möchten sie alle Primzahlen in einem bestimmten bereich wissen?") == True: 
        number = input("Biss zu welcher zahl soll der Bereich gehen?\n")
        print(Generator.primarynumberscontroller(False,number))
        Exitq.exitq(True)
        Main()
    if Question.question(True,"Möchten sie wissen ob eine bestimmte zahl eine Primzahl ist?") == True:
        number = input("Fur welche zahl wollen sie das wissen?\n")
        print("Es ist eine Primzahl") if Generator.individualprimarynumber(number) == True else print("Es ist keine Primzahl")
        Exitq.exitq(True)
        Main()
    Exitq.exitq(False)
Main()