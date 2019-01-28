import json
import os
import pickle

from ClauseWizard import cwformat

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def test_format():
    parseres_file = os.path.join(THIS_DIR, 'res/list_res')
    formatres_file = os.path.join(THIS_DIR, 'res/json_res.json')
    with open(parseres_file, 'rb') as resf:
        res = pickle.load(resf)
        res_format = cwformat(res)
        with open(formatres_file, 'r', encoding='utf-8') as jsonf:
            res_json = json.loads(jsonf.read())
            assert json.loads(json.dumps(res_format, indent=2, ensure_ascii=False)) == res_json
