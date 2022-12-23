import cv2


def read_qr_code(filepath: str) -> str:
    try:
        img = cv2.imread(filepath)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except cv2.error as error:
        return error


if __name__ == "__main__":
    print(read_qr_code("IMG_20221211_162336.jpg"))