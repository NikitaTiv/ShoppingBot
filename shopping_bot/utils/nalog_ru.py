"""
This module take from https://github.com/valiotti/get-receipts.git
"""
import requests

class NalogRuPython:
    HOST = 'irkkt-mobile.nalog.ru:8888'
    DEVICE_OS = 'iOS'
    CLIENT_VERSION = '2.9.0'
    DEVICE_ID = '7C82010F-16CC-446B-8F66-FC4080C66521'
    ACCEPT = '*/*'
    USER_AGENT = 'billchecker/2.9.0 (iPhone; iOS 13.6; Scale/2.00)'
    ACCEPT_LANGUAGE = 'ru-RU;q=1, en-US;q=0.9'
    CLIENT_SECRET = 'IyvrAbKt9h/8p6a7QPh8gpkXYQ4='
    OS = 'Android'

    def __init__(self, phone_number, code = 0):
        self.session_id = None
        self.phone = phone_number
        self.code = code


    def sends_sms_to_the_user(self):
        """Sends a phone number, receives a code."""
        url = f'https://{self.HOST}/v2/auth/phone/request'
        payload = {
            'phone': self.phone,
            'client_secret': self.CLIENT_SECRET,
            'os': self.OS,
        }
        headers = {
            'Host': self.HOST,
            'Accept': self.ACCEPT,
            'Device-OS': self.DEVICE_OS,
            'Device-Id': self.DEVICE_ID,
            'clientVersion': self.CLIENT_VERSION,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'User-Agent': self.USER_AGENT,
        }

        resp = requests.post(url, json=payload, headers=headers)


    def entering_code(self):
        """sends the code to the server, opens the session."""
        headers = {
            'Host': self.HOST,
            'Accept': self.ACCEPT,
            'Device-OS': self.DEVICE_OS,
            'Device-Id': self.DEVICE_ID,
            'clientVersion': self.CLIENT_VERSION,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'User-Agent': self.USER_AGENT,
        }

        url = f'https://{self.HOST}/v2/auth/phone/verify'
        payload = {
        'phone': self.phone,
        'client_secret': self.CLIENT_SECRET,
        'code': self.code,
        'os': self.OS,
        }

        resp = requests.post(url, json=payload, headers=headers)

        self.session_id = resp.json()['sessionId']
        self.refresh_token = resp.json()['refresh_token']


    def refresh_token_function(self) -> None:
        """Refresh token."""
        url = f'https://{self.HOST}/v2/mobile/users/refresh'
        payload = {
            'refresh_token': self.refresh_token,
            'client_secret': self.CLIENT_SECRET,
        }

        headers = {
            'Host': self.HOST,
            'Accept': self.ACCEPT,
            'Device-OS': self.DEVICE_OS,
            'Device-Id': self.DEVICE_ID,
            'clientVersion': self.CLIENT_VERSION,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'User-Agent': self.USER_AGENT,
        }

        resp = requests.post(url, json=payload, headers=headers)

        self.session_id = resp.json()['sessionId']
        self.refresh_token = resp.json()['refresh_token']

    def _get_ticket_id(self, qr: str) -> str:
        """
        Get ticker id by info from qr code
        :param qr: text from qr code. Example "t=20200727T174700&s=746.00&fn=9285000100206366&i=34929&fp=3951774668&n=1"
        :return: Ticket id. Example "5f3bc6b953d5cb4f4e43a06c"
        """
        url = f'https://{self.HOST}/v2/ticket'
        payload = {'qr': qr}
        headers = {
            'Host': self.HOST,
            'Accept': self.ACCEPT,
            'Device-OS': self.DEVICE_OS,
            'Device-Id': self.DEVICE_ID,
            'clientVersion': self.CLIENT_VERSION,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'sessionId': self.session_id,
            'User-Agent': self.USER_AGENT,
        }

        resp = requests.post(url, json=payload, headers=headers)

        return resp.json()['id']

    def get_ticket(self, qr: str) -> dict:
        """
        Get JSON ticket
        :param qr: text from qr code. Example "t=20200727T174700&s=746.00&fn=9285000100206366&i=34929&fp=3951774668&n=1"
        :return: JSON ticket
        """
        ticket_id = self._get_ticket_id(qr)
        url = f'https://{self.HOST}/v2/tickets/{ticket_id}'
        headers = {
            'Host': self.HOST,
            'sessionId': self.session_id,
            'Device-OS': self.DEVICE_OS,
            'clientVersion': self.CLIENT_VERSION,
            'Device-Id': self.DEVICE_ID,
            'Accept': self.ACCEPT,
            'User-Agent': self.USER_AGENT,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'Content-Type': 'application/json',
        }

        resp = requests.get(url, headers=headers)

        return resp.json()
