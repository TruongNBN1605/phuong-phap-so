import sympy as sp
from tabulate import tabulate
from module import ProgramNoiSuyLagrange, ProgramHorner, ProgramNoiSuyNewton
from supporter import getPolynomialValue

""" Fake Data """
xCachDeu = [1.0, 2.0, 3.0, 4.0]
yCachDeu = [0.0, 1.0, 8.0, 27.0]

xKhongCachDeu = [1.0, 2.0, 3.0, 4.0, 6.0]
yKhongCachDeu = [0.0, 1.0, 8.0, 27.0, 216.0]


""" Các chương trình demo """
# HamLagrange, symbolic = ProgramNoiSuyLagrange(xCachDeu, yCachDeu)
# getPolynomialValue(HamLagrange, symbolic, 4)

# ProgramHorner([2, -3, 4, -5], 1, 3)

# HamXapXiCachDeu, symbolic = ProgramNoiSuyNewton(xCachDeu, yCachDeu, True)
# getPolynomialValue(HamXapXiCachDeu, symbolic, 4)
# HamXapXiKhongCachDeu, symbolic = ProgramNoiSuyNewton(xKhongCachDeu, yKhongCachDeu, False)
# getPolynomialValue(HamXapXiKhongCachDeu, symbolic, 6)

""" Nhập enter để kết thúc """
input()
