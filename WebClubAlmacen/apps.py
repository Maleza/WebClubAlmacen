from django.apps import AppConfig



class WebclubalmacenConfig(AppConfig):
    name = 'WebClubAlmacen'

    def ready(self):
        import WebClubAlmacen.signals