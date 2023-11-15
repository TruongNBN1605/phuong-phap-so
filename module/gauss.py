import numpy as np
import sympy as sp
import math
import pandas as pd
from tabulate import tabulate
from supporter import drawPolynomial

""" ---------------------------------- Defined ----------------------------------  """
def taoBangTiSaiPhan(xValues, yValues, forward=True):
    """
    Tính các tỉ sai phân tiến.
    Args:
        yValues: Danh sách các giá trị x (các điểm dữ liệu đã biết, cách đều).
        yValues: Danh sách các giá trị y (giá trị của hàm tại các điểm đã biết).
        forward: True nếu tính tỉ sai phân tiến, False nếu tính tỉ sai phân lùi.
    Returns:
        Ma trận các tỉ sai phân.
    """
    n = len(xValues)
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = yValues
    
    for j in range(1, n):
        for i in range(n - j):
            if forward:
                divided_diff[i][j] = divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]
            else:
                divided_diff[i][j] = divided_diff[i][j - 1] - divided_diff[i + 1][j - 1]
    
    return divided_diff

def NoiSuyGauss(xValues, yValues, x, forward=True):
    """
    Tính các tỉ sai phân tiến.
    Args:
        yValues: Danh sách các giá trị x (các điểm dữ liệu đã biết, cách đều).
        yValues: Danh sách các giá trị y (giá trị của hàm tại các điểm đã biết).
        x: Giá trị x mà bạn muốn tính giá trị xấp xỉ của hàm tại đó.
        forward: True nếu tính tỉ sai phân tiến, False nếu tính tỉ sai phân lùi.
    Returns:
        Ma trận các tỉ sai phân.
    """
    BangTiSaiPhan = taoBangTiSaiPhan(xValues, yValues, forward)
    n = len(xValues)

    # Xử lý dữ liệu bảng tỉ sai phân
    # data = [[xValues[i]] + [BangTiSaiPhan[i][j] for j in range(n - i)] for i in range(n)]
    # df = pd.DataFrame(data, columns=[f'x'] + [f'Δ^{i}y' for i in range(n)])

    start = 0 if forward else n - 1 
    result = yValues[start]
    u = (x - xValues[start]) / (xValues[1] - xValues[0])
    
    for i in range(1, n):
        result += (u * BangTiSaiPhan[start][i]) / (math.factorial(i)) 
        u *= (u + (-1 if forward else 1 )) / i
    
    return result# , df

""" ---------------------------------- Program ---------------------------------- """
def ProgramNoiSuyGauss(xKnown, yKnown, forward=True):
    """
    Thực hiện demo chương trình nội suy Newton.
    Args:
        xKnown: Danh sách các giá trị x đã biết.
        yKnown: Danh sách các giá trị f(x) đã biết tương ứng với x.
        forward: True nếu tính tỉ sai phân tiến, False nếu tính tỉ sai phân lùi.
    Returns:
        Hàm xấp xỉ và tên biến
    """
    # Example usage:
    symbolic = sp.symbols('x')

    HamXapXiGauss, BangTiSaiPhan = NoiSuyGauss(xKnown, yKnown, symbolic, forward)
    # HamRutGon = sp.simplify(HamXapXiGauss)

    # Bảng tỉ sai phân
    # print("Bảng tỉ sai phân:")
    # print(tabulate(BangTiSaiPhan, headers = "keys", tablefmt="psql", showindex=False))

    # In đa thức kết quả
    # print("Đa thức kết quả:")
    # sp.pprint(HamRutGon, use_unicode=True)

    # Vẽ đồ thị hàm đã biết và đa thức kết quả
    # drawPolynomial(HamRutGon, symbolic, xKnown, yKnown)

    return HamXapXiGauss, symbolic
