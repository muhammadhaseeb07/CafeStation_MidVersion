from django.db import models


# Create your models here.

class DebitCard(models.Model):
    Card_ID = models.AutoField(primary_key=True)
    Card_Number = models.fields.CharField(max_length=20, unique=True)
    First_Name = models.fields.CharField(max_length=30)
    Last_Name = models.fields.CharField(max_length=30)
    Expiry_Date = models.fields.DateField()
    Security_Number = models.fields.CharField(max_length=4)

    class Meta:
        db_table = "DebitCard"
        verbose_name = "Card"
        constraints = [
            models.UniqueConstraint(fields=['Card_Number'], name='unique_Card_Number')
        ]


class Institute(models.Model):
    Institute_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30, unique=True)
    Address = models.CharField(max_length=60)
    URL = models.CharField(max_length=40, unique=True)
    Card_ID = models.ForeignKey(DebitCard, on_delete=models.CASCADE, verbose_name="Card")
    Token = models.IntegerField(default=0)

    class Meta:
        db_table = "Institute"
        constraints = [
            models.UniqueConstraint(fields=['Name'], name='unique_Name'),
            models.UniqueConstraint(fields=['URL'], name='unique_URL')
        ]


class InstituteOwner(models.Model):
    InstituteOwner_ID = models.AutoField(primary_key=True)
    CNIC = models.CharField(max_length=15, unique=True)
    DOB = models.DateField()
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Contact_Number = models.CharField(max_length=11, unique=True)
    Password = models.CharField(max_length=32)
    Email = models.CharField(max_length=30, unique=True)
    Institute_ID = models.ForeignKey(Institute, on_delete=models.CASCADE)

    class Meta:
        db_table = "InstituteOwner"
        constraints = [
            models.UniqueConstraint(fields=['CNIC'], name='unique_CNIC'),
            models.UniqueConstraint(fields=['Contact_Number'], name='unique_Contact_Number'),
            models.UniqueConstraint(fields=['Email'], name='unique_Email')
        ]
