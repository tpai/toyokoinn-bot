#!/usr/bin/env bash

while true; do
  IS_PRODUCTION=false \
    TOKYOINN_EMAIL= \
    TOKYOINN_PASSWORD= \
    PHONE_NUMBER= \
    CHECKIN_DATE=2025/08/02 \
    GUESTS=1 \
    AREA=22 \
    HOTEL=00060 \
    PERSON_PER_ROOM=1 \
    python3 main.py
  sleep 60
done
