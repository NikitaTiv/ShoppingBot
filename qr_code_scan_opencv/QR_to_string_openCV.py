import cv2


def read_qr_code(filepath: str) -> str:
    try:
        img = cv2.imread(filepath)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        if points is None:
            return 'QR-код не обнаружен'
        else:
            codes_receipt = ['fn=', 'i=', 'fp=']
            if all(tech_codes in value for tech_codes in codes_receipt):
                return value
            return 'QR-код не с кассового чека'
    except cv2.error:
        return 'Неверное имя/путь файла'


if __name__ == '__main__':
    print(read_qr_code('photo_2022-12-23_15-15-29.jpg'))
