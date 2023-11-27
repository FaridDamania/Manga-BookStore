
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('coupons/', include('coupons.urls')),
    path('',include('users.urls')),
    path('',include('bookshop.urls')),
    path('orders/', include('orders.urls')),
    path('payment/', include('payment.urls')),
   
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#So, when DEBUG is True, this code dynamically adds a URL pattern to serve media files.
#This is convenient during development because it allows you to access uploaded media files directly via your application's URLs.
#However, in a production environment, you would typically configure a web server (e.g., Nginx or Apache) to serve these files efficiently, rather than relying on Django's built-in development server.