def question(bias = True,question = ""):
    if bias == True:
        end = "Y/n"
    if bias == False:
        end = "y/N"
    awnser = bias
    temp = input(question+" "+end+"\n")
    if temp == "N" or temp == "n" or temp == "No" or temp == "no" and bias != False:
        awnser = False
    if temp == "Y" or temp == "y" or temp == "Yes" or temp == "yes" and bias != True:
        awnser = True
    return awnser