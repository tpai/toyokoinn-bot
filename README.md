# Tokyo INN Reservation Bot

## Prerequisites

```bash
$ python3 -m venv .python
$ source .python/bin/activate
(.python) $ pip3 install -r requirements.txt
(.python) $ playwright install
```

## How to use

```bash
# dev mode
IS_PRODUCTION=false TOKYOINN_EMAIL=your_email TOKYOINN_PASSWORD=your_password PHONE_NUMBER=your_phone python3 main.py

# loop every 5 minutes
./batch.sh

# run on local
docker-compose up --build
```
