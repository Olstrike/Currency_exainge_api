
import requests

url = "https://currency-exchange.p.rapidapi.com/exchange"

querystring = {"from":"SEK","to":"DKK","q":"1.0"}

headers = {
	"X-RapidAPI-Key": "201a289868msh0e86c97a5408242p168a1bjsn1d77b054a80b",
	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)