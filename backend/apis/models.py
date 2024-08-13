from django.db import models

# Create your models here.
class Expense(models.Model):
    #amount payment_method category description bankname
    date = models.DateField(null=False )
    amount = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False)
    payment_method = models.CharField(max_length=100,blank=False,null=False)
    category = models.CharField(max_length=100,blank=False,null=False)
    description = models.TextField(max_length=750, blank=True,null=True)
    bankName = models.CharField(max_length=75,blank=True,null=True) 
    def __str__(self):
        return self.category+" "+str(self.amount)
    