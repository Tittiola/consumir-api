from criptoexchange.models import AllCoinApiIO,Exchange,ModelError
from config_template import apiKey

#creamos objeto de AllCoinApiIO
allcoint = AllCoinApiIO()
#ejecutar el metodo getCoins que consulta y carga lista de coins
allcoint.getCoins(apiKey)

print("La cantidad de criptos son {} ,\
       y la de no criptos son {}"\
      .format(len(allcoint.criptos),len(allcoint.no_criptos)))

crypto = input("Ingrese moneda digital conocida: ").upper()

while crypto != "" and crypto.isalpha():
    if crypto in allcoint.criptos:
        exchange = Exchange(crypto)
        try:
            #si todo bien esto se ejecuta
            exchange.updateExchange(apiKey)
            print( "{:,.2f}€".format(exchange.rate).replace(",","@").replace(".",",").replace("@",".") )

        except ModelError as error:# si falla imprime esto de aqui
            print(error)    

       

    crypto = input("Ingrese moneda digital conocida: ").upper()