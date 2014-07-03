from django.contrib import admin

# Register your models here.

from writing.models import *

class TextAdmin(admin.ModelAdmin):
	list_display = ('text', 'datetime')

	class Media:
		js=('/static/tiny_mce/tiny_mce.js', '/static/tiny_mce/textarea.js')

admin.site.register(Review, TextAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Character, TextAdmin)
admin.site.register(Event, TextAdmin)

