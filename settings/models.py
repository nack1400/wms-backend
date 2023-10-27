from django.db import models


class SystemConfig(models.Model):
    pallet_number = models.PositiveIntegerField(default=1)
    inbound_number = models.PositiveIntegerField(default=1)
    outbound_number = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.pk and SystemConfig.objects.exists():
            return SystemConfig.objects.first()
        return super(SystemConfig, self).save(*args, **kwargs)

    def __str__(self):
        return "System Configuration"

    class Meta:
        verbose_name = "System Configuration"
