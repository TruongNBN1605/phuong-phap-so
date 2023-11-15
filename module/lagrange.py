from supporter import drawPolynomial
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

""" ---------------------------------- Defined ----------------------------------  """
def NoiSuyLagrange(xValues, yValues, symbolic=sp.symbols('x')):
    """
    Thực hiện nội suy Lagrange để tính giá trị của hàm tại điểm x.
    Args:
        xValues: Danh sách các giá trị x đã biết.
        yValues: Danh sách các giá trị f(x) đã biết tương ứng với x.
        symbolic: Giá trị x (hoặc biến x) mà bạn muốn tính f(x) ở đó.
    Returns:
        Giá trị f(x) được tính bằng nội suy Lagrange.
    """
    n = len(xValues)
    result = 0.0
    for i in range(n):
        term = yValues[i]
        for j in range(n):
            if j != i:
                term *= (symbolic - xValues[j]) / (xValues[i] - xValues[j])
        result += term
    return result

""" ---------------------------------- Program ---------------------------------- """
def ProgramNoiSuyLagrange(xKnown, yKnown):
    """
    Thực hiện demo chương trình nội suy Lagrange.
    Args:
        xKnown: Danh sách các giá trị x đã biết.
        yKnown: Danh sách các giá trị f(x) đã biết tương ứng với x.
    Returns:
        Hàm xấp xỉ và tên biến
    """
    # Tạo biến ký hiệu cho x
    symbolic = sp.symbols('x')

    # Thực hiện nội suy Lagrange và đưa ra đa thức kết quả
    HamSapxiLagrange = NoiSuyLagrange(xKnown, yKnown, symbolic)
    # HamRutGon = sp.simplify(HamSapxiLagrange)

    # In đa thức kết quả
    # print("Đa thức kết quả:")
    # sp.pprint(HamRutGon, use_unicode=True)

    # Vẽ đồ thị hàm đã biết và đa thức kết quả
    # drawPolynomial(HamRutGon, symbolic, xKnown, yKnown)
    return HamSapxiLagrange, symbolic
