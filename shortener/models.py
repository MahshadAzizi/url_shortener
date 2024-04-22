from django.db import models


class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=100, unique=True)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return self.short_url
