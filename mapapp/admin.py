from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Carbon

@admin.register(Carbon)
class CarbonAdmin(ImportExportModelAdmin):
    list_display = ('country', 'code', 'year', 'annual_co2_emissions_tonnes')
