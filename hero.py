import random

def fun(arg):
    pass

def relu(arg):
    if arg > 0:
        return arg
    else:
        return 0

xprint = fun
#xprint = print

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
            xprint('{0}发动了必杀技，{1}受到了{2},{3},{4},{5}点攻击，{1}还有{6}点生命'.format(self.name, arg.name, a, b, c, d, arg.hp))
        else:
            arg.hp -= self.atk - arg.defence
            xprint('{0}对{1}进行了普通攻击，{1}受到了{2}点攻击，{1}还有{3}点生命'.format(self.name, arg.name, self.atk - arg.defence, arg.hp))
        if arg.hp <= 0:
            xprint('{}赢了'.format(self.name))
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
            xprint('{0}发动了必杀技，{1}受到了{2}*8点攻击，{1}还有{3}点生命'.format(self.name, arg.name, 12 - arg.defence, arg.hp))
        else:
            arg.hp -= self.atk - arg.defence
            xprint('{0}对{1}进行了普通攻击，{1}受到了{2}点攻击，{1}还有{3}点生命'.format(self.name, arg.name, self.atk - arg.defence, arg.hp))
        if arg.hp <= 0:
            xprint('{}赢了'.format(self.name))
            self.win_time += 1
            self.win = True

class Lita(object):
    """docstring for Lita"""
    name = "丽塔"
    hp = 100
    atk = 26
    defence = 8
    counter = 0
    win = False
    win_time = 0

    def attack(self, arg):
        arg.hp -= relu(self.atk - arg.defence)
        xprint('{0}对{1}进行了攻击，{1}受到了{2}点攻击，{1}还有{3}点生命'.format(self.name, arg.name, self.atk - arg.defence, arg.hp))
        if random.randint(1, 100) <= 20:
            self.counter = 1
            xprint('{}发动了必杀技，{}下次攻击无法进行'.format(self.name, arg.name))
        if random.randint(1, 100) <= 30:
            self.hp += relu(self.atk - arg.defence)
            xprint('{}发动了被动，生命值恢复了{}'.format(self.name, relu(self.atk - arg.defence)))
        if arg.hp <= 0:
            xprint('{}赢了'.format(self.name))
            self.win_time += 1
            self.win = True 
        else:
            arg.hp += 7
            xprint('{}发动了被动，生命值恢复了7,现在还有{}'.format(arg.name, arg.hp))

    def reformat(self):
        self.hp = 100
        self.counter = 0
        self.win = False

class Xier(object):
    """docstring for Xier"""
    name = "希儿"
    hp = 100
    atk = 23
    defence = 10
    counter = 0
    win = False
    win_time = 0

    def attack(self, arg):
        self.counter += 1
        if arg.counter == 1:
            arg.counter = 0
            xprint('本回合不能攻击')
            if self.counter == 4:
                self.counter = 0
        else:
            if self.counter == 4:
                self.counter = 0
                if random.randint(1, 100) <= 25:
                    arg.hp -= 100
                    xprint('{0}发动了必杀技，{1}受到了100点攻击，{1}还有{2}点生命'.format(self.name, arg.name, arg.hp))
                else:
                    xprint('{0}发动了必杀技，然而并没有命中'.format(self.name))
            else:
                arg.hp -= self.atk - arg.defence
                xprint('{0}对{1}进行了普通攻击，{1}受到了{2}点攻击，{1}还有{3}点生命'.format(self.name, arg.name, self.atk - arg.defence, arg.hp))
            if arg.hp <= 0:
                xprint('{}赢了'.format(self.name))
                self.win_time += 1
                self.win = True

    def reformat(self):
        self.hp = 100
        self.counter = 0
        self.win = False