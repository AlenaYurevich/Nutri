from django.shortcuts import render
from django.http import HttpResponse
from .forms import BMIForm, ContactForm
from calc.imt import calculate_bmi
from django.core.mail import send_mail


def index(request):
    bmi_result = None
    contact_success = False
    bmi_form = BMIForm(request.POST if 'bmi_submit' in request.POST else None)
    contact_form = ContactForm()
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
            # Сохранение данных и отправка email
            # contact = contact_form.save()
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            print("Форма валидна! Данные:")
            print(f"Имя: {contact_form.cleaned_data['name']}")
            print(f"Телефон: {contact_form.cleaned_data['phone']}")
            print(f"Email: {contact_form.cleaned_data['email']}")
            print(f"Сообщение: {contact_form.cleaned_data['message']}")
            # Отправка email (пример)
            send_mail(
                'Новая заявка с сайта',
                f'Имя: {name}\nТелефон: {phone}\nEmail: {phone}\nСообщение: {message}',
                'noreply@example.com',
                ['you@example.com'],
                fail_silently=False,
            )
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
    }
    return render(request, 'index.html', context)


def about_view(request):
    return render(request, 'about.html')
