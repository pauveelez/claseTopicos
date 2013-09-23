# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'estudiante'
        db.create_table('app_estudiante', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('app', ['estudiante'])

        # Adding model 'carrera'
        db.create_table('app_carrera', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('app', ['carrera'])


    def backwards(self, orm):
        # Deleting model 'estudiante'
        db.delete_table('app_estudiante')

        # Deleting model 'carrera'
        db.delete_table('app_carrera')


    models = {
        'app.carrera': {
            'Meta': {'object_name': 'carrera'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'app.estudiante': {
            'Meta': {'object_name': 'estudiante'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['app']