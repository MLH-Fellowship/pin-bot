# MLH Fellowship Pin Bot

Discord bot to allow Fellows to pin messages!

![Build and Deploy to Google Compute Engine](https://github.com/MLH-Fellowship/pin-bot/workflows/Build%20and%20Deploy%20to%20Google%20Compute%20Engine/badge.svg)

## Setup

Replace `"MY_TOKEN"` with the token generated in the Discord Developer Portal.

```
docker build -t pin-bot .
cat TOKEN="MY_TOKEN" > .env
```

## Run

```
docker run --rm -d -p 443:443 pin-bot
```

## Usage

### Pin message

```
/pin {url}
```

### Unpin message

```
/unpin {url}
```

![Example](example.png)