
class des:
    def __init__(self):
        self.table1 = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
                       62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
                       57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,
                       61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
        self.table2 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,
                       10,2,59,51,43,35,27,19,11,3,60,52,44,36,
                       63,55,47,39,31,23,15,7,62,54,46,38,30,22,
                       14,6,61,53,45,37,29,21,13,5,28,20,12,4]
        self.table3 = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
        self.table4 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,
                        26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,
                        51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
        self.table5 = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,
                        12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,
                        22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
        self.table6 = [[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
                        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
                        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
                        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
                       [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
                        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
                        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
                        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
                       [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
                        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
                        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
                        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
                       [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
                        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
                        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
                        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
                       [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
                        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
                        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
                        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
                       [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
                        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
                        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
                        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
                       [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
                        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
                        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
                        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
                       [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
                        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
                        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
                        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]]
        self.table7 = [16,7,20,21,29,12,28,17,
                       1,15,23,26,5,18,31,10,
                        2,8,24,14,32,27,3,9,
                       19,13,30,6,22,11,4,25]
        self.table8 = [40,8,48,16,56,24,64,32,
                        39,7,47,15,55,23,63,31,
                        38,6,46,14,54,22,62,30,
                        37,5,45,13,53,21,61,29,
                        36,4,44,12,52,20,60,28,
                        35,3,43,11,51,19,59,27,
                        34,2,42,10,50,18,58,26,
                        33,1,41, 9,49,17,57,25]
    def int2bin(self, x, base):
        r1 = []
        for i in range(base):
            r1.append(x & 1)
            x >>= 1
        return r1
    def letter2bin(self, x, base):
        return self.int2bin(ord(x), base)
    def Input(self, DataValue, KeyValue):
        self.DATA64 = []
        for i in DataValue:
            self.DATA64.append(self.letter2bin(i, 64))
        temp1 = 0
        for i in KeyValue:
            temp1 <<= 8
            temp1 += ord(i)
        self.KEY64 = self.int2bin(temp1, 64)
    def generate_key(self):
        temp1 = []
        for i in range(56):
            temp1.append(self.KEY64[self.table2[i]-1])
        self.KEY56 = temp1
    def generate_16_key(self):
        temp1 = self.KEY56
        temp1.reverse()
        c = temp1[:28]
        d = temp1[28:]
        self._16_KEY48 = []
        for i in range(16):
            w1 = self.table3[i]
            cc = c[w1:]
            for j in range(w1):
                cc.append(c[j])
            dd = d[w1:]
            for j in range(w1):
                dd.append(d[j])
            ccdd = cc + dd
            ccdd.reverse()
            tt1 = []
            for k in range(48):
                tt1.append(ccdd[self.table4[k]-1])
            self._16_KEY48.append(tt1)
    def generate_16_key_2(self):
        temp1 = self.KEY56
        temp1.reverse()
        c = temp1[:28]
        d = temp1[28:]
        self._16_KEY48_2 = []
        for i in range(16):
            w1 = self.table3[i]
            cc = c[28 - w1:]
            for j in range(0, 28 - w1):
                cc.append(c[j])
            dd = d[28 - w1:]
            for j in range(0, 28 - w1):
                dd.append(d[j])
            ccdd = cc + dd
            ccdd.reverse()
            tt1 = []
            for k in range(48):
                tt1.append(ccdd[self.table4[k]-1])
            self._16_KEY48_2.append(tt1)
    def xor(self, a, b, base):
        t = []
        for i in range(base):
            t.append(a[i]^b[i])
        return t
    def mainProcess(self):
        self.LAST_DATA64 = []
        for LR in self.DATA64:
            for cn in range(16):
                t1 = []
                for i in range(48):
                    t1.append(LR[self.table5[i]-1])
                en_data = self.xor(t1, self._16_KEY48[cn], 48)
                en_data.reverse()
                en_data2 = []
                t2 = 0
                for i in range(8):
                    row = en_data[0] * 2 + en_data[5]
                    col = en_data[1] * 8 + en_data[2] * 4 + en_data[3] * 2 + en_data[4]
                    xx = self.table6[t2][row][col]
                    en_data2 += self.int2bin(xx, 4)
                    t2 += 1
                    en_data = en_data[6:]
                en_data2.reverse()
                s1 = []
                for i in range(32):
                    s1.append(en_data2[self.table7[i]-1])
                R = self.xor(LR[32:], s1, 32)
                L = LR[:32]
                LR = R + L
            t1 = []
            for i in range(64):
                t1.append(LR[self.table8[i]-1])
            self.LAST_DATA64.append(t1)
    def mainProcess2(self):
        self.LAST_DATA64_2 = []
        for LR in self.LAST_DATA64:
            for cn in range(15,-1,-1):
                t1 = []
                for i in range(48):
                    t1.append(LR[self.table5[i]-1])
                en_data = self.xor(t1, self._16_KEY48_2[cn], 48)
                en_data.reverse()
                en_data2 = []
                t2 = 0
                for i in range(8):
                    row = en_data[0] * 2 + en_data[5]
                    col = en_data[1] * 8 + en_data[2] * 4 + en_data[3] * 2 + en_data[4]
                    xx = self.table6[t2][row][col]
                    en_data2 += self.int2bin(xx, 4)
                    t2 += 1
                    en_data = en_data[6:]
                en_data2.reverse()
                s1 = []
                for i in range(32):
                    s1.append(en_data2[self.table7[i]-1])
                R = self.xor(LR[32:], s1, 32)
                L = LR[:32]
                LR = R + L
            t1 = []
            for i in range(64):
                t1.append(LR[self.table8[i]-1])
            self.LAST_DATA64_2.append(t1)
    def Output(self):
        for i in self.LAST_DATA64:
            x = 0
            for j in range(64):
                x <<= 1
                x += i[j]
            print x
    def Output2(self):
        for i in self.LAST_DATA64_2:
            print i
    def encryption(self, DataValue, KeyValue):
        self.Input(DataValue, KeyValue)
        self.generate_key()
        self.generate_16_key()
        self.mainProcess()
        self.Output()
    def decryption(self, ):
        for i in self.DATA64:
            print i
        print ''
        self.generate_16_key_2()
        self.mainProcess2()
        self.Output2()

test1 = des()
test1.encryption('HelloWorld', 'ycl')
test1.decryption()