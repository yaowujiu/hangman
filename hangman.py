"""
Hangman猜词游戏
1.玩家一挑选一个秘密单词，单词中有多少个字母，则划多少横线（_）
2.玩家二每次猜一个字母
3.如果玩家二猜的字母正确，玩家一将下划线修改为正确的字母。如果单词中有一个字母出现多次，玩家二也必须猜多次。
如果玩家二猜错，玩家一画出上吊的人的一部分身体（从头开始）
4.如果玩家二在玩家一画完上吊的人之前猜对单词，玩家二胜利，反之失败
5.玩家一：计算机，玩家二：用户

Version: 0.1
Athuor: 姚云龙
"""

import random

#第一部分
"""
1.创建hangman函数保存游戏。该函数接收变量 word 作为参数即玩家二猜的单词
2.变量 wrong 记录玩家二猜错的字母数
3.变量stages 是一个列表，含有用来画上吊的人的字符串。Python 将 stages 列表中的每个字符串换行打印出来之后，就会组成一个上吊的人的图案
4.变量rletter 也是一个列表，用来保存word 变量中的每个字母，同时也用来记录还需要猜对的字母
5.变量board 也是一个字符串列表，用来记录显示给玩家二的提示，假如单词是cat则可能显示c__t（玩家二已经猜对了c 和t）。
  这里用["__"]* len(word)来填充board 列表，变量 word 中的每个字母都用一个下划线表示。例如，如果单词是cat，
  board 列表一开始的元素就是["__", "__", "__"]。
6.变量 win 的起始值为False，用来记录玩家二是否赢了游戏
"""
#第二部门
"""
1.只要变量wrong 的值小于len(stages) - 1，循环（和游戏）就会继续。变量wrong 记录了玩家二猜错的次数，
因此当玩家二猜错的次数大于画完上吊的人所需字符串的数量时（stages 列表中的字符串数量），游戏结束。
我们将stages 列表的长度减去1，这是因为列表从0 开始计数，而wrong 变量则是从1 开始。
2.进入循环之后，打印一个空白行，让shell 中的游戏界面看上去不乱。然后，通过内置的input 函数收集玩家二的答案，并保存在变量guess 中。
如果guess 在rletters（记录玩家二没猜对的字母列表）中，则猜测正确。如果猜对了，则需要更新board 列表，后面会用来打印剩余的字母。
如果玩家二猜了字母c，则要将board 列表改为["c", "__", "__"]。
3.因此，应使用rletters 列表的index 方法，获取玩家二所猜字母的第一个索引，并在board 列表中的对应索引位置替换为正确的字母。
但是有一个问题。由于index 只返回要查找字母的第一个索引，那么如果变量word中相同的字母有两个或两个以上，代码就会出错。
为了解决这个问题，我们把rletters中猜对的字母替换为美元符号，这样下次循环时，index 函数就能找到字母下一次出现
的索引（如果有的话），而不是仍返回第一个索引。如果玩家二猜错了，则将wrong 的值递增1。
4.下一步，用board 和stages 列表打印得分情况和上吊的人。打印得分情况的代码是" ".join(board)。打印上吊的人会更复杂一些。
当stages 列表中的每个元素打印在一行之后，完整图案就打印完了。可通过'\n'.join(stages)打印整个图案，
代码会在列表中的各个元素后加入一个换行符，这样就能确保每个字符串各占一行了。如果要在游戏的每个阶段都打印上吊的人，
则需对stages 列表进行切片。从阶段0 开始，切片至目前所处的阶段（用变量wrong 表示）并加一。加一，是因为在切片时尾端不会出现在结果里。
切片只会返回打印当前上吊的人进度所需要的字符串。
6.最后，检查玩家二是否赢得游戏。如果board 列表中没有了下划线，就表示猜对了所有字母，玩家二赢得游戏。如果是这样，则打印You win! It was:和猜对的单词。
同时将变量variable 设为True，跳出循环。
7.退出循环之后，如果玩家二赢了游戏，则程序结束。如果输了，变量win 被设为False。如果是这种情况，则打印完整的上吊的人和You lose!，最后是没有猜对的
那个单词：
"""
def hangman(word):
    wrong = 0
    stages = ["",
        "_______        ",
        "|              ",
        "|      |       ",
        "|      O       ",
        "|     /|\      ",
        "|     / \      ",
        "|              ",
         ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
       print("\n")
       msg = "猜一个单词: "
       char = input(msg)
       if char in rletters:
           cind = rletters.index(char)
           board[cind] = char
           rletters[cind] = '$'
       else:
           wrong += 1
       print(" ".join(board))
       e = wrong + 1
       print("\n".join(stages[0:e]))
       if "__" not in board:
           print("\n你赢了！")
           print(" ".join(board))
           win = True
           break
    if not win:
           print("\n".join(stages[0:wrong]))
           print("\n你输了！单词是 {}".format(word))

listres = ["cat","dog","bird"]
res = random.choice(listres)
#print(res)
hangman(res)


        
