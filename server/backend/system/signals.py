# system/signals.py
from django.core.signals import request_started
from django.dispatch import receiver
from .SystemController import SystemController

@receiver(request_started)
def initialize_system(sender, **kwargs):
    # 确保只在首次请求时运行一次
    if not hasattr(initialize_system, 'has_run'):
        initialize_system.has_run = True
        controller = SystemController()
        controller.firstRequestRun()