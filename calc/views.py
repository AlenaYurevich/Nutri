from django.shortcuts import render
from .forms import ImtForm
from .imt import idmt


def calculation_view(request):
    if request.method == "POST":
        form = ImtForm(request.POST)
        if form.is_valid():
            height = int(request.POST.get('height'))
            gender = int(request.POST.get('gender'))
            result = idmt(height, gender)
            context = {'form': form, 'result': result,
                       'gender': gender,
                       }
            return render(request, 'calc.html', context)
    else:
        form = ImtForm()
        return render(request, 'calc.html', {'form': form})  # внутри фигурных скобок
