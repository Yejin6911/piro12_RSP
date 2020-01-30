from django import forms
from django.contrib.auth.models import User

from RSP.models import FriendRequest


class RequestForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields = ("from_user_rsp", "to_user",)

    def __init__(self, *args, **kwargs):
        # print(kwargs["initial"]["current"])
        # print(type(kwargs["initial"]["current"]))
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields["to_user"].queryset = User.objects.all().exclude(
            id=kwargs["initial"]["current_user"]
        )


class AcceptForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields = ("to_user_rsp",)
