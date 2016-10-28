# -*- coding: utf-8 -*-
# 
# author: william tiria wamburu | tiriawamburu@gmail.com
#

import numpy as np

def calculate_success_rate(crop, region):
    """
    Calculate weights of all minerals, pH and rainfall
    Normalize by dividing (L+N), where L is the highest index, N is the number of inputs
    Calculate Banzhaf power index for all weights
    Calculate overall index by a version of Weighted Majority Algorithm
    Return percentage
    """
    crop_minerals = crop.mineral_requirements.all()
    weights = []
    weights.append(region.ph_high-crop.ph_high)
    weights.append(region.ph_low-crop.ph_low)
    for m in crop_minerals:
        if region.mineral_composition.filter(mineral=m.mineral).exists():
            composition = region.mineral_composition.filter(mineral=m.mineral).first()
            weights.append(composition.percentage - m.percentage)
        else:
            weights.append(m.percetage*-1)

    min_weight = min(weights)
    if min_weight <= 0:
        diff = 1 - min_weight
    else:
        diff = 0

    # Normalize
    weights = map(lambda x: x+diff, weights)

    max_weight = max(weights)

    # Calculate Banzhaf power index on normalized weights
    weights = map(lambda x: x/(max_weight+len(weights)), weights)

    # Calculate average percentage
    average = np.mean(weights) * 100
    average = int(average)

    return average
