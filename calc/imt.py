import math
# from .sheets import sheet1, sheet2
# from .vat import vat
# from .round_as_excel import round_as_excel
# from .format import formatted


def idmt(height, gender):
    if height <= 200:
        if gender == 1:
            result = height - 100 - (height - 152) * 0.4
        else:
            result = height - 100 - (height - 152) * 0.2
        return f'Ваша идеальная масса тела {result} кг'
    else:
        return f'Максимальный рост 200 см'
