from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    class Meta:
        app_label = "tracker"
