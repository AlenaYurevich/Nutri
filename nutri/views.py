from django.shortcuts import render
from .forms import ImtForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from calc.imt import calculate_bmi


def main_view(request):
    if request.method == "POST":
        form = ImtForm(request.POST)
        # form2 = ContactForm(request.POST)
        if form.is_valid():
            height = int(request.POST.get('height'))
            weight = float(request.POST.get('weight'))
            result = calculate_bmi(height, weight)
            context = {'form': form, 'result': result}
            return render(request, 'index.html', context)
        # if form2.is_valid():
        #     subject = 'Пробное сообщение'
        #     body = {'name': form2.cleaned_data['name'],
        #             'email': form2.cleaned_data['email'],
        #             'phone': form2.cleaned_data['phone'],
        #             'message': form2.cleaned_data['message'],
        #             }
        #     message = '\n'.join(body.values())
        #     try:
        #         send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
        #     except BadHeaderError:
        #         return HttpResponse('Найден некорректный заголовок')
        #     print('Сообщение отправлено')
    else:
        form = ImtForm()
        form2 = ContactForm
        return render(request, 'index.html', {'form': form})  # внутри фигурных скобок


def about_view(request):
    return render(request, 'about.html')
#
#
# def page_not_found_view(request):
#     return render(request, '404/404.html', status=404)
