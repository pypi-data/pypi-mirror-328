"""
Tests for config module
Author: Sergey Bobkov
"""

import random
import pytest
import h5py

from spi_em_class import em_data, config


def test_check(tmpdir):
    data_file = tmpdir.join('tmpfile.h5')

    assert not em_data.check_cxi_file(data_file)

    with h5py.File(data_file, 'w') as h5file:
        h5file.require_group('entry_1/image_1')

    assert not em_data.check_cxi_file(data_file)

    with h5py.File(data_file, 'a') as h5file:
        group = h5file.require_group('entry_1/image_1')
        group.create_dataset('data', shape=(100,))

    assert em_data.check_cxi_file(data_file)

def test_convert(tmpdir):
    cxi_file = tmpdir.join('tmpcxi.h5')
    data_file = tmpdir.join('tmpdata.h5')

    params = config.default_config()

    with h5py.File(cxi_file, 'w') as h5file:
        group = h5file.require_group('entry_1/image_1')
        group.create_dataset('data', shape=(100, 20, 20), fillvalue=1)
        group.create_dataset('mask', shape=(20, 20), fillvalue=0)
        group.create_dataset('image_center', data=[10, 10, 0])

    params['cxi_file'] = cxi_file.strpath
    params['q_max'] = 5
    params['logscale'] = False

    config.save_config(data_file, params)
    assert em_data.load_convert_params(data_file) is None

    em_data.convert_cxi_data(data_file)
    convert_params = em_data.load_convert_params(data_file)
    for k in em_data.CONVERT_PARAMS:
        assert convert_params[k] == params[k]

    names = em_data.get_converted_group_names(data_file)
    assert names == ['image_1']

    assert em_data.get_num_frames(data_file, names[0]) == 100

    convert_values, convert_index = em_data.load_data_values(data_file, names[0],)
    assert (convert_values == 1).all()
    assert convert_values.shape == convert_index.shape

    convert_q_vals = em_data.load_q_values(data_file, names[0])
    assert convert_q_vals.max() <= params['q_max']

    convert_t_vals = em_data.load_t_values(data_file, names[0])
    assert convert_q_vals.shape == convert_t_vals.shape


def test_iteration(tmpdir):
    data_file = tmpdir.join('tmpdata.h5')

    params = config.default_config()
    params['cxi_file'] = 'empty'
    config.save_config(data_file, params)

    iter_params = {}
    for k in em_data.ITERATION_PARAMS:
        iter_params[k] = [random.randint(0, 100)]

    assert em_data.get_num_saved_iterations(data_file) == 0

    em_data.save_iteration_data(data_file, iter_params)
    assert em_data.get_num_saved_iterations(data_file) == 1

    em_data.save_iteration_data(data_file, iter_params)
    assert em_data.get_num_saved_iterations(data_file) == 2

    with pytest.raises(ValueError):
        em_data.load_iteration_data(data_file, 0)
    with pytest.raises(ValueError):
        em_data.load_iteration_data(data_file, 3)

    read_params = em_data.load_iteration_data(data_file, 1)
    for k in em_data.ITERATION_PARAMS:
        assert read_params[k] == iter_params[k]

    em_data.reset_data(data_file)
    assert em_data.get_num_saved_iterations(data_file) == 0
