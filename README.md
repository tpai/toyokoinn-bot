# Tokyo INN Bot

A Python bot checks Tokyo INN website and reserve rooms if available.

## Prerequisites

```bash
$ python3 -m venv .python
$ source .python/bin/activate
(.python) $ pip3 install -r requirements.txt
(.python) $ playwright install
```

## How to use

```bash
# run headless chrome
docker run -d -p 9222:9222 --cap-add=SYS_ADMIN justinribeiro/chrome-headless

# dev mode(open browser)
IS_PRODUCTION=false TOKYOINN_EMAIL=your_email TOKYOINN_PASSWORD=your_password PHONE_NUMBER=your_phone python3 main.py

# headless mode loop every minute
./batch.sh

# run one time on local
docker-compose up --build
```
