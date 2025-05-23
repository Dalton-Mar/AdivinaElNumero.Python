import random 

def adivina_el_numero():
    print("bienvenido al juego 'adivina el numero'")
    print("Estoy pensando un numero entre 1 y 100. tienes 10 intentos para adivinarlo")

    numero_secreto = random.randint(1,100)
    intentos_restantes = 10

    while intentos_restantes > 0:
        try:
            adivinanza = int(input(f"\n ingresa tu numero (te quedan {intentos_restantes} intentos):"))

            if adivinanza < 1 or adivinanza > 100:
                print("por favor ingresa un numero entre 1 y 100")

                continue

            if adivinanza == numero_secreto:
                print("FELICIDADES! adivinaste el numero")
                break
            elif adivinanza < numero_secreto:
                print("el numero secreto es mayor")
            else:
                print("el numero es menor")

            intentos_restantes -=1

        except ValueError:
         print("por favor ingresa un numero valido")

    if intentos_restantes == 0:
        print(f"\n Te has quedado sin intentos.el numero secreto era {numero_secreto}. mejor suerte la proxima vez!")

adivina_el_numero()



