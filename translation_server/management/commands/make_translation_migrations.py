# -*- coding: utf-8 -*-
# Created by Gustavo Del Negro <gustavodelnegro@gmail.com> on 10/1/16.
import django
from django.core.management import BaseCommand
from django.apps import *
from datetime import datetime
from django.core.management import call_command
import os
import glob
from translation_server.models import Translation


class Command(BaseCommand):
    help = "This command generates migrations for translations, based on the contents of 'Translation' model"
    app_name = None
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    updated_translations = []

    migration_string = """# -*- coding: utf-8 -*-
# Generated by Django %(django_version)s on %(timestamp)s
from __future__ import unicode_literals

from django.db import migrations


def __load_data(**kwargs):
    apps = kwargs.pop('apps', None)
    if apps:
        translation_type = apps.get_model("%(app_name)s", "TranslationType")
        model = apps.get_model("%(app_name)s", "Translation")
        try:
            mdl = model.objects.get(tag=kwargs['tag'])
        except model.DoesNotExist:
            mdl = model()
        except Exception as err:
            raise err
        for k, v in kwargs.items():
            if k == "type":
                setattr(mdl, k, translation_type.objects.get(tag=v))
            else:
                setattr(mdl, k, v)
        setattr(mdl, "migration_created", True)
        mdl.save()


def clear_data(apps, schema_editor):
    model = apps.get_model("%(app_name)s", "Translation")
    model.objects.filter(tag__in=[%(tags_to_remove)s]).delete()


def load_data(apps, schema_editor):
%(translation_strings)s


class Migration(migrations.Migration):

    dependencies = [
        ('%(app_name)s', '%(dependency)s'),
    ]

    operations = [
        migrations.RunPython(load_data, clear_data)
    ]

        """

    def __create_translation_lines(self):
        new_lines = []
        fields_to_ignore = ['id', 'created_at', 'updated_at']
        fields_string = ""
        fields_options = {}
        model_fields = [field.name if field.name not in fields_to_ignore else None for field in
                      apps.get_model('translation_server', "Translation")._meta.get_fields()]
        for field in model_fields:
            if field:
                fields_string += ', %s="%%(%s)s"' % (field, field)
                fields_options.update({field: ''})

        base_str = '    __load_data(apps=apps%(fields)s)' % {'fields': fields_string}

        for translation in Translation.objects.filter(migration_created=False):
            for field in fields_options:
                value = getattr(translation, field)
                if type(value) is str:
                    value = value.replace('"', '\\"') if len(value) > 0 else ""
                if field == 'type':
                    value = value.tag
                if field == 'migration_created':
                    value = True
                fields_options[field] = value
            new_lines.append(base_str % fields_options)
            self.updated_translations.append(translation.tag)
        return new_lines

    def __update_translation(self):
        for tag in self.updated_translations:
            translation = Translation.objects.get(tag=tag)
            translation.migration_created = True
            translation.save()

    def __create_translation_migration(self):
        """ """
        """ Create an empty migration """
        migrations_dir = os.path.join(self.BASE_DIR, "../../migrations/")
        dependency_migration = os.path.basename(max(glob.iglob(migrations_dir + '*.py'), key=os.path.getctime)).replace(
            ".py", "")
        """
        If there's no migration before this, which is unlikely to happen, then create a migration without dependencies
        """
        if "__init__" in dependency_migration:
            dependency_migration = ""
        """ Make an empty migration """
        call_command('makemigrations', self.app_name, "--empty")
        """ Get last migration name and edit it, adding the new code """
        last_migration_file = max(glob.iglob(migrations_dir + '*.py'), key=os.path.getctime)
        new_lines = self.__create_translation_lines()
        try:
            if len(new_lines) > 0:
                with open(last_migration_file, 'w+') as file:
                    file.write(self.migration_string % {
                        'django_version': django.get_version(),
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'translation_strings': "\n".join(new_lines),
                        'dependency': dependency_migration,
                        'tags_to_remove': ", ".join('"{0}"'.format(tag) for tag in self.updated_translations),
                        'app_name': self.app_name
                    })
            else:
                os.remove(last_migration_file)
                self.stdout.write(self.style.NOTICE("There was no new translations to make migrations"))
                return
        except Exception as error:
            os.remove(last_migration_file)
            raise error
        else:
            self.__update_translation()
            self.stdout.write(self.style.SUCCESS("Translation migration file create successfully"))
            return

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str)

    def handle(self, *args, **options):
        self.app_name = options['app_name']
        self.__create_translation_migration()