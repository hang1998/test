import random

class Delisha(object):
    """docstring for Delisha"""
    name = "德莉傻"
    hp = 100
    atk = 24
    defence = 8
    counter = 0
    win = False
    win_time = 0

    def attack(self, arg):
        self.counter += 1
        if self.counter == 2:
            self.counter = 0
            a = random.randint(1, 16)
            b = random.randint(1, 16)
            c = random.randint(1, 16)
            d = random.randint(1, 16)
            arg.hp -= a+b+c+d
            print('{0}发动了必杀技，{1}受到了{2},{3},{4},{5}点攻击，{1}还有{6}点生命'.format(self.name, arg.name, a, b, c, d, arg.hp))
        else:
            arg.hp -= self.atk - arg.defence
            print('{0}对{1}进行了普通攻击，{1}受到了{2}点攻击，{1}还有{3}点生命'.format(self.name, arg.name, self.atk - arg.defence, arg.hp))
        if arg.hp <= 0:
            print('{}赢了'.format(self.name))
            self.win_time += 1
            self.win = True
        
class Qiyana(object):
    """docstring for Qiyana"""
    name = "草履虫"
    hp = 120
    atk = 23
    defence = 11
    counter = 0
    win = False
    win_time = 0

    def attack(self, arg):
        self.counter += 1
        if self.counter == 3:
            self.counter = 0
            arg.hp -= (12 - arg.defence) * 8
            print('{0}发动了必杀技，{1}受到了{2}*8点攻击，{1}还有{3}点生命'.format(self.name, arg.name, 12 - arg.defence, arg.hp))
        else:
            arg.hp -= self.atk - arg.defence
            print('{0}对{1}进行了普通攻击，{1}受到了{2}点攻击，{1}还有{3}点生命'.format(self.name, arg.name, self.atk - arg.defence, arg.hp))
        if arg.hp <= 0:
            print('{}赢了'.format(self.name))
            self.win_time += 1
            self.win = True

de = Delisha()
qi = Qiyana()

while True:
    de.attack(qi)
    if de.win:
        break
    qi.attack(de)
    if qi.win:
        break
        