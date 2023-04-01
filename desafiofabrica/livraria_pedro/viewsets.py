from rest_framework import viewsets, status
from livraria_pedro import serializers, models
from rest_framework.response import Response


class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializer
    queryset = models.Livros.objects.all()

    def delete(self, request, id=None):
        livro = models.Livros.objects.filter(id_livro=id)
        livro.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id=None):
        livro = models.Livros.filter(id_livro=id)
        serializer = models.Livros(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientesSerializer
    queryset = models.Cliente.objects.all()

    def delete(self, request, id=None):
        cliente = models.Cliente.objects.filter(id_cliente=id)
        cliente.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id=None):
        cliente = models.Clientes.filter(id_livro=id)
        serializer = models.Cliente(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
