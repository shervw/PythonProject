import os
from aip import AipImageClassify
import openpyxl
from PIL import Image, ImageDraw

# 初始化客户端
APP_ID = '16440749'
API_KEY = 'NUfytN0wfHnHAv8QpY4rxM6m'
SECRET_KEY = 'IIPVXIaX2QZBBH9DaQz0iR8aEGGnvGtg'
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

# 确保图片文件夹存在（若不存在则自动创建）
image_folder = "img"  # 修改文件夹名称为img
os.makedirs(image_folder, exist_ok=True)  # 自动创建img文件夹

# 创建Excel文件
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["文件名", "车型", "颜色", "年份"])

# 处理图片
# 处理图片
for img_file in os.listdir(image_folder):
    image_path = os.path.join(image_folder, img_file)
    with open(image_path, "rb") as f:
        image_data = f.read()  # 修复缩进

    # 调用车辆识别接口（修正方法名）
    result = client.carDetect(image_data)  # 从 canDetect 改为 carDetect

    # 解析结果（修复语法错误）
    if "result" in result and result["result"]:
        car_info = result["result"][0]  # 修正索引语法和变量名
        car_name = car_info.get("name", "未知")
        color = car_info.get("color", "未知")
        year = car_info.get("year", "未知")  # 需验证字段名是否匹配接口返回
    else:
        car_name, color, year = "未知", "未知", "未知"

    # 在图片上添加文字并保存
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), f"车型：{car_name}\n颜色：{color}\n年份：{year}", fill="red")
    output_path = os.path.join("output", f"annotated_{img_file}")
    os.makedirs("output", exist_ok=True)  # 创建输出文件夹
    img.save(output_path)

    # 写入Excel
    sheet.append([img_file, car_name, color, year])

wb.save("车辆识别结果.xlsx")