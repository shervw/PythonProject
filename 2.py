
result={'log_id': 5153046660609868740, 'words_result_num': 6, 'direction': 0, 'image_status': 'normal', 'words_result': {'住址': {'location': {'width': 1051, 'top': 1088, 'height': 224, 'left': 653}, 'words': '安徽省宿州市埇桥区朱仙庄镇'}, '出生': {'location': {'width': 836, 'top': 873, 'height': 90, 'left': 657}, 'words': '19661102'}, '姓名': {'location': {'width': 283, 'top': 449, 'height': 113, 'left': 661}, 'words': '徐乐'}, '公民身份号码': {'location': {'width': 1426, 'top': 1620, 'height': 103, 'left': 1055}, 'words': '652901196611026716'}, '性别': {'location': {'width': 74, 'top': 679, 'height': 88, 'left': 664}, 'words': '男'}, '民族': {'location': {'width': 65, 'top': 683, 'height': 78, 'left': 1186}, 'words': '汉'}}}
# ...（原始数据）


# 提取信息
姓名 = result['words_result']['姓名']['words']
性别 = result['words_result']['性别']['words']
出生 = result['words_result']['出生']['words']
住址 = result['words_result']['住址']['words']

# 格式化生日
生日 = f"{出生[:4]}年{出生[4:6]}月{出生[6:8]}日"

# 输出结果
print(f"姓名：{姓名}")
print(f"性别：{性别}")
print(f"生日：{生日}")
print(f"住址：{住址}")