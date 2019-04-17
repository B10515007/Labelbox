from django.contrib import admin
from labeling.models import Labeling, Project, Group
# Register your models here.

class LabelingAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'choice', 'image', 'judge', 'comment')
    search_fields = ('choice',)
    # raw_id_fields = ("project",)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'member', 'state')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'project')
    fields = ['member']

admin.site.register(Labeling, LabelingAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Group, GroupAdmin)
