import requests


class ModelError(Exception):
    pass

class AllCoinApiIO:
    def __init__(self):
        self.criptos=[]
        self.no_criptos=[]
    
    def getCoins(self,apiKey):
        r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={apiKey}')
        if r.status_code != 200:
            raise ModelError( "Error en consulta de assets:{}".format(r.status_code) )
    
        lista_general= r.json()
        for item in lista_general:
            if item["type_is_crypto"] == 1:
                self.criptos.append(item['asset_id'])
            else:
                self.no_criptos.append( item['asset_id'])


class Exchange:
    def __init__(self,cripto):
        self.cripto = cripto
        self.rate = None
        self.time = None
        self.r = None
        self.resultado = None

    def updateExchange(self,apiKey):
        self.r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{self.cripto}/EUR?apikey={apiKey}')
        self.resultado = self.r.json()
        if self.r.status_code == 200:
            self.rate = self.resultado['rate']#si va bien
            self.time = self.resultado['time']
        else:    
            raise ModelError( f"status: {self.r.status_code} error: {self.resultado['error']} ")

class Exchange2:
    def __init__(self,moneda):
        self.moneda = moneda
        self.rate = None
        self.time = None
        self.r = None
        self.resultado = None

    def updateExchange(self,apiKey):
        self.r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{self.moneda}/BTC?apikey={apiKey}')
        self.resultado = self.r.json()
        if self.r.status_code == 200:
            self.rate = self.resultado['rate']#si va bien
            self.time = self.resultado['time']
        else:    
            raise ModelError( f"status: {self.r.status_code} error: {self.resultado['error']} ")