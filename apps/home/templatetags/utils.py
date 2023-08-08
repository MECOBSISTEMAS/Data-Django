from django.template import Library
from django.utils.formats import number_format

register = Library()

@register.filter(name='custom_number_format')
def custom_number_format(value):
    # Substitui pontos por vírgulas e vice-versa
    value = value.replace(',', '|').replace('.', ',').replace('|', '.')

    return value
