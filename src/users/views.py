from django.shortcuts import render
from users.models import User
from users.tables import UserTable

def users(request):
    users = User.objects.all()
    return render(
        request, 
        "users/users.html", 
        {
            "users": users, 
            "table": UserTable(users)
        } 
    )