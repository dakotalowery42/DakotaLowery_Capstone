from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home, name = 'home'),
    path('proposals/', views.proposals, name = 'proposals'),
    path('add_proposal/', views.add_proposal, name = 'add_proposal'),
    path('proposal_view/<int:id>', views.proposal_view, name = 'proposal_view'),
    path('details/<int:id>', views.see_details, name = 'see_details'),
    path('delete_task/<int:id>', views.delete_task, name = 'delete_task'),
    path('add_task/<int:id>', views.add_task, name = 'add_task'),
    path('serialized/', views.serialized, name = 'serialized'),
    path('proposal_detail/<int:pk>', views.proposal_detail, name = 'proposal_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)