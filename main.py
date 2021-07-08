# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import matplotlib.pyplot as plt
import scipy.special as st


def sigm(x, n):
    S = 0
    for i in range(len(x)):
        S += (x[i] ** 2) * n[i]
    return S


def mat(x, n):
    S = 0
    for i in range(len(x)):
        S += x[i] * n[i]
    return S


def show_hist(d, n):
    db = dict(zip(d, n))
    plt.bar(db.keys(), db.values(), color='g', alpha=0.5)
    plt.show()


class Gauss:
    __xi = []
    __epsi = []
    __N = 12
    __ai = []
    __ni = []
    __pi = []
    x2kr = 11.1
    x2b = 0
    N = 100

    def __init__(self, a, sgm):
        self.__epsi = self.randx(sgm, a)
        self.__ai = self.adx()
        self.__xi = self.newx(self.__ai)
        self.__ni = self.newn()

        xb = mat(self.__xi, self.__ni) / self.N
        sigmb = (sigm(self.__xi, self.__ni)- xb ** 2) / self.N

        self.__pi = self.newp(xb, sigmb, self.__ai)

        self.x2b = self.newx2b(self.__ni, self.__pi)
        show_hist(self.__xi, self.__ni)
        if self.x2b < self.x2kr:
            print("Yes")
        else:
            print("No")

    def randx(self, sgm, a):
        S = 0
        epsi_norm = []
        eps = []
        for i in range(100):
            for j in range(self.__N):
                self.__xi.append(random.random())
                S += self.__xi[j]
            self.__xi = []
            epsi_norm.append(S - 6)
            S = 0
            eps.append(sgm * epsi_norm[i] + a)
        return eps

    def adx(self):
        a = []
        h = (max(self.__epsi) - min(self.__epsi)) / 8
        self.__xi.sort()
        for i in range(self.__N):
            a.append(min(self.__epsi) + i * h)
        return a

    def newn(self):
        count = 0
        n = []
        for i in range(self.__N):
            for j in range(len(self.__epsi)):
                if self.__ai[i - 1] <= self.__epsi[j] < self.__ai[i]:
                    count += 1
            n.append(count)
            count = 0
        return n

    @staticmethod
    def newp(xb, sigmb, a):

        p = []
        for i in range(len(a)):
            p.append(
                st.erf((a[i] - xb) / (sigmb ** 2)) - st.erf((a[i - 1] - xb) / (sigmb ** 2)))
        return p

    @staticmethod
    def newx(a):
        x = []
        for i in range(len(a)):
            x.append((a[i - 1] + a[i]) / 2)
        return x

    def newx2b(self, n, p):
        x2 = 0
        for i in range(len(n)):
            x2 += ((n[i]-self.N * p[i])**2)/self.N*p[i]
        return x2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gs = Gauss(5, 3)
