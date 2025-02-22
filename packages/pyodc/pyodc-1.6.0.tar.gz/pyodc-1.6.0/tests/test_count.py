import os

import pytest
from conftest import odc_modules

data_file1 = os.path.join(os.path.dirname(__file__), "data/data1.odb")


@pytest.mark.parametrize("odyssey", odc_modules)
def test_count(odyssey):
    r = odyssey.Reader(data_file1, aggregated=False)

    frames = r.frames

    assert len(frames) == 11
    assert all(t.ncolumns == 55 for t in frames)
    assert sum(t.nrows for t in frames) == 13


@pytest.mark.parametrize("odyssey", odc_modules)
def test_count_file(odyssey):
    """Check that we can open a file like object"""
    with open(data_file1, "rb") as f:
        r = odyssey.Reader(f, aggregated=False)

    frames = r.frames
    assert len(frames) == 11
    assert all(t.ncolumns == 55 for t in frames)
    assert sum(t.nrows for t in frames) == 13


@pytest.mark.parametrize("odyssey", odc_modules)
def test_count_aggregated_file(odyssey):
    """Check that we can open a file like object"""
    with open(data_file1, "rb") as f:
        r = odyssey.Reader(f, aggregated=True)

    frames = r.frames
    assert len(frames) == 1
    assert all(t.ncolumns == 55 for t in frames)
    assert sum(t.nrows for t in frames) == 13


if __name__ == "__main__":
    pytest.main()
