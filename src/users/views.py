from django.core.paginator import Paginator
from django.shortcuts import render

from users.models import User
from users.tables import UserTable


def users(request):
    users = User.objects.all()
    paginator = Paginator(users, 25)

    page_number = request.GET.get("page", 0)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "users/users.html",
        {"users": users, "table": UserTable(page_obj), "page_obj": page_obj,},
    )
