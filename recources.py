import requests

url = "https://currency-exchange.p.rapidapi.com/listquotes"

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)