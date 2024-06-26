from django.shortcuts import render
from .models import Cliente, Cidade
from .serializer import ClienteSerializer, CidadeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def listar_clientes(request):
    if request.method == 'GET':
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClienteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
@permission_classes([AllowAny]) #Permissão total
def create_city(request):
    if request.method == 'POST':
        serializer = CidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])  # Adjust permission as necessary
def delete_city(request, pk):
    city = get_object_or_404(Cidade, pk=pk)
    city.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


    
class ClientesView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClientesDetailView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CidadeView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class CidadeDetailView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer