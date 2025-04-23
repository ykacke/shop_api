from django.db import models

class SMSCode(models.Model):
    code = models.CharField(max_length=6)
    user = models.OneToOneField('auth.User',
                                on_delete=models.CASCADE,
                                related_name='sms_code')

    def __str__(self) -> str:
        return f'{self.code} - {self.user.username}'