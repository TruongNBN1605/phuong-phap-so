import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def drawPolynomial(polynomial, symbolic, xKnown, yKnown, count=100, xlabel='x', ylabel="f(x)"):
    """
    Vẽ đồ thị của đa thức.
    Args:
        polynomial: Biểu thức đa thức (phải là biểu thức sympy).
        symbolic: Biến ký hiệu trong biểu thức (phải là biến sympy).
        xKnown: Mảng các điểm đã biết.
        yKnown: Mảng giá trị đa thức tại các điểm đã biết.
        count: Số điểm được tạo trên đồ thị.
        xlabel: Mô tả trục hoành.
        ylabel: Mô tả trục hoành.
    Returns:
        None.
    """
    # Tạo mảng chứa các giá trị x trong khoảng
    start = xKnown[0]
    end = xKnown[-1]
    xValues = np.linspace(start, end, count)

    # Tính giá trị tương ứng của đa thức cho từng giá trị x
    xApproximate = sp.lambdify(symbolic, polynomial, 'numpy')
    yValues = xApproximate(xValues)

    # Vẽ đồ thị
    plt.plot(xKnown, yKnown, 'o', label='Dữ liệu đã biết')
    plt.plot(xValues, yValues, label=f'{ylabel} = {sp.latex(polynomial)}', linewidth=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f'Đồ thị của đa thức {ylabel} = {sp.latex(polynomial)}')
    plt.legend()
    plt.grid(True)
    plt.ioff()
    plt.show(block=False)

def getPolynomialValue(polynomial, symbolic, symbolicValue, showResult=True):
    """
    Vẽ đồ thị của đa thức.
    Args:
        polynomial: Biểu thức đa thức (phải là biểu thức sympy).
        symbolic: Biến ký hiệu trong biểu thức (phải là biến sympy).
        symbolicValue: Giá trị biến cần tính.
        showResult: True nếu hiển thị kết quả lên màn hình (terminal), False nếu không
    Returns:
        Kết quả giá trị hàm tại biến cung cấp.
    """
    # Tạo mảng chứa các giá trị x trong khoảng
    rs = polynomial.subs(symbolic, symbolicValue).evalf()
    if showResult:
        print(f'Giá trị của hàm: F({symbolicValue}) = {rs}')
    return rs