#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@gradiant.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain
from bob.gradiant.core import FeaturesExtractor
from bob.ip.qualitymeasure import galbally_iqm_features as iqm
import numpy as np
import cv2

SIZE_INPUT_IMAGE = 320 #based on REPLAYMOBILE SIZE (240x320)
def resize_image_to_default(np_image):
    return resize_image_with_side_target_size(np_image, SIZE_INPUT_IMAGE)

def resize_image_with_side_target_size(np_image, side_target_size):
    height, width = np_image.shape[:2]
    scale_factor = 1
    if height > side_target_size or width > side_target_size:
        if height > width:
            scale_factor = float(side_target_size) / height
        else:
            scale_factor = float(side_target_size) / width
    size = (int(scale_factor * width), int(scale_factor * height))
    resized_image = cv2.resize(np_image, size, interpolation=cv2.INTER_CUBIC)
    return resized_image, scale_factor

class IqmFeaturesExtractor(FeaturesExtractor):
    def __init__(self):
        super(IqmFeaturesExtractor, self).__init__()

    def run(self, dict_images, annotations = None):
        dict_features = {}
        for key, image in dict_images.iteritems():
            resized_image, factor = resize_image_to_default(image)
            image_bob_format = np.swapaxes(resized_image,0,2)
            features = iqm.compute_quality_features(image_bob_format)
            dict_features[key] = features
        return dict_features




