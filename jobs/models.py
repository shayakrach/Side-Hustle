from django.db import models


# Enum for Job Types
class JobType(models.TextChoices):
    FULL_TIME = '1', 'Full time'
    PART_TIME = '2', 'Part time'
    INTERNSHIP = '3', 'Internship'


class Location(models.TextChoices):
    Tel_Aviv = '1', 'Tel Aviv'
    Jerusalem = '2', 'Jerusalem'
    Haifa = '3', 'Haifa'


# Jobs Model
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    location = models.CharField(
        max_length=15,
        choices=Location.choices,
        default=Location.Tel_Aviv,
        blank=True, null=True
    )
    job_type = models.CharField(
        max_length=15,
        choices=JobType.choices,
        default=JobType.PART_TIME,
        blank=True, null=True
    )
    company_name = models.CharField(max_length=255)
    post_until = models.DateField()
    is_active = models.BooleanField()
    marked_count = models.IntegerField(default=0)
    apply_link = models.URLField(unique=True, null=True)

    # Function to create a new job
    @classmethod
    def create_job(cls, title, description, location, job_type,
                   company_name, post_until, is_active, marked_count, apply_link):
        job = cls(title=title, description=description, location=location,
                  job_type=job_type, company_name=company_name,
                  post_until=post_until, is_active=is_active, marked_count=marked_count, apply_link=apply_link)
        job.save()
        return job

    def del_job(self):
        try:
            self.job.delete()
        except Job.DoesNotExist:
            return False
        return True

    # Function to reduce the length of description
    def snippet_description(self):
        return self.description[:25] + '...'

    # Jobs title to string - return the title of the job
    def __str__(self) -> str:
        return self.title

    @staticmethod
    # Function to search job by title
    def get_jobs_by_title(title):
        return set(Job.objects.filter(name=title))
