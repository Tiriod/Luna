def HP(value):
    # HP计算公式
    result = ((((value * 2) + 31 + (252 / 4)) * 50) / 100) + 10 + 50
    return int(result)


def add(value):
    # 修正为加
    result = (((((value * 2) + 31 + (252 / 4)) * 50) / 100) + 5) * 1.1
    return result // 1


def low(value):
    # 修正为减
    result = (((((value * 2) + 0 + (0 / 4)) * 50) / 100) + 5) * 0.9
    return result // 1


def normal(value):
    # 无修正
    result = (((((value * 2) + 31 + (6 / 4)) * 50) / 100) + 5) * 1
    return result // 1


def durable(HPValue, defense, spDefense):
    defenseAllow = 0
    spDefenseAllow = 0
    HPValue = HP(HPValue)
    defenseValue = (((((defense * 2) + 31 + (defenseAllow / 4)) * 50) / 100) + 5) * 1.1
    spDefenseValue = (((((spDefense * 2) + 31 + (spDefenseAllow / 4)) * 50) / 100) + 5) * 1
    allowance = 256
    while allowance > 0:
        defenseValue = (((((defense * 2) + 31 + (defenseAllow / 4)) * 50) / 100) + 5) * 1.1
        spDefenseValue = (((((spDefense * 2) + 31 + (spDefenseAllow / 4)) * 50) / 100) + 5) * 1
        if allowance == 256:
            if defenseValue > spDefenseValue:
                spDefenseAllow += 4
                allowance -= 4
            else:
                defenseAllow += 4
                allowance -= 4
        else:
            if defenseValue > spDefenseValue:
                spDefenseAllow += 8
                allowance -= 8
            else:
                defenseAllow += 8
                allowance -= 8
    defenseValue = defenseValue // 1
    spDefenseValue = spDefenseValue // 1
    result = HPValue / ((0.5 / defenseValue) + (0.5 / spDefenseValue))
    return result // 1
