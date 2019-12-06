from django.apps import AppConfig


class DashboardappConfig(AppConfig):
    name = 'dashboardapp'
    def ready(self):
        import dashboardapp.signals
