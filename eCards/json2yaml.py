from json import load
from yaml import dump
from shutil import copy

def j2y(filename):
    src=filename
    dst=src.replace(".json",".yaml")
    with open(src,'r') as f:
        t=load(f)

    with open(dst,'w') as f:
        f.write(dump(t))


j2y('openapi.json')
j2y('UserInfo/openapi.json')
j2y('C:/cygwin64/home/Freek Driesenaar/gitbucket/ecards/apidoc/openapi.json')

