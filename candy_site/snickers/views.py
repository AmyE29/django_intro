

# Create your views here.

from django.views.generic import TemplateView

# Create your views here.
class SnickersHomeView(TemplateView):
    template_name = "snickers.html"
    
class AboutUsView(TemplateView):
    template_name = "about.html"

class HomePageView(TemplateView):
    template_name = "home.html"
