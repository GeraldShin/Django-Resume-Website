from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name