from django.contrib import admin

from site_ong.models import UserLogin, Coordinator, Volunteer, Materials, Reviews

# Register your models here.

admin.site.register(UserLogin)
admin.site.register(Coordinator)
admin.site.register(Volunteer)
admin.site.register(Materials)
admin.site.register(Reviews)