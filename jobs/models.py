from django.db import models


class JobApplication(models.Model):
    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    application_date = models.DateField()
    status = models.CharField(max_length=20, default="Applied")

    def __str__(self):
        return f"{self.company_name} - {self.job_role}"