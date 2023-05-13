from django.shortcuts import render

# Create your views here.
#from heladeria.models import cliente, helado, topping, factura

def index(request):
    return render(request, 'index.html')

def tipo(request):
    if request.method == 'POST':
        tipo_helado=request.POST.get('tipo')
        print(tipo_helado)
        if tipo_helado == 'cremoso':
            return render(request, 'cremoso.html')
        elif tipo_helado == 'hielo':
            return render(request, 'hielo.html')
        else:
            return render(request, 'index.html')


def cremoso(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        tamano = request.POST['tamano']
        precio = 1
        total = precio * int(tamano)

        nombre1 = request.POST['nombre']
        email2 = request.POST['email']
        tamano2 = request.POST['tamano2']
        #      total2 = precio * int()

        cliente = clientes(nombre=nombre1, correo=email2)
        cliente.save()

        reserva = helados(tam=tamano2)
        reserva.save()

    return render(request, 'facturacremoso.html', {
        'nombre': nombre,
        'celular': celular,
        'email': email,
        'tamano': tam,
        'total': total

    })

def hielo(request):
    return render(request, 'hielo.html')

def facturacremoso(request):
    return render(request, 'facturacremoso.html')
