#!/usr/bin/python

import os, sys

sys.path.insert(0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'lib')))

sys.path.insert(0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'framework')))

# ========================================

import framework
import pygame

pygame.init()
framework.Bootstrapper().bootstrap()
