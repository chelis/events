# -*- coding: utf-8 -*-
# @Author: Marcela Campo
# @Date:   2016-05-06 17:57:39
# @Last Modified by:   Marcela Campo
# @Last Modified time: 2016-05-09 11:57:41
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URL="postgresql://chelis:chelis@localhost:5433/seguimiento"

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
