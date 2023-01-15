import cv2


def read_qr_code(filepath: str) -> str:
    """Парсит QR в строку."""
    try:
        img = cv2.imread(filepath)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except cv2.error as error:
        return error
