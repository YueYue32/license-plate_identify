from PIL import Image
import pytesseract
import os
import cv2

# 設定 tesseract 執行檔的路徑
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_folder = r'C:\Users\user\PycharmProjects\pythonProject\yolov7\license_plate'  # 替換為你的文件夾路徑


# 打開圖像文件 路徑
image = Image.open('C:/Users/user/PycharmProjects/pythonProject/yolov7/license_plate/ll1.jpg')


# 循環讀取該文件夾中的每一張圖片
for image_name in os.listdir(image_folder):

    if image_name.endswith(('.png', '.jpg', '.jpeg')):  # 只讀取圖片文件
        # 構造完整的圖片路徑
        image_path = os.path.join(image_folder, image_name)

        # 讀取圖片
        image = cv2.imread(image_path)

        # 將圖像轉換為灰度圖
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 二值化處理
        _, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

        # 使用 pytesseract 進行文字識別
        custom_config = r'--oem 3 --psm 7'
        text = pytesseract.image_to_string(binary_image, config=custom_config)

        # 打印每張圖片的識別結果
        print(f"圖片 {image_name} 的識別結果:", text)
