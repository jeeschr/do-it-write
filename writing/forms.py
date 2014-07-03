
# from tinymce.widgets import TinyMCE
from django import forms
from writing.models import *

from tinymce.widgets import TinyMCE

class ReviewForm(forms.ModelForm):

	class Meta:
		model = Review

		fields = ('text',)

	views = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
	text= forms.CharField(widget=TinyMCE())


class CharacterForm(forms.ModelForm):

	class Meta:
		model = Character

		fields = ('text',)

	views = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
	text= forms.CharField(widget=TinyMCE())

class EventForm(forms.ModelForm):

	class Meta:
		model = Event

		fields = ('text',)

	views = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
	text= forms.CharField(widget=TinyMCE())


class TextForm(forms.ModelForm):

	class Meta:
		model = Text

		fields = ('text',)

	views = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
	text= forms.CharField(widget=TinyMCE())