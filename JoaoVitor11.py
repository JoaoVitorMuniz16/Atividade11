distancia = int(input("insira a distãncia de viagem"))
if distancia < int("200"):
    print("valor da passagem:",float(distancia*0.50))
else:
    print("o valor da passagem:",float(distancia*0.45))