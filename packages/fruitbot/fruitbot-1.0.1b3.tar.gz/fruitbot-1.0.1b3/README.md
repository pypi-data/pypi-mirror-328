## fruitbot
A simple, easy-to-use and powerful library for automating gameplay in the Fruit Craft game through APIs.


## Quick Example

```
from fruitbot import Client
from fruitbot.enums import CardPackTypes

bot = Client(session_name="fruit", restore_key="TOUR ACCOUNT RESTORE KEY")

data = bot.loadPlayer(save_session=True)
print(f"name: {data['name']},   amount of gold: {data['gold']},  id: {data['id']}")
print(bot.buyCardPack(CardPackTypes.BROWN_PACK))
```