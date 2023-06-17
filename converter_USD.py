import requests

def convert_currency(amount, base_currency, target_currency):
    api_key = "YOUR_API_KEY"  # Получите API-ключ от сервиса обменных курсов
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        conversion_rate = data["rates"][target_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    except requests.exceptions.RequestException as e:
        print("Error connecting to the API:", e)
        return None

amount = float(input("Введите сумму для конвертации: "))
base_currency = input("Введите базовую валюту: ")
target_currency = input("Введите целевую валюту: ")

converted_amount = convert_currency(amount, base_currency, target_currency)

if converted_amount:
    print(amount, base_currency, "равно", converted_amount, target_currency)
