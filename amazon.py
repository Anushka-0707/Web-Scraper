import requests
from lxml import html
import pandas as pd
url = 'https://www.amazon.in/s?k=shirts'
cookies = {
    'session-id': '257-2926628-0722806',
    'ubid-acbin': '258-3648071-6937161',
    'urtk': '%7B%22at%22%3A%22Atna%7CEwICIAW9SwgybMxuXv_UCfS6MzXoeT08dkeSYwh7BKBdsIhpaRQYAxejYcPYbVGB-_gMtAS4ioOAyFrjrStalWTQI-xojMP-hiSdUYQ1hYmFAr_nQaZ8JzXljJ6CbvDeD7ms2fWx9nDz8ZPkkknrK36ryB1Hf-nKX8B6KzKh0iHWJzGhyhYW4ayvl_T4ryUMXkUPucTnIvm8qz0xxZLA6RcdyI3Kk5VzO2IWtt6r3Pf4kEFn02aUTFnyo1ci565HXnrc1Qh9lQ0yAayszFzJ_5tu5v_TXez5Dx7eTsJCKpPsMZuhu_bJvcGtCOEn5GrXkDrG3qNI1IARaFhdg1lv01wwBNeOtgNu6hGnf_TMfLPBzNwE1A%22%2C%22atTtl%22%3A1719662644079%2C%22rt%22%3A%22Atnr%7CEwICINzNB31oW9vtm2HiZh2D4tWVKjUF__zyMuZxV4W2QqOqo_5W4d2HHS-lNtbr7i73XyAFyhZ3_KwHk49u-oN2Ttiv7JBstIztEZA0wyCg7IsQu0Trl5CTNHlJFfo3_UHkTb_exYAZM3kSEAp5FxHcTRotHkbw4X-lzeC78U8RliocSl0SZngFIP9EVRa508vmm3zeKp2B1TJxiq15v4I7IYu05siW6_Ik4d9FkhbFvkiWNLTIvyISs7DgUfr5J_YlDU6rvQWQKjHEGB-r74puIw7bDN8k_VAyKcADFaRJ7shzxx2MNCqcnnN7td1K70GodUh4FZpck3H_ZIJWsBI6T7dN%22%7D',
    'sst-acbin': 'Sst1|PQH894PTCzoKywcELrFHPpcxB8VGzRx1syUDjtzJP2YBMTcePXHYlA_QsvzpKZHeVpsGMNZUWE6Sx4OVjAPcZoYTQeFEUrAuAaPb3qAdqugo1ennTqWTKlPCjDEM8TCduoAnRAOv0OE8zTBgnGJjOzDYyYSOvfBucyjx1vAF8ZhRI8g1QVx-8DPdi3kEQcUCdcTXIIcqI2SVTYfn2V-9AyizFm5wVe5BZ5f2gqfeRAu3gRNhgABf1qvZ-yZYdVAUyFNQ',
    'i18n-prefs': 'INR',
    'session-token': 'UjQAHMFofqH7Vs0uSxr4Lo7p7wF6bCst/bzmnqA4JNRQLUfmonIgSFKD6CO82SOilbZfqTw222q37pK+iZSTqXXFXixi5CqPV3ZCIbWsW20rsB4blSRDKucEIGJBvxcGPnh59MkKYIcVFSTWHYMXLNPAy2RkIOD50c04BxuP8MLgvNps98y4hLbitzrMMLfHIPrLbUnsHwbYL8Vo5aXKEPvOe+R7uXmmEQ/FVjHU9PhBWLjo0+GXQqEV8pxvyle0CWa/uQoYJVlO9gi4qzeJ5+1gy3/G5YOGTYwIFEjG1AldrCGrfuJR28hxK8GQRTodo8G2STSC9oYbO9pkRyz9Tx+O1dTsPdYt',
    'csm-hit': 'tb:F7MMQDEYVBGDEJETRM8R+s-SYWNGXV8EMD49GBGFPRN|1732248522512&t:1732248522512&adb:adblk_yes',
    'session-id-time': '2082758401l',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'session-id=257-2926628-0722806; ubid-acbin=258-3648071-6937161; urtk=%7B%22at%22%3A%22Atna%7CEwICIAW9SwgybMxuXv_UCfS6MzXoeT08dkeSYwh7BKBdsIhpaRQYAxejYcPYbVGB-_gMtAS4ioOAyFrjrStalWTQI-xojMP-hiSdUYQ1hYmFAr_nQaZ8JzXljJ6CbvDeD7ms2fWx9nDz8ZPkkknrK36ryB1Hf-nKX8B6KzKh0iHWJzGhyhYW4ayvl_T4ryUMXkUPucTnIvm8qz0xxZLA6RcdyI3Kk5VzO2IWtt6r3Pf4kEFn02aUTFnyo1ci565HXnrc1Qh9lQ0yAayszFzJ_5tu5v_TXez5Dx7eTsJCKpPsMZuhu_bJvcGtCOEn5GrXkDrG3qNI1IARaFhdg1lv01wwBNeOtgNu6hGnf_TMfLPBzNwE1A%22%2C%22atTtl%22%3A1719662644079%2C%22rt%22%3A%22Atnr%7CEwICINzNB31oW9vtm2HiZh2D4tWVKjUF__zyMuZxV4W2QqOqo_5W4d2HHS-lNtbr7i73XyAFyhZ3_KwHk49u-oN2Ttiv7JBstIztEZA0wyCg7IsQu0Trl5CTNHlJFfo3_UHkTb_exYAZM3kSEAp5FxHcTRotHkbw4X-lzeC78U8RliocSl0SZngFIP9EVRa508vmm3zeKp2B1TJxiq15v4I7IYu05siW6_Ik4d9FkhbFvkiWNLTIvyISs7DgUfr5J_YlDU6rvQWQKjHEGB-r74puIw7bDN8k_VAyKcADFaRJ7shzxx2MNCqcnnN7td1K70GodUh4FZpck3H_ZIJWsBI6T7dN%22%7D; sst-acbin=Sst1|PQH894PTCzoKywcELrFHPpcxB8VGzRx1syUDjtzJP2YBMTcePXHYlA_QsvzpKZHeVpsGMNZUWE6Sx4OVjAPcZoYTQeFEUrAuAaPb3qAdqugo1ennTqWTKlPCjDEM8TCduoAnRAOv0OE8zTBgnGJjOzDYyYSOvfBucyjx1vAF8ZhRI8g1QVx-8DPdi3kEQcUCdcTXIIcqI2SVTYfn2V-9AyizFm5wVe5BZ5f2gqfeRAu3gRNhgABf1qvZ-yZYdVAUyFNQ; i18n-prefs=INR; session-token=UjQAHMFofqH7Vs0uSxr4Lo7p7wF6bCst/bzmnqA4JNRQLUfmonIgSFKD6CO82SOilbZfqTw222q37pK+iZSTqXXFXixi5CqPV3ZCIbWsW20rsB4blSRDKucEIGJBvxcGPnh59MkKYIcVFSTWHYMXLNPAy2RkIOD50c04BxuP8MLgvNps98y4hLbitzrMMLfHIPrLbUnsHwbYL8Vo5aXKEPvOe+R7uXmmEQ/FVjHU9PhBWLjo0+GXQqEV8pxvyle0CWa/uQoYJVlO9gi4qzeJ5+1gy3/G5YOGTYwIFEjG1AldrCGrfuJR28hxK8GQRTodo8G2STSC9oYbO9pkRyz9Tx+O1dTsPdYt; csm-hit=tb:F7MMQDEYVBGDEJETRM8R+s-SYWNGXV8EMD49GBGFPRN|1732248522512&t:1732248522512&adb:adblk_yes; session-id-time=2082758401l',
    'priority': 'u=0, i',
    'referer': 'https://www.amazon.in/',
    'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}
data = {
    'title' : [],
    "price" : [],
    'brand': []
}
df = pd.DataFrame(data)
response = requests.get(url, cookies=cookies, headers=headers)
print(response)
tree = html.fromstring(response.content)

title = tree.xpath('//div[@class="a-section a-spacing-small puis-padding-left-micro puis-padding-right-micro"]//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()')
# print(len(title))
# print(title)
df['title'] = title
price = tree.xpath('//div[@class="a-section a-spacing-small puis-padding-left-micro puis-padding-right-micro"]//span[@class="a-price-whole"]/text()')
# print( len(price))
# print(price)

df['price'] = price
brand = tree.xpath('//div[@class="a-section a-spacing-small puis-padding-left-micro puis-padding-right-micro"]//span[@class="a-size-base-plus a-color-base"]/text()')
# print(len(brand))
# print(brand)
df['brand'] = brand

print(df)

