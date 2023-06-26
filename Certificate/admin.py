from django.contrib import admin
from Certificate.models import Certificate

class ProjectAdmin(admin.ModelAdmin):
    list_display=('Certificate_name','image','Certificate_tag')
# Register your models here.

admin.site.register(Certificate,ProjectAdmin)
