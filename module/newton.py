from supporter import drawPolynomial
import sympy as sp
import pandas as pd
from tabulate import tabulate

""" ---------------------------------- Defined ----------------------------------  """
def taoBangTiSaiPhanCachDeu(xValues, yValues):
    """
    Tính các tỉ sai phân cho các mốc cách đều.
    Args:
        yValues: Danh sách các giá trị x (các điểm dữ liệu đã biết, cách đều).
        yValues: Danh sách các giá trị y (giá trị của hàm tại các điểm đã biết).
    Returns:
        Ma trận các tỉ sai phân.
    """
    n = len(xValues)
    divided_diff = [[0] * n for _ in range(n)]
    for i in range(n):
        divided_diff[i][0] = yValues[i]

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (xValues[i + j] - xValues[i])

    return divided_diff

def taoBangTiSaiPhanKhongCachDeu(xValues, yValues):
    """
    Tính các tỉ sai phân cho các mốc không cách đều.
    Args:
        xValues: Danh sách các giá trị x (các điểm dữ liệu đã biết, không cách đều).
        yValues: Danh sách các giá trị y (giá trị của hàm tại các điểm đã biết).
    Returns:
        Ma trận các tỉ sai phân.
    """
    n = len(xValues)
    divided_diff = [[0] * n for _ in range(n)]
    for i in range(n):
        divided_diff[i][0] = yValues[i]

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (xValues[i + j] - xValues[i])

    return divided_diff

def NoiSuyNewTon(xValues, yValues, x, equallySpaced=True):
    """
    Thực hiện nội suy Newton-Gregory để tính giá trị xấp xỉ của hàm tại điểm x.
    Args:
        xValues: Danh sách các giá trị x (các điểm dữ liệu đã biết).
        yValues: Danh sách các giá trị y (giá trị của hàm tại các điểm đã biết).
        x: Giá trị x mà bạn muốn tính giá trị xấp xỉ của hàm tại đó.
        equallySpaced: True nếu các mốc cách đều, False nếu không cách đều.
    Returns:
        Giá trị xấp xỉ của hàm tại x và bảng tỉ sai phân (nếu được yêu cầu).
    """
    n = len(xValues)
    if equallySpaced:
        divided_diff = taoBangTiSaiPhanCachDeu(xValues, yValues)
    else:
        divided_diff = taoBangTiSaiPhanKhongCachDeu(xValues, yValues)
    
    result = divided_diff[0][0]
    product_term = 1

    # table_data = []  # Dữ liệu cho bảng tỉ sai phân
    for i in range(n):
        # row = [f'f[x{i}]']
        # for j in range(n - i):
        #     row.append(divided_diff[i][j])
        # table_data.append(row)

        if i < n - 1:
            product_term *= (x - xValues[i])
            result += divided_diff[0][i + 1] * product_term
    
    # df = pd.DataFrame(table_data, columns=[f'x{i}' for i in range(n + 1)])
    
    return result# , df

""" ---------------------------------- Program ---------------------------------- """
def ProgramNoiSuyNewton(xKnown, yKnown, equallySpaced=True):
    """
    Thực hiện demo chương trình nội suy Newton.
    Args:
        xKnown: Danh sách các giá trị x đã biết.
        yKnown: Danh sách các giá trị f(x) đã biết tương ứng với x.
        equallySpaced: True nếu các mốc cách đều, False nếu không cách đều.
    Returns:
        Hàm xấp xỉ và tên biến
    """
    symbolic = sp.symbols('x')
    HamXapXiNewton, BangTiSaiPhan = NoiSuyNewTon(xKnown, yKnown, symbolic, equallySpaced)
    # HamRutGon = sp.simplify(HamXapXiNewton)
    # Bảng tỉ sai phân
    # print("Bảng tỉ sai phân:")
    # print(tabulate(BangTiSaiPhan, headers='keys', tablefmt='psql'))

    # In đa thức kết quả
    # print("Đa thức kết quả:")
    # sp.pprint(HamRutGon, use_unicode=True)

    # Vẽ đồ thị hàm đã biết và đa thức kết quả
    # drawPolynomial(HamRutGon, symbolic, xKnown, yKnown)

    return HamXapXiNewton, symbolic
