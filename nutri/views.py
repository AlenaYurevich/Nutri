from django.shortcuts import render
from django.http import HttpResponse
from .forms import BMIForm, ContactForm
from calc.imt import calculate_bmi
from django.core.mail import send_mail


def index(request):
    bmi_result = None
    contact_success = False
    bmi_form = BMIForm()
    contact_form = ContactForm()
    # Обработка формы ИМТ
    if 'bmi_submit' in request.POST:
        bmi_form = BMIForm(request.POST)
        if bmi_form.is_valid():
            height = bmi_form.cleaned_data['height']
            weight = bmi_form.cleaned_data['weight']
            bmi_result = calculate_bmi(height, weight)
            # Не валидна - форма сохранит ошибки
        # else:
        #     bmi_form = BMIForm()
            # Обработка контактной формы
    elif 'contact_submit' in request.POST:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Сохранение данных и отправка email
            contact = contact_form.save()
            # Отправка email (пример)
            send_mail(
                'Новая заявка с сайта',
                f'Имя: {contact.name}\nТелефон: {contact.phone}\nСообщение: {contact.message}',
                'noreply@example.com',
                ['you@example.com'],
                fail_silently=False,
            )
            contact_success = True
            contact_form = ContactForm()  # Очищаем форму после успешной отправки
            # Не валидна - форма сохранит ошибки
        else:
            contact_form = ContactForm()
    context = {
        'bmi_form': bmi_form,
        'bmi_result': bmi_result,
        'contact_form': contact_form,
        'contact_success': contact_success,
    }
    return render(request, 'index.html', context)


def about_view(request):
    return render(request, 'about.html')
#
#
# def page_not_found_view(request):
#     return render(request, '404/404.html', status=404)
