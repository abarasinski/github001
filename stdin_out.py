import sys

#plik_error = open("errors.txt","w")
#sys.stderr = plik_error

while True:
    try:
        number = input("Podaj liczbe: \n")
    except EOFError: #np. Ctrl+d
        print("Koniec")
        break
    else:
        number = int(number)
        if number == 0:
            print("Nie ma dzielenia przez 0", file=sys.stderr)
        else:
            print("Liczba odwrotna do {:d} to  {:f}".format(number, 1.0/number))    


#plik_error.close()
