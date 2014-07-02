from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from writing.models import Review

class ReviewAdmin(SummernoteModelAdmin):
	list_display = ('text', 'datetime')
	print 'hi'

admin.site.register(Review, ReviewAdmin)

