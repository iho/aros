from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from users.forms import LoginForm, UserForm
from users.models import User
from users.tables import UserTable


def users(request):
    users = User.objects.all()
    paginator = Paginator(users, 25)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    form = UserForm(request.POST or None)
    if form.is_valid():
        return HttpResponseRedirect("/users/")

    return render(
        request,
        "users/users.html",
        {
            "users": users,
            "table": UserTable(page_obj),
            "page_obj": page_obj,
            "form": form,
        },
    )


def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return JsonResponse({"status": "ok"})


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy("users")
    template_name = "users/user_create.html"

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data["password"])
        return super().form_valid(form)


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy("users")
    template_name = "users/user_update.html"

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data["password"])
        return super().form_valid(form)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/users")
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            login(request, user)
            return redirect("/loggedin")
        else:
            messages.add_message(request, messages.INFO, "Credendtias are not correct.")

    return render(request, "users/login.html", {"form": form,},)


def loggedin_view(request):
    return render(request, "users/loggedin.html", {})


def logout_view(request):
    logout(request)
    return redirect("/")
