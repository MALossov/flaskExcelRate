import os

import pyexcel

def saveScore(dict1, APP_STATIC_STATIC=None):
    # 创建文件夹finalScore，如果已经存在就不创建
    if not os.path.exists(APP_STATIC_STATIC + '/finalScore'):
        os.makedirs(APP_STATIC_STATIC + '/finalScore')
    # 将字典中的数据，按照姓名分别创建xlsx文件，文件名为姓名，如果存在就进行数据的追加
    for i in range(len(dict1)):
        if not os.path.exists(APP_STATIC_STATIC + '/finalScore/' + dict1[i]['姓名'] + '.xlsx'):
            pyexcel.save_as(records=[dict1[i]],
                            dest_file_name=APP_STATIC_STATIC + '/finalScore/' + dict1[i]['姓名'] + '.xlsx')
        else:
            # 先读取原有的文件，然后将新的数据追加到原有的数据中
            records = pyexcel.get_records(file_name=APP_STATIC_STATIC + '/finalScore/' + dict1[i]['姓名'] + '.xlsx')
            # 如果打分者已经存在，就覆盖原有的数据
            breakFlg = False
            for j in range(len(records)):
                if records[j]['打分者'] == dict1[i]['打分者']:
                    records[j] = dict1[i]
                    breakFlg = True
                    break
            # 如果打分者不存在，就追加新的数据
            if breakFlg == False:
                records.append(dict1[i])
            pyexcel.save_as(records=records,
                            dest_file_name=APP_STATIC_STATIC + '/finalScore/' + dict1[i]['姓名'] + '.xlsx')





