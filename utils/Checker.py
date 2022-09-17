def checkNull(dict1):
    try:
        # 遍历字典数组，如果key为思想道德素质分，身心素质分，审美与人文素养分，劳动素养分,姓名，学号，打分者，是否为空，返回false
        for i in range(len(dict1)):
            if dict1[i]['思想道德素质分'] == '' or dict1[i]['身心素质分'] == '' or dict1[i]['审美与人文素养分'] == '' or dict1[i]['劳动素养分'] == '' or dict1[i]['姓名'] == '' or dict1[i]['学号'] == '' or dict1[i]['打分者'] == '':
                # 将错误的字典数组中的值返回
                return dict1[i]
        # 如果遍历完了，都没有返回false，那么就返回true
    except:
        return '存在空key'
    return True


def checkSigner(dict1):
    # 遍历字典数组，如果key为打分者时，值不相等，返回false
    for i in range(len(dict1)):
        if dict1[i]['打分者'] != dict1[0]['打分者']:
            # 将错误的打分者姓名返回
            return dict1[i]['打分者'] + ' 打分者不一致'
        # 检查打分者的格式是否为2021010910开头的13位数字
        if len(str(dict1[i]['打分者'])) != 13 or str(dict1[i]['打分者'])[:10] != '2021010910':
            return str(dict1[i]['打分者']) + ' 打分者格式不正确'
    # 如果遍历完了，都没有返回false，那么就返回true
    return True


def checkNames(dict1, dict2):
    # 首先遍历两个字典数组，如果长度不一致，就返回两者相差的长度
    if len(dict1) != len(dict2):
        return len(dict1) - len(dict2)
    # 如果长度一致，遍历两个字典数组，如果key为学号和姓名时，value不相等，返回false
    for i in range(len(dict1)):
        if dict1[i]['学号'] != dict2[i]['学号'] or dict1[i]['姓名'] != dict2[i]['姓名']:
            # 将错误的字典数组中的值返回
            return dict1[i]
    # 如果遍历完了，都没有返回false，那么就返回true
    return True


def checkScore(dict1):
    # 遍历字典数组，如果key为思想道德素质分，身心素质分，审美与人文素养分，劳动素养分时，值超过100，返回false
    try:
        for i in range(len(dict1)):
            # 将字典数组中对应的值转换为浮点类型后比较
            if float(dict1[i]['思想道德素质分']) > 100 or float(dict1[i]['身心素质分']) > 100 or float(dict1[i]['审美与人文素养分']) > 100 or float(dict1[i]['劳动素养分']) > 100:
                # 将错误的字典数组中大于100评价项目和姓名返回
                return dict1[i]
            # 如果key为思想道德素质分，身心素质分，审美与人文素养分，劳动素养分时，值小于0，返回false
            if float(dict1[i]['思想道德素质分']) < 0 or float(dict1[i]['身心素质分']) < 0 or float(dict1[i]['审美与人文素养分']) < 0 or float(dict1[i]['劳动素养分']) < 0:
                # 将错误的字典数组中小于0评价项目和姓名返回
                return dict1[i]
    except:
        return '数据不符合标准，请填写数字！'
    # 如果遍历完了，都没有返回false，那么就返回true
    return True
