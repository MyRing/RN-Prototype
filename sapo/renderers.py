from django_medusa.renderers import StaticSiteRenderer

class HomeRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/",
            "/pricing/",
            "/tos/",
            "/privacy/",
            "/aup/",
            "/404error.html",
        ])

renderers = [HomeRenderer, ]