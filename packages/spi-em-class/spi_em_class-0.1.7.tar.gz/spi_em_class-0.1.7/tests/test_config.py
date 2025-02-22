"""
Tests for config module
Author: Sergey Bobkov
"""

import random

from spi_em_class import config


def test_config(tmpdir):
    data_file = tmpdir.join('tmpfile.h5')
    text_file = tmpdir.join('tmpfile.ini')

    params = {
        'best_proba': False,
        'binning': random.randint(1, 4),
        'cxi_file': "some_file",
        'friedel': False,
        'logscale': True,
        'num_class': random.randint(10, 50),
        'num_rot': random.randint(10, 50),
        'q_max': random.randint(10, 50),
        'q_min': random.randint(10, 50),
    }

    config.save_config(data_file, params)
    read_params = config.load_config(data_file)

    for key in config.CONFIG_PARAMS:
        assert params[key] == read_params[key]

    config.save_text_config(text_file, params)
    read_params = config.load_text_config(text_file)

    for key in config.CONFIG_PARAMS:
        assert params[key] == read_params[key]

    def_params = config.default_config()

    for key in config.CONFIG_PARAMS:
        assert key in def_params
