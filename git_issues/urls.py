from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),

    path('github_issues/',views.github_issues, name='github_issues'),
]

# path('draftOrderCreate/', views.draftOrder, name='draftOrderCreate'),
#     path('createOrder_GraphQl/', views.createOrder_GraphQl,
#          name='createOrder_GraphQl'),