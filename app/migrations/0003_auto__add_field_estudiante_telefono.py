# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Estudiante.telefono'
        db.add_column(u'app_estudiante', 'telefono',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Estudiante.telefono'
        db.delete_column(u'app_estudiante', 'telefono')


    models = {
        u'app.carrera': {
            'Meta': {'object_name': 'Carrera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'app.estudiante': {
            'Meta': {'object_name': 'Estudiante'},
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Carrera']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        }
    }

    complete_apps = ['app']