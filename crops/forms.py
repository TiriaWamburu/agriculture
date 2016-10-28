# -*- coding: utf-8 -*-
# 
# author: william tiria wamburu | tiriawamburu@gmail.com
#

from django import forms
from django.forms import ModelForm

from crops.models import Crop, Region, Mineral, RegionMinerals, CropMinerals

LAND_SIZES = [
    (1, "1 Acre"),
    (2, "2 Acres"),
    (3, "3 Acres"),
    (5, "5 Acres"),
    (10, "10 Acres"),
    (15, "15 Acres"),
    (20, "20 Acres"),
    (50, "50 Acres"),
    (100, "100 Acres"),
]

class CropForm(ModelForm):
    """
    Crop details form
    """
    class Meta:
        model = Crop
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "rainfall": forms.TextInput(attrs={"class": "form-control"}),
            "ph_high": forms.TextInput(attrs={"class": "form-control"}),
            "ph_low": forms.TextInput(attrs={"class": "form-control"}),
        }
        exclude = ()


class RegionForm(ModelForm):
    """
    Region details form
    """
    class Meta:
        model = Region
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "rainfall": forms.TextInput(attrs={"class": "form-control"}),
            "ph_high": forms.TextInput(attrs={"class": "form-control"}),
            "ph_low": forms.TextInput(attrs={"class": "form-control"}),
        }
        exclude = ()


class MineralForm(ModelForm):
    """
    Mineral details form
    """
    class Meta:
        model = Mineral
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "symbol": forms.TextInput(attrs={"class": "form-control"}),
        }
        exclude = ()


class RegionMineralsForm(ModelForm):
    """
    Mineral composition details form
    """
    class Meta:
        model = RegionMinerals
        widgets = {
            "region": forms.Select(attrs={"class": "form-control"}),
            "mineral": forms.Select(attrs={"class": "form-control"}),
            "percentage": forms.TextInput(attrs={"class": "form-control"}),
        }
        exclude = ()


class CropMineralsForm(ModelForm):
    """
    Mineral requirement details form
    """
    class Meta:
        model = CropMinerals
        widgets = {
            "crop": forms.Select(attrs={"class": "form-control"}),
            "mineral": forms.Select(attrs={"class": "form-control"}),
            "percentage": forms.TextInput(attrs={"class": "form-control"}),
        }
        exclude = ()


class CropSelectForm(forms.Form):
    """
    Crop select form
    """
    crop = forms.ModelChoiceField(
        widget = forms.Select(attrs={"class": "form-control"}),
        label = "Crop list (select one)",
        queryset = Crop.objects.all(),
        empty_label = None
    )


class RegionSelectForm(forms.Form):
    """
    Region select form
    """
    region = forms.ModelChoiceField(
        widget = forms.Select(attrs={"class": "form-control"}),
        label = "Region list (select one)",
        queryset = Region.objects.all(),
        empty_label = None
    )


class LandSizeSelectForm(forms.Form):
    """
    Land size select form
    """
    land_size = forms.ChoiceField(
        widget = forms.Select(attrs={"class": "form-control"}),
        label = "Area list (select one)",
        choices = LAND_SIZES
    )
