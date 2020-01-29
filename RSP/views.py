from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import *
from RSP.models import FriendRequest


def main(request):
    return render(request, 'RSP/main.html')


def login(request):
    return render(request, 'RSP/login.html')


def list(request):
    current_user = request.user
    game_list = FriendRequest.objects.all()
    game_list_filter = game_list.filter(to_user=current_user) | game_list.filter(from_user=current_user)

    ctx = {
        "game_list": game_list_filter.order_by("-id"),
        "current_user": current_user,
    }
    return render(request, "RSP/list.html", ctx)


def send_friend_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        friend_request = form.save()

        friend_request.from_user = request.user
        friend_request.result = "진행중..."
        friend_request.from_user_num = request.user.id
        friend_request.save()

        return redirect("list")

    else:
        form = RequestForm()
        ctx = {
            "form": form
        }
        return render(request, "RSP/request.html", ctx)


def rsp_result(user1, user2):
    if user1 == user2:
        return "비김"
    else:
        if user1 == "가위":
            if user2 == "바위":
                return "패배"
            else:  # user2 == "보"
                return "승리"

        if user1 == "바위":
            if user2 == "가위":
                return "승리"
            else:
                return "패배"

        if user1 == "보":
            if user2 == "가위":
                return "패배"
            else:
                return "승리"


def accept_friend_request(request, pk):
    if request.method == "POST":
        friend_request = FriendRequest.objects.get(pk=pk)

        form = AcceptForm(request.POST).save()
        friend_request.to_user_rsp = form.to_user_rsp
        friend_request.save()

        to_user_rsp = friend_request.to_user_rsp
        from_user_rsp = friend_request.from_user_rsp

        friend_request.to_user_result = rsp_result(to_user_rsp, from_user_rsp)
        friend_request.from_user_result = rsp_result(from_user_rsp, to_user_rsp)

        friend_request.save()
        form.delete()

        return redirect("list")

    else:
        form = AcceptForm()
        ctx = {
            "form": form,
        }
        return render(request, "RSP/request.html", ctx)

def detail(request, pk):
    pass