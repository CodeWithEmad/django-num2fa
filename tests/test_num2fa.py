import pytest
from django.template import Context, Template
from num2fa import numbers, ordinal_words, words


@pytest.fixture(
    params=[
        (1984, numbers(1984)),
        (456, numbers(456)),
        (789, numbers(789)),
    ]
)
def fa_numbers(request):
    return request.param


@pytest.fixture(
    params=[
        (1984, words(1984)),
        (456, words(456)),
        (789, words(789)),
    ]
)
def fa_words(request):
    return request.param


@pytest.fixture(
    params=[
        (1984, ordinal_words(1984)),
        (456, ordinal_words(456)),
        (789, ordinal_words(789)),
    ]
)
def fa_ordinal_words(request):
    return request.param


# Test each filter
def test_fa_numbers(fa_numbers):
    t = Template("{% load num2fa %}{{ value|fa_numbers }}")
    value, expected = fa_numbers
    c = Context({"value": value})
    assert t.render(c) == expected


def test_fa_words(fa_words):
    t = Template("{% load num2fa %}{{ value|fa_words }}")
    value, expected = fa_words
    c = Context({"value": value})
    assert t.render(c) == expected


def test_fa_ordinal_words(fa_ordinal_words):
    t = Template("{% load num2fa %}{{ value|fa_ordinal_words }}")
    value, expected = fa_ordinal_words
    c = Context({"value": value})
    assert t.render(c) == expected
