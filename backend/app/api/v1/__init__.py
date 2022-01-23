#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from backend.app.api.v1.user import user

v1 = APIRouter(prefix='/v1')

v1.include_router(user, tags=['用户'])