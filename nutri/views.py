from django.shortcuts import render
from calc.forms import ImtForm
from calc.imt import calculate_bmi


def main_view(request):
    if request.method == "POST":
        form = ImtForm(request.POST)
        if form.is_valid():
            height = int(request.POST.get('height'))
            weight = float(request.POST.get('weight'))
            result = calculate_bmi(height, weight)
            context = {'form': form, 'result': result}
            return render(request, 'index.html', context)
    else:
        form = ImtForm()
        return render(request, 'index.html', {'form': form})  # внутри фигурных скобок


def about_view(request):
    return render(request, 'about.html')
#
#
# def page_not_found_view(request):
#     return render(request, '404/404.html', status=404)
