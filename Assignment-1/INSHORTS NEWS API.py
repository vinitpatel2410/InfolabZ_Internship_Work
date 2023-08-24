import requests
#How many main keys are there in this API? Extract and print all keys.
url = "https://inshortsapi.vercel.app/news?category=all"
response = requests.get(url)
data = response.json()

main_keys = data.keys()
print("Main keys in the API:")
for key in main_keys:
    print(key)
#How many news are available in this API?
num_news = len(data['data'])
print("Number of news available in the API:", num_news)
#Print all news in the given format:
print("News in the given format:")
for index, news_item in enumerate(data['data'], 1):
    content = news_item['content']
    author = news_item['author']
    date = news_item['date']

    print(f"{index}. {content}, Author: {author}, DATE: {date}")
