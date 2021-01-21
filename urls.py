
from django.contrib import admin
from django.urls import path, include

# đây là đường dẫn urls
urlpatterns = [
	path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('product/', include('product.urls')),
    path('contact/', include('contact.urls')),
    
]
