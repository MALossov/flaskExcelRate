# 分析static/finalScore文件夹中的文件，生成分析结果
# 计算finalScore文件夹中，每个文件中每列的平均分，需要去掉最高分和最低分
from inspect import _void
import os

import pyexcel


def analysis_basic(APP_STATIC_STATIC=None):
    result=[]
    # 获取finalScore文件夹中的所有文件
    files = os.listdir(os.path.join(APP_STATIC_STATIC, 'finalScore'))
    # 遍历finalScore文件夹中的所有文件
    for file in files:
        # 获取每个文件的路径
        # 如果文件名中包含~$，则跳过
        if '~' in file:
            continue
        else:
            filePath = os.path.join(APP_STATIC_STATIC, 'finalScore', file)
            # 获取每个文件的数据
            data = pyexcel.get_records(file_name=filePath)
            # 直接计算文件当中的平均分
            # 思想道德素质分
            moral = getAverage(data, '思想道德素质分')
            # 身心素质分
            physical = getAverage(data, '身心素质分')
            # 审美与人文素养分
            aesthetic = getAverage(data, '审美与人文素养分')
            # 劳动素养分
            labor = getAverage(data, '劳动素养分')
            # 将每个文件中的每列的平均分添加到字典中，同时将data中的姓名也存入字典中
            result.append({'A姓名': data[0]['姓名'], 'A学号': data[0]['学号'], '思想道德素质分': moral,
                           '身心素质分': physical, '审美与人文素养分': aesthetic, '劳动素养分': labor})

    # 将result字典中的数据写入到文件中
    #print(result)
    # 检测目录Analisis是否存在，不存在则创建
    if not os.path.exists(os.path.join(APP_STATIC_STATIC, 'Analisis')):
        os.mkdir(os.path.join(APP_STATIC_STATIC, 'Analisis'))
    pyexcel.save_as(records=result, dest_file_name=os.path.join(APP_STATIC_STATIC, 'Analisis/analysis_raw.xls'))


# 创建计算平均分的函数
def getAverage(data, key):
    # 创建一个列表，用来存放每个文件中，思想道德素质分，身心素质分，审美与人文素养分，劳动素养分列的数据
    list = []
    # 遍历每个文件中的数据
    for i in range(len(data)):
        # 将每个文件中，思想道德素质分，身心素质分，审美与人文素养分，劳动素养分列的数据添加到列表中
        list.append(data[i][key])
    # 将列表中的数据进行排序
    list.sort()
    list.pop()
    list.pop(0)
    # 计算列表中的数据的平均分
    average = sum(list) / len(list)
    # 返回平均分
    return average


