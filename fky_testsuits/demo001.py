count = 3
while count > 0:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)
    if guess == 8:
        print("你是小甲鱼心里的蛔虫吗？")
        print("哼，猜中了也没有奖励！")
        break
    elif guess < 8:
        print("小了")
    else:
        print("大了")
    count = count - 1
print("游戏结束，不玩啦")