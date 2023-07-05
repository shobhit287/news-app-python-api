import requests
choice=input("What You Want To See:")
response = requests.get(f"https://newsapi.org/v2/everything?q={choice}&from=2023-06-05&sortBy=publishedAt&apiKey=a3b03c5cbfbe480e866851901c86c644")
data = response.json()

if response.status_code == 200 and data["status"] == "ok":
    articles = data["articles"]
    for article in articles:
        print("Title:", article["title"])
        print("Source:", article["source"]["name"])
        print("Published At:", article["publishedAt"])
        print("Description:", article["description"])
        print("-" * 50)
else:
    print("Error occurred while fetching news:", data["message"])
