#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@gradiant.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain
from bob.gradiant.pad.evaluator import FacePad
from .iqm_features_extractor import IqmFeaturesExtractor
from bob.gradiant.pipelines import  RbfSvc
import numpy as np

#TO UPDATE
THRESHOLD = -0.975393
SVM_PATH = '/media/data/workspace/biometrics/experiments_data/face/pad/iqm_framerate_and_temporal_evaluation/oulu_npu/iqm-galbally/pipelines/rbfsvc-gamma1.5/configurations/grandtest/framerate25_time_capture2000/'


class IqmFacePad(FacePad):
    def __init__(self, name='IqmFacePad', threshold=THRESHOLD):
        self.features_extractor = IqmFeaturesExtractor()
        self.classifier = RbfSvc(name='RbfSvc')
        self.classifier.load(SVM_PATH)
        self.scores = []
        super(IqmFacePad, self).__init__(name, threshold)

    def process(self, im):
        dict_images = {'0': im}
        dict_features = self.features_extractor.run(dict_images)
        X = {'features': np.reshape(dict_features['0'], (1, dict_features['0'].shape[0]))}
        X = self.classifier.run(X)
        score = X['scores'][0]
        self.scores.append(score)

    def isfinished(self):
        pass

    def reset(self):
        pass

    def get_decission(self):
        average_score = np.mean(self.scores)
        self.scores = []
        if average_score < self.threshold:
            return 'ATTACK', average_score
        else:
            return 'NO_ATTACK', average_score

