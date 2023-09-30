import sympy as sp

""" ---------------------------------- Defined ----------------------------------  """
def hornerEvaluation(coefficients, x, c):
    """
    Sử dụng phương pháp Horner để đánh giá giá trị của đa thức tại điểm x.

    Args:
        coefficients: Danh sách các hệ số của đa thức, từ hệ số cao nhất đến hệ số tự do.
        x: Giá trị x mà bạn muốn đánh giá đa thức tại đó.
        c: Giá trị c trong đa thức Horner.

    Returns:
        Giá trị của đa thức tại x.
    """
    result = 0
    for coefficient in coefficients:
        result = result * (x - c) + coefficient
    return result

def hornerDivision(coefficients, x, c):
    """
    Thực hiện phép chia đa thức Horner Pn(x) cho (x - c).

    Args:
        coefficients: Danh sách các hệ số của đa thức, từ hệ số cao nhất đến hệ số tự do.
        x: Giá trị x mà bạn muốn đánh giá đa thức tại đó.
        c: Giá trị c trong đa thức Horner.

    Returns:
        Giá trị của Pn(x) / (x - c).
    """
    result = 0
    for coefficient in coefficients:
        result = result * (x - c) + coefficient
    return result

def hornerToPolynomial(coefficients, x, c):
    """
    Chuyển đa thức Horner Pn(x) thành dạng đa thức thông thường Pn(x).

    Args:
        coefficients: Danh sách các hệ số của đa thức Horner, từ hệ số cao nhất đến hệ số tự do.
        x: Giá trị x mà bạn muốn đánh giá đa thức tại đó.
        c: Giá trị c trong đa thức Horner.

    Returns:
        Giá trị của đa thức thông thường Pn(x).
    """
    n = len(coefficients)
    result = 0
    for i, coefficient in enumerate(coefficients):
        result += coefficient * (x - c)**(n - i - 1)
    return result

def derivativeAtPoint(coefficients, c, k):
    """
    Tính đạo hàm cấp k của đa thức Horner Pn(x) tại điểm c.

    Args:
        coefficients: Danh sách các hệ số của đa thức Horner, từ hệ số cao nhất đến hệ số tự do.
        c: Giá trị c trong đa thức Horner.
        k: Bậc của đạo hàm cần tính.

    Returns:
        Giá trị của đạo hàm cấp k của đa thức tại điểm c.
    """
    if k == 0:
        return hornerEvaluation(coefficients, c, c)
    else:
        # Tính đạo hàm bậc k
        derivative_coefficients = coefficients[:-k]  # Loại bỏ k hệ số cao nhất
        for i in range(k):
            derivative_coefficients = [coeff * (len(coefficients) - i - 1) for i, coeff in enumerate(derivative_coefficients)]
        return hornerEvaluation(derivative_coefficients, c, c)

""" ---------------------------------- Program ---------------------------------- """
def ProgramHorner(coefficients, c, k):
    """
    Thực hiện demo chương trình Horner.
    Args:
        coefficients: Danh sách các hệ số của đa thức, từ hệ số cao nhất đến hệ số tự do.
        c: Giá trị c trong đa thức Horner.
        k: Bậc của đạo hàm cần tính.
    Returns:
        Giá trị của đa thức tại x.
    """
    symbolic = sp.symbols('x')
    # 1. Đánh giá đa thức Pn(x) tại x
    result_evaluation = hornerEvaluation(coefficients, symbolic, c)
    print(f"Giá trị của đa thức Pn({symbolic}) là {result_evaluation}")

    # 2. Thực hiện phép chia Pn(x) cho (x - c)
    result_division = hornerDivision(coefficients, symbolic, c)
    print(f"Kết quả chia đa thức P({symbolic})) cho ({symbolic} - {c}) là {result_division}")

    # 3. Chuyển đa thức Horner thành đa thức thông thường
    result_to_polynomial = hornerToPolynomial(coefficients,symbolic, c)
    print(f"Đa thức thông thường tương ứng là {result_to_polynomial}")

    # 4. Tính đạo hàm cấp k tại điểm c
    k = 3
    result_derivative = derivativeAtPoint(coefficients, c, k)
    print(f"Đạo hàm cấp {k} tại điểm {c} là {result_derivative}")
