#!/bin/bash
exec gunicorn --config /app/gunicorn_config.py server:app
