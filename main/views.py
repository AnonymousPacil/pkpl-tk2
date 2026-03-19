from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306207796',
        'nama': 'Najwa Zarifa',
        'jenis_kelamin': 'Perempuan'
    }

    return render(request, "main.html", context)