from django.shortcuts import render
from .forms import IdmtForm
from .imt import idmt, calculate_bmi, energy


def idmt_view(request):
    if request.method == "POST":
        form = IdmtForm(request.POST)
        if form.is_valid():
            height = int(request.POST.get('height'))
            weight = int(request.POST.get('weight'))
            gender = int(request.POST.get('gender'))
            age = int(request.POST.get('age'))
            activity = float(request.POST.get('activity'))
            result_idmt = idmt(height, gender)
            bmi_result = calculate_bmi(height, weight)
            result_energy = energy(height, weight, age, gender, activity)
            context = {'form': form, 'result_idmt': result_idmt, 'bmi_result': bmi_result,
                       'result_energy': result_energy,
                       }
            return render(request, 'calc.html', context)
    else:
        form = IdmtForm()
        return render(request, 'calc.html', {'form': form})  # внутри фигурных скобок
