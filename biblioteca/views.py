from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from biblioteca.models import Autor, Libro
from biblioteca.serializers import AutorSerializer, LibroSerializer


############Autor##############
@api_view(['POST','PUT'])
def crear_autor(request):
    datos_autor_deserializado = AutorSerializer(data=request.data)

    if datos_autor_deserializado.is_valid(): # Validar básico
        datos_autor_deserializado.save() # Guardar
        return Response(datos_autor_deserializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(datos_autor_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def modificar_autor(request, id):
    try:
        autor_seleccionado = Autor.objects.get(id=id)
        serializado = AutorSerializer(autor_seleccionado, data=request.data) # request.data = datos modificados desde frontend

        if serializado.is_valid(): # Verifica si cumple con los datos básicos
            serializado.save()
            return Response(serializado.data, status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_autor(request, id):
    try:
        autor_obtenido = Autor.objects.get(id=id)
        autor_obtenido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def listar_autores(request):
    try:
        listado_autor = Autor.objects.all()  # SELECT * FROM cliente;
        serializado = AutorSerializer(listado_autor, many=True)  # Convertimos a JSON

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_autor(request, id):
    try:
        autor_obtenido = Autor.objects.get(id=id)
        serializado = AutorSerializer(autor_obtenido, many=True) # Al ser 1 resultado es many=False

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)




#########LIBRO##########


@api_view(['POST','PUT'])
def crear_libro(request):
    datos_libro_deserializado = LibroSerializer(data=request.data)

    if datos_libro_deserializado.is_valid(): # Validar básico
        datos_libro_deserializado.save() # Guardar
        return Response(datos_libro_deserializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(datos_libro_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def modificar_libro(request, id):
    try:
        libro_seleccionado = Libro.objects.get(id=id)
        serializado = LibroSerializer(libro_seleccionado, data=request.data) # request.data = datos modificados desde frontend

        if serializado.is_valid(): # Verifica si cumple con los datos básicos
            serializado.save()
            return Response(serializado.data, status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminar_libro(request, id):
    try:
        libro_obtenido = Libro.objects.get(id=id)
        libro_obtenido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def listar_libros(request):
    try:
        listado_libro = Libro.objects.all()  # SELECT * FROM cliente;
        serializado = LibroSerializer(listado_libro, many=True)  # Convertimos a JSON

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_libro(request, id):
    try:
        libro_obtenido = Libro.objects.get(id=id)
        serializado = LibroSerializer(libro_obtenido, many=True) # Al ser 1 resultado es many=False

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
