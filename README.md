# VJ Join Request Acceptor Bot

**A Advance Join Request Accept Bot Which Can Accept Both All Pending Join Request And New Join Request With Login Feature.**

**For New Join Request Use This Repo [Click Here](https://github.com/VJBots/VJ-Auto-Approval-Bot)**

## How To Deploy [Video Tutorial](https://youtu.be/2Unf-cLbJLY)

#### Environment Variables

- <b>`API_ID` : Get From [my.telegram.org](https://my.telegram.org)
- `API_HASH` : Get From [my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN` : Get From [BotFather](https://telegram.me/BotFather)
- `DB_URI` : Mongodb Database Url [Tutorial Watch Here](https://youtu.be/DAHRmFdw99o)
- `ADMINS` : It mean Admin/Owner Id For Broadcasting Message.
- `LOG_CHANNEL` : Log channel id start with -100xxxxxx</b>

#### Commands To Use Bot
- <b>`/start` : check bot is alive or not, know about bot
- `/accept` : accept all pending request form channel or group.
- `/login` : login your telegram account for string session
- `/logout` : logout your telegram account 
- `/broadcast` : reply this command to your broadcast message in bot.</b>

## Render Deployment

This repository includes `render.yaml` and `Procfile` for Render.

### Option 1: Blueprint deploy

1. Open Render Dashboard.
2. Select **New → Blueprint**.
3. Connect this GitHub repository.
4. Select the `main` branch.
5. Render will use the included `render.yaml` automatically.

### Option 2: Manual Web Service

- **Runtime:** Python
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT & python3 bot.py`
- **Branch:** `main`
- **Plan:** Free
- **Health Check Path:** `/`

The Flask endpoint keeps the Render Web Service port open while the Telegram bot runs in the same service.

## Update Channel [VJ Botz](https://telegram.me/vj_botz)

## Support Group [VJ Support](https://telegram.me/vj_bot_disscussion)

## Credit - [Tech VJ](https://youtube.com/@Tech_VJ)
