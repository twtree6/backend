from django.db import models

class kpiConfiguration(models.Model):
    OS = models.CharField(max_length=20,null=False)
    kernel = models.CharField(max_length=20,null=False)
    server_info = models.CharField(max_length=20,null=False)
    cpu_info = models.CharField(max_length=20,null=False)
    bios_info = models.CharField(max_length=20,null=False)
    gpu_info = models.CharField(max_length=20,null=False)
    ram = models.CharField(max_length=20,null=False)
    gpu_driver = models.CharField(max_length=20,null=False)

    class Meta:
        db_table = 'kpiConfiguration'

