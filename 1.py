from aip import AipImageCensor
from PIL import Image, ImageDraw, ImageFont
import glob
import os

""" 你的 APPID AK SK """
APP_ID = '118527301'
API_KEY = 'dbAq7f8rlhHzKoZQIXj6jj0A'
SECRET_KEY = 'ZbuKpP7YcIFGWZIwmipLUSkjBgbaBbdU'
client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)

# 修复水印加载逻辑
original_ps = Image.open('wrong.jpg')
ps = original_ps.resize((
    original_ps.width // 4,  # 使用整数除法运算符
    original_ps.height // 4
))

tfont = ImageFont.truetype("C:/WINDOWS/Fonts/simsun.ttc", 18)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# ... 保持前面导包和配置不变 ...

for filename in glob.glob('images/*.jpg'):
    try:
        result = client.imageCensorUserDefined(get_file_content(filename))
        im = Image.open(filename)
        print(f"处理文件: {filename} - 结果: {result['conclusion']}")
        
        # 创建绘图对象（无论是否合规都需要）
        draw = ImageDraw.Draw(im)
        
        if result['conclusion'] == '不合规':
            msg = '\n'.join([reason['msg'] for reason in result['data']])
            print(f"违规原因:\n{msg}")
            
            # 违规水印（左上角）
            im.paste(ps, (0, 0))
            draw.text((0, 0), msg, fill='red', font=tfont)
        else:
            # 合格水印（右下角）
            text = "合格"
            bbox = draw.textbbox((0,0), text, font=tfont)
            x = im.width - (bbox[2]-bbox[0]) - 10  # 右侧留10像素边距
            y = im.height - (bbox[3]-bbox[1]) - 10 # 底部留10像素边距
            draw.text((x, y), text, fill='green', font=tfont)
        
        # 统一保存处理结果
        im.save(filename)
        print(f"已保存处理结果到: {filename}\n")

    except Exception as e:
        print(f"处理文件 {filename} 时出错: {str(e)}")

