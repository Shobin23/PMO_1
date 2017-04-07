from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# MVC MODEL VIEW CONTROLLER

class Post(models.Model):
    title = models.CharField(max_length=120)
    image=models.FileField(null=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.NullBooleanField()
    bu_field = models.CharField(max_length=10,null=True)
    invoice_name = models.CharField(max_length=500,null=True)
    sow_name = models.CharField(max_length=500,null=True)
    probability = models.IntegerField(null=True)
    sow_type = models.CharField(max_length=50,null=True)
    sow_start_date = models.DateField(null=True)
    sow_end_date = models.DateField(null=True)
    project_id = models.CharField(max_length=500,null=True)
    project_manager = models.CharField(max_length=500, null=True)
    po_number = models.IntegerField(null=True)
    sow_value = models.DecimalField(max_digits=8, decimal_places=2,null=True)
    current_month = models.CharField(max_length=20,null=True)
    current_year = models.CharField(max_length=5,null=True)
    month_value = models.DecimalField(max_digits=8, decimal_places=2,null=True)
    q1_value = models.IntegerField(null=True)
    q2_value = models.IntegerField(null=True)
    q3_value = models.IntegerField(null=True)
    q4_value = models.IntegerField(null=True)
    total_value_of_year = models.IntegerField(null=True)
    probability_month_value = models.IntegerField(null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    def edit_url(self):

        return reverse ()

    class Meta:
        ordering = ["-timestamp", "-updated"]