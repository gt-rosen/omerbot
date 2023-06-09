import re
import os
from pathlib import Path
from omerbot.bot import Bot

"""
Run the bot.

Usage:

```
python3 run.py
```
"""

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    bot_secrets = Path(dir_path).joinpath("bot_secrets.txt").read_text()
    # Get the bot token.
    token = re.search(r"token=(.*)", bot_secrets).group(1)
    # Get the Discord channel.
    channel = re.search(r"channel=(.*)", bot_secrets).group(1)
    bot = Bot(channel=int(channel))
    bot.run(token)
