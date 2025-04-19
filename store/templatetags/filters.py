from atexit import register
from django import template
from store.models import File

register = template.Library()


@register.filter(name='get_first_image')
def get_first_image(product):
    imagem = File.objects.filter(product=product).first()
    print(imagem.image.url)
    if imagem:
        return imagem.image.url
    else:
        return False
