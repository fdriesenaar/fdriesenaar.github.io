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


copy('../Qiy-Scheme/Qiy-Node/openapi.json','openapi.json')
copy('../Qiy-Scheme/Qiy-Node/Server/openapi.json','Server')
copy('../Qiy-Scheme/Qiy-Node/Client/openapi.json','Client')
copy('../Qiy-Scheme/Qiy-Node/Controller/openapi.json','Controller')

j2y('openapi.json')
j2y('Server/openapi.json')
j2y('Client/openapi.json')
j2y('Controller/openapi.json')

