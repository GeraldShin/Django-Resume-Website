from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.company}"


class Project(models.Model):
    name = models.CharField(max_length=200)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name