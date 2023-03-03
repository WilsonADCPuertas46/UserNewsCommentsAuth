from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from authApp.models import Comment
from authApp.serializers import CommentSerializer
from authApp.permissions import IsOwner
from authApp.utils import get_valid_token_data


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        valid_data = get_valid_token_data(request)

        if valid_data['user_id'] != request.data['owner']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Comentario realizado', status=status.HTTP_201_CREATED)
    

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def put(self, request, *args, **kwargs):
        valid_data = get_valid_token_data(request)

        if valid_data['user_id'] != kwargs['owner']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().put(request, *args, **kwargs)


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def delete(self, request, *args, **kwargs):
        valid_data = get_valid_token_data(request)

        if valid_data['user_id'] != kwargs['owner']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)