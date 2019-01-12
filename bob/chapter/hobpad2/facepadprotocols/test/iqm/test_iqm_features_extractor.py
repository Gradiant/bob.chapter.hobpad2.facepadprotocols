#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@gradiant.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain
import unittest
import numpy as np
from bob.chapter.hobpad2.facepadprotocols import IqmFeaturesExtractor
from bob.chapter.hobpad2.facepadprotocols.test.test_utils import TestUtils


class UnitTestIqmFeaturesExtractor(unittest.TestCase):

    def test_should_extract_18_length_feature_vector_from_horizontal_image(self):
        dict_images = {'0': TestUtils.get_numpy_image(),
                       '33': TestUtils.get_numpy_image(),
                       '66': TestUtils.get_numpy_image()}

        iqm_features_extractor = IqmFeaturesExtractor()

        dict_features = iqm_features_extractor.run(dict_images)

        self.assertEqual(len(dict_features['0']), 18)
        self.assertEqual(len(dict_features['33']), 18)
        self.assertEqual(len(dict_features['66']), 18)

    def test_should_extract_18_length_feature_vector_from_vertical_image(self):
        dict_images = {'0': np.rot90(TestUtils.get_numpy_image()),
                       '33': np.rot90(TestUtils.get_numpy_image()),
                       '66': np.rot90(TestUtils.get_numpy_image())
                       }

        iqm_features_extractor = IqmFeaturesExtractor()

        dict_features = iqm_features_extractor.run(dict_images)

        self.assertEqual(len(dict_features['0']), 18)
        self.assertEqual(len(dict_features['33']), 18)
        self.assertEqual(len(dict_features['66']), 18)
