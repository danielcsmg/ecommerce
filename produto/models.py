from django.db import models
from pathlib import Path
from django.conf import settings

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagem/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_procional = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples'),
        )
    )


    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = Path(settings.MEDIA_ROOT, img.name)
        img_pill = Image.open(img_full_path)
        original_width, original_heigth = img_pill.size
        print(original_heigth, original_width)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if imagem:
            self.resize_image(self.imagem, max_image_size)


    def __str__(self):
        return self.nome