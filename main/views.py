from django.shortcuts import render

def show_anggota(request):
    anggota = [
        {
            "nama": "Farras Syafiq U",
            "npm": "2406495722",
            "jenis_kelamin": "Laki-laki"
        },
        {
            "nama": "Neal Guarddin",
            "npm": "2406348282",
            "jenis_kelamin": "Laki-laki"
        },
        {
            "nama": "Muhammad Fazil Tirtana",
            "npm": "2306274983",
            "jenis_kelamin": "Laki-laki"
        },
        {
            "nama": "Izzudin Abdul Rasyid",
            "npm": "2406495786",
            "jenis_kelamin": "Laki-laki"
        },
        {
            "nama": "Najwa Zarifa",
            "npm": "2306207796",
            "jenis_kelamin": "Perempuan"
        }
    ]

    font = request.GET.get('font', 'font-sans')
    warna = request.GET.get('warna', '#000000')

    context = {
        'anggota': anggota,
        'font': font,
        'warna': warna
    }

    return render(request, "main.html", context)