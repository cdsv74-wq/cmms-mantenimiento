# CMMS - Sistema de Gestión de Mantenimiento Computarizado

Un sistema web funcional para gestionar órdenes de trabajo, activos y mantenimiento preventivo.

## 📋 Características

- ✅ Gestión de activos/equipos
- ✅ Órdenes de trabajo (Work Orders)
- ✅ Historial de mantenimiento
- ✅ Usuarios y autenticación
- ✅ Dashboard con estadísticas

## 🛠️ Tecnologías

- **Backend:** Python + Flask
- **Frontend:** HTML + CSS + JavaScript
- **Base de Datos:** PostgreSQL
- **Otros:** SQLAlchemy ORM

## 📁 Estructura del Proyecto

```
cmms-mantenimiento/
├── backend/                 # Aplicación Flask
│   ├── app.py              # Archivo principal
│   ├── models.py           # Modelos de BD
│   ├── config.py           # Configuración
│   └── requirements.txt     # Dependencias Python
├── frontend/               # Interfaz web
│   ├── index.html          # Página principal
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── database/
│   └── init.sql            # Script inicial
└── .env.example
```

## 🚀 Instalación Rápida

### Prerequisitos
- Python 3.8+
- PostgreSQL
- Git

### Pasos

1. **Clonar repositorio**
```bash
git clone https://github.com/cdsv74-wq/cmms-mantenimiento.git
cd cmms-mantenimiento
```

2. **Crear ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r backend/requirements.txt
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Edita .env con tus datos
```

5. **Configurar base de datos**
```bash
# Crear base de datos en PostgreSQL
createdb cmms_db

# Ejecutar script de inicialización
psql cmms_db < database/init.sql
```

6. **Ejecutar aplicación**
```bash
cd backend
python app.py
```

7. **Acceder**
Abre tu navegador en: `http://localhost:5000`

## 📚 Guía para Principiantes

### ¿Qué es un CMMS?
Un Sistema de Gestión de Mantenimiento Computarizado es una herramienta para:
- Registrar equipos y máquinas (Activos)
- Crear órdenes de trabajo (mantenimiento preventivo o correctivo)
- Mantener historial de todas las acciones
- Mejorar la eficiencia operativa

### Conceptos Clave

**Activos:** Son los equipos, máquinas o instalaciones que requieren mantenimiento.

**Órdenes de Trabajo:** Son tareas de mantenimiento asignadas a un activo.

**Tipos de Mantenimiento:**
- **Preventivo:** Mantenimiento programado para evitar fallas
- **Correctivo:** Reparación cuando algo falla
- **Predictivo:** Mantenimiento basado en monitoreo

## 📝 Licencia

MIT

## ✨ Autor

Proyecto creativo desarrollado con GitHub Copilot
