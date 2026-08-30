"""
Modelos de base de datos para CMMS
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    """Modelo de Usuario"""
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(50), default='tecnico')  # admin, supervisor, tecnico
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    ordenes_trabajo = db.relationship('OrdenTrabajo', backref='asignado_a', lazy=True)
    
    def __repr__(self):
        return f'<Usuario {self.nombre}>'


class Activo(db.Model):
    """Modelo de Activos/Equipos"""
    __tablename__ = 'activos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.Text)
    tipo = db.Column(db.String(100))  # Bomba, Motor, Compresor, etc.
    ubicacion = db.Column(db.String(200))
    estado = db.Column(db.String(50), default='operativo')  # operativo, inactivo, en_mantenimiento
    fecha_adquisicion = db.Column(db.DateTime)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    ordenes_trabajo = db.relationship('OrdenTrabajo', backref='activo', lazy=True)
    historial = db.relationship('HistorialMantenimiento', backref='activo', lazy=True)
    
    def __repr__(self):
        return f'<Activo {self.nombre}>'


class OrdenTrabajo(db.Model):
    """Modelo de Órdenes de Trabajo"""
    __tablename__ = 'ordenes_trabajo'
    
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), unique=True, nullable=False)
    activo_id = db.Column(db.Integer, db.ForeignKey('activos.id'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # preventivo, correctivo, predictivo
    descripcion = db.Column(db.Text, nullable=False)
    estado = db.Column(db.String(50), default='pendiente')  # pendiente, en_progreso, completado, cancelado
    prioridad = db.Column(db.String(50), default='normal')  # baja, normal, alta, critica
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_inicio = db.Column(db.DateTime)
    fecha_completacion = db.Column(db.DateTime)
    
    # Relaciones
    tareas = db.relationship('Tarea', backref='orden_trabajo', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<OrdenTrabajo {self.numero}>'


class Tarea(db.Model):
    """Modelo de Tareas dentro de Órdenes de Trabajo"""
    __tablename__ = 'tareas'
    
    id = db.Column(db.Integer, primary_key=True)
    orden_id = db.Column(db.Integer, db.ForeignKey('ordenes_trabajo.id'), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    completada = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Tarea {self.id}>'


class HistorialMantenimiento(db.Model):
    """Modelo de Historial de Mantenimiento"""
    __tablename__ = 'historial_mantenimiento'
    
    id = db.Column(db.Integer, primary_key=True)
    activo_id = db.Column(db.Integer, db.ForeignKey('activos.id'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # preventivo, correctivo, predictivo
    descripcion = db.Column(db.Text)
    fecha_mantenimiento = db.Column(db.DateTime, default=datetime.utcnow)
    costo = db.Column(db.Float, default=0.0)
    notas = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Historial {self.id}>'
