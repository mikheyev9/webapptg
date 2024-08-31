#!/bin/bash
gunicorn -c gunicorn_config.py _backend._main:app