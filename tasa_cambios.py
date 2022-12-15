import requests
from config_template import apiKey

moneda_cripto = input("ingrese una criptomoneda conocida:").upper()

while moneda_cripto != "" and moneda_cripto.isalpha():

    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apiKey}')




    #print(r.status_code)#codigo 200 correcto que otro seria incorrecto
    #print(r.text)

    #ej 1, como capturamos res correcto
    resultado = r.json()#guardamos el jason en resulytado(dicionario en python)
    if r.status_code == 200:
    #ej 3 cono formateamos el valor rate €
        print("{:,.2f}€".format(resultado["rate"]) )
    #ej 2, como capturamos errores    
    else:
        print(resultado["error"])

    #ej 4 como controlo input vacio, que no realze consultasi esta vacio
    moneda_cripto = input("ingrese una criptomoneda conocida:").upper()







