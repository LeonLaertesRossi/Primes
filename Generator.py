def Individualprimarynumber(number = 1):
    number = int(number)
    iterator = 2
    while iterator < number:
        if number % iterator == 0:
            return False
        iterator = iterator + 1
    return True
def primarynumberscontroller(mode = True,number = 1):
    number = int(number)
    iterator = 3
    primes = [2]
    if mode == True:
        while len(primes) < number:
            primes,iterator = primarynumbers(primes,iterator)
    if mode == False:
        while iterator < number:
            primes,iterator = primarynumbers(primes,iterator)
    return primes
def primarynumbers(primes = [2],iterator = 3):
    test = True
    for x in primes:
        if iterator % x == 0:
            test = False
    if test == True:
        primes.append(iterator)        
    iterator = iterator + 1
    return primes,iterator