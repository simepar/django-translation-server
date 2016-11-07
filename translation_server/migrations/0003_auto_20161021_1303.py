# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-21 13:03:04
from __future__ import unicode_literals

from django.db import migrations


def __load_data(**kwargs):
    apps = kwargs.pop('apps', None)
    if apps:
        translation_type = apps.get_model("translation_server", "TranslationType")
        model = apps.get_model("translation_server", "Translation")
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
    model = apps.get_model("translation_server", "Translation")
    model.objects.filter(tag__in=["DTSM5", "DTSMT2", "DTSE1", "DTSM12", "DTSMT1", "DTSM1", "DTSM8", "DTSM9", "DTSM7", "DTSM10", "DTSM11", "DTSM2", "DTSM3", "DTSM4", "DTSM6"]).delete()


def load_data(apps, schema_editor):
    __load_data(apps=apps, type="DTSM", tag="DTSM5", text="Has auxiliary text?", text_en="Has auxiliary text?", text_pt_br="Tem texto auxiliar?", auxiliary_tag="DTST5", auxiliary_text="If the translation type have auxiliary text", auxiliary_text_en="If the translation type have auxiliary text", auxiliary_text_pt_br="Se o tipo de tradução tem texto auxiliar", migration_created="True")
    __load_data(apps=apps, type="DTSMT", tag="DTSMT2", text="Translation", text_en="Translation", text_pt_br=u"Tradução", auxiliary_tag="DTSMTP2", auxiliary_text="Translations", auxiliary_text_en="Translations", auxiliary_text_pt_br=u"Traduções", migration_created="True")
    __load_data(apps=apps, type="DTSE", tag="DTSE1", text="The auxiliary text must be different from the primary text", text_en="The auxiliary text must be different from the primary text", text_pt_br="O texto auxiliar deve ser diferente do texto principal", auxiliary_tag="", auxiliary_text="", auxiliary_text_en="", auxiliary_text_pt_br="", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM12", text="Migration created", text_en="Migration created", text_pt_br="\"Migration\" criada", auxiliary_tag="DTST12", auxiliary_text="If this record migration was created", auxiliary_text_en="If this record migration was created", auxiliary_text_pt_br="Se a migration desse registro foi criada", migration_created="True")
    __load_data(apps=apps, type="DTSMT", tag="DTSMT1", text="Translation Type", text_en="Translation Type", text_pt_br="Tipo de tradução", auxiliary_tag="DTSMTP1", auxiliary_text="Translation Types", auxiliary_text_en="Translation Types", auxiliary_text_pt_br="Tipos de tradução", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM1", text="Created at", text_en="Created at", text_pt_br="Criado em", auxiliary_tag="DTST1", auxiliary_text="Record creation date", auxiliary_text_en="Record creation date", auxiliary_text_pt_br="Data de criação do registro", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM8", text="Tag", text_en="Tag", text_pt_br="Tag", auxiliary_tag="DTST8", auxiliary_text="Unique identifier", auxiliary_text_en="Unique identifier", auxiliary_text_pt_br="Identificador único", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM9", text="Text", text_en="Text", text_pt_br="Texto", auxiliary_tag="DTST9", auxiliary_text="Translation text", auxiliary_text_en="Translation text", auxiliary_text_pt_br="Texto da tradução", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM7", text="Translation Type", text_en="Translation Type", text_pt_br="Tipo de tradução", auxiliary_tag="DTST7", auxiliary_text="Record translation type", auxiliary_text_en="Record translation type", auxiliary_text_pt_br="Tipo de tradução do registro", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM10", text="Auxiliary tag", text_en="Auxiliary tag", text_pt_br="Tag auxiliar", auxiliary_tag="DTST10", auxiliary_text="Auxiliary text unique identifier", auxiliary_text_en="Auxiliary text unique identifier", auxiliary_text_pt_br="Identificador único do texto auxiliar", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM11", text="Auxiliary text", text_en="Auxiliary text", text_pt_br="Texto auxiliar", auxiliary_tag="DTST11", auxiliary_text="Auxiliary text", auxiliary_text_en="Auxiliary text", auxiliary_text_pt_br="Texto auxiliar", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM2", text="Updated at", text_en="Updated at", text_pt_br="Atualizado em", auxiliary_tag="DTST2", auxiliary_text="Record update time", auxiliary_text_en="Record update time", auxiliary_text_pt_br="Data de atualização do registro", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM3", text="Tag", text_en="Tag", text_pt_br="Tag", auxiliary_tag="DTST3", auxiliary_text="Unique identifier that will be used as prefix for the translations tag", auxiliary_text_en="Unique identifier that will be used as prefix for the translations tag", auxiliary_text_pt_br="Identificador único que será usado como prefixo da tag das traduções", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM4", text="Name", text_en="Name", text_pt_br="Nome", auxiliary_tag="DTST4", auxiliary_text="Record name", auxiliary_text_en="Record name", auxiliary_text_pt_br="Nome do registro", migration_created="True")
    __load_data(apps=apps, type="DTSM", tag="DTSM6", text="Auxiliary text tag", text_en="Auxiliary text tag", text_pt_br="Tag do texto auxiliar", auxiliary_tag="DTST6", auxiliary_text="The unique identifier prefix for auxiliary text", auxiliary_text_en="The unique identifier prefix for auxiliary text", auxiliary_text_pt_br="O prefixo para o  identificador único do texto auxiliar", migration_created="True")


class Migration(migrations.Migration):

    dependencies = [
        ('translation_server', '0002_auto_20161021_1254'),
    ]

    operations = [
        migrations.RunPython(load_data, clear_data)
    ]

        
