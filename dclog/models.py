from django import forms
from django.db import models 
from datetime import datetime, date
from django.contrib.auth.models import User

INFO = 1
WARN = 2
FIRE = 3

STATUS_CHOICES = (
    (INFO, 'Informational'),
    (WARN, 'Warning'),
    (FIRE, 'Critical'),
)

# MF_CHOICES display names are available to the templates via 
# the helper method as such: {{ object.get_mf_area_display }}
MF_CHOICES = (
    (u'ad', u'Adabas'),
    (u'br', u'Broker'),
    (u'cp', u'Com-plete'),
    (u'vp', u'VPS'),
    (u'pp', u'PPS'),
    (u'pr', u'Printer'),
    (u'ot', u'Other'),
)

class Log(models.Model): 
    title      = models.CharField(max_length="30",unique=True)  
    # created    = models.DateField(default=date.today, editable=False)
    created    = models.DateTimeField(default=datetime.now, editable=False)
    updated    = models.DateTimeField(default=datetime.now, editable=False)
    eventTime  = models.DateTimeField(default=datetime.now)
    notes      = models.TextField()
    area       = models.ForeignKey('Area', verbose_name='Type of log')       # This is required as it will help us to group the logs
    status     = models.IntegerField(choices=STATUS_CHOICES, default=INFO) 
    alarm      = models.ForeignKey('Alarm', blank=True, null=True)           # Foreign Key is the alarm which might be associated with this event
    facility   = models.ForeignKey('Facility', blank=True, null=True, verbose_name='facility area')  
    created_by = models.ForeignKey(User, editable=False)
    mf_area = models.CharField(max_length=2,choices=MF_CHOICES, blank=True, verbose_name='mainframe area')

    def save(self):
        if not self.id:
            self.created = datetime.today()
            #self.eventTime = datetime.today()
        self.updated     = datetime.today()
#        self.created_by  = created_by
        super(Log, self).save() 

    def __unicode__(self):
        return self.notes

#    @models.permalink
#    def get_absolute_url(self):
#        return ('system-display', (), {'object_id': self.id})

class Alarm(models.Model):
    name        = models.CharField(max_length="30",unique=True)
    description = models.TextField(blank=True)  

    def __unicode__(self):
        return self.name

class Area(models.Model):
    name        = models.CharField(max_length="30",unique=True)
    description = models.TextField(blank=True)  

    def __unicode__(self):
        return self.name

class Facility(models.Model):
    name        = models.CharField(max_length="30",unique=True)
    description = models.TextField(blank=True)  

    def __unicode__(self):
        return self.name

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=3, widget=forms.Select(choices=STATUS_CHOICES))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=STATUS_CHOICES)
    birth_date = forms.DateField(required=False)