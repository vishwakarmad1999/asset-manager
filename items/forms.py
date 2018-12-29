from django import forms
from .models import Asset
import datetime
from django.contrib.admin import widgets

class DateInput(forms.DateInput):
	input_type = 'date'


class AssetModelForm(forms.ModelForm):
	pass
	class Meta:
		model 	= Asset
		exclude = ['user']
		widgets = {
			'date_of_purchase': DateInput(),
			'warranty_expiry': DateInput(),
		}


	# def clean_date_of_issue(self):
	# 	doi = self.cleaned_data.get("date_of_issue")
	# 	if doi == datetime.date(1999, 1, 24):
	# 		print("date_of_issue", doi)
	# 		raise forms.ValidationError("Cmon man, it's your birthday")
	# 	return doi