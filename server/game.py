import ctypes
import copy

class CoinBag(ctypes.Structure):
    _fields_ = [('coin1', ctypes.c_int),
                ('coin5', ctypes.c_int),
                ('coin10', ctypes.c_int),
                ('coin50', ctypes.c_int),
                ('coin100', ctypes.c_int),
                ('coin500', ctypes.c_int)]

class Game:
    def __init__(self):
        self.PointA = 0
        self.PointB = 0
        self.w = 8
        self.h = 8
        self.coin_map = [0 for i in range(self.w * self.h)]
        self.coinbag_A = CoinBag();
        self.coinbag_B = CoinBag();
        self.coinbag_A.coin1 = 5;
        self.coinbag_A.coin5 = 5;
        self.coinbag_A.coin10 = 5;
        self.coinbag_A.coin50 = 5;
        self.coinbag_A.coin100 = 5;
        self.coinbag_A.coin500 = 5;
        self.coinbag_B = copy.deepcopy(self.coinbag_A)

        self.setCoin('A',3,3,10)
        self.setCoin('B',3,4,10)
        self.setCoin('B',4,3,5)
        self.setCoin('A',4,4,1)

    def getCoin(self, x, y):
        if(x > 7 or y > 7 or x < 0 or y < 0):
            return 0 
        return self.coin_map[y * self.w + x]

    def isEnemyCoin(self,player, x, y):
        if(x > 7 or y > 7 or x < 0 or y < 0):
            return -1
        if(self.coin_map[y * self.w + x] == 0):
            return -1
        if(player == 'A'):
            return 1 if (self.coin_map[y * self.w + x] < 0) else 0
        elif(player == 'B'):
            return 1 if (self.coin_map[y * self.w + x] > 0) else 0
        return -1 

    def isExistCoin(self, x, y):
        if(x > 7 or y > 7 or x < 0 or y < 0):
            return -1
        return 1 if(self.coin_map[y * self.w + x] == 0) else 0

    def flipCoin(self,x,y):
        if(x > 7 or y > 7 or x < 0 or y < 0):
            return False
        self.coin_map[y * self.w + x] *= -1 

    def setCoin(self,player,x,y,coin):
        if(x > 7 or y > 7 or x < 0 or y < 0):
            return False
        if(player=='B'):
            coin *= -1; 
        self.coin_map[y * self.w + x] = coin

    def doJudge(self,player, x, y, coin):
        coin = abs(coin)
        if(player == 'A'):
            coinbag = self.coinbag_A
        else:
            coinbag = self.coinbag_B
        if(coin != 1 and coin != 5 and coin != 10 and coin != 50 and coin != 100 and coin != 500):
            print("no coin")
            return False
        if(coin == 1   & coinbag.coin1 == 0):return False 
        if(coin == 5   & coinbag.coin5 == 0):return False 
        if(coin == 10  & coinbag.coin10 == 0):return False 
        if(coin == 50  & coinbag.coin50 == 0):return False 
        if(coin == 100 & coinbag.coin100 == 0):return False 
        if(coin == 500 & coinbag.coin500 == 0):return False 
        if(self.countPointAction(player, x, y, coin, False) == 0):return False
        return True

    def countPointAction(self,player, x, y, coin, forceFlip = False):
        point = 0
        search_arrow = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0, -1), (1, -1)]
        if(x > 7 or y > 7 or x < 0 or y < 0):
            return 0
        for sa in search_arrow:
            countEnemy = 0
            nx = x
            ny = y
            nx += sa[0]
            ny += sa[1]
            while(self.isEnemyCoin(player, nx, ny) > 0):
                nx += sa[0]
                ny += sa[1]
                # enemy coin
                countEnemy += 1;
            if(self.isEnemyCoin(player, nx, ny) == 0):
                # ally coin
                mx = nx - sa[0]
                my = ny - sa[1]
                while(countEnemy>0):
                    if(forceFlip == True):
                        self.flipCoin(mx, my)
                    point += abs(self.getCoin(mx, my))
                    countEnemy -= 1
        return point

    def start(self):
        return 1;

    def doAction(self, player):
        tmp_coin_map = copy.deepcopy(self.coin_map)
        if(player == 'A'):
            coinbag = self.coinbag_A
            pointSum = self.PointA
        elif(player == 'B'):
            coinbag = self.coinbag_B
            pointSum = self.PointB
            i = 0
            for tmp_coin_map[i] in range(len(tmp_coin_map)):
                tmp_coin_map[i] *= -1
        else:
            return False

        next_x = ctypes.c_uint32(0)
        next_y = ctypes.c_uint32(0)
        next_coin = ctypes.c_int32(0)

        PATH_TO_LIB = "./autobot/libDyn/libDyn.so"
        libc = ctypes.CDLL(PATH_TO_LIB)
        Play = libc.Play
        Play.restype = ctypes.c_int
        Play.argtypes = (
                ctypes.POINTER(ctypes.c_int32),
                ctypes.c_uint32, 
                ctypes.c_uint32, 
                ctypes.POINTER(CoinBag), 
                ctypes.POINTER(ctypes.c_uint32), 
                ctypes.POINTER(ctypes.c_uint32),
                ctypes.POINTER(ctypes.c_int32))
        rtn = libc.Play(
                (ctypes.c_int * len(tmp_coin_map))(*tmp_coin_map),
                ctypes.c_uint32(self.h), 
                ctypes.c_uint32(self.w),
                ctypes.byref(coinbag),
                ctypes.byref(next_x),
                ctypes.byref(next_y),
                ctypes.byref(next_coin)
                )
        if(False == self.doJudge(player, next_x.value, next_y.value, next_coin.value)):
            print("Algorithm Judge Failed!")
            return False
        pointSum += self.countPointAction(player, next_x.value, next_y.value, next_coin.value, True)
        if(player == 'A'):
            self.PointA = pointSum
        elif(player == 'B'):
            self.PointB = pointSum
        return True

