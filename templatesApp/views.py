from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    return render(request, 'templatesApp/template1.html')

def electronica(request):
    dato ={
        "titulo" : "Electronica",
        "producto" : "Mac",
        "producto2" : "iPhone",
        "producto3" : "Playstation"
    }
    return render(request, 'templatesApp/productos.html', dato)

def juguetes(request):
    dato ={
        "titulo" : "Juguetes",
        "producto" : "Auto",
        "producto2" : "Pelota de Futbol",
        "producto3" : "Figura de Acción"
    }
    return render(request, 'templatesApp/productos.html', dato)

def ropa(request):
    dato ={
        "titulo" : "Ropa",
        "producto" : "Pantalones",
        "producto2" : "Chaqueta",
        "producto3" : "Camisa"
    }
    return render(request, 'templatesApp/productos.html', dato)
