import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pkpl_tk2.settings')
django.setup()

from main.models import Biodata
from django.contrib.sites.models import Site

print("Clearing Biodata...")
Biodata.objects.all().delete()

members = [
    {"nama": "Farras Syafiq Ulumuddin", "NPM": 2406495722, "jenis_kelamin": "Laki-laki", "email": "aunknown145@gmail.com"},
    {"nama": "Neal Guarddin", "NPM": 2406348282, "jenis_kelamin": "Laki-laki", "email": "guarddin29@gmail.com"},
    {"nama": "Muhammad Fazil Tirtana", "NPM": 2306274983, "jenis_kelamin": "Laki-laki", "email": "fazil@ristek.cs.ui.ac.id"},
    {"nama": "Izzudin Abdul Rasyid", "NPM": 2406495786, "jenis_kelamin": "Laki-laki", "email": "izzudin@example.com"},
    {"nama": "Najwa Zarifa", "NPM": 2306207796, "jenis_kelamin": "Perempuan", "email": "najwa@example.com"},
]

for m in members:
    Biodata.objects.create(**m)
print("Seeded Biodata.")

site, _ = Site.objects.get_or_create(id=1)
site.domain = 'localhost:8000'
site.name = 'PKPL TK 2'
site.save()
print("Configured Site ID 1.")
