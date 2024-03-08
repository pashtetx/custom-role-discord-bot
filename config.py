from configparser import ConfigParser


def load_config(path: str = "config.ini"):
    configparser = ConfigParser()
    configparser.read(path)

config = load_config()

TOKEN = config.get("Bot", "Token")
CUSTOM_ROLE_ID = config.get("Settings", "RoleId")
GUILD_ID = config.get("Settings", "GuildId")