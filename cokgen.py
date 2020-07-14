"""by kaankilic"""

from __future__ import print_function, division

import math
import turtle

def kare(t, u):
    """Verilen uzunlukta kare çizer, turtle ilk pozisyonuna döner.
    """
    for i in range(4):
        t.fd(u)
        t.lt(90)


def coklucizgi(t, n, u, a):
    """N tane çizgi çizer.
    t: Turtle objesi,
    n: çizilecek çizgi adedi,
    u: uzunluk,
    a: açı.
    """

    for i in range(n):
        t.fd(u)
        t.lt(a)


def cokgen(t, n, u):
    """N köşeli Çokgen çizer.
    t: Turtle,
    n: köşe sayısı
    u: uzunluk
    """
    a = 360.0/n
    coklucizgi(t, n, u, a)

def yay(t, r, a):
    """Verilen çap ve açı ile yay çizer.
    t: Turtle
    r: çap
    a: açı
    """

    yay_u = 2 * math.pi * r * abs(a) / 360
    n = int(yay_u / 4) + 3
    step_u = yay_u / n
    step_a = float(a) / n
    t.lt(step_a/2)
    coklucizgi(t, n, step_u, step_a)
    t.rt(step_a/2)

def cember(t, r):
    """verilen çapta çember çizer.
    t: Turtle
    r: çap
    """
    yay(t, r, 360)


if __name__ == '__main__':
    oogway = turtle.Turtle()

    #merkezde çember çiz
    cembercap = 100
    oogway.pu()
    oogway.fd(cembercap)
    oogway.lt(90)
    oogway.pd()
    cember(oogway, cembercap)

    #kullanıcı pencereyi kapatana kadar bekle
    turtle.mainloop()
