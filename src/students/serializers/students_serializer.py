from loducode_utils.serializers import AuditSerializer

from students.models.students import Student


class StudentSerializer(AuditSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'last_name', 'note',)


class StudentListSerializer(AuditSerializer):
    class Meta:
        model = Student
        fields = ('name', 'last_name', 'note',)
