from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto, Brownie

def editar_brownie(request, pk):
    brownie = get_object_or_404(Brownie, id=pk)
    # Lógica para editar el brownie (puedes renderizar un formulario de edición)

def eliminar_brownie(request, pk):
    brownie = get_object_or_404(Brownie, id=pk)
    brownie.delete()
    return redirect('crud')  # Redirige de vuelta a la lista de brownies después de eliminar uno


def index(request):
    context = {}
    return render(request, 'pagina/index.html', context)

def contacto(request):
    context = {}
    return render(request, 'pagina/contacto.html', context)

def browniesadd(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "")
        imagen = request.FILES.get("imagen", None)  # Obtén el archivo de imagen
        precio = request.POST.get("precio", "")

        if imagen:
            # Crear una instancia del modelo Brownie y guardar los datos
            obj = Brownie(nombre=nombre, imagen=imagen, precio=precio)
            obj.save()

            context = {'mensaje': "Ok, datos grabados correctamente."}
            return render(request, 'pagina/browniesadd.html', context)
        else:
            context = {'mensaje': "Error: No se ha enviado ninguna imagen."}
            return render(request, 'pagina/browniesadd.html', context)
    else:
        context = {}
        return render(request, 'pagina/browniesadd.html', context)


def brownies_del(request,pk):
    context={}
    try:
        brownie=Brownie.objects.get(rut=pk)

        brownie.delete()
        mensaje="Datos Eliminados..."
        brownies=Brownie.objects.all()
        context={'brownies': brownies, 'mensaje': mensaje}
        return render(request, 'pagina/brownies_del.html', context)
    except:
        mensaje="Error, id no existe..."
        brownies=Brownie.objects.all()
        context={'brownies': brownies, 'mensaje': mensaje}
        return render(request, 'pagina/brownies_del.html', context)

def brownies_findEdit(request,pk):
    if pk != "":
        brownie=Brownie.objects.get(id=pk)

        context={'brownie':brownie}
        if brownie:
            return render(request, 'pagina/brownies_findEdit.html', context)
        else:
            context={'mensaje':"Error, id no existe..."}
            return render(request, 'pagina/brownies_findEdit.html', context)

def registrar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        email = request.POST.get('email', '')
        mensaje = request.POST.get('mensaje', '')

        # Guardar el contacto en la base de datos
        contacto = Contacto(nombre=nombre, email=email, mensaje=mensaje)
        contacto.save()

        # Redireccionar o mostrar mensaje de éxito
        return redirect('index')  # redirige a la página de inicio después de guardar

    return render(request, 'pagina/index.html')  # renderiza el formulario de nuevo si no es POST

def crud(request):
    brownies = Brownie.objects.all()
    context = {'brownies': brownies}
    return render(request, 'pagina/brownies_list.html', context)

def Nosotros(request):
    context = {}
    return render(request, 'pagina/Nosotros.html', context)

def BrowniesTodos(request):
    context = {}
    return render(request, 'pagina/BrowniesTodos.html', context)

def browniesUpdate(request):
    if request.method == "POST":
        pk = request.POST.get("pk", None)  # Obtener el ID del brownie a actualizar
        nombre = request.POST.get("nombre", "")
        imagen = request.FILES.get("imagen", None)  # Obtener la imagen actualizada
        precio = request.POST.get("precio", "")

        if pk:
            brownie = get_object_or_404(Brownie, id=pk)
            brownie.nombre = nombre
            if imagen:
                brownie.imagen = imagen
            brownie.precio = precio
            brownie.save()
            return redirect('crud')  # Redirigir a la lista de brownies después de actualizar

    # Si no es un POST o si falta el pk, mostrar la lista de brownies para editar
    brownies = Brownie.objects.all()
    context = {'brownies': brownies}
    return render(request, 'pagina/brownies_findEdit.html', context)

def editar_brownie(request, pk):
    brownie = get_object_or_404(Brownie, id=pk)
    context = {'brownie': brownie}
    return render(request, 'pagina/brownies_findEdit.html', context)
