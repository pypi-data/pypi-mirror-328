from enum import Enum

class Exchange(Enum):
    BJ = 2
    SHF = 3
    CFE = 4
    DCE = 5
    CZC = 6
    INE = 7
    SH = 101
    SZ = 102
    HK = 103
    SZN = 253
    SHN = 254

class Variety(Enum):
    all = 0
    stock = 1
    fund = 2
    bond = 3
    option = 4
    index = 5
    hkt = 6
    futureoption = 7
    cfetsrmb = 8
    hkex = 9
    cvtbond = 20
    reits = 21
    future = 22
    inxfuture = 23


def get_exchange_value(name):
    exchange_code=[]
    for ex in name:
       for exchange in Exchange:
          if ex == exchange.name:
              exchange_code.append(exchange.value)
              break
    return exchange_code

def get_variety_value(name):
       value=0
       for variety in Variety:
          if name == variety.name:
              value=variety.value

       return value
