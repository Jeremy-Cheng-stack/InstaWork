from django.urls import path
from .views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView, TeamMemberDeleteView

urlpatterns = [
    path('', TeamMemberListView.as_view(), name='team_member_list'),
    path('add/', TeamMemberCreateView.as_view(), name='team_member_add'),
    path('<int:pk>/edit/', TeamMemberUpdateView.as_view(), name='team_member_edit'),
    path('<int:pk>/delete/', TeamMemberDeleteView.as_view(),
         name='team_member_delete'),
]
