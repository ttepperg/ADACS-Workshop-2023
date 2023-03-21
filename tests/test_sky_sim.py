"""
Will be read by pytest
"""
import sys
from numpy import testing
sys.path.append('/Users/tepper/tutorials/ADACS-Workshop-2023/project')


def test_module_import():
    try:
        from mymodule import sky_sim
    except:
        raise AssertionError('Failed importing module')
    return


def test_get_radec():
    from mymodule import sky_sim
    answer = (14.215420962967535, 41.26916666666667)
    result = sky_sim.get_radec()
    testing.assert_allclose(answer, result, atol=1./3600.)
    return


if __name__ == "__main__":
    # introspect and run all the functions starting with 'test'
    for f in dir():
        if f.startswith('test_'):
            print(f)
            globals()[f]()
