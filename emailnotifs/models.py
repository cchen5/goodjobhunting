from django.db import models

# Create your models here.

class EmailAddress(models.Model):
        address = models.CharField(max_length=200)

        class Meta:
                unique_together = ('address',)

class Email(models.Model):
	sender = models.ForeignKey(EmailAddress, related_name='sender')
#	company = models.CharField(max_length=200)
#	time_stamp = DateTimeField('date sent')
	recipient = models.ForeignKey(EmailAddress, related_name='recipient')
	subject_line = models.CharField(max_length=500)
	email_body = models.CharField(max_length = 5000)
