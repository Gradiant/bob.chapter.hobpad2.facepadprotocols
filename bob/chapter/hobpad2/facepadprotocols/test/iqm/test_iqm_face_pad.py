#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@gradiant.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain
import unittest
from bob.chapter.hobpad2.facepadprotocols import IqmFacePad
from bob.chapter.hobpad2.facepadprotocols.test.test_utils import TestUtils


class UnitTestIqmFacePad(unittest.TestCase):

    def test_should_run_succesfully_with_valid_values(self):
        threshold = -0.975393
        svm_model_path = TestUtils.get_svm_model_path()
        image = TestUtils.get_numpy_image()

        iqm_face_pad = IqmFacePad(svm_model_path, threshold)

        iqm_face_pad.process(image)

        assert iqm_face_pad.is_finished()
        assert iqm_face_pad.get_decision() == ('NO_ATTACK',  0.15644622200332736)

    def test_should_be_not_finished_if_not_process_image(self):
        threshold = -0.975393
        svm_model_path = TestUtils.get_svm_model_path()

        iqm_face_pad = IqmFacePad(svm_model_path,
                                  threshold=threshold)

        assert not iqm_face_pad.is_finished()

    def test_raise_an_error_if_svm_model_path_is_not_valid(self):
        threshold = -0.975393
        svm_model_path = "wrong_path"

        with self.assertRaises(IOError):
            IqmFacePad(svm_model_path, threshold=threshold)




