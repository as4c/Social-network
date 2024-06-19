from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, Friendship
from .serializers import UserSerializer, FriendshipSerializer
from .throttling import FriendRequestThrottle



class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        request.data['email'] = request.data.get('email', '').lower()  # to make email case insensitive
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email', '').lower()
        password = request.data.get('password', '')
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)





class UserSearchView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '').strip().lower()

        if not query:
            return User.objects.none()  # Return an empty queryset if query is empty

        if '@' in query:
            # Search by email
            return User.objects.filter(email__iexact=query)

        # Search by name
        return User.objects.filter(name__icontains=query)

    def list(self, request, *args, **kwargs):
        # Filter users by name or email and paginate the result
        queryset = self.get_queryset()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SendFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [FriendRequestThrottle]

    def post(self, request):
        to_user_id = request.data.get('to_user')
        try:
            to_user = User.objects.get(id=to_user_id)
            from_user = request.user
            if Friendship.objects.filter(from_user=from_user, to_user=to_user).exists():
                return Response({"detail": "Friend request already sent"}, status=status.HTTP_400_BAD_REQUEST)
            friendship = Friendship.objects.create(from_user=from_user, to_user=to_user, status='sent')
            serializer = FriendshipSerializer(friendship)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)




class PendingRequestsView(ListAPIView):
    serializer_class = FriendshipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Friendship.objects.filter(to_user=self.request.user, status='sent')



class FriendsListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(
            to_friend_set__from_user=self.request.user,
            to_friend_set__status='accepted'
        )




class AcceptFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            # Get the friendship request from the current user to the target user
            friendship_to_target = Friendship.objects.get(id=pk, to_user=request.user, status='sent')
            # Change the status of the friendship request from the target user to the current user
            friendship_from_target = Friendship.objects.get(
                from_user=request.user, to_user=friendship_to_target.from_user, status='sent'
            )

            # Update the status to 'accepted' for both requests
            friendship_to_target.status = 'accepted'
            friendship_from_target.status = 'accepted'

            # Save both friendship objects
            friendship_to_target.save()
            friendship_from_target.save()

            return Response({"message:" : "friend request accepted! You're now friends"}, status=status.HTTP_204_NO_CONTENT)

        except Friendship.DoesNotExist:
            return Response({"detail": "Friend request not found"}, status=status.HTTP_404_NOT_FOUND)
        



class RejectFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            friendship = Friendship.objects.get(id=pk, to_user=request.user, status='sent')
            friendship.status = 'rejected'
            friendship.save()
            return Response({"message:" : "friend request rejected!"} ,status=status.HTTP_204_NO_CONTENT)
        except Friendship.DoesNotExist:
            return Response({"detail": "Friend request not found"}, status=status.HTTP_404_NOT_FOUND)


