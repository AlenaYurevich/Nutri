from django.shortcuts import render
from django.http import HttpResponse
from nutri.forms import BMIForm, ContactForm
from calc.imt import calculate_bmi
from django.core.mail import send_mail, BadHeaderError
from .models import Service  # Импортируем модель Service


def index(request):
    bmi_result = None
    contact_success = False
    bmi_form = BMIForm(request.POST if 'bmi_submit' in request.POST else None)
    contact_form = ContactForm()
    # Получаем все активные услуги с их пунктами
    services = Service.objects.filter(is_active=True).prefetch_related('items').order_by('order')
    # Обработка формы ИМТ
    if 'bmi_submit' in request.POST:
        bmi_form = BMIForm(request.POST)
        if bmi_form.is_valid():
            height = bmi_form.cleaned_data['height']
            weight = bmi_form.cleaned_data['weight']
            bmi_result = calculate_bmi(height, weight)

    # Обработка контактной формы
    elif 'contact_submit' in request.POST:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = 'Пробное сообщение'
            body = {'name': contact_form.cleaned_data['name'],
                    'email': contact_form.cleaned_data['email'],
                    'phone': contact_form.cleaned_data['phone'],
                    'message': contact_form.cleaned_data['message'],
                    }
            message = '\n'.join(body.values())
            print("Форма валидна! Данные:")
            print(f"Имя: {contact_form.cleaned_data['name']}")
            print(f"Телефон: {contact_form.cleaned_data['phone']}")
            print(f"Email: {contact_form.cleaned_data['email']}")
            print(f"Сообщение: {contact_form.cleaned_data['message']}")
            # Отправка email (пример)
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            print('Сообщение отправлено')
            contact_success = True
            contact_form = ContactForm()  # Очищаем форму после успешной отправки
            # Не валидна - форма сохранит ошибки
        else:
            print("Ошибки формы:", contact_form.errors)

    context = {
        'bmi_form': bmi_form,
        'bmi_result': bmi_result,
        'contact_form': contact_form,
        'contact_success': contact_success,
        'services': services,  # Добавляем услуги в контекст
    }
    return render(request, 'index.html', context)


def about_view(request):
    return render(request, 'about.html')


def handler404(request, exception):
    context = {'error_message': 'Страница не найдена'}
    return render(request, '404.html', context, status=404)


def handler500(request):
    context = {'error_message': 'Ошибка сервера'}
    return render(request, '500.html', context, status=500)

