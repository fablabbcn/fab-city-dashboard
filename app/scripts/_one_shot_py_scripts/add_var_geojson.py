# -*- encoding: utf-8 -*-

### 
### read JSON files from current directory and
### add : 'var file_name = ' at the very beginning
### for Leaflet to read it simply

import json
import os

from os import listdir
from os.path import isfile, join


### current directory
cwd = os.getcwd()
print cwd 

### list all files in current directory
files_ = [f for f in listdir(cwd) if isfile(join(cwd, f))]

adresses_ = []

for file_ in files_:
    local_file_adress = cwd+"/"+file_
    adress_list = [file_, local_file_adress ]
    adresses_.append(adress_list)


### part to erase from file_name
to_subst = ".geo.json"

for adress_ in adresses_ :
    #open file
    path_      = adress_[1]
    file_name_ = adress_[0]
    var_to_add = file_name_.replace(to_subst, "")
    
    to_append  = "var "+ var_to_add +" = "
    print to_append, "---", path_
    print
    #data_in = open(path_, 'w')
    with open(path_, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(to_append + content)
        f.close()

