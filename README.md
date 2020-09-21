# MLH Fellowship Pin Bot

Discord bot to allow Fellows to pin messages!

![Docker Image CI](https://github.com/MLH-Fellowship/pin-bot/workflows/Docker%20Image%20CI/badge.svg)

![Deploying to Google Compute Engine](https://github.com/MLH-Fellowship/pin-bot/workflows/Deploying%20to%20Google%20Compute%20Engine/badge.svg)

## Setup

Replace `"MY_TOKEN"` with the token generated in the Discord Developer Portal.

```
docker-compose build
cat TOKEN="MY_TOKEN" > .env
```

## Run

```
docker-compose up -d
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
