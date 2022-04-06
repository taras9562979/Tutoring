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

class Customer(Warehouse):
    def get_Outflow(self,outflow):
        for item in outflow:
            self.items.remove(item)
        print('Items after Outflow: ',self.items)
        print('--------------------------------------------------------------------------------------------')

class Supplier(Warehouse):

    def get_Inflow(self,inflow):
        for item in inflow:
            self.items.append(item)
        print('Items after Inflow: ',self.items)
        print('--------------------------------------------------------------------------------------------')

warehouse_1 = Warehouse()
warehouse_1.get_Items()
warehouse_1.get_Balance()
supplier_1 = Supplier()
supplier_1.get_Inflow(['window','table'])
warehouse_1.get_Items()
warehouse_1.get_Balance()
customer_1 = Customer()
customer_1.get_Outflow(['window','window','window'])
warehouse_1.get_Items()
warehouse_1.get_Balance()