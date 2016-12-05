# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'hello_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'hello', ['Profile'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'hello_profile')


    models = {
        u'hello.profile': {
            'Meta': {'object_name': 'Profile'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hello']