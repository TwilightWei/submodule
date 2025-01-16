from datetime import datetime


class GeneralUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_current_date():
        return datetime.now().strftime("%Y-%m-%d")