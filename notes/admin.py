from django.contrib import admin

# Register your models here.
from .models import Notes
from django.contrib import admin
from .models import PersonalNotes



class NotesAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')


# Register your models here.
admin.site.register(Notes, NotesAdmin)
admin.site.register(PersonalNotes)