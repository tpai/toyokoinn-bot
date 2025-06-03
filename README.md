# Toyoko INN Bot

A Python bot checks Tokyo INN website and reserve rooms if available.

## Prerequisites

```bash
$ python3 -m venv .python
$ source .python/bin/activate
(.python) $ pip3 install -r requirements.txt
(.python) $ playwright install-deps
(.python) $ playwright install chromium-headless-shell
```

## How to use

```bash
# run headless chrome
docker run -d -p 9222:9222 --cap-add=SYS_ADMIN --name chrome-headless --restart=always justinribeiro/chrome-headless

# run one time on local
docker-compose up --build

# inline command
(.python) $ IS_PRODUCTION=false \
TOKYOINN_EMAIL=your_email \
TOKYOINN_PASSWORD=your_password \
PHONE_NUMBER=your_phone \
CHECKIN_DATE=2025-08-07 \
CHECKOUT_DATE=2025-08-08 \
CHECKIN_TIME=22:00:00 \
ROOMS=1 \
GUESTS=2 \
ROOM_TYPE=20 \
SMOKE=noSmoking \
HOTEL=00319 \
python3 main.py
```

## Environment Variables

# Tokyo Inn Environment Variables

| Variable | Value | Description |
|----------|--------|-------------|
| `IS_PRODUCTION` | `false` | true: headless mode, false: browser on |
| `TOKYOINN_EMAIL` | `your_email` | Your Tokyo Inn account email |
| `TOKYOINN_PASSWORD` | `your_password` | Your Tokyo Inn account password |
| `PHONE_NUMBER` | `your_phone` | Your phone number |
| `CHECKIN_DATE` | `2025/08/07` | Check-in date (YYYY/MM/DD format) |
| `CHECKOUT_DATE` | `2025/08/08` | Check-out date (YYYY/MM/DD format) |
| `CHECKIN_TIME` | `22:00:00` | Check-in time |
| `ROOMS` | `1` | Number of rooms |
| `GUESTS` | `2` | Number of guests |
| `ROOM_TYPE` | `20` | Room type (10: single room, 20: double room, 30: twin room) |
| `SMOKE` | `noSmoking` | Smoking preference (smoking, noSmoking, all) |
| `HOTEL` | `00319` | Hotel code (00319: 東横INN青森駅前) |
