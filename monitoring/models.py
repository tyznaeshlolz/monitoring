from django.db import models


class OSUser(models.Model):
    login = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pass_number = models.CharField(max_length=255, unique=True)
    at_work = models.BooleanField()

    def __str__(self):
        return self.login


class Gate(models.Model):
    gate_number = models.CharField(max_length=10, unique=True)
    work_end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.gate_number


class VisitLog(models.Model):
    user = models.ForeignKey(OSUser, on_delete=models.CASCADE)
    user_status = models.BooleanField()
    gate = models.ForeignKey(Gate, on_delete=models.CASCADE)
    pass_number = models.CharField(max_length=255)
    pass_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} @ {self.pass_time}'
