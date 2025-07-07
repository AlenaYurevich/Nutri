from django.shortcuts import render
from .forms import IdmtForm
from .imt import idmt


def idmt_view(request):
    if request.method == "POST":
        form = IdmtForm(request.POST)
        if form.is_valid():
            height = int(request.POST.get('height'))
            gender = int(request.POST.get('gender'))
            result_idmt = idmt(height, gender)
            context = {'form': form, 'result': result_idmt,
                       'gender': gender,
                       }
            return render(request, 'calc.html', context)
    else:
        form = IdmtForm()
        return render(request, 'calc.html', {'form': form})  # внутри фигурных скобок
