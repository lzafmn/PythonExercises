class Foo:#类方法无视类名变化
    #类方法和静态方法肆虐
    X = 1
    Y = 2
    def __init__(self):#静态方法和类方法所不能及
        self.x = 10
        self.y = 20
    @staticmethod
    def average(num1, num2):
        return (num1 + num2)/2
    @staticmethod
    def static_method():#静态方法调用类属性和方法时要用加上类名调用
        print('在静态方法中调用静态方法')
        a = Foo.average(Foo.X, Foo.Y)
        return a
    @classmethod
    def class_method(cls):#类方法传入的第一个参数是类名形参，方法体中调用时使用类名形参
        print('在类方法中使用静态方法')
        return cls.average(cls.X, cls.Y)
    def obj_method(self):
        print('在对象方法中使用静态方法')#实例对象方法调用属性和方法时可用类名或self调用
        return Foo.average(self.X, Foo.Y)
foo = Foo()
print(foo.static_method())
print(foo.class_method())
print(foo.obj_method())
#总之通过确定的类名如Foo调用类属性和类方法是万能的
#引用：静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护。
###引用：原则上，类方法是将类本身作为对象进行操作的方法。假设有个方法，且这个方法在逻辑上
##采用类本身作为对象来调用更合理，那么这个方法就可以定义为类方法。另外，如果需要继承，也
##可以定义为类方法

