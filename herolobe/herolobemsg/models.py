from django.db import models


class Msg(models.Model):
    sender = models.CharField(max_length=30, null=False)
    receiver = models.CharField(max_length=30, null=False)
    subject = models.CharField(max_length=50, null=False)
    message = models.CharField(max_length=200, null=False)
    creation_date = models.DateTimeField(null=False)
    been_read = models.BooleanField(default=False)
