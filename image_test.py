import requests
import cv2
import numpy as np

# 下载图像
url = 'https://gitee.com/hongcyu/image/raw/master/images/image.jpg'
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    with open('downloaded_image.jpg', 'wb') as f:  # 修正了这里的错误
        f.write(response.content)
else:
    print("Failed to download image. Status code:", response.status_code)
    exit()  # 如果下载失败，则退出

# 使用 OpenCV 读取下载的图像
pic = cv2.imread('downloaded_image.jpg')
if pic is None:
    print("Failed to load image. Please check the file path.")
    exit()

# 后续处理
# xy = array_pic(pic)  # 确保这个函数可以正确处理 pic