# 获取analysis.xls文件中的数据，并且对每一列进行排序
# 为每一列添加排名，前15%为A，之后35%位B，随后35%为C，最后15%为D
def analysis_rank(APP_STATIC_STATIC=None):
    # 获取analysis.xls文件中的数据
    data = _void
    data = pyexcel.get_records(file_name=os.path.join(APP_STATIC_STATIC, 'Analisis/analysis_raw.xls'))
    # 将analysis.xls文件中的数据进行排序
    # 从data中取出劳动素养分	审美与人文素养分	思想道德素质分	身心素质分，分别填入四个数组当中，进行排序
    labor = []
    aesthetic = []
    moral = []
    physical = []
    for i in range(len(data)):
        labor.append(data[i]['劳动素养分'])
        aesthetic.append(data[i]['审美与人文素养分'])
        moral.append(data[i]['思想道德素质分'])
        physical.append(data[i]['身心素质分'])
    # 对四个数组进行排序
    labor.sort(reverse=True)
    aesthetic.sort(reverse=True)
    moral.sort(reverse=True)
    physical.sort(reverse=True)
    # 查找每个数组中在15%,50%,85%和100%位置的数值
    labor_15 = labor[4]
    labor_50 = labor[16]
    labor_85 = labor[28]
    aesthetic_15 = aesthetic[4]
    aesthetic_50 = aesthetic[16]
    aesthetic_85 = aesthetic[28]
    moral_15 = moral[4]
    moral_50 = moral[16]
    moral_85 = moral[28]
    physical_15 = physical[4]
    physical_50 = physical[16]
    physical_85 = physical[28]
    # 将这几个值和原始数据进行比较，前15%为A，之后35%位B，随后35%为C，最后15%为D
    for i in range(len(data)):
        if data[i]['劳动素养分'] >= labor_15:
            data[i]['劳动素养分'] = 'A'
        elif data[i]['劳动素养分'] >= labor_50:
            data[i]['劳动素养分'] = 'B'
        elif data[i]['劳动素养分'] >= labor_85:
            data[i]['劳动素养分'] = 'C'
        else:
            data[i]['劳动素养分'] = 'D'
        if data[i]['审美与人文素养分'] >= aesthetic_15:
            data[i]['审美与人文素养分'] = 'A'
        elif data[i]['审美与人文素养分'] >= aesthetic_50:
            data[i]['审美与人文素养分'] = 'B'
        elif data[i]['审美与人文素养分'] >= aesthetic_85:
            data[i]['审美与人文素养分'] = 'C'
        else:
            data[i]['审美与人文素养分'] = 'D'
        if data[i]['思想道德素质分'] >= moral_15:
            data[i]['思想道德素质分'] = 'A'
        elif data[i]['思想道德素质分'] >= moral_50:
            data[i]['思想道德素质分'] = 'B'
        elif data[i]['思想道德素质分'] >= moral_85:
            data[i]['思想道德素质分'] = 'C'
        else:
            data[i]['思想道德素质分'] = 'D'
        if data[i]['身心素质分'] >= physical_15:
            data[i]['身心素质分'] = 'A'
        elif data[i]['身心素质分'] >= physical_50:
            data[i]['身心素质分'] = 'B'
        elif data[i]['身心素质分'] >= physical_85:
            data[i]['身心素质分'] = 'C'
        else:
            data[i]['身心素质分'] = 'D'
        # 将处理后的数据写入到新的文件中
    pyexcel.save_as(records=data, dest_file_name=os.path.join(APP_STATIC_STATIC,"Analisis/analysis_grade.xls"))
    for i in range(len(data)):
        # 为A添加得分93，为B添加得分91，为C添加得分89，为D添加得分87
        if data[i]['劳动素养分'] == 'A':
            data[i]['劳动素养分'] = 93
        elif data[i]['劳动素养分'] == 'B':
            data[i]['劳动素养分'] = 91
        elif data[i]['劳动素养分'] == 'C':
            data[i]['劳动素养分'] = 89
        else:
            data[i]['劳动素养分'] = 87
        if data[i]['审美与人文素养分'] == 'A':
            data[i]['审美与人文素养分'] = 93
        elif data[i]['审美与人文素养分'] == 'B':
            data[i]['审美与人文素养分'] = 91
        elif data[i]['审美与人文素养分'] == 'C':
            data[i]['审美与人文素养分'] = 89
        else:
            data[i]['审美与人文素养分'] = 87
        if data[i]['思想道德素质分'] == 'A':
            data[i]['思想道德素质分'] = 93
        elif data[i]['思想道德素质分'] == 'B':
            data[i]['思想道德素质分'] = 91
        elif data[i]['思想道德素质分'] == 'C':
            data[i]['思想道德素质分'] = 89
        else:
            data[i]['思想道德素质分'] = 87
        if data[i]['身心素质分'] == 'A':
            data[i]['身心素质分'] = 93
        elif data[i]['身心素质分'] == 'B':
            data[i]['身心素质分'] = 91
        elif data[i]['身心素质分'] == 'C':
            data[i]['身心素质分'] = 89
        else:
            data[i]['身心素质分'] = 87
        # 将处理后的数据写入到新的文件中
    pyexcel.save_as(records=data, dest_file_name=os.path.join(APP_STATIC_STATIC,"Analisis/analysis_score.xls"))


if __name__ == '__main__':
    analysis_basic()
    analysis_rank()
