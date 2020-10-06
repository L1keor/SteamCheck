from steam_community_market import Market, AppID
import re

market = Market("RUB")

item1 = "Sticker | FURIA | Berlin 2019"
item2 = "Berlin 2019 Legends Autograph Capsule"
item3 = "Katowice 2019 Legends Autograph Capsule"

pricesf = market.get_lowest_price(item1, AppID.CSGO)
pricebc = market.get_lowest_price(item2, AppID.CSGO)
pricekc = market.get_lowest_price(item3, AppID.CSGO)

allprice = int(re.search(r'\d+', pricesf).group(0)) + 4*int(re.search(r'\d+', pricebc).group(0)) + int(re.search(r'\d+', pricekc).group(0))

print('Sticker Furia -', pricesf)
print('Berlin Capsule -', pricebc)
print('Katowice Capsule -', pricekc)
print('Твоя прибыль =', allprice, 'руб.')