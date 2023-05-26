import requests as rt

api_key = '3682092f43e76976fd513d843d69ed23'

url = "http://api.mediastack.com/v1/news?"\
      "access_key=3682092f43e76976fd513d843d69ed23"\
      "&date=2023-05-26"\
      "&categories=science"

print(url)
request = rt.get(url)
content = request.json()
print(content)
print(content["data"])
print(len(content["data"]))

for article in content["data"]:
    print(f"{article['title']}:")
    print(article['description'])



