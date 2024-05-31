# system/SystemController.py
import os

from utils.smart_search import create_search_index
class SystemController:
    def __init__(self):
        pass  # 在初始化中不做任何事情

    def run(self):
        print("System Controller Run")

    def firstRequestRun(self):
        print("System Controller First Request Run")
        indexdir = "indexdir"
        if not os.path.exists(indexdir):
            os.makedirs(indexdir)
        create_search_index()