#!/usr/bin/env bash
# exit on error
set -o errexit

gunicorn app:app 