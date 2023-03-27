from django.urls import path, include

from exam_30_10_22.web.views import index, catalogue, \
    create_profile, details_profile, edit_profile, delete_profile, \
    create_car, edit_car, detail_car, delete_car

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('details/<int:pk>/', detail_car, name='details car'),
        path('edit/<int:pk>/', edit_car, name='edit car'),
        path('delete/<int:pk>/', delete_car, name='delete car'),
    ])),
)
