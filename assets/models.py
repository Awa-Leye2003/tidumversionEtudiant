from django.db import models
# Create your models here.
from django.db import models

class Asset(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    domain_name = models.CharField(max_length=255, null=True, blank=True)
    scan_date = models.DateTimeField(auto_now_add=True)
    is_web_based = models.BooleanField(default=False)

    def __str__(self):
        return self.domain_name or self.ip_address


class Port(models.Model):
    asset = models.ForeignKey(Asset, related_name='ports', on_delete=models.CASCADE)
    number = models.IntegerField()
    protocol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.number}/{self.protocol} - {self.asset.ip_address}"

class Application(models.Model):
    port = models.ForeignKey(Port, related_name='applications', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.version})"

class WebMetadata(models.Model):
    asset = models.OneToOneField(Asset, related_name='web_metadata', on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/', null=True, blank=True)
    http_headers = models.JSONField(default=dict)

    def __str__(self):
        return f"Web Metadata for {self.asset.ip_address}"


class ScanResult(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    scan_date = models.DateTimeField()
    port = models.IntegerField()
    protocol = models.CharField(max_length=10)
    application = models.CharField(max_length=100)
    version = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.asset} - {self.port}/{self.protocol} - {self.application}"
       



