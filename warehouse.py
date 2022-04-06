import datetime

tm = datetime.datetime.now()
print('--------------------------------------------------------------------------------------------')
print ("%s/%s/%s -> %s:%s:%s" % (tm.day,tm.month,tm.year,tm.hour,tm.minute,tm.second))
print('--------------------------------------------------------------------------------------------')

class Warehouse:
    items = ['window','glass','window','table']
    window = 12.50
    glass = 3.25
    table = 42.00

    def get_Balance(self):
        balance = 0.00
        for item in self.items:
            if item=='window': balance += 12.50
            elif item=='glass': balance += 3.25
            elif item=='table': balance += 42.00
            else: continue
        print('Current Balance:  ',balance)
        print('--------------------------------------------------------------------------------------------')

    def get_Items(self):
        print('Current Items: ',self.items)
        print('window -> 12.50, glass -> 3.25, table -> 42.00')