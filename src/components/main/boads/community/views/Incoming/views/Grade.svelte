<script>
    import { onMount } from "svelte";
    let color = "grey";

    onMount(() => {
        setInterval(() => {
            color = color === "orange" ? "grey" : "orange";
        }, 1000); // Cambia cada 2 segundos
    });
</script>

<ul class="list-disc pl-5">
    <li>Contador Público</li>
    <li>Licenciatura en Administración</li>
</ul>

<h4 class="text-lg font-semibold pt-2">APERTURA DE INSCRIPCIONES</h4>
<p class="mb-4 pt-2">
    Les informamos que el período de preinscripción estará habilitado desde el 1
    de diciembre de 2025 hasta el 23 de diciembre de 2025, y se reanudará del 2
    de febrero al 11 de febrero de 2026.
</p>
<p class="mb-4 pt-2">
    Todas las novedades y actualizaciones se publicarán en el sitio oficial <strong
    >
        <a class="text-blue-600 s-HL7iPF8fmwQi" href="https://eco.unca.edu.ar/"
            >eco.unca.edu.ar</a
        >
    </strong> y en nuestras redes sociales (Facebook e Instagram).
</p>

<div class="flex items-center gap-2">
    <h4 class="text-lg font-semibold pt-2">Pre-Inscripción</h4>
    <!-- <h4 class="pt-2" style="color: {color};">
        Prórroga hasta el 28 de febrero
    </h4>-->
</div>

<p class="mb-4 pt-2">
    Para hacer la preinscripción debes contar con una cuenta personal de correo
    electrónico que se encuentre activa.
</p>
<p class="mb-4 pt-2">
    Deberás ingresar a <strong
        ><a
            class="text-blue-600 s-HL7iPF8fmwQi"
            href="http://preinscripcion.unca.edu.ar"
            target="_blank">preinscripcion.unca.edu.ar</a
        ></strong
    > (disponible a partir del 01 de diciembre de 2025) y completar el formulario
    con todos los datos solicitados, cargar la documentación requerida, y seleccionar
    el día y horario para concurrir a la Facultad para la verificación y preinscripción
    definitiva. Es fundamental no cometer errores en la información ingresada, especialmente
    en los datos de contacto (teléfonos y email).
</p>

<h4 class="text-lg font-semibold pt-2">REQUISITOS</h4>
<p class="mb-4 pt-2">
    La documentación que deberás cargar y presentar para la verificación y
    preinscripción definitiva es la siguiente:
</p>
<ul class="list-disc pl-5">
    <li>
        Constancia/Formulario de preinscripción emitido por el sistema
        SIU-GUARANI.
    </li>
    <li>DNI o pasaporte (anverso y reverso).</li>
    <li>Título del nivel secundario o constancia de título en trámite.</li>
    <li>Certificación de adeudamiento de materias (máximo 2).</li>
    <li>Foto tipo carnet.</li>
    <li>Partida de nacimiento legalizada.</li>
    <li>Constancia de CUIL.</li>
</ul>

<h4 class="text-lg font-semibold pt-2">
    MODALIDAD DE PRESENTACIÓN DE LA DOCUMENTACIÓN
</h4>

<p class="mb-4 pt-2">
    PRESENCIAL: En Unidad Alumnos de la Facultad. Dirección: Maestro Quiroga 51
    - Planta Alta.
</p>

<h4 class="text-lg font-semibold pt-2">
    FECHAS PARA PRESENTAR LA DOCUMENTACIÓN
</h4>
<p></p>
<p class="mb-4 pt-2">
    Del 01 de diciembre al 23 de diciembre y del 02 de febrero al 11 de febrero.
</p>

<h4 class="text-lg font-semibold pt-2">
    INGRESANTES CON MATERIAS PENDIENTES DEL SECUNDARIO
</h4>
<p class="mb-4 pt-2">
    Fecha límite para rendir asignaturas pendientes: 31 de mayo de 2026.
</p>

<h4 class="text-lg font-semibold pt-2">ACREDITACIÓN DE CONOCIMIENTOS</h4>
<p class="mb-4 pt-2">
    El plan de estudios prevé un examen de acreditación de conocimientos en
    Matemáticas y Contabilidad para nivelar los conocimientos de los
    ingresantes.
</p>

<h4 class="text-lg font-semibold pt-2">CURSO DE NIVELACIÓN PRESENCIAL</h4>
<p class="mb-4 pt-2">
    El Curso de Nivelación 2026 es de carácter VOLUNTARIO y está dirigido a
    quienes lo requieran.
</p>

<h3 class="text-xl font-semibold pt-4 text-[#6d0205]">
    Programa ingreso 2026 <a
        class="text-xl font-semibold pt-4 text-blue-600"
        href="/assets/pdf/ingresantes/Programas Ingreso 2026.pdf"
        target="_blank"
    >
        Descargar programa
    </a>
</h3>
<!--<ul class="list-disc pl-5">
    <li>
        Matemáticas | <strong
            ><a
                href="/assets/pdf/ingresantes/programa-matematicas-2025.pdf"
                class="text-blue-600 s-HL7iPF8fmwQi"
                target="_blank">Ver Programa</a
            ></strong
        >
    </li>
    <li>
        Contabilidad | <strong>
            <a
                href="/assets/pdf/ingresantes/programa-contabilidad-2025.pdf"
                class="text-blue-600 s-HL7iPF8fmwQi"
                target="_blank">Ver Programa</a
            ></strong
        >
    </li>
</ul>-->
<p class="mb-4 pt-2">
    El curso de nivelación se dictará de manera presencial en las instalaciones
    de la Facultad de Ciencias Económicas y de Administración (FCEyA) y, de
    forma complementaria, a través de la plataforma Económicas Virtual.
</p>

<h4 class="text-lg font-semibold pt-2">INFORMES E INSCRIPCIÓN</h4>
<p class="mb-4 pt-2">
    Secretaría Académica, Facultad de Ciencias Económicas y de Administración –
    UNCA
</p>
<a
    class="text-blue-600 s-HL7iPF8fmwQi"
    href="mailto:ingreso2025@eco.unca.edu.ar">Ingreso2026@eco.unca.edu.ar</a
>

<p class="pt-2">Unidad Alumnos</p>

<a class="text-blue-600 s-HL7iPF8fmwQi" href="tel:+543836014652">
    Teléfono: +54 383 6014652</a
>
