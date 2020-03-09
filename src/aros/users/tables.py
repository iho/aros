import django_tables2 as tables
from users.models import User

class UserTable(tables.Table):
    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ("username", "first_name", "last_name", "email")
