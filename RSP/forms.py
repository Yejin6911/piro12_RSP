from django import forms

from RSP.models import FriendRequest


class RequestForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields = ("to_user","from_user_rsp",)

class AcceptForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields=("to_user_rsp",)