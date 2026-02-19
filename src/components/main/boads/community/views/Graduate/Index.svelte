<script>
    // @ts-ignore
    import BoardLayout from "$BoardLayout";
    import Images from "./Images.svelte";
</script>

<BoardLayout title="Información General | Egresados">
    <!-- Sección de Información General -->
    <div class="info-section">
        <h3 class="text-xl font-semibold text-[#6d0205] pt-4">
            Títulos y Diplomas
        </h3>

        <h4 class="text-lg font-semibold pt-4">Trámites del Título</h4>
        <p>Requisitos para iniciar el trámite del título universitario:</p>

        <p class="mb-4">
            El alumno deberá tener el 100% de las materias cargadas en el
            SiuGuaraní para poder iniciar dicho trámite.
        </p>
        <ul class="list-disc pl-5 mb-4">
            <li>Libre deuda de la biblioteca de la FCEyA.</li>
            <li>Libre deuda de la biblioteca central de la UNCA.</li>
            <li>Fotocopia del DNI actualizada.</li>
            <li>1 (una) fotografía 4x4 actualizada.</li>
            <li>Fotocopia de la partida de nacimiento.</li>
        </ul>

        <p class="mb-4 pt-3">
            Una vez iniciado el trámite, en el plazo de 1 (una) semana, el
            expediente pasará a la Secretaría Académica de la FCEyA para las
            correspondientes firmas. Firmado el expediente, regresará a Unidad
            Alumnos de la Facultad. Los egresados deberán acercarse
            personalmente a Unidad Alumnos en el horario de 07:00 a 13:00 hs.
            para elegir la opción de la fórmula de juramento y firmar el
            expediente de finalización de la carrera. En Unidad Alumnos se le
            hará entrega al egresado de:
        </p>

        <ul class="list-disc pl-5 mb-4">
            <li>Resolución de la Facultad</li>
            <li>Analítico Provisorio</li>
            <li>Certificado de Diploma en Trámite</li>
            <li>Certificado de Finalización de Carrera</li>
        </ul>

        <p class="mb-4 pt-2">
            Luego, el expediente pasará a la Secretaría Académica de la
            Universidad Nacional de Catamarca para su certificación
            correspondiente. El egresado, en una fecha cercana a su colación,
            deberá abonar el diploma en la Secretaría Académica de la UNCA. Una
            vez que el diploma haya sido abonado por el egresado y certificado
            en el Ministerio de Educación de la Nación, el mismo regresará a
            Unidad Alumnos de la FCEyA para que el graduado firme su respectivo
            diploma. Finalmente, el título es entregado en el Acto de Colación
            de Grado.
        </p>

        <h3 class="text-xl font-semibold text-[#6d0205] pt-6 mb-4">
            Encuestas
        </h3>
        <p class="mb-2">Encuestas para Egresados</p>
        <p class="mb-6">
            Te agradeceríamos tu participación en nuestras encuestas para
            egresados:
            <strong>
                <a
                    href="https://docs.google.com/forms/d/e/1FAIpQLSf5q7wpjHKWMieABf2fcaWTqeHvcWyUG_g0dbHTtaeGk7UZPA/viewform"
                    target="_blank"
                    class="a-oscuro hover:underline"
                >
                    Encuestas para Egresados
                </a>
            </strong>
        </p>
    </div>
</BoardLayout>

<!-- Divisor visual -->
<div class="divider"></div>

<!-- Componente de Galería de Imágenes -->
<Images />

<style>
    .info-section {
    
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
       
    }

    .divider {
        height: 2px;
        background: linear-gradient(to right, #6d0205, transparent);
        margin: 2rem 0;
        border-radius: 1px;
    }

    .a-oscuro {
        color: #6d0205;
        font-weight: 600;
        transition: color 0.3s ease;
    }

    .a-oscuro:hover {
        color: #8b0308;
        text-decoration: underline;
    }

    /* Mejorar el espaciado y tipografía */
    p {
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    ul {
        margin-bottom: 1rem;
    }

    li {
        margin-bottom: 0.5rem;
        line-height: 1.5;
    }

    h3,
    h4 {
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }

    /* Responsive improvements */
    @media (max-width: 768px) {
        .info-section {
            padding: 1rem;
            margin-bottom: 1.5rem;
        }
    }
</style>
