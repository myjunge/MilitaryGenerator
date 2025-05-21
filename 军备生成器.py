#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON

data = readJSON.读JSON文件("CarTank.json")
名人名言 = data["famous"] # 主要取自军备名言
前面垫话 = data["before"] # 在名言前面弄点话
后面垫话 = data['after']  # 在名言后面弄点话
废话 = data['bosh'] # 文章主要废话

xx = "兵器"

重复度 = 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

下一句废话 = 洗牌遍历(废话)
下一句名人名言 = 洗牌遍历(名人名言)

def 来点名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(前面垫话) )
    xx = xx.replace(  "b",random.choice(后面垫话) )
    return xx

def 另起一段():
    xx = "。"
    xx += "\r\n"
    xx += "    "
    return xx

def 自动生成一篇文章(标题, 字数):
    xx = 标题
    for x in xx:
        tmp = "    "
        while ( len(tmp) < 字数 ) :
            分支 = random.randint(0,int(int(字数)/2))
            if 分支 < int(int(字数)/15):
                tmp += 另起一段()
            elif 分支 < int(int(字数)/4):
                tmp += 来点名人名言()
            else:
                tmp += next(下一句废话)
        tmp = tmp.replace("x",xx).replace("。 。", "。").replace("， 。", "。").replace("    。\r\n","").replace(", 。", "。").replace(", ", "。").replace(": ", "。").replace(": 。", "。").replace("？。", "。").replace("。。", "。")
        return tmp

if __name__ == "__main__":
    xx = input("请输入文章主题:")
    num = int(input("请输入字数:"))
    print(自动生成一篇文章(xx,num))
    os.system("pause")

