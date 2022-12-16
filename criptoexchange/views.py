#clases o funciones

#la vista se encarga de interactuar 
#con el usuario
class Views():
    def __init__(self):
        pass

    def insertCoint(self):
        crypto = input("Ingrese moneda conocida: ").upper()
        return crypto

    def viewCointsList(self,allcoint):
        print("La cantidad de criptos son {} ,y la de no criptos son {}".format(len(allcoint.criptos),len(allcoint.no_criptos)))
 
    def getRateExchange(self,exchange):
        print( "{:,.8f}€".format(exchange.rate).replace(",","@").replace(".",",").replace("@",".") )

    def getError(self,error):
        print(error)     