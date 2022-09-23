# 1번
from collections import defaultdict


class Customer:
    def __init__(self):
        self.id = None
        self.address = None

    def register(self, id, address):
        self.id = id
        self.address = address

    def update(self,ud_id,ud_add):
        self.id = ud_id
        self.address = ud_add

class PurchaseInfo:
    def __init__(self):
        self.purchase_num = None
        self.purchase_customer = None
        self.purchase_process = None

    def select(self,num):
        self.purchase_num = num

    def update(self,sta):
        self.purchase_process = sta
        self.purchase_customer = customer.id

    def delete(self):
        self.purchase_num = None
        self.purchase_process = None

class ProductList:
    def __init__(self):
        self.pro_list = []

    def update(self):
        self.pro_list.append(product.num)

    def delete(self,num):
        if num in pro_list:
            self.pro_list.remove(num)
        else:
            print("없는 번호입니다.")

    def search(self,thing):
        if thing in pro_list:
            return True


class Product:
    def __init__(self):
        self.product = defaultdict(list)

    def register(self,num,name):
        self.product_num = num
        self.product_name = name
        self.product[self.product_name].append(self.product_num)

    def delete(self,name):
        if name in self.product:
            del(self.product[name])
        else:
            print("없는 상품입니다.")

    def search(self,product):
        if product in self.product:
            print("존재합니다.")
        else:
            print("존재하지 않습니다.")

# 2번
class Computer:
    def __init__(self,own,model):
        self.own = own
        self.model = model
    def setComposition(self,mouse=None,monitor=None):
        self.mouse = mouse
        self.monitor = monitor
        print(f'{self.own}: {self.mouse.brand},{self.monitor.brand}')

class Mouse:
    def __init__(self,brand):
        self.brand = brand
    def setMaking(self,year,country):
        self.year = year
        self.country = country

class Monitor:
    def __init__(self,brand):
        self.brand = brand
    def setMaking(self,year,country,size=24):
        self.size = size
        self.year = year
        self.country = country

class Body:
    def setMaking(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.graphic = GRAPHIC()
    def setPrint(self):
        print(f'이 컴퓨터의 CPU는 {self.cpu.company} 이며, 성능은'
              f'{self.cpu.processor}')
        print(f'또한, RAM은 {self.ram.memory}giga이고 그래픽카드는 '
              f'{self.graphic.memory}giga 입니다')

class CPU:
    def setPerformance(self,company,processor,clock):
        self.company =company
        self.processor = processor
        self.clock = clock

class RAM:
    def setPerformance(self,type_,memory):
        self.type_ = type_
        self.memory = memory

class GRAPHIC():
    def setPerformance(self,memory):
        self.memory = memory

if __name__ == '__main__':
    # 1번
    customer = Customer()
    purchase_info = PurchaseInfo()
    product = Product()
    product_list = ProductList()

    # 2번
    mouse1 = Mouse("logit")
    monitor = Monitor("Sam")
    gildong_c = Computer('gildong',"A1011")
    gildong_c.setComposition(mouse1, monitor)
    body1 = Body()
    body1.setMaking()
    body1.cpu.setPerformance("DAM","i7-7000","3.5GHz")
    body1.ram.setPerformance("Desktop","32")
    body1.graphic.setPerformance("16")
    body1.setPrint()