# system/SystemController.py
import os
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