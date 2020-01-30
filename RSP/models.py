from django.contrib.auth.models import User
from django.db import models

class Weapons(models.Model):
    WEAPON_CHOICES = (
        ('가위', "가위"),
        ('바위', "바위"),
        ('보', "보"),
    )
    weapon=models.CharField(max_length=255, null=True, blank=True, choices=WEAPON_CHOICES)

    def __str__(self):
        return self.weapon


class FriendRequest(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user", null=True, blank=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user",null=True, blank=True)
    to_user_rsp = models.ForeignKey(Weapons, on_delete=models.CASCADE, related_name='to_user_rsp', null=True, blank=True)
    from_user_rsp = models.ForeignKey(Weapons, on_delete=models.CASCADE, related_name='from_user_rsp', null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    to_user_result = models.CharField(max_length=255, null=True, blank=True)
    from_user_result = models.CharField(max_length=255, null=True, blank=True)
    from_user_num=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.to_user}에게 {self.from_user}가"