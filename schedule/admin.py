from django.contrib import admin
from .models import Vehicle, Project, Date, DateBoundWithProject, Profile, Artifact, Subproject, SIT_project, SIT_with_date

class DateAdmin(admin.ModelAdmin):
    search_fields = ['date', "is_holiday"]
    change_list_template = "admin/date_change_list.html"

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['profile']

class ArtifactAdmin(admin.ModelAdmin):
    search_fields = ['artifact']

admin.site.register(Vehicle)
admin.site.register(Project)
admin.site.register(Date, DateAdmin)
admin.site.register(DateBoundWithProject)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Artifact, ArtifactAdmin)
admin.site.register(Subproject)

admin.site.register(SIT_project)
admin.site.register(SIT_with_date)
