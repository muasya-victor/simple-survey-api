from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from . import serializers
from .models import Question, Response
from .serializers import QuestionSerializer, ResponseSerializer, BulkResponseSerializer
from rest_framework import status
from .serializers import ResponseSerializer
from rest_framework.response import Response as DRFResponse


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    def create(self, request, *args, **kwargs):
        # Log incoming data

        # Wrap data in `responses` if necessary
        if isinstance(request.data, list):
            request_data = {'responses': request.data}
        else:
            request_data = request.data

        # Validate and process
        serializer = BulkResponseSerializer(data=request_data)
        if not serializer.is_valid():
            return DRFResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create responses
        self.perform_create(serializer)

        return DRFResponse(serializer.data, status=status.HTTP_201_CREATED)



class QuestionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, retrieving, creating, updating, and deleting Question objects.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # Optionally, you can also override methods like create, update, or destroy if you need custom logic

