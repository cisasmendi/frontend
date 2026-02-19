<script>
  // @ts-ignore

  import Accordion from "$utilsMain/Accordion.svelte";
  export let open = false;
  export const courseTitle = "Diplomatura en Gestión Turística Sustentable";
  let director = "Esp. Lic. Raúl Mura";
  let inicio = "13 de abril de 2026";
  let modalidad = "Presencial";
  let duracion = "6 meses";
  let diasHorarios = "Lunes y miércoles, de 18:00 a 21:00 hs";
  let inscripcionCosto = "$40.000";
  let arancel = "6 cuotas de $70.000";

  let inscriptionLink = "https://forms.gle/38KcgmMrKjZSHErJ7";
  let qrCode = "/assets/posgrado/Diplomatura/11_qr.png";
  
  let bankDetails = {
    nombre: "FC.CS.ECON.Y ADM.",
    cuit: "30641870931",
    numeroCuenta: "31554660081889",
    alias: "FCEyA.UNCA",
    cbu: "0110466420046600818894",
    emailComprobante: "paulrasgido@eco.unca.edu.ar",
  };

  let objetivoGeneral = "Que el alumno en su proceso de formación académica adquiera aquellas competencias consideradas como fundamentales para su desenvolvimiento en la organización y gestión de emprendimientos turísticos.";

  let objetivosEspecificos = [
    "Que el alumno adquiera conocimientos básicos sobre el turismo como actividad económica y su contribución al desarrollo, visualizando la importancia de la articulación público-privado.",
    "Que el alumno reconozca a la empresa turística como unidad central de análisis en sus estudios y como lugar en el que desarrollará su trabajo. El alumno debe reconocer sus principales características, los distintos subsistemas que conforman su funcionamiento y sus relaciones con los elementos del entorno, todo ello desde el punto de vista de la dirección de la empresa turística.",
    "Que el alumno sea capaz de distinguir la importancia de la calidad y la excelencia en el sector turístico, y conocer la forma de gestionar tanto a personas como a equipos para alcanzar la competitividad de la empresa en el mercado.",
    "Que el alumno incorpore aspectos conceptuales y herramentales de marketing tradicional y digital aplicado al sector turístico para entender el funcionamiento del mercado, diseñar, posicionar y comercializar productos turísticos en forma adecuada.",
  ];

  let caracteristicas = "La Diplomatura ofrece una formación sistemática y específica en una pluralidad de contenidos propios y específicos, necesarios para desenvolverse en el mercado turístico, con el fin de profundizar los conocimientos y mejorar las calificaciones laborales incorporando herramientas de planificación, organización y gestión. Asimismo, se establecen en cada módulo orientaciones en el dictado aplicadas al destino que nos ocupa y de las características de la Provincia de Catamarca como destino emergente de acuerdo a la demanda relevada como producto de los Proyectos de Investigación, transferencia y extensión desarrollados en los últimos diez años por la Facultad de Ciencias Económicas y de Administración. La carga horaria total es de ciento ochenta (180) horas reloj las que se distribuyen en el desarrollo de clases sincrónicas y trabajo autónomo del alumno a partir de las indicaciones de cada docente-tutor.";

  let destinatarios = "Ciudadanos interesados en la gestión turística. Se contemplarán especialmente los casos de quienes posean experiencia laboral en el sector turismo.";

  let planEstudios = [
    "Turismo como actividad económica. La revolución 4.0 en los negocios y el turismo.",
    "Planificación del desarrollo de un destino turístico. Comunidad anfitriona.",
    "Organización y Gestión de empresas turísticas.",
    "Marketing turístico: Plan de negocios en la empresa turística.",
    "Calidad y competitividad turística.",
    "Taller de integración y tutorías.",
  ];

  let informes = {
    unidad: "Unidad de Formación Continua | Secretaría de Posgrado",
    direccion: "Av. José Figueroa 257",
    email: "formacioncontinua@eco.unca.edu.ar",
  };
</script>

<Accordion title={courseTitle} isOpen={open}>
  <div slot="content">
    <h1>{courseTitle}</h1>
    
    <p><strong>Director:</strong> {director}</p>
    <p><strong>Inicio:</strong> {inicio}</p>
    <p><strong>Modalidad:</strong> {modalidad}</p>
    <p><strong>Duración:</strong> {duracion}</p>
    <p><strong>Días y Horarios:</strong> {diasHorarios}</p>
    <p><strong>Inscripción:</strong> {inscripcionCosto}</p>
    <p><strong>Arancel:</strong> {arancel}</p>

     <h2>Inscripciones</h2>
    <a href={inscriptionLink} target="_blank" style="color:blue"
      >► FORMULARIO DE INSCRIPCIÓN</a
    >

       <div class="animate-slide-in-up">
      <img src={qrCode} alt="Código QR de inscripción" />
    </div>

    <h2>Datos Bancarios</h2>
    <p><strong>Nombre:</strong> {bankDetails.nombre}</p>
    <p><strong>CUIT:</strong> {bankDetails.cuit}</p>
    <p><strong>Número de cuenta:</strong> {bankDetails.numeroCuenta}</p>
    <p><strong>Alias:</strong> {bankDetails.alias}</p>
    <p><strong>CBU:</strong> {bankDetails.cbu}</p>
    <p><strong>Envío de comprobante de pago:</strong> <a href="mailto:{bankDetails.emailComprobante}">{bankDetails.emailComprobante}</a></p>

    <h2>Objetivo General</h2>
    <p>{objetivoGeneral}</p>

    <h2>Objetivos Específicos</h2>
    <ul>
      {#each objetivosEspecificos as obj}
        <li>{obj}</li>
      {/each}
    </ul>

    <h2>Características y Carga Horaria</h2>
    <p>{caracteristicas}</p>

    <h2>Destinatarios</h2>
    <p>{destinatarios}</p>

    <h2>Plan de Estudios</h2>
    <ol>
      {#each planEstudios as modulo}
        <li>{modulo}</li>
      {/each}
    </ol>

    <h2>Informes</h2>
    <p><strong>{informes.unidad}</strong></p>
    <p>{informes.direccion}</p>
    <p>Correo electrónico: <a href="mailto:{informes.email}">{informes.email}</a></p>
  </div>
</Accordion>

<style>
  h1 {
    font-weight: 600;
    font-family: "Merriweather", serif;
    font-size: 1.5rem;
    color: #6d0205;
    padding-top: 1rem;
  }
  h2 {
    font-family: "Merriweather", serif;
    font-weight: 600;
    font-size: 1.25rem;
    padding-top: 1rem;
    color: #7a1c0b;
  }
  ul, ol {
    margin-left: 1.5rem;
  }
  a {
    color: #6d0205;
    text-decoration: underline;
  }
  a:hover {
    color: #7a1c0b;
  }

</style>
