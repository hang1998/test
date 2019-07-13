import hero

li = hero.Lita()
xi = hero.Xier()

for x in range(1,1000):
    xi.reformat()
    li.reformat()
    while True:
        xi.attack(li)
        if xi.win:
            break
        li.attack(xi)
        if li.win:
            break
print(xi.win_time)
print(li.win_time)