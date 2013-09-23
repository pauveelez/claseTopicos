# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Estudiante.carrera'
        db.add_column('app_estudiante', 'carrera',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Carrera'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Estudiante.carrera'
        db.delete_column('app_estudiante', 'carrera_id')


    models = {
        'app.carrera': {
            'Meta': {'object_name': 'Carrera'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'app.estudiante': {
            'Meta': {'object_name': 'Estudiante'},
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Carrera']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['app']