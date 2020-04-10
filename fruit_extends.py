class Fruit:
    color = '绿色'
    def harvest(self, color):
        print('水果是'+color+'颜色的')
        print('水果已经收获')
        print('水果原来是' + Fruit.color)

class Apple(Fruit):
    color = '红色'
    def __init__(self):
        print('我是苹果')
class Orange(Fruit):
    color = '橙色'
    def __init__(self):
        print('我是橙子')
apple = Apple()
apple.harvest(Apple.color)

orange = Orange()

orange.harvest(Orange.color)
    
