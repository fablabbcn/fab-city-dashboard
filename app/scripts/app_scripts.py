# -*- encoding: utf-8 -*-

from makerlabs import fablabs_io

### DATASETS FABLABS
## generate datasets from Fablabs.io
## get datas from app DB

def test_fablab_io_json () :
    test = fablabs_io.get_fablabs_dict()
    print test
    return test