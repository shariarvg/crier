#!/bin/bash

export EMAIL_APP_PASSWORD=$(cat ~/.email_app_password | tr -d '[:space:]')
python3 source_write_send.py
