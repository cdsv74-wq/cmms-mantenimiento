/* ==================== FUNCIONES DE NAVEGACIÓN ==================== */

/**
 * Mostrar una sección y ocultar las demás
 */
function mostrar(seccionId) {
    // Ocultar todas las secciones
    const secciones = document.querySelectorAll('.section');
    secciones.forEach(sec => sec.classList.remove('active'));

    // Mostrar la sección seleccionada
    document.getElementById(seccionId).classList.add('active');

    // Actualizar menú activo
    document.querySelectorAll('.menu a').forEach(link => {
        link.classList.remove('active');
    });
    event.target.classList.add('active');

    // Cargar datos según la sección
    if (seccionId === 'dashboard') {
        cargarDashboard();
    } else if (seccionId === 'activos') {
        cargarActivos();
    } else if (seccionId === 'ordenes') {
        cargarOrdenes();
    }
}

/* ==================== DASHBOARD ==================== */

function cargarDashboard() {
    fetch('/api/dashboard')
        .then(response => response.json())
        .then(data => {
            document.getElementById('total-activos').textContent = data.total_activos;
            document.getElementById('ordenes-pendientes').textContent = data.ordenes_pendientes;
            document.getElementById('ordenes-completadas').textContent = data.ordenes_completadas;
            document.getElementById('activos-inactivos').textContent = data.activos_inactivos;
        })
        .catch(error => console.error('Error cargando dashboard:', error));
}

/* ==================== GESTIÓN DE ACTIVOS ==================== */

function cargarActivos() {
    fetch('/api/activos')
        .then(response => response.json())
        .then(data => {
            llenarTablaActivos(data);
            llenarSelectActivos(data);
        })
        .catch(error => console.error('Error cargando activos:', error));
}

function llenarTablaActivos(activos) {
    const tabla = document.getElementById('tabla-activos');
    tabla.innerHTML = '';

    if (activos.length === 0) {
        tabla.innerHTML = '<tr><td colspan="5" style="text-align: center; padding: 20px;">No hay activos registrados</td></tr>';
        return;
    }

    activos.forEach(activo => {
        const fila = document.createElement('tr');
        fila.innerHTML = `
            <td>${activo.codigo}</td>
            <td>${activo.nombre}</td>
            <td>${activo.tipo || 'N/A'}</td>
            <td>${activo.ubicacion || 'N/A'}</td>
            <td><span class="badge-${activo.estado}">${activo.estado}</span></td>
        `;
        tabla.appendChild(fila);
    });
}

function llenarSelectActivos(activos) {
    const select = document.getElementById('orden-activo');
    select.innerHTML = '<option value="">Seleccionar Activo</option>';
    
    activos.forEach(activo => {
        const option = document.createElement('option');
        option.value = activo.id;
        option.textContent = `${activo.codigo} - ${activo.nombre}`;
        select.appendChild(option);
    });
}

function mostrarFormularioActivo() {
    document.getElementById('formulario-activo').style.display = 'block';
}

function ocultarFormularioActivo() {
    document.getElementById('formulario-activo').style.display = 'none';
    limpiarFormularioActivo();
}

function limpiarFormularioActivo() {
    document.getElementById('activo-nombre').value = '';
    document.getElementById('activo-codigo').value = '';
    document.getElementById('activo-descripcion').value = '';
    document.getElementById('activo-tipo').value = '';
    document.getElementById('activo-ubicacion').value = '';
}

function guardarActivo(event) {
    event.preventDefault();

    const datos = {
        nombre: document.getElementById('activo-nombre').value,
        codigo: document.getElementById('activo-codigo').value,
        descripcion: document.getElementById('activo-descripcion').value,
        tipo: document.getElementById('activo-tipo').value,
        ubicacion: document.getElementById('activo-ubicacion').value
    };

    fetch('/api/activos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        alert('✅ Activo creado exitosamente!');
        ocultarFormularioActivo();
        cargarActivos();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('❌ Error al crear el activo');
    });
}

/* ==================== GESTIÓN DE ÓRDENES DE TRABAJO ==================== */

function cargarOrdenes() {
    // Cargar activos para el select
    cargarActivos();

    // Cargar órdenes existentes
    fetch('/api/ordenes')
        .then(response => response.json())
        .then(data => {
            llenarTablaOrdenes(data);
        })
        .catch(error => console.error('Error cargando órdenes:', error));
}

function llenarTablaOrdenes(ordenes) {
    const tabla = document.getElementById('tabla-ordenes');
    tabla.innerHTML = '';

    if (ordenes.length === 0) {
        tabla.innerHTML = '<tr><td colspan="6" style="text-align: center; padding: 20px;">No hay órdenes de trabajo</td></tr>';
        return;
    }

    ordenes.forEach(orden => {
        const fila = document.createElement('tr');
        const fecha = new Date(orden.fecha_creacion).toLocaleDateString('es-ES');
        fila.innerHTML = `
            <td><strong>${orden.numero}</strong></td>
            <td>${orden.activo}</td>
            <td>${orden.tipo}</td>
            <td><span class="badge-${orden.estado}">${orden.estado}</span></td>
            <td><span class="badge-${orden.prioridad === 'critica' ? 'danger' : orden.prioridad}">${orden.prioridad}</span></td>
            <td>${fecha}</td>
        `;
        tabla.appendChild(fila);
    });
}

function mostrarFormularioOrden() {
    document.getElementById('formulario-orden').style.display = 'block';
}

function ocultarFormularioOrden() {
    document.getElementById('formulario-orden').style.display = 'none';
    limpiarFormularioOrden();
}

function limpiarFormularioOrden() {
    document.getElementById('orden-activo').value = '';
    document.getElementById('orden-tipo').value = '';
    document.getElementById('orden-descripcion').value = '';
    document.getElementById('orden-prioridad').value = 'normal';
}

function guardarOrden(event) {
    event.preventDefault();

    const datos = {
        activo_id: document.getElementById('orden-activo').value,
        tipo: document.getElementById('orden-tipo').value,
        descripcion: document.getElementById('orden-descripcion').value,
        prioridad: document.getElementById('orden-prioridad').value
    };

    if (!datos.activo_id) {
        alert('❌ Debe seleccionar un activo');
        return;
    }

    fetch('/api/ordenes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        alert(`✅ Orden ${data.numero} creada exitosamente!`);
        ocultarFormularioOrden();
        cargarOrdenes();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('❌ Error al crear la orden');
    });
}

/* ==================== INICIALIZACIÓN ==================== */

// Cargar dashboard al iniciar
document.addEventListener('DOMContentLoaded', function() {
    cargarDashboard();
});
