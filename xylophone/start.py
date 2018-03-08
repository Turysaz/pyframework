#!/usr/bin/python

import os, sys

#sys.path.insert(0,
    #os.path.abspath(
        #os.path.join(
            #os.path.dirname(__file__),
            #'lib')))
#sys.path.insert(0,
#    os.path.abspath(
#        os.path.join(
#            os.path.dirname(__file__),
#            'framework')))

# ========================================

import pgw
import pygame

pygame.init()
pgw.Bootstrapper().bootstrap()
