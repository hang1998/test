import random

def fun(arg):
    pass

def relu(arg):
    if arg > 0:
        return arg
    else:
        return 0

xprint = fun

class Fuhua(object):
    """docstring for Fuhua"""
    name = "浮华"
    _hp = 100
    _atk = 27
    _defe = 8
    _counter = 0
    win = False
    win_time = 0

    def attack(self, enemy):
        self._counter += 1
        if self._counter == 3:
            self._counter = 0
            xprint('浮华发动了必杀技')
            enemy.defence(self, random.randint(10, 30) + enemy._defe)
        else:
            xprint('浮华发动了普通攻击')
            enemy.defence(self, self._atk)
    
    def defence(self, enemy, atk):
        self._hp -= relu(atk - self._defe)
        xprint('德莉傻受到了{}伤害，剩余{}生命'.format(relu(atk - self._defe), self._hp))
        if self._hp <= 0:
            xprint('{}赢了'.format(enemy.name))
            enemy.win_time += 1
            enemy.win = True

    def reformat(self):
        self._hp = 100
        self.counter = 0
        self.win = False

class Bulangya(object):
    """docstring for Bulangya"""
    name = "布狼牙"
    _hp = 100
    _atk = 26
    _defe = 8
    _counter = 0
    win = False
    win_time = 0

    def attack(self, enemy):
        self._counter += 1
        if self._counter == 3:
            self._counter = 0
            xprint('布狼牙发动了必杀技')
            atk = random.randint(1, 100) + enemy._defe
        else:
            xprint('布狼牙发动了普通攻击')
            atk = self._atk
        enemy.defence(self, atk)
    
    def defence(self, enemy, atk):
        if enemy.win:
            return
        if random.randint(1, 100) <= 15:
            xprint('布狼牙闪避了攻击')
        else:
            self._hp -= relu(atk - self._defe)
            xprint('布狼牙受到了{}伤害，剩余{}生命'.format(relu(atk - self._defe), self._hp))
        if self._hp <= 0:
            xprint('{}赢了'.format(enemy.name))
            enemy.win_time += 1
            enemy.win = True

    def reformat(self):
        self._hp = 100
        self.counter = 0
        self.win = False

de = Delisha()
bu = Bulangya()

xprint = print

for x in range(0,1):
    de.reformat()
    bu.reformat()
    while True:
        de.attack(bu)
        if de.win:
            break
        bu.attack(de)
        if bu.win:
            break
print(de.win_time)
print(bu.win_time)