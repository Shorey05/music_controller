from django.urls import path
from api.views import RoomView, CreateRoomView, GetRoom, JoinRoom, UserInRoom, LeaveRoom, RoomUpdate

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
    path('leave-room', LeaveRoom.as_view()),
    path('update-room', RoomUpdate.as_view()),
]