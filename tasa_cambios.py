import requests

r = requests.get('https://rest.coinapi.io/v1/exchangerate/ETH/EUR?apikey=24E07BC2-CA11-4FD2-9F14-889CEE3B8DBF')


print(r.status_code)
print(r.text)
