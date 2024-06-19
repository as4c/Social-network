
from django.urls import path
from .views import (
    SignupView, 
    LoginView, 
    UserSearchView, 
    SendFriendRequestView,
    PendingRequestsView, 
    FriendsListView, 
    AcceptFriendRequestView, 
    RejectFriendRequestView
)

urlpatterns = [

    path('signup/', SignupView.as_view(), name='signup'),

    path('login/', LoginView.as_view(), name='login'),

    path('search/', UserSearchView.as_view(), name='user-search'),

    path('friend/send-request/', SendFriendRequestView.as_view(), name='send-friend-request'),

    path('friend/pending-request/', PendingRequestsView.as_view(), name='pending-requests'),

    path('friends/', FriendsListView.as_view(), name='friends-list'),

    path('friend/<int:pk>/accept-request/', AcceptFriendRequestView.as_view(), name='accept-friend-request'),

    path('friend/<int:pk>/reject-request/', RejectFriendRequestView.as_view(), name='reject-friend-request'),

]


