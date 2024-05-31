# system/apps.py
from django.apps import AppConfig




class SystemConfig(AppConfig):
    name = 'system'

    def ready(self):
        from system.SystemController import SystemController
        import system.signals  # 导入信号处理器以确保其注册
        controller = SystemController()
        controller.run()