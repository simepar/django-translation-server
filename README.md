Django translation server
=========================

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Requirements
-----------

Django REST framework - http://www.django-rest-framework.org/

Quick start
-----------

1. Add "translation_server" to your INSTALLED_APPS setting like this::
```
    INSTALLED_APPS = [
        ...
        'translation_server',
    ]
```
2. Include the Translation Server URLconf in your project urls.py like this::
```
    router = routers.DefaultRouter()
    router.register(r'translation', TranslationViewSet)


    url(r'^api/last_translation_tag/(?P<tag>\w+)[/]?$', LastTranslationTagView.as_view(), name='get_last_translation_tag'),
```
3. Run ```python manage.py migrate``` to create the Translation models, and load the initial data.

4. Start the development server and visit http://127.0.0.1:8000/admin/ to create a translation (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/api/translation/ to view all translations