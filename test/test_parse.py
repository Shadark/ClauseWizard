import os
import pickle

from ClauseWizard import cwparse

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def test_parse():
    test_file = os.path.join(THIS_DIR, 'res/sample.txt')
    parseres_file = os.path.join(THIS_DIR, 'res/list_res')
    with open(test_file, 'r', encoding='iso-8859-1') as f:
        res = cwparse(f.read(), False)
        with open(parseres_file, 'rb') as resf:
            reslist = pickle.load(resf)
            assert res == reslist
