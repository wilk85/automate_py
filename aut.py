#!/usr/bin/env python3

""" Program do automatyzacji tworzenia i pushowania image dockera na acr w azure"""
""" Pierwszy argument ktory podajemy w wywolaniu funkcji to nazwa image z tagiem np. newimage:v1
    drugi argument to nazwa naszego kontenera w azure container registry np. newcontainer lub newContainer"""

__author__      = "Sebastian Ostrowski"
__copyright__   = "Copyright 2019, Sebastian Ostrowski"

import os, sys

print(sys.argv[1])
print(sys.argv[2])

def d_build(): # buduje image dockera
    d_build_done = os.system('sudo docker build -t ' + str(sys.argv[1]) + ' .')
    return d_build_done # os.system exit code = 0 print(d_build_done))

def d_tag(): # taguje image dockera
    d_build_done = d_build()
    if d_build_done == 0:
        tagged_image = str(sys.argv[1])+ '.10'
        d_tag_done = os.system('sudo docker tag '+str(sys.argv[1]) + ' ' + tagged_image)
        os.system('sudo docker images')
    return d_tag_done, tagged_image

def acr_login(): # loguje do acr
    d_tag_done = d_tag()
    if d_tag_done == 0:
        acr_login_done = os.system('sudo az acr login --name ' + str(sys.argv[2]))
    return acr_login_done

def acr_push_image(): # pushuje image dockera do acr
    tagged_image = d_tag()[1]
    acr_login_done = acr_login()
    if acr_login_done == 0:
        acr_push_image_done = os.system('sudo docker push ' + str(sys.argv[2]).lower() + 'azurecr.io/' + str(tagged_image))
    return acr_push_image_done

acr_push_image()
