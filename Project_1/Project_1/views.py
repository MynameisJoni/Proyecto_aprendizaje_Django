from django.http import HttpResponse 
import datetime
from django.template import Template, Context, loader

# ruta para este proyecto /Users/laurasuarez/Cositas/Django/Projects/Project_1

def saludo (request): # Esta funcion sería la primera vista
    
    temasCurso = ['Plantillas', 'Modelos', 'Formularios','Vistas', 'Despliegue']
    hora = datetime.datetime.now()

    """plantilla = open("/Users/laurasuarez/Cositas/Django/Projects/Project_1/Project_1/Plantillas/Plantilla.html")
    plt = Template(plantilla.read())
    plantilla.close()"""
    
    plantilla = loader.get_template('Plantilla.html')
    
    #ctx = Context({"respuesta" : "General Kenobi!!", "hora":hora, "temas":temasCurso})
    
    saludo_final = plantilla.render({"respuesta" : "General Kenobi!!", "hora":hora, "temas":temasCurso})
        
    return HttpResponse(saludo_final)


def despedida (request):
    return HttpResponse("General Kenobi!")


def fechaActual(request):
    fecha = datetime.datetime.now()
    
    mostrar_fecha="""
        <html>
        <body>
        <h2>Fecha y hora actuales %s </h1>
        </body>
        </html>""" %fecha
        
    return HttpResponse(mostrar_fecha)


def edadActual (request, anio, edad_actual):
    #edadActual = 35 ya la pasamos por parámetro
    anios = anio - 2025
    edadFutura = edad_actual + anios
    mostrar_edad = """
        <html>
        <body>
        <h2> En el año %s tendrás %s años</h2>
        </body>
        </html>""" %(anio, edadFutura)
    
    return HttpResponse(mostrar_edad)
        

        
        
        
        
        
        
        
        
        
        
    