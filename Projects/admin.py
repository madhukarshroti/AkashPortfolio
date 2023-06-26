from django.contrib import admin
from Projects.models import ProjectShow

class ProjectAdmin(admin.ModelAdmin):
    list_display=('project_name','desc','link')
# Register your models here.

admin.site.register(ProjectShow,ProjectAdmin)
