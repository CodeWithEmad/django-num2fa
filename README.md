# Django Num2Fa

[![PyPI releases](https://img.shields.io/pypi/v/django-num2fa?logo=python&logoColor=white)](https://pypi.python.org/pypi/django-num2fa)
[![License](https://img.shields.io/github/license/codewithemad/django-num2fa.svg?style=flat-square)](https://opensource.org/license/agpl-v3/)

`django-num2fa` is a wrapper around [num2fa](https://github.com/codewithemad/num2fa) package which provides a set of filters to convert numbers to Persian numbers and words.

## Installation

```bash
pip install -U django-num2fa
```

That's it!

## Usage

First, add `django_num2fa` inside your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_num2fa',
    # other packages
]
```

load `num2fa` inside your template:

```jinja
{% load num2fa %}
```

then, wherever you have a number in your code template, pipe it with one of the `fa_numbers`, `fa_words`, and `fa_ordinal_words` template filters.

```jinja
{% load num2fa %}

{{ number | fa_numbers }}
{{ number | fa_words }}
{{ number | fa_ordinal_words }}
```

## Contributing

We welcome contributions! To learn how you can contribute, please check the [Contributing](https://github.com/codewithemad/django-num2fa/blob/master/docs/Contributing.md) document.

## License

This work is licensed under the terms of the [GNU Affero General Public License (AGPL)](https://github.com/codewithemad/django-num2fa/blob/master/LICENSE.txt).
