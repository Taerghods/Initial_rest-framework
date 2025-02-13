from django.shortcuts import get_object_or_404
from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from weblog.api.v1.serializer import *
from weblog.models import *



class CategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]
    model = Category
    serializer_class = CategorySerializer

    def get(self, request, id=None, *args, **kwargs):
        if id is None:
            model_list = self.model.objects.all()
            serializer = self.serializer_class(model_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        model_obj = get_object_or_404(self.model, pk=id)
        serializer = self.serializer_class(model_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        body_req = request.data
        serializer = self.serializer_class(data=body_req)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"created successfully"}, status=status.HTTP_201_CREATED)

    def put(self, request, id=None, *args, **kwargs):
        model_obj = get_object_or_404(self.model, pk=id)
        body_req = request.data
        serializer = self.serializer_class(model_obj, data=body_req)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'updated successfully'}, status=status.HTTP_200_OK)


    def patch(self, request, id=None, *args, **kwargs):
        model_obj = get_object_or_404(self.model, pk=id)
        body_req = request.data
        serializer = self.serializer_class(model_obj, data=body_req, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'updated successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, id=None, *args, **kwargs):
        model_obj = get_object_or_404(self.model, pk=id)
        model_obj.delete()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_200_OK)

class ArticleListGenericAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

