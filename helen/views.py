from django.shortcuts import render
from django.http import HttpResponse
from nutri.forms import BMIForm, ContactForm
from calc.imt import calculate_bmi
from blog.models import Post
from django.core.mail import send_mail
from .models import Service  # Импортируем модель Service


def handle_forms(request):
    """Обработка обеих форм"""
    context = {
        'bmi_form': BMIForm(),
        'contact_form': ContactForm(),
        'bmi_result': None,
        'contact_success': False,
        'contact_errors': None,
    }

    # Обработка ИМТ
    if 'bmi_submit' in request.POST:
        bmi_form = BMIForm(request.POST)
        if bmi_form.is_valid():
            height = bmi_form.cleaned_data['height']
            weight = bmi_form.cleaned_data['weight']
            context['bmi_result'] = calculate_bmi(height, weight)
        context['bmi_form'] = bmi_form

    # Обработка контактов
    if 'contact_submit' in request.POST:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # try:
            #     # Отправка email
            #     subject = 'Новое сообщение с сайта'
            #     body = f"""
            #         Имя: {contact_form.cleaned_data['name']}
            #         Email: {contact_form.cleaned_data['email']}
            #         Телефон: {contact_form.cleaned_data['phone']}
            #         Сообщение: {contact_form.cleaned_data['message']}
            #         """
            #
            #     send_mail(
            #         subject,
            #         body,
            #         DEFAULT_FROM_EMAIL,  # из settings.py
            #         ['admin@yourdomain.com'],  # куда отправлять
            #         fail_silently=False,
            #     )
            print("=" * 50)
            print("ФОРМА ОТПРАВЛЕНА (тестовый режим):")
            print(f"Имя: {contact_form.cleaned_data['name']}")
            print(f"Email: {contact_form.cleaned_data['email']}")
            print(f"Телефон: {contact_form.cleaned_data['phone']}")
            print(f"Сообщение: {contact_form.cleaned_data['message']}")
            print("=" * 50)

            context['contact_success'] = True
            context['contact_form'] = ContactForm()  # очищаем форму
        else:
            context['contact_form'] = contact_form
            context['contact_errors'] = "Пожалуйста, проверьте заполнение формы."

    return context


def index(request):
    forms_context = handle_forms(request)
    services = Service.objects.filter(is_active=True)
    posts = Post.objects.order_by('order')[:3]
    context = {
        **forms_context,
        'services': services,  # Добавляем услуги в контекст
        "posts": posts,
    }
    return render(request, 'index.html', context)


def about(request):
    forms_context = handle_forms(request)
    context = {
        **forms_context,
    }
    return render(request, 'about.html', context)


def services(request):
    forms_context = handle_forms(request)
    services = Service.objects.filter(is_active=True)
    context = {
        'services': services,
        **forms_context,
    }
    return render(request, 'services.html', context)


def handler404(request, exception):
    context = {'error_message': 'Страница не найдена'}
    return render(request, '404.html', context, status=404)


def handler500(request):
    context = {'error_message': 'Ошибка сервера'}
    return render(request, '500.html', context, status=500)
