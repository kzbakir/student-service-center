from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

bachelor_urls = [path('bachelor', views.bachelor)]

postgraduate_urls = [path('postgraduate', views.postgraduate)]

abroad_urls = [path('abroad', views.abroad)]

certificate_urls = [path('certificate', views.certificate)]

hostel_urls = [path('hostel', views.hostel)]

duplicate_urls = [path('duplicate', views.DuplicateView.as_view()),
                  path('duplicate/report/<obj_id>/', views.DuplicateView.render)]

reference_urls = [path('reference', views.ReferenceView.as_view()),
                  path('reference/report/<obj_id>/', views.ReferenceView.render)]

academic_leave_urls = [path('academic-leave', views.academic_leave)]

transfer_and_recovery_urls = [path('transfer-and-recovery', views.transfer_and_recovery)]


urlpatterns = [
    path('', views.index),
] + bachelor_urls + \
    postgraduate_urls + \
    abroad_urls + \
    certificate_urls + \
    hostel_urls + \
    duplicate_urls + \
    reference_urls + \
    academic_leave_urls + \
    transfer_and_recovery_urls + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
