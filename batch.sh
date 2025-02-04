#!/usr/bin/env bash

while true; do
  IS_PRODUCTION=true \
    TOKYOINN_EMAIL= \
    TOKYOINN_PASSWORD= \
    PHONE_NUMBER= \
    python3 main.py
  sleep 300
done
