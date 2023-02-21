from flask import Flask, render_template, request, jsonify,redirect
import database as dbase
from matricula import Matricula
from user import User

db = dbase.dbConnection()

app = Flask(__name__)

# http://127.0.0.1:5000/
# Mykol9988
# lester.aucapina@unl.edu.ec


@app.route('/')
def home():
    return render_template('buscar_ficha.html')

@app.route('/logout')
def logout():
    return redirect('/')

@app.route('/ver_estudiantes_matriculados')
def ver_estudiantes_matriculados():
    matriculas = db['matricula']
    def filtrar_por_matriculados(matricula,matriculado):
        return matricula['matriculado']==True
    personas = filter(lambda m: filtrar_por_matriculados(m,'matriculado'),matriculas.find())
    return render_template('ver_estudiantes.html',personas=personas)

@app.route('/aceptar_matriculas')
def acept():
    return render_template('aceptar_matriculas.html')

@app.route('/aceptar_matriculas',methods=['POST'])
def matricular():
    promedio = request.form['promedio']
    cupos = request.form['cupos']
    matriculas = db['matricula']
    todas_las_matriculas = matriculas.find()
    def filtrar_por_grado(matricula,curso_estudiante):
        return matricula['curso_estudiante']==curso_estudiante
    
    primero = filter(lambda m: filtrar_por_grado(m,'1ro básica'),todas_las_matriculas)
    segundo = filter(lambda m: filtrar_por_grado(m,'2do básica'),todas_las_matriculas)
    tercero = filter(lambda m: filtrar_por_grado(m,'3ro básica'),todas_las_matriculas)
    cuarto = filter(lambda m: filtrar_por_grado(m,'4to básica'),todas_las_matriculas)
    quito = filter(lambda m: filtrar_por_grado(m,'5to básica'),todas_las_matriculas)
    sexto = filter(lambda m: filtrar_por_grado(m,'6to básica'),todas_las_matriculas)
    septimo = filter(lambda m: filtrar_por_grado(m,'7mo básica'),todas_las_matriculas)
    octavo = filter(lambda m: filtrar_por_grado(m,'8vo colegio'),todas_las_matriculas)
    noveno = filter(lambda m: filtrar_por_grado(m,'9no colegio'),todas_las_matriculas)
    decimo = filter(lambda m: filtrar_por_grado(m,'10mo colegio'),todas_las_matriculas)
    primeroB = filter(lambda m: filtrar_por_grado(m,'1ro Bachillerato'),todas_las_matriculas)
    segundoB = filter(lambda m: filtrar_por_grado(m,'2do Bachillerato'),todas_las_matriculas)
    terceroB = filter(lambda m: filtrar_por_grado(m,'3ro Bachillerato'),todas_las_matriculas)

    def matricular_estudiantes_correctos(curso):
        cupos_admitidos = 0
        for matricula in curso:
            promedio_estudiante = matricula['promedio_estudiante']
            cupos_admitidos+=1
            if int(cupos_admitidos)<=int(cupos) and float(promedio_estudiante)>=float(promedio):
                matriculas.update_one({'cedula_estudiante':matricula['cedula_estudiante']}, {'$set': {'matriculado': True}})
        
    matricular_estudiantes_correctos(primero)
    matricular_estudiantes_correctos(segundo)
    matricular_estudiantes_correctos(tercero)
    matricular_estudiantes_correctos(cuarto)
    matricular_estudiantes_correctos(quito)
    matricular_estudiantes_correctos(sexto)
    matricular_estudiantes_correctos(septimo)
    matricular_estudiantes_correctos(octavo)
    matricular_estudiantes_correctos(noveno)
    matricular_estudiantes_correctos(decimo)
    matricular_estudiantes_correctos(primeroB)
    matricular_estudiantes_correctos(segundoB)
    matricular_estudiantes_correctos(terceroB)

    return redirect('/ver_estudiantes_matriculados')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def loginPost():
    email = request.form['email']
    contrasena = request.form['contrasena']
    usuarios = db['usuario']
    result = usuarios.find_one({'email':email})
    alert = ""
    if result:
        if result['contrasena'] == contrasena:
            alert = "Bienvenid@ "+result['nombre']
            return render_template('aceptar_matriculas.html',alert=alert)
        else:
            alert = "credenciales incorrectas"
            return render_template('login.html',alert = alert)
    else:
        alert = "No se ha registrado aun, registrese."
        return render_template('login.html',alert = alert)

