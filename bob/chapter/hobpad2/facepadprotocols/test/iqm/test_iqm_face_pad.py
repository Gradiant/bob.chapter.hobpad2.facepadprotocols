#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@gradiant.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain
import unittest
from bob.chapter.hobpad2.facepadprotocols import IqmFacePad


class UnitTestIqmFacePad(unittest.TestCase):

    def test_construct_a_iqm_based_face_pad(self):

        iqm_face_pad = IqmFacePad()

