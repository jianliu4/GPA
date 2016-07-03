#coding=utf-8
import re
import SDU


while True:
    name = raw_input("请输入您的学号:")
    if re.match('\d{10}', name, re.S):
        break
    print("请输入正确的学号！")

psw = raw_input("请输入您的密码：")

sdu = SDU.SDU(name, psw)
sdu.getPage()
#sdu.getGrades()