@app.route('/admitir_matriculas')
def admitir_matriculas():
    return render_template('admitir_matriculas.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def registerPost():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    cedula = request.form['cedula']
    email = request.form['email']
    contrasena = request.form['contrasena']

    user = User(nombre,apellido,telefono,cedula,email,contrasena)
    usuarios = db['usuario']

    result = usuarios.find_one({'cedula':cedula})
    alert = ""
    if result:
        alert = "El usuario ya esta registrado"
        return render_template("register.html",alert = alert)
    else:
        usuarios.insert_one(user.toDBCollection())
        result = usuarios.find_one({'cedula':cedula})
        if result:
            alert = "Usuario registrado satisfactoriamente"
            return render_template('login.html',alert = alert)
        else:
            alert = "Usuario registrado satisfactoriamente"
            return render_template("register.html",alert = alert)

# http://127.0.0.1:5000/imprimir-ficha/1150579124


@app.route('/imprimir-ficha/<string:student_id>')
def ficha(student_id):
    matriculas = db['matricula']
    cedula = student_id
    result = matriculas.find_one({"cedula_estudiante": cedula})
    return render_template('imprimir_ficha.html', student=result)


@app.route('/get-estudent', methods=['POST'])
def getStudent():
    matriculas = db['matricula']
    cedula = request.form['cedula']
    result = matriculas.find_one({"cedula_estudiante": cedula})
    if result:
        return render_template('estudiante_existente.html', student=result)
    else:
        return render_template('index.html')


@app.route('/matriculas')
def getMatriculas():
    matriculas = db['matricula']
    personas = matriculas.find()
    return render_template("matriculas_registradas.html", personas=personas)


@app.route('/matricula', methods=['POST'])
def addMatricula():
    matriculas = db['matricula']

    nombre_estudiante = request.form['nombre_estudiante']
    apellido_estudiante = request.form['apellido_estudiante']
    lugar_nacimiento_estudiante = request.form['lugar_nacimiento_estudiante']
    fecha_nacimiento_estudiante = request.form['fecha_nacimiento_estudiante']
    cedula_estudiante = request.form['cedula_estudiante']
    curso_estudiante = request.form['curso_estudiante']
    contacto_estudiante = request.form['contacto_estudiante']
    email_estudiante = request.form['email_estudiante']
    promedio_estudiante = request.form['promedio_estudiante']

    nombre_representante = request.form['nombre_representante']
    apellido_representante = request.form['apellido_representante']
    edad_representante = request.form['edad_representante']
    cedula_representante = request.form['cedula_representante']
    profesion_representante = request.form['profesion_representante']
    contacto_representante = request.form['contacto_representante']
    correo_representante = request.form['correo_representante']
    lugar_trabajo_representante = request.form['lugar_trabajo_representante']

    nombre_madre = request.form['nombre_madre']
    apellido_madre = request.form['apellido_madre']
    edad_madre = request.form['edad_madre']
    instruccion_madre = request.form['instruccion_madre']
    profesion_madre = request.form['profesion_madre']
    contacto_madre = request.form['contacto_madre']
    lugar_trabajo_madre = request.form['lugar_trabajo_madre']

    nombre_padre = request.form['nombre_padre']
    apellido_padre = request.form['apellido_padre']
    edad_padre = request.form['edad_padre']
    instrucion_padre = request.form['instrucion_padre']
    profesion_padre = request.form['profesion_padre']
    lugar_trabajo_padre = request.form['lugar_trabajo_padre']
    contacto_padre = request.form['contacto_padre']

    if nombre_estudiante and apellido_estudiante and cedula_estudiante and contacto_estudiante and nombre_madre and edad_madre and instruccion_madre and profesion_madre and lugar_trabajo_madre and contacto_madre and nombre_padre and edad_padre and profesion_padre and lugar_trabajo_padre and contacto_padre:
        matricula = Matricula(promedio_estudiante,nombre_estudiante, apellido_estudiante, lugar_nacimiento_estudiante, fecha_nacimiento_estudiante, cedula_estudiante, curso_estudiante, contacto_estudiante, email_estudiante, nombre_representante, apellido_representante, edad_representante, cedula_representante, profesion_representante,
                              contacto_representante, correo_representante, lugar_trabajo_representante, nombre_madre, apellido_madre, edad_madre, instruccion_madre, profesion_madre, contacto_madre, lugar_trabajo_madre, nombre_padre, apellido_padre, instrucion_padre, profesion_padre, contacto_padre, lugar_trabajo_padre, edad_padre)
        matriculas.insert_one(matricula.toDBCollection())
        personas = matriculas.find()
        # return redirect(url_for('matriculas_registradas'))
        return render_template("matriculas_registradas.html", personas=personas, exito=True)
    else:
        return notFound()


@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True, port=4000)
