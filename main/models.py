from django.db import models


class Biodata(models.Model):
    nama = models.CharField(max_length=255)
    NPM = models.IntegerField()
    jenis_kelamin = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.nama


class SiteSetting(models.Model):
    FONT_CHOICES = [
        ("font-sans", "Sans"),
        ("font-serif", "Serif"),
        ("font-mono", "Mono"),
    ]

    background_color = models.CharField(max_length=7, default="#f3f4f6")
    text_color = models.CharField(max_length=7, default="#000000")
    font_family = models.CharField(
        max_length=20, choices=FONT_CHOICES, default="font-sans"
    )

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"
