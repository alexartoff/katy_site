from django.db import models
from django.urls import reverse


class MainMenu(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('main_index', kwargs={'menu_slug': self.slug})

    class Meta:
        ordering = ['pk']
