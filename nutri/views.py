from django.shortcuts import render


def main_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')
#
#
# def page_not_found_view(request):
#     return render(request, '404/404.html', status=404)
