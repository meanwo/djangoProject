from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#Account가 삭제 되었을 경우, 해당되는 profile도 삭제하는 옵션
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)