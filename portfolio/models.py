from django.db import models


class ContactInfo(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='personal/')

    def __str__(self):
        return self.name


class CVFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title


class Skills(models.Model):
    icon = models.ImageField(upload_to='icons/')
    category = models.CharField(max_length=100)  # Field for the skill category
    skills = models.TextField()  # or adjust according to your needs

    def __str__(self):
        return self.category


class Experience(models.Model):
    icon = models.ImageField(upload_to='icons/')
    company_name = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.company_name

    def get_start_date_display(self):
        if self.start_date:
            return self.start_date.strftime('%b %Y')  # Format as 'Month Year'
        return 'N/A'  # Handle None case

    def get_end_date_display(self):
        if self.current:
            return 'Present'
        elif self.end_date:  # Check if end_date is not None
            return self.end_date.strftime('%b %Y')
        return 'N/A'  # Default message when end_date is None
