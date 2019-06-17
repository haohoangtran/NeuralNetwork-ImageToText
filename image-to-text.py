import cv2
import pytesseract
import os
import numpy as np
from PIL import Image
import sys
import ntpath
import shutil


#  dung opem cv tien xu ly anh
def get_string(img_path):
    # Doc file
    img = cv2.imread(img_path)
    # Xu ly anh tu mau sang gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Dung thuat toan de giam noise ảnh
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # Lưu tạm ảnh đã xử lý để đọc string
    cv2.imwrite("temp.png", img)
    # Đọc string từ image vừa lưu tạm
    result = pytesseract.image_to_string(Image.open("temp.png"))
    # xong rồi xóa ảnh temp
    os.remove("temp.png")

    return result


if __name__ == '__main__':
    from sys import argv

    current_directory = os.getcwd()
    output = os.path.join(current_directory, r'output')

    # xoa file cu
    shutil.rmtree(output)
    os.makedirs(output)

    if len(argv) != 2:
        print("chạy: python image-to-text.py đườngdẫn")
    else:
        inputdir = argv[1]
        print('--- Bắt đầu ---')
        if not os.path.exists(inputdir):
            print("Đường dẫn k tồn tại!")
        else:
            for file in os.listdir(inputdir):
                img_path = inputdir + '/' + file
                txtfilepath = ntpath.basename(img_path).rpartition('.')[0] + '.txt'
                txtfile = open(os.path.join(output, txtfilepath), 'w')
                str = get_string(img_path)
                print(file)
                txtfile.write(str)
                txtfile.close()
                print()
                print()

            print('------ Xong -------')
