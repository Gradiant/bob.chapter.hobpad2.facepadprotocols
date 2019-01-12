#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@gradiant.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain

import os
import logging
import coloredlogs
from bob.chapter.hobpad2.facepadprotocols import parser
from shutil import copyfile

OUTPUT = 'result/chapter'


def get_logger(level='INFO'):
    logger = logging.getLogger('Retrieve Results')
    coloredlogs.install(level=level, logger=logger)
    return logger


def main():
    args = parser()

    if args.verbose:
        logger = get_logger(level='DEBUG')
    else:
        logger = get_logger(level='INFO')

    results = {'summary.html': 'doc/reproducible_research/template.html',
               'results/table_1_iqm.html':
                   'result/iqm_from_scores/AUE/oulu-npu/pipelines/iqm_from_scores/evaluation/grandtest/tables/summary/oulu-npu@grandtest_all_attacks_summary_table.html',
               'results/table_1_gradiant.html':
                   'result/gradiant_from_scores/AUE/oulu-npu/pipelines/gradiant_from_scores/evaluation/grandtest/tables/summary/oulu-npu@grandtest_all_attacks_summary_table.html',
               'results/fig_5_a_iqm.png':
                   'result/iqm_from_scores/ACE/oulu-npu/pipelines/iqm_from_scores/evaluation/grandtest/plots/framerate_and_time_comparison/matplotlib/oulu-npu@grandtest_all_attacks_ACER@EER_figure.png',
               'results/fig_5_b_gradiant.png':
                   'result/gradiant_from_scores/ACE/oulu-npu/pipelines/gradiant_from_scores/evaluation/grandtest/plots/framerate_and_time_comparison/matplotlib/oulu-npu@grandtest_all_attacks_ACER@EER_figure.png',
               'results/fig_6_a_iqm.png':
                   'result/iqm_from_scores_pretrained/ACE/oulu-npu/pipelines/iqm_from_scores_pretrained/evaluation/grandtest/plots/framerate_and_time_comparison/matplotlib/oulu-npu@grandtest_all_attacks_ACER@EER_figure.png',
               'results/fig_6_b_gradiant.png':
                   'result/gradiant_from_scores_pretrained/ACE/oulu-npu/pipelines/gradiant_from_scores_pretrained/evaluation/grandtest/plots/framerate_and_time_comparison/matplotlib/oulu-npu@grandtest_all_attacks_ACER@EER_figure.png'
               }

    for name, src in results.iteritems():
        dst = OUTPUT + '/' + name
        if not os.path.isdir(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))
        logger.debug('Retrieving {} and storing in {}'.format(name, OUTPUT))
        copyfile(src, dst)

    # TODO, set the same colors in fig_5_a_iqm as in chapter
    # TODO, add end-to-end evaluation


if __name__ == '__main__':
    main()
