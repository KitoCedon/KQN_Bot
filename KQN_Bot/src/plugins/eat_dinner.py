import nonebot
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import CommandArg
from random import randint

addmeal = on_command("addmeal")
eatdinner = on_command("摆酒席")

@addmeal.handle()
async def handle_addmeal(matcher: Matcher, args: Message = CommandArg()):
    mesg = args
    f = open("meal.txt", mode = "a+", encoding = "UTF-8")
    f.write("{},".format(mesg))
    f.close()
    await addmeal.send("已添加 {}".format(mesg))

@eatdinner.handle()
async def handle_eatmeal(matcher: Matcher):
    f = open("meal.txt", mode = "r", encoding = "UTF-8")
    meal = f.read()
    f.close()
    tmp = list(map(str, meal.split(",")))
    tmp = tmp[:-1]
    num = []
    while len(num) < 5:
        x = randint(0, len(tmp) - 1)
        if x in num:
            continue
        else:
            num.append(x)
    meals = await get_meal(tmp, num)
    await eatdinner.send("{}".format(meals))

async def get_meal(lst: list, num: int):
    x = ""
    for i in num:
        x += f"{lst[i]}\n"
    return x