"""
Aplicación Flask - CMMS
"""
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import config
from models import db, Usuario, Activo, OrdenTrabajo, Tarea, HistorialMantenimiento
import os

# Crear aplicación Flask
app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')

# Cargar configuración
env = os.getenv('FLASK_ENV', 'development')
app.config.from_object(config[env])

# Inicializar base de datos
db.init_app(app)

# ==================== RUTAS ====================

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/activos', methods=['GET'])
def get_activos():
    """Obtener todos los activos"""
    activos = Activo.query.all()
    return jsonify([{
        'id': a.id,
        'nombre': a.nombre,
        'codigo': a.codigo,
        'tipo': a.tipo,
        'ubicacion': a.ubicacion,
        'estado': a.estado
    } for a in activos])

@app.route('/api/activos', methods=['POST'])
def crear_activo():
    """Crear nuevo activo"""
    data = request.get_json()
    
    nuevo_activo = Activo(
        nombre=data.get('nombre'),
        codigo=data.get('codigo'),
        descripcion=data.get('descripcion'),
        tipo=data.get('tipo'),
        ubicacion=data.get('ubicacion')
    )
    
    db.session.add(nuevo_activo)
    db.session.commit()
    
    return jsonify({'mensaje': 'Activo creado', 'id': nuevo_activo.id}), 201

@app.route('/api/ordenes', methods=['GET'])
def get_ordenes():
    """Obtener todas las órdenes de trabajo"""
    ordenes = OrdenTrabajo.query.all()
    return jsonify([{
        'id': o.id,
        'numero': o.numero,
        'activo': o.activo.nombre if o.activo else 'N/A',
        'tipo': o.tipo,
        'estado': o.estado,
        'prioridad': o.prioridad,
        'fecha_creacion': o.fecha_creacion.isoformat()
    } for o in ordenes])

@app.route('/api/ordenes', methods=['POST'])
def crear_orden():
    """Crear nueva orden de trabajo"""
    data = request.get_json()
    
    # Generar número de orden
    ultima_orden = OrdenTrabajo.query.order_by(OrdenTrabajo.id.desc()).first()
    numero = f"ORD-{(ultima_orden.id + 1 if ultima_orden else 1):05d}"
    
    nueva_orden = OrdenTrabajo(
        numero=numero,
        activo_id=data.get('activo_id'),
        tipo=data.get('tipo'),
        descripcion=data.get('descripcion'),
        prioridad=data.get('prioridad', 'normal')
    )
    
    db.session.add(nueva_orden)
    db.session.commit()
    
    return jsonify({'mensaje': 'Orden creada', 'numero': numero}), 201

@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    """Obtener estadísticas del dashboard"""
    total_activos = Activo.query.count()
    ordenes_pendientes = OrdenTrabajo.query.filter_by(estado='pendiente').count()
    ordenes_completadas = OrdenTrabajo.query.filter_by(estado='completado').count()
    activos_inactivos = Activo.query.filter_by(estado='inactivo').count()
    
    return jsonify({
        'total_activos': total_activos,
        'ordenes_pendientes': ordenes_pendientes,
        'ordenes_completadas': ordenes_completadas,
        'activos_inactivos': activos_inactivos
    })

# ==================== MANEJO DE ERRORES ====================

@app.errorhandler(404)
def no_encontrado(error):
    return jsonify({'error': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def error_servidor(error):
    return jsonify({'error': 'Error del servidor'}), 500

# ==================== INICIALIZACIÓN ====================

def crear_tablas():
    """Crear tablas si no existen"""
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        crear_tablas()
    app.run(debug=True, host='0.0.0.0', port=5000)
