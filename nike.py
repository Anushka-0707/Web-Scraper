import requests
from lxml import html
import pandas as pd

url = 'https://www.amazon.in/s?k=shirts'

cookies = {
    'session-id': '257-2926628-0722806',
    'ubid-acbin': '258-3648071-6937161',
    'urtk': '%7B%22at%22%3A%22Atna%7CEwICIAW9SwgybMxuXv_UCfS6MzXoeT08dkeSYwh7BKBdsIhpaRQYAxejYcPYbVGB-_gMtAS4ioOAyFrjrStalWTQI-xojMP-hiSdUYQ1hYmFAr_nQaZ8JzXljJ6CbvDeD7ms2fWx9nDz8ZPkkknrK36ryB1Hf-nKX8B6KzKh0iHWJzGhyhYW4ayvl_T4ryUMXkUPucTnIvm8qz0xxZLA6RcdyI3Kk5VzO2IWtt6r3Pf4kEFn02aUTFnyo1ci565HXnrc1Qh9lQ0yAayszFzJ_5tu5v_TXez5Dx7eTsJCKpPsMZuhu_bJvcGtCOEn5GrXkDrG3qNI1IARaFhdg1lv01wwBNeOtgNu6hGnf_TMfLPBzNwE1A%22%2C%22atTtl%22%3A1719662644079%2C%22rt%22%3A%22Atnr%7CEwICINzNB31oW9vtm2HiZh2D4tWVKjUF__zyMuZxV4W2QqOqo_5W4d2HHS-lNtbr7i73XyAFyhZ3_KwHk49u-oN2Ttiv7JBstIztEZA0wyCg7IsQu0Trl5CTNHlJFfo3_UHkTb_exYAZM3kSEAp5FxHcTRotHkbw4X-lzeC78U8RliocSl0SZngFIP9EVRa508vmm3zeKp2B1TJxiq15v4I7IYu05siW6_Ik4d9FkhbFvkiWNLTIvyISs7DgUfr5J_YlDU6rvQWQKjHEGB-r74puIw7bDN8k_VAyKcADFaRJ7shzxx2MNCqcnnN7td1K70GodUh4FZpck3H_ZIJWsBI6T7dN%22%7D',
    'i18n-prefs': 'INR',
    'lc-acbin': 'en_IN',
    'x-acbin': '"w7r?m5QIyC0dvCjMkoqWZtGUsI2R3utA5dMHD66ATPjgc0SIl18P8GVcOMaMZ9M6"',
    'at-acbin': 'Atza|IwEBIFqa8KJQyuhEYvD8BI82UmjMj34I4ySn4wc-Dtex0R5esBBQzgBc_mxpYIwyd0SOM1WhmxND6qpQ1Nat8xUE0Kd1xGlVMmRGKrZ1PUNsgI1KK0_pKrA9KczcaPsIxURbkMTTKBYN9lrqeez4NYyHzK5NewnV1tovfOKEYG5CnUMnjNxm0fttnkks-4u_4JnV3nHFDh1lpQUwTMP03dzmf6AJuVKr8QEB4QCvZZI2Pu17nw',
    'sess-at-acbin': '"i6RlZ7BS2emhak8jOJWcdTumVKOnuqSWJu8XFV0nMAQ="',
    'sst-acbin': 'Sst1|PQHdN_dQG1mP2Qq7rsTPZ2iACQwaWJUqtJ5-N7UXc0XVL4RLACGrv_UuZ9FfB56QfjwgefzDPSijZDjYpzgGtJhpGFkn9T5DmnitlaiGmQJJqbt7jbx9Epjl74VPFo2AGzyHr62ybAaEeAHVmtIy_Mz3wsfo6uvgpeOiqUfjfPPmWRVeWTX5eIGD10Gir8b9zgwT4EggtvvQuJItxhWf9kowdetrz6OMpkF97do9uMMznYXEJVvouS6FnIJmRsqwE8gQnE2o6apTT6eUXgQUfSV6GdUIBO-ptIUa9z11xJl0-kI',
    'session-token': 'v3dW2XkyrIXUO31ZxROKhsBFf7Rd4BKQYWCW1D1Qmf0FfLNDXaFHuYAGibOPvF+WB6uhXuOmlE9NZJUrOevkYZSw4sMTU+GDkQScCb1i2rNrI9HmY3C6LxiBUNWnMKc3xwSElX8X2Ym0POPnZFvij3SSK6StpBViyUTfQEeNgk6To/RoaDqqNrrksXoDPpd41aWeOQvgW4kKpNKCtVd9EkTkOAJaS9A17yNCBgiiZOQB08/nHcSnFqYE0pc85rKrGL0228cfX8kIXLmSXvc+nVLxMvDvAtEzwaMlO/mxMCpmls8xwh+dtBwt78KhrnVDNBDIypHCyAYuX/0QlDHO0fv8wuErR11aB6yfYeJP1JssNmQ6qQexbyYAF6pVVcM1',
    'csm-hit': 'tb:PXNJXR89PDDRWKHSWXZ7+s-N4KFZ54Q36QGXPHXS5V5|1731918801112&t:1731918801112&adb:adblk_yes',
    'session-id-time': '2082758401l',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'session-id=257-2926628-0722806; ubid-acbin=258-3648071-6937161; urtk=%7B%22at%22%3A%22Atna%7CEwICIAW9SwgybMxuXv_UCfS6MzXoeT08dkeSYwh7BKBdsIhpaRQYAxejYcPYbVGB-_gMtAS4ioOAyFrjrStalWTQI-xojMP-hiSdUYQ1hYmFAr_nQaZ8JzXljJ6CbvDeD7ms2fWx9nDz8ZPkkknrK36ryB1Hf-nKX8B6KzKh0iHWJzGhyhYW4ayvl_T4ryUMXkUPucTnIvm8qz0xxZLA6RcdyI3Kk5VzO2IWtt6r3Pf4kEFn02aUTFnyo1ci565HXnrc1Qh9lQ0yAayszFzJ_5tu5v_TXez5Dx7eTsJCKpPsMZuhu_bJvcGtCOEn5GrXkDrG3qNI1IARaFhdg1lv01wwBNeOtgNu6hGnf_TMfLPBzNwE1A%22%2C%22atTtl%22%3A1719662644079%2C%22rt%22%3A%22Atnr%7CEwICINzNB31oW9vtm2HiZh2D4tWVKjUF__zyMuZxV4W2QqOqo_5W4d2HHS-lNtbr7i73XyAFyhZ3_KwHk49u-oN2Ttiv7JBstIztEZA0wyCg7IsQu0Trl5CTNHlJFfo3_UHkTb_exYAZM3kSEAp5FxHcTRotHkbw4X-lzeC78U8RliocSl0SZngFIP9EVRa508vmm3zeKp2B1TJxiq15v4I7IYu05siW6_Ik4d9FkhbFvkiWNLTIvyISs7DgUfr5J_YlDU6rvQWQKjHEGB-r74puIw7bDN8k_VAyKcADFaRJ7shzxx2MNCqcnnN7td1K70GodUh4FZpck3H_ZIJWsBI6T7dN%22%7D; i18n-prefs=INR; lc-acbin=en_IN; x-acbin="w7r?m5QIyC0dvCjMkoqWZtGUsI2R3utA5dMHD66ATPjgc0SIl18P8GVcOMaMZ9M6"; at-acbin=Atza|IwEBIFqa8KJQyuhEYvD8BI82UmjMj34I4ySn4wc-Dtex0R5esBBQzgBc_mxpYIwyd0SOM1WhmxND6qpQ1Nat8xUE0Kd1xGlVMmRGKrZ1PUNsgI1KK0_pKrA9KczcaPsIxURbkMTTKBYN9lrqeez4NYyHzK5NewnV1tovfOKEYG5CnUMnjNxm0fttnkks-4u_4JnV3nHFDh1lpQUwTMP03dzmf6AJuVKr8QEB4QCvZZI2Pu17nw; sess-at-acbin="i6RlZ7BS2emhak8jOJWcdTumVKOnuqSWJu8XFV0nMAQ="; sst-acbin=Sst1|PQHdN_dQG1mP2Qq7rsTPZ2iACQwaWJUqtJ5-N7UXc0XVL4RLACGrv_UuZ9FfB56QfjwgefzDPSijZDjYpzgGtJhpGFkn9T5DmnitlaiGmQJJqbt7jbx9Epjl74VPFo2AGzyHr62ybAaEeAHVmtIy_Mz3wsfo6uvgpeOiqUfjfPPmWRVeWTX5eIGD10Gir8b9zgwT4EggtvvQuJItxhWf9kowdetrz6OMpkF97do9uMMznYXEJVvouS6FnIJmRsqwE8gQnE2o6apTT6eUXgQUfSV6GdUIBO-ptIUa9z11xJl0-kI; session-token=v3dW2XkyrIXUO31ZxROKhsBFf7Rd4BKQYWCW1D1Qmf0FfLNDXaFHuYAGibOPvF+WB6uhXuOmlE9NZJUrOevkYZSw4sMTU+GDkQScCb1i2rNrI9HmY3C6LxiBUNWnMKc3xwSElX8X2Ym0POPnZFvij3SSK6StpBViyUTfQEeNgk6To/RoaDqqNrrksXoDPpd41aWeOQvgW4kKpNKCtVd9EkTkOAJaS9A17yNCBgiiZOQB08/nHcSnFqYE0pc85rKrGL0228cfX8kIXLmSXvc+nVLxMvDvAtEzwaMlO/mxMCpmls8xwh+dtBwt78KhrnVDNBDIypHCyAYuX/0QlDHO0fv8wuErR11aB6yfYeJP1JssNmQ6qQexbyYAF6pVVcM1; csm-hit=tb:PXNJXR89PDDRWKHSWXZ7+s-N4KFZ54Q36QGXPHXS5V5|1731918801112&t:1731918801112&adb:adblk_yes; session-id-time=2082758401l',
    'priority': 'u=0, i',
    'referer': 'https://www.amazon.in/s?k=dress&crid=WE39IPV36QOL&sprefix=dress%2Caps%2C318&ref=nb_sb_noss_2',
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
response = requests.get(url , headers = headers,cookies=cookies)
tree = html.fromstring(response.content)
data ={
    "title" : [],
    "price" :[],
    "brand" :[]
}
df= pd.DataFrame(data)
title = tree.xpath('//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()')
# print(len(title))
df['title'] = title
# print(title)

price = tree.xpath('//div[@class="a-row"]//span[@class="a-price-whole"]/text()')
# print(len(price))
# print(price)
df['price'] = price
brand = tree.xpath('//span[@class="a-size-base-plus a-color-base"]/text()')
# print(len(brand))
# print(brand)
df['brand'] = brand

print(df)


