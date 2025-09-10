from django.shortcuts import render
from .forms import IdmtForm
from .imt import idmt, calculate_bmi


def idmt_view(request):
    if request.method == "POST":
        form = IdmtForm(request.POST)
        if form.is_valid():
            height = int(request.POST.get('height'))
            weight = int(request.POST.get('weight'))
            gender = int(request.POST.get('gender'))
            result_idmt = idmt(height, gender)
            result_bmi = calculate_bmi(height, weight)
            context = {'form': form, 'result_idmt': result_idmt, 'result_bmi': result_bmi,
                       'gender': gender,
                       }
            return render(request, 'calc.html', context)
    else:
        form = IdmtForm()
        return render(request, 'calc.html', {'form': form})  # внутри фигурных скобок
