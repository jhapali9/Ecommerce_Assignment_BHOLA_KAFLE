from django.db import models

# Create your models here.
class LabExam(models.Model):
    exam_date = models.DateField()
    exam_name = models.CharField(max_length=255)
    exam_description = models.TextField()
    total_marks = models.FloatField(null=True, blank=True)
    pass_marks = models.FloatField(null=True, blank=True)
    exam_status = models.BooleanField()

    def __str__(self):
        return self.exam_name