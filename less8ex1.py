class Date:
    def __init__(self, date):
        self.date = date.split('-')

    @staticmethod
    def check_date(date):
        date = date.split('-')
        try:
            if int(date[0]) in range(1, 32) and int(date[1]) in range(1, 13) and int(date[2]) in range(1970, 2100):
                print('Корректная дата')
            else:
                raise TypeError
        except:
            print('Некорректная дата')

    @classmethod
    def int_date(cls, date):
        cls.date = date.split('-')
        for d in cls.date:
            print(int(d), end=' ')


Date.check_date('1-1-1970')
Date.check_date('31-12-2099')
date = Date('05-11-2017')
date.int_date('05-11-2017')
