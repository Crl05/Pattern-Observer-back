from django.contrib import admin
from loducode_utils.admin import AuditAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from students.models.students import Student


class StudentsResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = '__all__'


@admin.register(Student)
class StudentsAdmin(AuditAdmin, ImportExportModelAdmin):
    resource_class = StudentsResource
    list_display = ('name', 'last_name', 'note',)
    list_display_links = ('name', 'last_name', 'note',)
    search_fields = ('name', 'last_name', )
