import random

def game():
    num = random.randint(1,100)
    cnt = 0
    user_input = int(input("请输入数字:"))
    while (num != user_input) :
        if (num > user_input) :
            user_input = int(input("太小了，再来一次:"))
        else :
            user_input = int(input("太大了，再来一次:"))
        cnt += 1
    if cnt >= 10 :
        print("你用了 {0} 次才猜中，你太笨了".format(cnt))
    else :
        print("你用了 {0} 次就猜中，你太聪明了".format(cnt))

if __name__ == "__main__":
    start_game = 'y'
    while(start_game == 'y') :
        game()
        start_game = str(input("再来一局？(y or n):"))
    print("游戏结束")
    
        