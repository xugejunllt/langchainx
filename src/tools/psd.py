from psd_tools import PSDImage

psd_file = PSDImage.open('任务二模版-001.psd')
print(f"图层数：{len(psd_file._layers)}")
print(f"图像尺寸：{psd_file.width} x {psd_file.height}")

# 遍历 PSD 文件中的所有图层
for layer in psd_file._layers:
    if layer.has_pixels():
        # 将图层转换为 PIL 图像对象
        layer_image = layer.topil()
        # 构建保存的文件名，使用图层的名称（如果可用），否则使用图层索引
        layer_name = layer.name if layer.name else f'layer_{layer.index}'
        save_path = f'{layer_name}.png'

        # 保存 PIL 图像对象为图片文件
        layer_image.save(save_path)
    else:
        print(f"图层 '{layer.name}' 不包含像素数据，无法转换为图像。")

psd_file.compose().save('merged_image.png')