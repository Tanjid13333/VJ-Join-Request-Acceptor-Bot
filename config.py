from os import environ

API_ID = int(environ.get("API_ID", "33796748"))
API_HASH = environ.get("API_HASH", "ff267637238b782578496c8559d3095d")
BOT_TOKEN = environ.get("BOT_TOKEN", "8659391871:AAGbtqQTVrEEPuYmD0UWbIcGzXaxsKPbJkk")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1004254771105"))
ADMINS = int(environ.get("ADMINS", "8048076527"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://tanjidislamdev_db_user:avPyDJQMtOk9n7JH@cluster0.ovc9iun.mongodb.net/?retryWrites=true&w=majority") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
