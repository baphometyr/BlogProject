# python
from datetime import timedelta, datetime
# django
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
# apps teceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
# Manager
from .managers import EntryManager

class Category(TimeStampedModel):
    """ Modelo de categorias para una entrada de blog """
    short_name = models.CharField('Nombre corto', max_length=15, unique=True)
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.short_name

class Tag(TimeStampedModel):
    """ Etiquetas de las entradas de blog """
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Entry(TimeStampedModel):
    """ Modelo para entradas o articulos del blog """

    # Llaves foraneas
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    title = models.CharField('Titulo', max_length=200)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField('Imagen', upload_to='Entry')
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    # slug
    slug = models.SlugField(editable=False, max_length=300)
    # manager
    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        now = datetime.now()
        total_time = timedelta(
            hours = now.hour,
            minutes = now.minute,
            seconds = now.second
        )

        seconds = int(total_time.total_seconds())

        slug = f"{self.title}-{seconds}"
        self.slug = slugify(slug)

        super(Entry, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse_lazy("entrada_app:entry_detail", kwargs={"slug": self.slug})
    
