import requests
import pandas as pd

url = "https://www.blibli.com/backend/search/merchant/BRO-35372"

res = []
for x in range(1, 2):
    querystring = {"promoTab": "false", "excludeProductList": "false", "page": f"{x}",
                   "start": "40", "intent": "false", "multiCategory": "true", "showFacet": "false"}

    payload = ""
    headers = {"cookie": "Blibli-User-Id=e8c56234-95bf-43fb-b17c-29ddccd5ed5f; Blibli-Is-Member=false; Blibli-Is-Remember=false; Blibli-Session-Id=7af112f7-8bf5-4e97-978b-90866b8fe05f; Blibli-Signature=165eec035cf51f9b1ad2c8e2df21d70ee010ce5d; _abck=B91060AEE0E16C39B11BA917A2794BD1~-1~YAAQlegyF0OY9FeEAQAAwhmRawj%2B%2BCnw3HgrEa6%2FZ%2FXs%2Bl5CMKeRVnB0A65TW5UfsaBRNFEaEtI7PLSkks78DI62YKMiTW7P%2BQg0%2BATUXAgfLHVWPJk6ZOHKOz01f5sXFyNeKNG56DI7ZTxPbqmSq%2B8mK%2BPKSgL6vIouztqrhoZj5Yhn1151UwOFBB2u%2FniryHtMnrPLAckwmpKPurNzMOhmNP6DkEiLTs4v91lgp%2FEl5ENkdLH45QUPYMAxr9R0w8QPbR9uxnfq5ikU6uELmmpygF2IJZGI2eWaOKUs6iY6MY64Kki4SruOryi60Wmf%2Btfx7Ybkpo%2FLX97bCou4Ss4azsRvA7PH0%2FgtAeLLuTgcPTFFwpo9c2M%3D~-1~-1~-1; ak_bmsc=E24F35D827B08D6EA6666F677C48E1EA~000000000000000000000000000000~YAAQlegyF0SY9FeEAQAAwhmRaxGtHOJ3bnLiTkG57esMgUdOIcHwxHWzMzOji0WjmqHhZ8qA0FvSYhcKVjLLtor8Lr%2B2ry%2B8uNkjBvvJfp0sJizgZgYsQdPsNHIcgvgYnOQGGF1aMP3qrpuM1MgB9DSnEQTFbEeAlhMMhX%2BfCq4jaMOhyPJ3WJMQO0RdIHS9Zen%2Bdz0UU%2FmNktaYHuuGJ7loF5rGgjmi1yMHWp04O8kGXKhMv%2BWNbkjzM0hpTupFyAeTXKniOJzOj%2BaJL1EQfgbl1f1wpKkeb1mOk7hI5ZeHnE2MvcIP2UTZqeU4wHBQl84vjCiXOUWvsq%2BgUWecvjBxDqXvuz1Y%2B5mPHjb%2FiKpZMPOdXGy17ODl4iCqroS%2F8afuAHX0hB5GObU%3D; bm_sz=57C642FDB28A742E34CD40653EEB9F18~YAAQlegyF0WY9FeEAQAAwhmRaxG%2F597hK%2BQj6Qfxhvf1lt%2ByiDT%2FZiQKiD3fffW%2BALTJH9tDtmoEfvPR5zvq5pLdGLkFVxwGd6gTdXCUVE4YBaesM0382QZ3PpRXu%2FXpF0KjPX3djd%2F5QTlJ1zkxw1byhjM13WPZHRQJVKXfSuzi%2F8NWwCZP8%2BFUlwLHs0k9IYbYTBCB83Yxhx2tgRyvmnbepepvWdiRmPYqrM%2F48NJhEN9uNAbciRy%2FQL0wY%2B3ZCauEKPalGgL8tmG%2BC7n1rI%2Fh1rCP2Qw%2Bh60KuVq8AYlDtdg%3D~3556673~4408629; bm_sv=933C1DF5F4E3E01D5C89FB86E7D75AA6~YAAQlegyF5Ij9VeEAQAA44CbaxEtJCP7vnLZBWE9b972smKuyFSLS9vsUwBMowUt1whWWb2moi1E4aCCNZoyclEnAgIbdSvx9JHbIo8toSqvMTNOPp4RwCcXPirCEwelpBOyYHFSrSSAUbBu7tJyUyahpyo128BI7LIUhMwS%2F3EMNT7HuDNs6S97eq%2FfgoNsFMNytIZIiRjokMex1SVklq9f9L%2FNiRqR35V5BU8wKcGKkJuv6XIMP1lybvuGo4jz~1"}

    response = requests.request(
        "GET", url, data=payload, headers=headers, params=querystring)

    data = response.json()
    for p in data["data"]["products"][0]["id"]:
        res.append(p)

df = pd.json_normalize(res)
print(df)
# df.to_csv('blibli list product scraping.csv')
