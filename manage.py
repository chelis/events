# -*- coding: utf-8 -*-
# @Author: Marcela Campo
# @Date:   2016-05-06 18:56:47
# @Last Modified by:   Marcela Campo
# @Last Modified time: 2016-05-06 19:03:21
import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from server import app, db


app.config.from_object('config.DevelopmentConfig')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
