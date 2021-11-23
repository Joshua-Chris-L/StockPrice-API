import requests
import twilio

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key


## STEP 1: Use https://www.alphavantage.co/documentation/#daily

parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "AGLG87XL4V21DFGM"
}
r = requests.get(STOCK_ENDPOINT, params=parameter)
data = r.json()

# print(data["Time Series (Daily)"]["2021-11-22"]["4. close"])
dataa = [value for (key, value) in data.items()]
data_1 = dataa[1]

# print(data_1)
data_2 = [value for (key, value) in data_1.items()]
yesterday_day = data_2[0]["4. close"]
before_yesterday_price = data_2[1]["4. close"]
diffrence = abs(float(yesterday_day) - float(before_yesterday_price))
percentage_diff = (diffrence / float(before_yesterday_price)) * 100

if percentage_diff > 1:
    End_point = "https://newsapi.org/v2/everything"

    parameter1 = {
        "q": COMPANY_NAME,
        "from": "2021-11-23",
        "sortBy": "popularity",
        "apiKey": "8019035b090642ce9020cbd8945f6e21",
    }
    response = requests.get(End_point, params=parameter1)
    dataa = response.json()
    news_data = dataa["articles"][:2]

    from twilio.rest import Client

    client = Client("ACbe991ae00d5488c12f4b51c0d9ba8f88", "f2ca27d1818b149d651f64c89cad473e")

    message = client.messages \
        .create(
        body=f"My lover, My lover. I love you so much.",
        from_='+18506695629',
        to='+4917674962986'
    )
    print(message.sid)

