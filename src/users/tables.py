import django_tables2 as tables

from django.utils.safestring import mark_safe

from users.models import User

class UserTable(tables.Table):
    edit = tables.Column(empty_values=())
    delete = tables.Column(empty_values=())

    def render_edit(self, value, record):
        return mark_safe(f'<a up-modal=".container" href="/users/{record.id}"><i class="fas fa-edit"></i></div>')

    def render_delete(self, value, record):
        return mark_safe(f'<div class="delete" data-id={record.id}><i class="fas fa-trash"></i></div>')

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ("username", "first_name", "last_name", "email", "edit", "delete")
        attrs = {"class": "table table-striped table-bordered"}
