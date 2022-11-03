#coding:utf-8

#数字炸弹

ggsddp=False
l_boomnum="boomnum"
l_luckynum="luckynum"
m_king=10
import random,time
def get_r(a,b):
    return random.randint(a, b)
def r_input(str):
    print(str,end="")
    temp=input()
    return temp
def cs(MAX,max,MIN,min,jsq,jiaocheng,luckynum,boomnum,J_C):
    global m_king
    if jiaocheng:
        if boomnum:
            print("这是数字炸弹游戏")
            print("我会随机一个数字,然后你猜%d次或以下,如果猜中,游戏就会失败,不然就会胜利"%m_king)
            if luckynum:
                print("在原本的基础上,会增加一个幸运数字,如果猜到幸运数字,则会直接胜利\n注意: 缩小范围可能会把幸运数字排除出去")
        if luckynum:
            print("这是幸运数字游戏")
            print("我会随机一个数字,然后你猜%d次或以下,如果猜中,游戏就会成功,不然就会失败"%m_king)
            if boomnum:
                print("在原本的基础上,会增加一个炸弹数字,如果猜到炸弹数字,则会直接失败\n注意: 缩小范围可能会把炸弹数字排除出去")
    print("游戏开始,",end="")
    if boomnum:
        print("生成炸弹数字中(范围为%d至%d)......"%(MIN,MAX),end="\t")
        target=get_r(MIN,MAX)
        print("生成完毕")
    if ggsddp and boomnum:
        print("[作弊]炸弹数字是 %d"%target)
    if luckynum:
        print("生成幸运数字中(范围为%d至%d)......"%(MIN,MAX),end="\t")
        l_target=get_r(MIN,MAX)
        print("生成完毕")
    if ggsddp and luckynum:
        print("[作弊]幸运数字是 %d"%l_target)
    print("开始猜吧")
    while True:
        think=int(r_input("请输入你猜的数字:"))
        if think>max or think<min:
            print("请输入范围内的数字!!")
            continue
        if luckynum:
            if think==l_target:
                print("你胜利了")
                if boomnum:
                    print("炸弹数字是%d"%target)
                return
        if boomnum:
            if think==target:
                print("BOOM!!!\n你输了")
                if luckynum:
                    print("幸运数字是%d"%l_target)
                return
        if True:
            if J_C=="boomnum":
                target_1=target
            else:
                target_1=l_target
            jsq+=1
            if jsq>=m_king:
                if J_C=="boomnum":
                    print("你胜利了")
                    if boomnum:
                        print("炸弹数字是%d"%target)
                    if luckynum:
                        print("幸运数字是%d"%l_target)
                    return
                else:
                    print("你失败了")
                    if boomnum:
                        print("炸弹数字是%d"%target)
                    if luckynum:
                        print("幸运数字是%d"%l_target)
                    return
            if think==max:
                max-=1
            elif think==min:
                min+=1
            elif think>target_1:
                max=think-1
            else:
                min=think+1
            print("范围更新为%d至%d"%(min,max))
            if J_C=="boomnum":
                print("还差%s次就能赢了!"%str(10-jsq))
            else:
                print("还有%s次就要输了!"%str(10-jsq))
def main(MAX="random_M",max=None,MIN="random_I",min=None,jsq=0,jiaocheng=False,luckynum=True,tellopen=True,boomnum=True,J_C="luckynum",wait=True,waittime=random.randint(0, 4)):
    if tellopen:
        if MAX=="random_M":
            print("最大值随机已开启")
        if MIN=="random_I":
            print("最小值随机已开启")
        if jiaocheng:
            print("数字炸弹规则教程已开启")
        if luckynum:
            print("[*]新增规则: 幸运数字")
        if boomnum:
            print("[*]新增规则: 炸弹数字")
        if ggsddp:
            print("作弊模式已开启")
    if MAX=="random_M":
        MAX=random.randint(20,200)
        max=MAX
    else:
        max=MAX
    if MIN=="random_I":
        if MAX>20:
            MIN=random.randint(1,MAX-20)
        elif MAX>10:
            MIN=random.randint(1,5)
        else:
            MIN=1
        min=MIN
    else:
        min=MIN
    print("准备加载主程序......\t",end="")
    if wait:
        time.sleep(waittime)
    print("OK")
    cs(MAX,max,MIN,min,jsq,jiaocheng,luckynum,boomnum,J_C)