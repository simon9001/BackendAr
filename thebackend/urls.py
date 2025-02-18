"""
URL configuration for thebackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.views.i18n import JavaScriptCatalog
from accounts.views import get_csrf_token
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = "Dj-LMS Admin"

urlpatterns = [
    path("admin/", admin.site.urls),


    
    # ✅ Keep API Routes Only
    path("", include("accounts.urls")), 
    path("api/get_csrf_token/", get_csrf_token, name="get_csrf_token"),  # Ensure CSRF token retrieval

    path("i18n/", include("django.conf.urls.i18n")),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    
    path("", include("core.urls")),  # Core application
    path("jet/", include("jet.urls", "jet")),  
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),  

    path("programs/", include("course.urls")),
    path("result/", include("result.urls")),
    path("search/", include("search.urls")),
    path("quiz/", include("quiz.urls")),
    path("payments/", include("payments.urls")),
]

# ✅ Remove this line because it duplicates authentication endpoints:
# path("accounts/", include("accounts.urls"))  🚨 REMOVE THIS LINE

# Debug Mode - Static & Media Files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug Mode - Error Pages
if settings.DEBUG:
    urlpatterns += [
        path("400/", default_views.bad_request, kwargs={"exception": Exception("Bad Request!")}),
        path("403/", default_views.permission_denied, kwargs={"exception": Exception("Permission Denied")}),
        path("404/", default_views.page_not_found, kwargs={"exception": Exception("Page not Found")}),
        path("500/", default_views.server_error),
    ]

urlpatterns += staticfiles_urlpatterns()