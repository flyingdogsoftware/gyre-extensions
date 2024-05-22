import asyncio
from aiohttp import web
import aiohttp
import requests
import shutil
import os
import sys
import threading
import subprocess  # don't remove this
from urllib.parse import urlparse
import subprocess
import os
import json

WEB_DIRECTORY = "entry"
DEFAULT_USER = "guest"
NODE_CLASS_MAPPINGS = {}
__all__ = ['NODE_CLASS_MAPPINGS']
version = "V1.0.0"
