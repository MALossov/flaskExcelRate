# -*- coding: utf-8 -*-
"""
app.py
:copyright: (c) 2022 by MALossov.
:license: GPL v3 or BSD
"""
import os

import flask_excel as excel
import pyexcel
from flask import Flask, request


import zipfile

from utils.Checker import checkNull, checkSigner, checkNames, checkScore
from utils.Savers import saveScore, saveScoreByRaw

from simpleAnalyser.analys_avg import analysis_rank,analysis_basic

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
excel.init_excel(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
APP_STATIC_STATIC = os.path.join(APP_ROOT, 'static')  # 设置一个专门的类似全局变量的东西

#点击按钮返回根页面

strReload = '<br />请重新上传<br /><button onclick="window.history.back();">返回上传</button>\
<br />本网页由<a href="http:////malossov.gitee.io">MALossov</a>制作'

# 创建一个校验一个字典数组中，是否存在key思想道德素质分，身心素质分，审美与人文素养分，劳动素养分,姓名，学号，打分者，是否为空的函数

# 创建一个校验两个字典数组中，key为学号和姓名时，value是否相等的函数


# 创建一个校验一个字典数组中，key为思想道德素质分，身心素质分，审美与人文素养分，劳动素养分时，值是否超过100的函数

#将字典数组中的数据，按照打分者分别创建xlsx文件，文件名为打分者


@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            scoreList = request.get_records(field_name='file')
        except:
            return "请先选择文件，再进行上传！"+strReload
        nameList = pyexcel.get_records(file_name=os.path.join(APP_STATIC_STATIC, '10班名单.xlsx'))

        #校验上传的文件是否符合要求
        if checkNull(scoreList) != True:
            return '上传的文件中有空值或未填写项目，请检查后重新上传<br />' + str(checkNull(scoreList)) + strReload
        if checkNames(scoreList, nameList) != True:
            return '上传的文件中，学号或姓名不匹配<br />' + str(checkNames(scoreList, nameList)) + strReload
        if checkScore(scoreList) != True:
            return '上传的文件中，评价项目分数超过100或小于0,或数据不符标准<br />' + str(checkScore(scoreList)) + strReload
        if checkSigner(scoreList) != True:
            return '上传的文件中，打分者姓名或不匹配<br />' + str(checkSigner(scoreList)) + strReload

        #将上传的文件保存到finalScore文件夹中
        saveScoreByRaw(scoreList,APP_STATIC_STATIC)
        saveScore(scoreList,APP_STATIC_STATIC)
        return '上传成功'+'<br />可以进行重复提交进行数据覆盖<br /><button onclick="window.history.back();">返回上传</button>\
<br />本网页由<a href="http:////malossov.gitee.io">MALossov</a>制作'
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file uploader</h1>
    <h3>(请传入评分表,xlsx形式)</h3>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value='向系统中上传表格'>
    </form>
    <br /><input type="button" onclick='location.href=("download")' value='下载评分样表'/>
    <input type="button" onclick='location.href=("rank")' value='实时计算最终分数'/>
    <br />本网页由<a href="http:////malossov.gitee.io">MALossov</a>制作
    '''
#下载在static文件夹中的10班名单.xlsx文件的链接
@app.route('/download')
def download():
    return app.send_static_file('10班名单.xlsx')

#计算总的排名的入口
@app.route('/rank')
def rank():
    try:
        analysis_basic(APP_STATIC_STATIC)
        analysis_rank(APP_STATIC_STATIC)
    except:
        return "数据太少/没有数据，无法自动计算"+strReload

    #发送多个static目录下的文件
    zipf = zipfile.ZipFile(os.path.join(APP_STATIC_STATIC,'Rank.zip'), 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(os.path.join(APP_STATIC_STATIC,'Analisis')):
        for file in files:
            if "analysis" in file:
                zipf.write(os.path.join(root, file),file,zipfile.ZIP_DEFLATED)
    zipf.close()
    return app.send_static_file('Rank.zip')

# insert database related code here
if __name__ == "__main__":
    app.run(debug=True,port=7777,host="0.0.0.0")  #测试环境，启用注释来打开
    #waitress.serve(app,host="0.0.0.0",port=7777)    #生产环境

