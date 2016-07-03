#coding=utf-8
import urllib
import urllib2
import cookielib
import re
import Calculate




import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class SDU:
    def __init__(self, name, psw):
        self.loginUrl = "http://bkjw.hfut.edu.cn/pass.asp" #登陆界面
        self.gradeUrl = "http://bkjw.hfut.edu.cn/student/asp/xsxxxxx.asp" #成绩获取界面

        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'UserStyle': 'student',
            'user': name,
            'password': psw
        })
        #构建opener
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

        #学分list
        self.credit = []
        #成绩list
        self.grades = []




    def getPage(self):
        request = urllib2.Request(
            url= self.loginUrl,
            data= self.postdata)
        result = self.opener.open(request)
        result2 = self.opener.open(self.gradeUrl)

        print(result2.read().decode('gbk'))
        return result.read().decode('gbk')
