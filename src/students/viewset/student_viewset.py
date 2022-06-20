from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.utils.translation import gettext_lazy as _

from students.models.students import Student
from students.serializers.students_serializer import StudentListSerializer, StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return StudentListSerializer
        return StudentSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


EXAMPLE = (' ** { '
           '"name": string, '
           '"last_name": string, '
           '"note": "float", '

           ' } **')

StudentViewSet.__doc__ = """
list:
   {LIST}
create:
    {CREATE}
retrieve:
   {RETRIEVE} 
update:
    {UPDATE}
partial_update:
    {PARTIAL_UPDATE}
destroy:
    {DESTROY}
""".format(
    LIST=_("List of all students registered in the system."),
    CREATE=_("Create a student data.") + EXAMPLE,
    RETRIEVE=_("Returns the information of a specific student."),
    UPDATE=_("Update a student data.") + EXAMPLE,
    PARTIAL_UPDATE=_("Partially update a student data.") + ' ** { "name": "example name" } **',
    DESTROY=_("Destroy a student data."),
)
