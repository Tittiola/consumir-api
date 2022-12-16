import requests
from config import apiKey

r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={apiKey}')
if r.status_code != 200:
    raise Exception("Error en consulta de assets:{}".format(r.status_code) )

lista_general = r.json()
lista_criptos = []

for item in lista_general:
    if item["type_is_crypto"] == 1:
        lista_criptos.append(item["asset_id"])



print("moneda digital: ",len(lista_criptos))
print("moneda no digital: ",(len(lista_general) - len(lista_criptos)))

#https://rest.coinapi.io/v1/assets/?apikey=24E07BC2-CA11-4FD2-9F14-889CEE3B8DBF

moneda_cripto = input("ingrese una criptomoneda conocida:").upper()

while moneda_cripto != "" and moneda_cripto.isalpha():
    if moneda_cripto in lista_criptos:
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apiKey}')

    #print(r.status_code)#codigo 200 correcto que otro seria incorrecto
    #print(r.text)
    # #ej 1, como capturamos res correcto
        resultado = r.json()#guardamos el jason en resulytado(dicionario en python)
        if r.status_code == 200:
    #ej 3 cono formateamos el valor rate €
            print("{:,.2f}€".format(resultado["rate"]) )
    #ej 2, como capturamos errores    
        else:
            print(resultado["error"])

    #ej 4 como controlo input vacio, que no realze consultasi esta vacio
    moneda_cripto = input("ingrese una criptomoneda conocida:").upper()







