from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406352304',
        'name': 'Afero Aqil Roihan',
        'class': 'PBP D '
    }

    return render(request, "main.html", context)
