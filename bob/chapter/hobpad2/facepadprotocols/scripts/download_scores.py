#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@gradiant.org>
# Copyright (C) 2017 Gradiant, Vigo, Spain
import os
import shutil
import logging
import coloredlogs
from bob.chapter.hobpad2.facepadprotocols import parser
import subprocess

SCORES_URL = 'https://portal.gradiant.org/GradBox/index.php/s/48E0XAaydabvZ2c/download'
SCORES_FOLDER = 'scores/oulu-npu/'


def is_already_downloaded():
    already_downloaded = False
    if os.path.isdir(SCORES_FOLDER):
        already_downloaded = True
    return already_downloaded


def get_logger(level='INFO'):
    logger = logging.getLogger('Download scores')
    coloredlogs.install(level=level, logger=logger)
    return logger


def main():
    args = parser()

    if args.verbose:
        quiet = ''
        logger = get_logger(level='DEBUG')
    else:
        quiet = '-q'
        logger = get_logger(level='INFO')

    if not is_already_downloaded():
        tmp_path = 'tmp'
        if not os.path.isdir(tmp_path):
            os.makedirs(tmp_path)

        name_zip = 'hobpad2_chapter14_scores'
        dest_path_zip = os.path.join(tmp_path, '{}.zip'.format(name_zip))

        if not os.path.isdir('scores'):
            os.makedirs('scores')

        commands = {'1-downloading': 'wget {} -O {} {}'.format(SCORES_URL, dest_path_zip, quiet),
                    '2-unzipping': 'unzip {} -d {}'.format(dest_path_zip, tmp_path),
                    '3-moving to scores folder': 'mv {}/{}/* scores'.format(tmp_path, name_zip)}

        for message, cmd in sorted(commands.iteritems()):
            logger.debug('{}...'.format(message))
            logger.debug('command : {}'.format(cmd))

            output = subprocess.check_output(cmd, shell=True)
            if args.verbose:
                print(output)
        if os.path.isdir(tmp_path):
            shutil.rmtree(tmp_path)
    else:
        logger.debug('The score files are already downloaded in {}'.format(SCORES_FOLDER))


if __name__ == '__main__':
    main()
