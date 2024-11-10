from flask import Flask, render_template, request
from faker import Faker
from faker.providers import DynamicProvider
import random

app = Flask(__name__)
faker = Faker('es_ES')


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
        if 'dni' in datos_seleccionados:
            usuario['dni'] = faker.random_number(digits=8)
        if 'cuit' in datos_seleccionados:
            documento_falso = f"{faker.random_number(digits=2)}-{faker.random_number(digits=8)}-{faker.random_number(digits=1)}"
            usuario['cuit'] = documento_falso
        if 'username' in datos_seleccionados:
            usuario['username'] = faker.user_name()
        if 'password' in datos_seleccionados:
            usuario['password'] = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
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
            usuario["profesion"] = faker.job()
        if "empresa" in datos_seleccionados:
            usuario["empresa"] = faker.company()
        if 'permisos' in datos_seleccionados:
            usuario["permisos"] = faker.random_element(elements=('admin', 'usuario', 'moderador'))
        if 'fecha' in datos_seleccionados:
            usuario["fecha"] = faker.date_this_century()
        if 'productos' in datos_seleccionados:
            usuario['productos'] = faker.word()
        if 'descripcion' in datos_seleccionados:
            usuario['descripcion'] = faker.sentence()
        if 'precio' in datos_seleccionados:
            fakePrecio = faker.random_int(min=100, max=10000)
            fakeCents = faker.random_int(min=0, max=90)
            usuario['precio'] = f'{fakePrecio}.{fakeCents}'
        if 'trueFalse' in datos_seleccionados:
            usuario['trueFalse'] = faker.pybool()
        
        usuarios_falsos.append(usuario)
        
    
    return render_template('index.html', usuarios=usuarios_falsos, cantidad=num_usuarios, datos_seleccionados=datos_seleccionados)



if __name__ == '__main__':
    app.run(debug=True)
