import cv2


def read_qr_code(filename: str) -> str: #принимает на вход путь до файла вместе с его расширением
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        if value:
            return value
        return "Не удалось распознать QR-код! Повторите попытку!"
    except:
        return "Не удалось распознать QR-код! Повторите попытку!"


if __name__ == "__main__":
    print(read_qr_code("IMG_20221211_162336.jpg"))