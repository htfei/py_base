__author__ = 'Terry'


class Hello:
    def __init__(self, name):
        self.name = name

    def sayhello(self):
        print("hellooooo {0},{1}".format(self.name, self.name))


# 继承Hello类
class Hi(Hello):
    def sayhi(self):
        print("hiiiiii {0},{1}".format(self.name, self.name))
