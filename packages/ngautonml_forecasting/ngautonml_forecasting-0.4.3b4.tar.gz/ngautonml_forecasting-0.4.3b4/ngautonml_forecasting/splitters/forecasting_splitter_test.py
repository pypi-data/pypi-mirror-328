'''Tests for sampled_splitter.py'''

# Copyright (c) 2023 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype as is_datetime

from ngautonml.config_components.dataset_config import DatasetConfig
from ngautonml.problem_def.cross_validation_config import CrossValidationConfig
from ngautonml.problem_def.problem_def import ProblemDefinition
from ngautonml.wrangler.dataset import Dataset, DatasetKeys
from .forecasting_splitter import ForecastingSplitter

# pylint: disable=missing-function-docstring, duplicate-code


TEST_PROBLEM_DEF = {
    'dataset': {
        'config': 'ignore',
        'column_roles': {
            'time': {'name': 'a'},
            'target': {'name': 'c'}
        }
    },
    'problem_type': {
        'task': 'forecasting'
    },
    'forecasting': {
        'horizon': 30,
        'input_size': 90,
        'frequency': 'ME'
    }
}


def test_split_sunny_day() -> None:
    problem_def = ProblemDefinition(TEST_PROBLEM_DEF)
    dataset_config = problem_def.get_conf(problem_def.Keys.DATASET)
    assert isinstance(dataset_config, DatasetConfig)
    dataframe = pd.DataFrame({
        'a': range(1, 1001),
        'b': range(1001, 2001),
        'c': range(2001, 3001)})
    data = Dataset(metadata=dataset_config.metadata, **{
        'dataframe': dataframe,
        'static_exogenous': None})

    dut = ForecastingSplitter(cv_config=CrossValidationConfig({}))

    dataset_config = problem_def.get_conf(problem_def.Keys.DATASET)
    assert isinstance(dataset_config, DatasetConfig)

    got = dut.split(dataset=data, dataset_config=dataset_config)
    assert len(got.folds) == 1

    assert got.folds[0].train.dataframe.shape == (970, 3)
    assert got.folds[0].validate.dataframe.shape == (90, 3)
    assert got.ground_truth is not None
    assert got.ground_truth.ground_truth.shape == (30, 3)

    # Confirm that order is preserved.
    assert got.folds[0].train[DatasetKeys.DATAFRAME.value].index[599] == 599


def test_datetime_parse() -> None:
    problem_def = ProblemDefinition(TEST_PROBLEM_DEF)
    dataset_config = problem_def.get_conf(problem_def.Keys.DATASET)
    assert isinstance(dataset_config, DatasetConfig)

    dataframe = pd.DataFrame({
        'a': ['2013-12-22', '2013-12-23', '2013-12-24'],
        'b': range(1000, 1003),
        'c': range(2000, 2003)})
    data = Dataset(metadata=dataset_config.metadata, **{
        'dataframe': dataframe,
        'static_exogenous': None})

    dut = ForecastingSplitter(cv_config=CrossValidationConfig({}))

    dataset_config = problem_def.get_conf(problem_def.Keys.DATASET)
    assert isinstance(dataset_config, DatasetConfig)

    got = dut.split(dataset=data, dataset_config=dataset_config)
    assert len(got.folds) == 1
    assert is_datetime(got.folds[0].train.get_dataframe()['a'])
    assert is_datetime(got.folds[0].validate.get_dataframe()['a'])
    assert got.ground_truth is not None
    assert is_datetime(got.ground_truth.ground_truth['a'])
