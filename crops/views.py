# -*- coding: utf-8 -*-
# 
# author: william tiria wamburu | tiriawamburu@gmail.com
#

from django.http import Http404
from django.contrib import messages
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from crops.models import Crop, Region, Mineral, RegionMinerals, CropMinerals
from crops.forms import CropForm, RegionForm, MineralForm, RegionMineralsForm, CropMineralsForm, CropSelectForm, RegionSelectForm, LandSizeSelectForm

from crops.algorithm import calculate_success_rate

def index(request):
    batch = {
        "active_menu": "index"
    }
    return render_to_response('index.html', batch, context_instance=RequestContext(request))


def crops(request):
    batch = {
        "active_menu": "crops"
    }
    return render_to_response('crops.html', batch, context_instance=RequestContext(request))


def crops_table(request):
    batch = {
        "crops": Crop.objects.all(),
        "active_menu": "crops"
    }
    return render_to_response('crops-table.html', batch, context_instance=RequestContext(request))


def minerals(request):
    batch = {
        "minerals": Mineral.objects.all(),
        "active_menu": "minerals"
    }
    return render_to_response('minerals.html', batch, context_instance=RequestContext(request))


def regions(request):
    batch = {
        "regions": Region.objects.all(),
        "active_menu": "regions"
    }
    return render_to_response('regions.html', batch, context_instance=RequestContext(request))


def crop_select(request):
    if request.method == "POST":
        form = CropSelectForm(request.POST)
        if form.is_valid():
            crop = form.cleaned_data.get("crop")
            return HttpResponseRedirect(reverse("region-select", kwargs={"crop_pk": crop.pk}))
    else:
        form = CropSelectForm()
    batch = {
        "form": form,
        "active_menu": "crops"
    }
    return render_to_response('analysis/crop-select.html', batch, context_instance=RequestContext(request))


def region_select(request, crop_pk):
    try:
        crop = Crop.objects.get(pk=int(crop_pk))
    except Crop.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = RegionSelectForm(request.POST)
        if form.is_valid():
            region = form.cleaned_data.get("region")
            return HttpResponseRedirect(reverse("land-size-select", kwargs={"crop_pk": crop.pk, "region_pk": region.pk}))
    else:
        form = RegionSelectForm()
    batch = {
        "form": form,
        "crop": crop,
        "active_menu": "regions"
    }
    return render_to_response('analysis/region-select.html', batch, context_instance=RequestContext(request))


def land_size_select(request, crop_pk, region_pk):
    try:
        crop = Crop.objects.get(pk=int(crop_pk))
        region = Region.objects.get(pk=int(region_pk))
    except (Crop.DoesNotExist, Region.DoesNotExist):
        raise Http404
    if request.method == "POST":
        form = LandSizeSelectForm(request.POST)
        if form.is_valid():
            land_size = form.cleaned_data.get("land_size")
            return HttpResponseRedirect(reverse("working", kwargs={"crop_pk": crop.pk, "region_pk": region.pk, "land_size": land_size}))
    else:
        form = LandSizeSelectForm()
    batch = {
        "form": form,
        "crop": crop,
        "region": region,
        "active_menu": "regions"
    }
    return render_to_response('analysis/land-size-select.html', batch, context_instance=RequestContext(request))


def working(request, crop_pk, region_pk, land_size):
    try:
        crop = Crop.objects.get(pk=int(crop_pk))
        region = Region.objects.get(pk=int(region_pk))
    except (Crop.DoesNotExist, Region.DoesNotExist):
        raise Http404
    batch = {
        "crop": crop,
        "region": region,
        "land_size": land_size,
        "active_menu": "analysis"
    }
    return render_to_response('analysis/working.html', batch, context_instance=RequestContext(request))


def results(request, crop_pk, region_pk, land_size):
    """
    Show results of computation
    """
    try:
        crop = Crop.objects.get(pk=int(crop_pk))
        region = Region.objects.get(pk=int(region_pk))
    except (Crop.DoesNotExist, Region.DoesNotExist):
        raise Http404

    average = calculate_success_rate(crop, region)

    other_crops = []
    for crp in Crop.objects.all():
        avg = calculate_success_rate(crp, region)
        other_crops.append({
            "crop": crp.name,
            "success_rate": avg
        })

    other_crops = sorted(other_crops, key=lambda k: k["success_rate"]) 
    
    batch = {
        "crop": crop,
        "region": region,
        "land_size": land_size,
        "percentage": average,
        "verdict": "Advisable" if average >= 50 else "Not Advisable",
        "other_crops": other_crops[5:],
        "active_menu": "analysis"
    }
    return render_to_response('analysis/results.html', batch, context_instance=RequestContext(request))


def add_crop(request):
    if request.method == "POST":
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Crop successfully added.")
            return HttpResponseRedirect(reverse("crops-table"))
    else:
        form = CropForm()
    batch = {
        "form": form,
        "active_menu": "crops"
    }
    return render_to_response('crud/add-crop.html', batch, context_instance=RequestContext(request))


def add_region(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Region successfully added.")
            return HttpResponseRedirect(reverse("regions"))
    else:
        form = RegionForm()
    batch = {
        "form": form,
        "active_menu": "regions"
    }
    return render_to_response('crud/add-region.html', batch, context_instance=RequestContext(request))


def add_mineral(request):
    if request.method == "POST":
        form = MineralForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mineral successfully added.")
            return HttpResponseRedirect(reverse("minerals"))
    else:
        form = MineralForm()
    batch = {
        "form": form,
        "active_menu": "minerals"
    }
    return render_to_response('crud/add-mineral.html', batch, context_instance=RequestContext(request))


def add_region_mineral(request):
    if request.method == "POST":
        form = RegionMineralsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mineral composition in region successfully added.")
            return HttpResponseRedirect(reverse("regions"))
    else:
        form = RegionMineralsForm()
    batch = {
        "form": form,
        "active_menu": "regions"
    }
    return render_to_response('crud/add-region-mineral.html', batch, context_instance=RequestContext(request))


def add_crop_mineral(request):
    if request.method == "POST":
        form = CropMineralsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mineral requirement for crop successfully added.")
            return HttpResponseRedirect(reverse("crops-table"))
    else:
        form = CropMineralsForm()
    batch = {
        "form": form,
        "active_menu": "crops"
    }
    return render_to_response('crud/add-crop-mineral.html', batch, context_instance=RequestContext(request))
