from django import template
from num2fa import numbers, ordinal_words, words

register = template.Library()


@register.filter(name="fa_numbers")
def farsi_numbers(value):
    return numbers(value)


@register.filter(name="fa_words")
def farsi_words(value):
    return words(value)


@register.filter(name="fa_ordinal_words")
def farsi_ordinal_words(value):
    return ordinal_words(value)
