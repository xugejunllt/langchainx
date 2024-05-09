from PIL import Image

# 图片文件的路径
image_path = '4BECD150063XMGRX00L-tmall.jpg'

# 使用Pillow打开图片
with Image.open(image_path) as img:
    # 获取图片的宽和高
    width, height = img.size
    format = img.format
    mode = img.mode

print(f"图片的宽度是：{width}像素")
print(f"图片的高度是：{height}像素")
print(f"图片的格式是：{format}")
print(f"图片的mode是：{mode}")