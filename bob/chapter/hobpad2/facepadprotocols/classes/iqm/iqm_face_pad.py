#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@gradiant.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain
from bob.gradiant.pad.evaluator import FacePad
from .iqm_features_extractor import IqmFeaturesExtractor
from bob.gradiant.pipelines import  RbfSvc
import numpy as np


class IqmFacePad(FacePad):
    def __init__(self, svm_model_path, threshold, name='IqmFacePad'):
        self.features_extractor = IqmFeaturesExtractor()
        self.classifier = RbfSvc(name='RbfSvc')
        self.classifier.load(svm_model_path)
        self.scores = []
        self.threshold = threshold
        self.finished = False
        super(IqmFacePad, self).__init__(name)

    def process(self, im):
        dict_images = {'0': im}
        dict_features = self.features_extractor.run(dict_images)
        X = {'features': np.reshape(dict_features['0'], (1, dict_features['0'].shape[0]))}
        X = self.classifier.run(X)
        score = X['scores'][0]
        self.scores.append(score)
        self.finished = True

    def is_finished(self):
        return self.finished

    def reset(self):
        self.scores = []
        self.finished = False

    def get_decision(self):
        average_score = np.mean(self.scores)
        self.scores = []
        if average_score < self.threshold:
            return 'ATTACK', average_score
        else:
            return 'NO_ATTACK', average_score

