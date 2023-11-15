import sympy as sp
from tabulate import tabulate
from module import ProgramNoiSuyLagrange, ProgramHorner, ProgramNoiSuyNewton, ProgramNoiSuyGauss
from supporter import getPolynomialValue
from data.getData import getDataFromExcel

""" Get Data """
fileName = "0"
filePath = "data/"
xValues, yValues, x = getDataFromExcel(fileName, filePath)

""" Các chương trình demo """
# HamLagrange, symbolic = ProgramNoiSuyLagrange(xValues[:5], yValues[:5])
# getPolynomialValue(HamLagrange, symbolic, 4)

# ProgramHorner([2, -3, 4, -5], 1, 3)

# HamNewtonCachDeu, symbolic = ProgramNoiSuyNewton(xValues, yValues, True)
# getPolynomialValue(HamNewtonCachDeu, symbolic, 4)
# HamNewtonKhongCachDeu, symbolic = ProgramNoiSuyNewton(xValues, yValues, False)
# getPolynomialValue(HamNewtonKhongCachDeu, symbolic, 6)

HamGauss, symbolic = ProgramNoiSuyGauss(xValues[:5], yValues[:5], True)
getPolynomialValue(HamGauss, symbolic, x)

""" Nhập enter để kết thúc """
input()
