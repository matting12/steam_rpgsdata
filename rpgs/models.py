from django.db import models


class Game(models.Model):
    steam_app_id = models.PositiveIntegerField(null=True, blank=True)
    rank = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500, blank=True)
    image = models.URLField(max_length=500, blank=True)
    discount = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=20, default="N/A")
    is_free = models.BooleanField(default=False)
    scraped_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["rank"]

    def __str__(self):
        return self.title
