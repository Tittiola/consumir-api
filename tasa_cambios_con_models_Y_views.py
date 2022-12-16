from criptoexchange.models import AllCoinApiIO,Exchange,ModelError
from criptoexchange.views import Views
from config import apiKey


allcoint = AllCoinApiIO()
allcoint.getCoins(apiKey)

viewsTools = Views()

viewsTools.viewCointsList(allcoint)

crypto = viewsTools.insertCoint()

while crypto != "" and crypto.isalpha():
    if crypto in allcoint.criptos:
        exchange = Exchange(crypto)
        try:
            #si todo bien esto se ejecuta
            exchange.updateExchange(apiKey)
            viewsTools.getRateExchange(exchange)

        except ModelError as error:# si falla imprime esto de aqui
            viewsTools.getError(error)   

       

    crypto = viewsTools.insertCoint()