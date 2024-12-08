import requests
from lxml import html
import pandas as pd
import requests

cookies = {
    'ni_d': '198D16BF-4350-4A23-a5A2-FDBDAA0D3600',
    'anonymousId': '1A7B523810011DCC8F4FA10B0911BEA1',
    'kndctr_F0935E09512D2C270A490D4D_AdobeOrg_identity': 'CiY1MTQ2NjU5MTgzNjE3MTk4MDA0MDIwNDcyMjYzMjE2NTExMjI3MFITCLLZosK1MhABGAEqBElORDEwAPABstmiwrUy',
    's_ecid': 'MCMID%7C51466591836171980040204722632165112270',
    'AMCV_F0935E09512D2C270A490D4D%40AdobeOrg': '1994364360%7CMCMID%7C51466591836171980040204722632165112270%7CMCAID%7CNONE%7CMCOPTOUT-1732360198s%7CNONE%7CvVersion%7C3.4.0',
    'geoloc': 'cc=IN,rc=UP,tp=vhigh,tz=GMT+5.50,la=26.47,lo=80.35',
    'AKA_A2': 'A',
    'ak_bmsc': 'CAD51D101935098372D6D9466B002611~000000000000000000000000000000~YAAQVmw/F/mNPiiTAQAAPrUNWRnXy38nVFBiWvdQV53jnX2aKHtj3D+wTwR6hsHNILkdbPKjM/Ycou3OFkvp5gZt+UqZD3IlSEGvsGSAYTroglKta2pD9HvdvrdwB+hfIMBCUDqQc6fgKXNyc2uvhCd9d1khONmZ9nSzQQWDkdmcEdwNJJ48vS+CmGsAknQ0IgYXbpPdmLK3E0UjYbFOyMF+QchRs3OlidCTdd5Kk34cHV8CS+XmNsJJoNoFgX7YYZjHnnnJo+zn64gEyotZk57LfAdGj2ihHwS0sZCCGHNZSusrKGFZF54Q1m3EhvJ7VOfDfdeDrmRNvbxJugVvMiY57MlqlLfymYE94lxlEJwSCh7MZrtfIlUyOQrubz3zdXF+wcob1DE=',
    'sq': '0',
    'kndctr_F0935E09512D2C270A490D4D_AdobeOrg_cluster': 'ind1',
    'ni_cs': '62d23742-dc75-4bb4-b3ee-d7b9bc10bf56',
    'mboxEdgeCluster': '41',
    'ppd': 'pdp|nikecom>pdp>nike%20air%20max%20plus',
    'mbox': 'session%2351466591836171980040204722632165112270%2DPdOSBQ%231732367773',
    'bm_sv': 'E76E2FA4A1077F40C826095204EE3513~YAAQnI0sMbCem0aTAQAAwREOWRmQUsJv8bSzDlf0ghxpaW0tgVWQLwBYp0nA6gfMxJoS2L1Cnh5uUwfoBOJj5CtCc6yZ1DztOa9iMtPeZETB1aM/LSsVRKik7fvtQLDZe9Qo40MQTVNCZQkbiPWvWOTmzV56DrAlpZIJ1Pag7mF5QE/NK/y37052ZEEAYNushY5zmVngXkywBVWrHT1I3qvUdQqDnz+oQPPT3K1BNEm90Ej9IdPaPObYX6Z+yOA=~1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'ni_d=198D16BF-4350-4A23-a5A2-FDBDAA0D3600; anonymousId=1A7B523810011DCC8F4FA10B0911BEA1; kndctr_F0935E09512D2C270A490D4D_AdobeOrg_identity=CiY1MTQ2NjU5MTgzNjE3MTk4MDA0MDIwNDcyMjYzMjE2NTExMjI3MFITCLLZosK1MhABGAEqBElORDEwAPABstmiwrUy; s_ecid=MCMID%7C51466591836171980040204722632165112270; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=1994364360%7CMCMID%7C51466591836171980040204722632165112270%7CMCAID%7CNONE%7CMCOPTOUT-1732360198s%7CNONE%7CvVersion%7C3.4.0; geoloc=cc=IN,rc=UP,tp=vhigh,tz=GMT+5.50,la=26.47,lo=80.35; AKA_A2=A; ak_bmsc=CAD51D101935098372D6D9466B002611~000000000000000000000000000000~YAAQVmw/F/mNPiiTAQAAPrUNWRnXy38nVFBiWvdQV53jnX2aKHtj3D+wTwR6hsHNILkdbPKjM/Ycou3OFkvp5gZt+UqZD3IlSEGvsGSAYTroglKta2pD9HvdvrdwB+hfIMBCUDqQc6fgKXNyc2uvhCd9d1khONmZ9nSzQQWDkdmcEdwNJJ48vS+CmGsAknQ0IgYXbpPdmLK3E0UjYbFOyMF+QchRs3OlidCTdd5Kk34cHV8CS+XmNsJJoNoFgX7YYZjHnnnJo+zn64gEyotZk57LfAdGj2ihHwS0sZCCGHNZSusrKGFZF54Q1m3EhvJ7VOfDfdeDrmRNvbxJugVvMiY57MlqlLfymYE94lxlEJwSCh7MZrtfIlUyOQrubz3zdXF+wcob1DE=; sq=0; kndctr_F0935E09512D2C270A490D4D_AdobeOrg_cluster=ind1; ni_cs=62d23742-dc75-4bb4-b3ee-d7b9bc10bf56; mboxEdgeCluster=41; ppd=pdp|nikecom>pdp>nike%20air%20max%20plus; mbox=session%2351466591836171980040204722632165112270%2DPdOSBQ%231732367773; bm_sv=E76E2FA4A1077F40C826095204EE3513~YAAQnI0sMbCem0aTAQAAwREOWRmQUsJv8bSzDlf0ghxpaW0tgVWQLwBYp0nA6gfMxJoS2L1Cnh5uUwfoBOJj5CtCc6yZ1DztOa9iMtPeZETB1aM/LSsVRKik7fvtQLDZe9Qo40MQTVNCZQkbiPWvWOTmzV56DrAlpZIJ1Pag7mF5QE/NK/y37052ZEEAYNushY5zmVngXkywBVWrHT1I3qvUdQqDnz+oQPPT3K1BNEm90Ej9IdPaPObYX6Z+yOA=~1',
    'if-none-match': '"79361-fVB8dN5bSIcx/E8uJycXFNaoORQ"',
    'priority': 'u=0, i',
    'referer': 'https://www.nike.com/in/',
    'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Brave";v="131.0.0.0", "Chromium";v="131.0.0.0", "Not_A Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
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


response = requests.get(url,cookies=cookies, headers=headers)
url = 'https://www.nike.com/in/w?q=shoes&vst=shoes'
response = requests.get(url,cookies=cookies, headers=headers)
print(response)

data = {
    'title' :[],
    'price' :[],
    'category':[]
}
df = pd.DataFrame(data)
tree = html.fromstring(response.content)
title = tree.xpath('//div[@class="product-card__title"]/text()')
print(len(title))
print(title)
df['title'] = title
price = tree.xpath('//div[@data-testid="product-price"]/text()')
print(price)
cleaned_prices = []

# Loop through each price and remove "MRP : ₹"
for p in price:
    # Clean the price string by removing 'MRP : ₹'
    cleaned_price = p.replace('MRP : ₹', '').strip()
    cleaned_prices.append(cleaned_price)

# Print to verify the cleaned prices
print(cleaned_prices)

# Assign the cleaned price list to the 'price' column in the DataFrame
df['price'] = cleaned_prices


choice = tree.xpath('//div[@class="product-card__subtitle"]/text()')
print(choice)
print(len(choice))
df['category'] = choice

print(df)
