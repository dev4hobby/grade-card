from . import os
async def create_directory(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)