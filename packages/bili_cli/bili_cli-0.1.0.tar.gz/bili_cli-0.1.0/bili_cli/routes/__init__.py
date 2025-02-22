#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com

from . import auth
from . import history
from . import season
from . import archive
from . import episode
from . import reply
from . import album


def include_router(app):
    app.include_router(auth.router, prefix='/api/auth')
    app.include_router(history.router, prefix='/api/history')
    app.include_router(season.router, prefix='/api/season')
    app.include_router(archive.router, prefix='/api/archive')
    app.include_router(episode.router, prefix='/api/episode')
    app.include_router(reply.router, prefix='/api/reply')
    app.include_router(album.router, prefix='/api/album')
