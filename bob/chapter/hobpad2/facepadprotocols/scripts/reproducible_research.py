#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@gradiant.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain
import os
import subprocess
import logging
import coloredlogs
from bob.chapter.hobpad2.facepadprotocols.classes import parser


def get_logger():
    logger = logging.getLogger('Reproducible Research')
    coloredlogs.install(level='INFO', logger=logger)
    return logger


def main():
    verbose = ''
    args = parser()
    logger = get_logger()
    if args.verbose:
        verbose = '--verbose'

    commands = {'1- download_scores': 'bin/download_scores.py',
                '2- algorithmic_unconstrained_evaluation - iqm':
                    'bin/algorithmic_unconstrained_evaluation.py -r experiments/configuration_iqm_from_scores.py',
                '3- algorithmic_unconstrained_evaluation - gradiant':
                    'bin/algorithmic_unconstrained_evaluation.py -r experiments/configuration_gradiant_from_scores.py',
                '4- algorithmic_constrained_evaluation - iqm':
                    'bin/algorithmic_constrained_evaluation.py -r experiments/configuration_iqm_from_scores.py',
                '5- algorithmic_constrained_evaluation - gradiant':
                    'bin/algorithmic_constrained_evaluation.py -r experiments/configuration_gradiant_from_scores.py',
                '6- algorithmic_constrained_evaluation - iqm (pretrained)':
                    'bin/algorithmic_constrained_evaluation.py -r experiments/configuration_iqm_from_scores_pretrained.py',
                '7- algorithmic_constrained_evaluation - gradiant (pretrained)':
                    'bin/algorithmic_constrained_evaluation.py -r experiments/configuration_gradiant_from_scores_pretrained.py',
                '8- retrieve_results': 'bin/retrieve_results.py'
                }

    # Declaration of databases path is mandatory if we extracted features.
    # As we are using pre-calculated scores we don't need the real path of the database data
    os.environ['OULU_NPU_PATH'] = 'bin/'

    for message, cmd in sorted(commands.items()):
        logger.info('{}'.format(message))
        logger.debug('command : {}'.format(cmd))
        output = subprocess.check_output('{} {}'.format(cmd, verbose), shell=True)
        if args.verbose:
            print(output)

    del os.environ['OULU_NPU_PATH']  # Undeclare the environment variable


if __name__ == '__main__':
    main()
