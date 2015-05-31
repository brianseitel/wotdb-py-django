from django.contrib import admin

# Register your models here.

from .models import Character, ChannelerType, Clan, Job, Place, Sept, Society

class CharacterAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'alignment', 'allegiance', 'gender', 'status', 'channeler_type', 'job', 'city', 'country', 'clan', 'sept', 'society')

admin.site.register(Character, CharacterAdmin)
admin.site.register(ChannelerType)
admin.site.register(Clan)
admin.site.register(Job)
admin.site.register(Place)
admin.site.register(Sept)
admin.site.register(Society)
