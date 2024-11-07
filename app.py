from flask import Flask, render_template, request
from faker import Faker
from faker.providers import DynamicProvider
import random

app = Flask(__name__)
faker = Faker('es_ES')

ProfesionProvider = DynamicProvider(
    provider_name="fake_professions",
    elements = [
            "Ingeniero en realidad aumentada",
            "Director de tecnología de drones",
            "Consultor de redes neuronales cuánticas",
            "Especialista en análisis de datos de unicornios",
            "Gerente de automatización de IA",
            "Diseñador de interfaces holográficas",
            "Coordinador de experiencias de usuario en metaverso",
            "Consultor de sostenibilidad espacial",
            "Desarrollador de algoritmos para robots autómatas",
            "Analista de tendencias en nanotecnología",
            "Médico",
            "Carpintero",
            "Analista de datos",
            "Bioquímico",
            "Farmacéutico",
            "Odontólogo",
            "Enfermero",
            "Piloto de Avión",
            "Soldado",
            "Vendedor"
        ]
)

faker.add_provider(ProfesionProvider)


@app.route('/', methods=['GET', 'POST'])
def home():
    datos_seleccionados = []
    
    # Número de usuarios a generar, por defecto 5
    num_usuarios = 5

    if request.method == 'POST':
        num_usuarios = int(request.form.get('cantidad', 5))
        datos_seleccionados = request.form.getlist('datos')

    # Genera la cantidad especificada de usuarios falsos
    usuarios_falsos = []
    
    for i in range(num_usuarios):
        usuario = {}
        if 'nombre' in datos_seleccionados:
            usuario['nombre'] = faker.first_name()
        if 'apellido' in datos_seleccionados:
            usuario['apellido'] = faker.last_name()
        if 'fecha_nacimiento' in datos_seleccionados:
            usuario['fecha_nacimiento'] = faker.date_of_birth()
        if 'direccion' in datos_seleccionados:
            usuario['direccion'] = faker.address()
        if 'email' in datos_seleccionados:
            usuario['email'] = faker.email()
        if 'telefono' in datos_seleccionados:
            usuario['telefono'] = faker.phone_number()
        if 'texto' in datos_seleccionados:
            usuario['texto'] = faker.text()
        if "profesiones" in datos_seleccionados:
            usuario["profesion"] = faker.fake_professions()
        
        usuarios_falsos.append(usuario)
        
    
    return render_template('index.html', usuarios=usuarios_falsos, cantidad=num_usuarios, datos_seleccionados=datos_seleccionados)



if __name__ == '__main__':
    app.run(debug=True)
