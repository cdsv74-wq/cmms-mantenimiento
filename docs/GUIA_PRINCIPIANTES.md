# Guía para Principiantes - CMMS

## ¿Qué aprenderás en este proyecto?

Este proyecto CMMS es perfecto para aprender:

1. **Python y Flask** - Framework web ligero
2. **PostgreSQL** - Base de datos relacional
3. **HTML/CSS/JavaScript** - Frontend web
4. **APIs REST** - Comunicación cliente-servidor
5. **Conceptos de mantenimiento industrial**

---

## 🎯 Ejercicios Propuestos

### Nivel 1: Principiante

**Ejercicio 1.1:** Entender la estructura
- [ ] Lee cada archivo Python (app.py, models.py, config.py)
- [ ] Entiende qué hace cada línea
- [ ] Documenta en un archivo NOTAS.txt

**Ejercicio 1.2:** Agregar nuevo campo a Activos
- [ ] Abre `models.py`
- [ ] Agrega un campo `proveedor` al modelo `Activo`
- [ ] Actualiza el HTML para mostrar este campo
- [ ] Crea una migración SQL en `database/init.sql`

**Ejercicio 1.3:** Modificar estilos CSS
- [ ] Cambia los colores del sidebar
- [ ] Agrega tu propio esquema de colores
- [ ] Experimenta con `background-color`, `color`, `border-radius`

### Nivel 2: Intermedio

**Ejercicio 2.1:** Crear nueva ruta en Flask
```python
@app.route('/api/estadisticas', methods=['GET'])
def get_estadisticas():
    # Tu código aquí
    return jsonify({...})
```

**Ejercicio 2.2:** Agregar formulario de Login
- [ ] Crea `frontend/login.html`
- [ ] Implementa autenticación básica
- [ ] Guarda sesión en localStorage

**Ejercicio 2.3:** Filtrar órdenes por estado
- [ ] Modifica `llenarTablaOrdenes()` en `main.js`
- [ ] Agrega un desplegable para filtrar
- [ ] Actualiza dinámicamente la tabla

### Nivel 3: Avanzado

**Ejercicio 3.1:** Generar reportes en PDF
- [ ] Instala librería `reportlab`
- [ ] Crea ruta `/api/reportes/pdf`
- [ ] Genera PDF con historial de mantenimiento

**Ejercicio 3.2:** Gráficos del Dashboard
- [ ] Integra librería `Chart.js`
- [ ] Crea gráficos de órdenes por mes
- [ ] Muestra tendencias

**Ejercicio 3.3:** Notificaciones y Alertas
- [ ] Implementa recordatorios de mantenimiento
- [ ] Agrega sistema de emails
- [ ] Crea alertas por fecha

---

## 📖 Comandos Útiles

### Python/Flask
```bash
# Activar ambiente virtual
source venv/bin/activate

# Instalar dependencia
pip install nombre_paquete

# Ejecutar aplicación
python backend/app.py

# Ver logs
tail -f debug.log
```

### PostgreSQL
```bash
# Conectar a base de datos
psql cmms_db

# Ver tablas
\dt

# Ver datos de una tabla
SELECT * FROM activos;

# Salir
\q
```

### Git
```bash
# Ver cambios
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "descripción del cambio"

# Ver historial
git log --oneline
```

---

## 🐛 Troubleshooting (Solucionar Problemas)

### Error: "conexión rechazada por PostgreSQL"
```
Solución: 
1. Verifica que PostgreSQL está corriendo
2. Comprueba las credenciales en .env
3. Asegúrate que la BD existe: createdb cmms_db
```

### Error: "Módulo no encontrado"
```
Solución:
1. pip install -r backend/requirements.txt
2. Verifica que estés en el venv correcto
```

### Error: "Puerto 5000 ya en uso"
```
Solución:
1. Cambia el puerto en backend/app.py
2. O cierra la aplicación que usa el puerto
```

---

## 📚 Recursos de Aprendizaje

- **Python:** [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- **Flask:** [Flask Official Docs](https://flask.palletsprojects.com/)
- **PostgreSQL:** [PostgreSQL Docs](https://www.postgresql.org/docs/)
- **JavaScript:** [MDN Web Docs](https://developer.mozilla.org/es/docs/Web/JavaScript)
- **SQL:** [W3Schools SQL](https://www.w3schools.com/sql/)

---

## 💡 Consejos para Principiantes

1. **Lee el código línea por línea** - No intentes entender todo de una vez
2. **Experimenta** - Cambia cosas y ve qué pasa
3. **Usa print/console.log** - Ayuda a entender qué está pasando
4. **Haz preguntas** - En foros o con otros desarrolladores
5. **Commit frecuente** - Guarda tu progreso en Git

---

## 🎓 Próximos Pasos

Una vez domines esto, puedes:

- Aprender **Django** (framework más completo que Flask)
- Explorar **React/Vue.js** para frontend más avanzado
- Estudiar **Docker** y **Kubernetes** para deployment
- Aprender **Testing** y **CI/CD**
- Contribuir a proyectos **Open Source**

---

¡Bienvenido al mundo del desarrollo web! 🚀
