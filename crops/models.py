from __future__ import unicode_literals

from django.db import models


class Region(models.Model):
    """
    Base model for region definition
    """
    name = models.CharField(max_length=200)
    rainfall = models.FloatField()
    ph_low = models.FloatField(verbose_name="Lower pH Bound")
    ph_high = models.FloatField(verbose_name="Higher pH Boung")

    def __str__(self):
        return self.name.title()
    

class Mineral(models.Model):
    """
    Base model for mineral definition
    """
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=20, verbose_name="Scientific Symbol")

    def __str__(self):
        return "{} ({})".format(self.name.title(), self.symbol)

    
class Crop(models.Model):
    """
    Base model for crop definition
    """
    name = models.CharField(max_length=200)
    rainfall = models.FloatField(verbose_name="Annual Rainfall Requirement (ml)")
    ph_low = models.FloatField(verbose_name="Lower pH Bound")
    ph_high = models.FloatField(verbose_name="Higher pH Bound")

    def __str__(self):
        return self.name.title()

    
class CropMinerals(models.Model):
    """
    Base model for crop mineral requirements
    """
    crop = models.ForeignKey(Crop, related_name="mineral_requirements")
    mineral = models.ForeignKey(Mineral)
    percentage = models.FloatField(verbose_name="Percetage Requirement")


class RegionMinerals(models.Model):
    """
    Base model for region mineral composition
    """
    region = models.ForeignKey(Region, related_name="mineral_composition")
    mineral = models.ForeignKey(Mineral)
    percentage = models.FloatField(verbose_name="Percentage Composition")
