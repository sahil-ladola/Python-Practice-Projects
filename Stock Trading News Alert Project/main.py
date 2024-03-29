import requests
STOCK_NAME = "ROLEXRINGS.BSE"
COMPANY_NAME = "Rolex Rings Limited"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ["STOCK_API_KEY"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"] # get daily data
# get yesterday's stock closing  price
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get the day before yesterday's stock closing price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# difference 
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#difference in percentage
diff_percentage = round((difference / float(yesterday_closing_price)) * 100)

# difference in percentage greater than 2 percentage
if abs(diff_percentage) > 2:
    news_params = {
        "apikey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }
    # get articles related to stock using news API 
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # get first 3 articles related to stock using python slice operator
    three_articles = articles[:3]

    formatted_article = [f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    # use twilio API to send SMS
    print(formatted_article)

