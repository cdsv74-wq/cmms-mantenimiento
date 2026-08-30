-- Script de inicialización de Base de Datos CMMS
-- Ejecutar: psql cmms_db < database/init.sql

-- ==================== TABLA USUARIOS ====================
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    rol VARCHAR(50) DEFAULT 'tecnico',
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==================== TABLA ACTIVOS ====================
CREATE TABLE IF NOT EXISTS activos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    codigo VARCHAR(50) UNIQUE NOT NULL,
    descripcion TEXT,
    tipo VARCHAR(100),
    ubicacion VARCHAR(200),
    estado VARCHAR(50) DEFAULT 'operativo',
    fecha_adquisicion TIMESTAMP,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==================== TABLA ÓRDENES DE TRABAJO ====================
CREATE TABLE IF NOT EXISTS ordenes_trabajo (
    id SERIAL PRIMARY KEY,
    numero VARCHAR(50) UNIQUE NOT NULL,
    activo_id INTEGER NOT NULL REFERENCES activos(id),
    tipo VARCHAR(50) NOT NULL,
    descripcion TEXT NOT NULL,
    estado VARCHAR(50) DEFAULT 'pendiente',
    prioridad VARCHAR(50) DEFAULT 'normal',
    usuario_id INTEGER REFERENCES usuarios(id),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_inicio TIMESTAMP,
    fecha_completacion TIMESTAMP
);

-- ==================== TABLA TAREAS ====================
CREATE TABLE IF NOT EXISTS tareas (
    id SERIAL PRIMARY KEY,
    orden_id INTEGER NOT NULL REFERENCES ordenes_trabajo(id) ON DELETE CASCADE,
    descripcion TEXT NOT NULL,
    completada BOOLEAN DEFAULT FALSE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==================== TABLA HISTORIAL ====================
CREATE TABLE IF NOT EXISTS historial_mantenimiento (
    id SERIAL PRIMARY KEY,
    activo_id INTEGER NOT NULL REFERENCES activos(id),
    tipo VARCHAR(50) NOT NULL,
    descripcion TEXT,
    fecha_mantenimiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    costo DECIMAL(10, 2) DEFAULT 0.00,
    notas TEXT
);

-- ==================== CREAR ÍNDICES ====================
CREATE INDEX idx_ordenes_activo ON ordenes_trabajo(activo_id);
CREATE INDEX idx_ordenes_usuario ON ordenes_trabajo(usuario_id);
CREATE INDEX idx_ordenes_estado ON ordenes_trabajo(estado);
CREATE INDEX idx_historial_activo ON historial_mantenimiento(activo_id);

-- ==================== DATOS DE PRUEBA ====================
-- Usuario Admin
INSERT INTO usuarios (nombre, email, contraseña, rol, activo) 
VALUES ('Admin', 'admin@cmms.local', 'admin123', 'admin', TRUE);

-- Activos de ejemplo
INSERT INTO activos (nombre, codigo, tipo, ubicacion, estado)
VALUES 
('Bomba Centrífuga', 'ACT-001', 'Bomba', 'Planta A', 'operativo'),
('Motor Eléctrico', 'ACT-002', 'Motor', 'Planta A', 'operativo'),
('Compresor de Aire', 'ACT-003', 'Compresor', 'Planta B', 'operativo');

-- Orden de trabajo de ejemplo
INSERT INTO ordenes_trabajo (numero, activo_id, tipo, descripcion, estado, prioridad)
VALUES ('ORD-00001', 1, 'preventivo', 'Mantenimiento mensual de la bomba', 'pendiente', 'normal');

-- Historial de ejemplo
INSERT INTO historial_mantenimiento (activo_id, tipo, descripcion, costo)
VALUES (1, 'preventivo', 'Cambio de aceite y filtros', 150.00);
