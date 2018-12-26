from django.conf import settings
from django.conf.urls import url
from django.core.cache import cache
from django.shortcuts import redirect, render

from random import choice
from string import ascii_letters
from urllib.parse import urlparse


# Задание 3. URL shortener
#
# Реализуйте сервис для сокращения ссылок. Примеры таких сервисов:
# http://bit.ly, http://t.co, http://goo.gl
# Пример ссылки: http://bit.ly/1qJYR0y
#
# Вам понадобится шаблон с формой для отправки ссылки (файл index.html),
# и две функции, одна для обработки запросов GET и POST для сабмита URL
# и отображения результата, и вторая для редиректа с короткого URL на исходный.
# Для хранения соответствий наших коротких ключей и полных URL мы будем
# использовать кеш Django, django.core.cache
# Экземпляр cache уже импортирован, и используется следующим образом.
# Сохранить значение:
#
#  cache.add(key, value)
#
# Извлечь значение:
#
#  cache.get(key, default_value)
#
# Второй аргумент метода get - значение по умолчанию,
# если ключ не найден в кеше.
#
# Вы можете запустить сервер для разработки, и посмотреть
# ответы ваших функций в браузере:
#
# python homework03.py runserver


# Конфигурация, не нужно редактировать
if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['']
        }]
    )

ALLOWED_SCHEMES = {'http', 'https', 'ftp'}

def random_key(key = ""):
    return key.join(choice(ascii_letters) for i in range(12))



def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        contex = {}
        url = request.POST.get('url')
        result = urlparse(url)
        if result.dcheme in ALLOWED_SCHEMES:
            key = random_key()
            cache.add(key, url)
            contex['url'] = key
            return render(request, 'index.html', contex)
        else:
            contex['Message'] = 'Only https, http, ftp addresses excepted!'
            return render(request, 'index.html', contex)

def redirect_view(request, key):
    redirect_url = cache.get(key, '/')
    return redirect(redirect_url)


def stats(request, key):
    try:
        result = stats_dict[key]
    except:
        result = 0
    return render(request, 'index.html', {'form_count': result})


urlpatterns = [
    url(r'^$', index),
    url(r'^([\w]*)$', redirect_view)
]


if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
