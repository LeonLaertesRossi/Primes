import Question
def exitq(bias = False):
    if Question.question(bias,"Mochten sie das Programm schließen?") == False:
        return
    else:
        exit()