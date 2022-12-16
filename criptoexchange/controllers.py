from criptoexchange.models import AllCoinApiIO,Exchange,ModelError,Exchange2
from criptoexchange.views import Views
from config import apiKey

class CriptoExchangeController:
 
    def executeProgram(self):
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

    def executeProgram2(self):
        allcoint = AllCoinApiIO()
        allcoint.getCoins(apiKey)
        viewsTools = Views()
        viewsTools.viewCointsList(allcoint)
        moneda = viewsTools.insertCoint()
        while moneda != "" and moneda.isalpha():
            if moneda in allcoint.no_criptos:
                exchange = Exchange2(moneda)
                try:
                    #si todo bien esto se ejecuta
                    exchange.updateExchange(apiKey)
                    viewsTools.getRateExchange(exchange)
                except ModelError as error:# si falla imprime esto de aqui
                    viewsTools.getError(error)   

            moneda = viewsTools.insertCoint()   