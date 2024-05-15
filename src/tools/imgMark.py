import cv2
from PIL import ImageFont

# 读取医学图像，这里以普通图片为例
img = cv2.imread('1.jpg')

# 假设我们已经知道肿瘤的大致位置，这里用矩形框来标注
tumor_top_left = (50, 50)  # 肿瘤左上角坐标
tumor_bottom_right = (150, 150)  # 肿瘤右下角坐标

# 在图像上绘制矩形框来标注肿瘤位置
cv2.rectangle(img, tumor_top_left, tumor_bottom_right, (0, 0, 255), 2)


# 中文字体的路径
font_path = 'Helvetica Bold.ttf'

# 加载中文字体
font = ImageFont.truetype(font_path, 24)

# 在肿瘤位置旁边添加文字说明
# font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, '中文', (tumor_top_left[0], tumor_top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1)

# 显示标注后的图像
cv2.imshow('Tumor Annotation', img)

# 等待用户按键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()