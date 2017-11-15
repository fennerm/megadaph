from pytest import fixture

from fmbiopy.fmpaths import (
        any_exist,
        all_exist,
        as_paths,
        )
from fmbiopy.fmsystem import remove_all

from ..rename_megadaph_files import rename_megadaph_files

@fixture(name='filenames')
def gen_filenames(sandbox):
    filenames = as_paths([
            'lane8-s046-indexD711-D501-TCTCGCGC-AGGCTATA-A10_73_FA7_S46_L008_R'
            '2_001.fq.gz',
            'lane7-s036-indexD701-D503-ATTACTCG-AGGATAGG-C01_3_IA_EC2_S36_L007'
            '_R2_001.fq.gz'])

    filenames = [sandbox / f for f in filenames]
    for f in filenames:
        f.touch()

    return filenames


@fixture(name='expected_outputs')
def gen_expected_outputs():
    return as_paths(['FA7.R2.fq.gz', 'IAEC2.R2.fq.gz'])


def test_rename_megadaph_files(filenames, expected_outputs):
    assert all_exist(filenames)
    assert not any_exist(expected_outputs)
    rename_megadaph_files(filenames)
    assert all_exist(expected_outputs)
    remove_all(expected_outputs)