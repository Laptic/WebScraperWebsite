from django.contrib import admin
from webScrapa.models import RamParts, GpuParts, MotherboardParts
# Register your models here.
admin.site.register(GpuParts)
admin.site.register(RamParts)
admin.site.register(MotherboardParts)
