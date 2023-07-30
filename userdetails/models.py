from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True, editable=False, null=False,)
    first_name = models.CharField(max_length=10, null=False)
    middle_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10, null=False)
    DOB = models.DateField(null=False)
    annual_salary = models.IntegerField(null=False)
    phone_number = models.IntegerField(null=False)
    email_id = models.CharField(max_length=20, null=False)
    pin_code = models.IntegerField(null=False)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=20)

    def __str__(self):
        return "%s%s%s%s%s%s%s%s%s%s%s" % (self.user_id, self.first_name, self.middle_name, self.last_name, self.DOB,
                                           self.annual_salary, self.phone_number, self.email_id, self.pin_code, self.city, self.state)

# Create your models here.
