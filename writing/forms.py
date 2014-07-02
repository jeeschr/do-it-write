from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django import forms
from writing.models import Review

class ReviewForm(forms.ModelForm):

	class Meta:
		model = Review

		fields = ('text',)

		widgets = {
	        'text': SummernoteWidget(),
            # 'text': SummernoteInplaceWidget(),
        }

	views = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)