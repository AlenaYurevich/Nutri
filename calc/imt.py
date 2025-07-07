# import math
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


def calculate_bmi(height: int, weight: float) -> list[dict]:
    """
    Рассчитывает индекс массы тела (ИМТ) и возвращает классификацию результата.

    Args:
        height: Рост в сантиметрах
        weight: Вес в килограммах

    Returns:
        Список словарей с результатами расчета и классификацией
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Рост и вес должны быть положительными числами")

    height_in_meters = height / 100
    bmi = round(weight / (height_in_meters ** 2), 1)
    classification = get_bmi_classification(bmi)

    return [{
        'description': 'Ваш индекс массы тела составляет',
        'bmi': bmi,
        'classification': classification,
        'advice': get_bmi_advice(bmi)
    }]


def get_bmi_classification(bmi: float) -> str:
    """Возвращает текстовую классификацию ИМТ."""
    if bmi < 16:
        return 'Выраженный дефицит массы тела'
    elif 16 <= bmi < 18.5:
        return 'Недостаточная масса тела'
    elif 18.5 <= bmi < 25:
        return 'Нормальная масса тела'
    elif 25 <= bmi < 30:
        return 'Избыточная масса тела (предожирение)'
    elif 30 <= bmi < 35:
        return 'Ожирение первой степени'
    elif 35 <= bmi < 40:
        return 'Ожирение второй степени'
    else:
        return 'Ожирение третьей степени (морбидное)'


def get_bmi_advice(bmi: float) -> str:
    """Возвращает рекомендацию на основе ИМТ."""
    if bmi < 18.5:
        return 'Рекомендуется повысить калорийность питания'
    elif 18.5 <= bmi < 25:
        return 'Ваш вес в норме, продолжайте в том же духе!'
    elif 25 <= bmi < 30:
        return 'Рекомендуется умеренная физическая активность'
    else:
        return 'Рекомендуется консультация специалиста для разработки плана коррекции веса'
