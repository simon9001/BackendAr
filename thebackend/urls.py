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

    # ✅ API Authentication Routes (Fixed)
    path("api/", include("accounts.urls")),  # ✅ Moves API under `/api/`

    # ✅ CSRF Token Route
    path("api/get_csrf_token/", get_csrf_token, name="get_csrf_token"),
    path("accounts/", include("django.contrib.auth.urls")),  # ✅ This includes the login view


    # ✅ Internationalization Routes
    path("i18n/", include("django.conf.urls.i18n")),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),

    # ✅ Other Applications
    path("", include("core.urls")),
    path("jet/", include("jet.urls", "jet")),
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),

    path("programs/", include("course.urls")),
    path("result/", include("result.urls")),
    path("search/", include("search.urls")),
    path("quiz/", include("quiz.urls")),
    path("payments/", include("payments.urls")),
]

# ✅ Serve Static & Media Files in Debug Mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ✅ Custom Error Pages in Debug Mode
if settings.DEBUG:
    urlpatterns += [
        path("400/", default_views.bad_request, kwargs={"exception": Exception("Bad Request!")}),
        path("403/", default_views.permission_denied, kwargs={"exception": Exception("Permission Denied!")}),
        path("404/", default_views.page_not_found, kwargs={"exception": Exception("Page not Found!")}),
        path("500/", default_views.server_error),
    ]

urlpatterns += staticfiles_urlpatterns()
