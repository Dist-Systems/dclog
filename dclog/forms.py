from django import forms
from dclog.models import *

class NewLogForm(forms.ModelForm):
    created_by = None

    def __init__(self, user, *args, **kwargs):
        self.created_by = user      
        super(NewLogForm, self).__init__(*args, **kwargs)

    def save(self):
        self.instance.created_by = self.created_by
        return super(NewLogForm, self).save()

    # https://docs.djangoproject.com/en/dev/ref/forms/widgets/#widgets-inheriting-from-the-select-widget

    class Meta:
        model = Log

class EditLogForm(forms.ModelForm):
    class Meta:
        model = Log

class NewUpdateForm(forms.ModelForm):
    created_by = None 

    def __init__(self, user, *args, **kwargs):
        self.created_by = user
        self.log = log_id
        super(NewUpdateForm, self).__init__(*args, **kwargs)

    def save(self):
        self.instance.created_by = self.created_by
        self.instance.log = self.log
        return super(NewUpdateForm, self).save()

    class Meta:
        model = Update 

class NewAlarmForm(forms.ModelForm):
    class Meta:
        model = Alarm

class NewAreaForm(forms.ModelForm):
    class Meta:
        model = Area

class NewFacilityTypeForm(forms.ModelForm):
    class Meta:
        model = Facility  