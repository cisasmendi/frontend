<script>
  // @ts-ignore
  import Accordion from "$utilsMain/Accordion.svelte";
  let imageUrl = "/assets/posgrado/Cursos de Posgrado/9.png";
  let qrCode = "/assets/posgrado/Cursos de Posgrado/9_qr.png";

  export const courseTitle =
    "Formación y Empleo en Tecnologías de Datos: Descubre Power BI";
  let startDate = "08 de Octubre 2024";
  let modality = "Modalidad a Distancia";
  let professors = ["Mg. Lic. Salomé Martini", "Lic. Nicolás San Marco"];
  let objectivesGeneral =
    "Formar profesionales capacitados en el uso de Power BI para la recolección, limpieza, visualización y análisis de datos, con el fin de tomar decisiones estratégicas basadas en datos en diferentes industrias.";
  let objectivesSpecific = [
    "Capacitar a los estudiantes en el uso de Power BI.",
    "Fomentar la comprensión de los conceptos fundamentales de ingeniería de datos, modelado, gestión de proyectos y visualización.",
    "Proporcionar a los estudiantes la oportunidad de trabajar en proyectos prácticos y reales para aplicar sus habilidades en entornos empresariales simulados.",
    "Propiciar oportunidades de trabajo para los graduados del programa, colaborando con empresas y organizaciones que valoran el talento en inteligencia de negocios.",
  ];
  let schedule = {
    totalClasses: 16,
    classDuration: "2 hs",
    weeks: 8,
    totalHours: 80,
    synchronousHours: 32,
    asynchronousHours: 48,
    platform: "Campus de la Facultad",
  };
  let methodology = [
    "Enfoque práctico y orientado a la aplicación.",
    "Introducción gradual a los conceptos clave de análisis de datos y Power BI.",
    "Ejercicios y proyectos prácticos.",
    "Manipulación y visualización de datos reales.",
    "Participación en foros de debate, actividades colaborativas y trabajo en equipo.",
    "Trabajo Final (TF) para integrar los conocimientos adquiridos.",
  ];
  let evaluationCriteria = [
    "Participar semanalmente de las actividades propuestas.",
    "75% de asistencia, considerando la participación en las actividades.",
    "Aprobación de la actividad integradora correspondiente.",
  ];
  let targetAudience = [
    "Docentes de las carreras en Ciencias Económicas.",
    "Público en general interesado.",
  ];
  let admissionRequirements = [
    "Conocimientos básicos de informática.",
    "Familiaridad con conceptos básicos de matemáticas y estadísticas es deseable pero no obligatorio.",
    "Título universitario o constancia de título en trámite.",
  ];
  let expectedOutcomes =
    "Los participantes finalizarán el curso con una comprensión sólida de los conceptos básicos de análisis de datos y la capacidad de utilizar Power BI para transformar datos en visualizaciones informativas.";
  let cost = {
    payments: 2,
    paymentAmount: "$40.000",
    paymentMethod: "Transferencia",
    bankDetails: {
      alias: "FCEyA.UNCA",
      accountNumber: "31554660081889",
      cbu: "0110466420046600818894",
      name: "FC.CS.ECON.Y ADM.",
      cuit: "30641870931",
    },
  };
  let contacts = {
    email: "formacioncontinua@eco.unca.edu.ar",
    address: "Av. José Figueroa 257. SFV de Catamarca. Catamarca.",
    inscriptionEmail: "lahumada@eco.unca.edu.ar",
  };
  let inscriptionDeadline = "25 de septiembre";
  export let open = false; // Controla si el acordeón está abierto o cerrado
</script>

<Accordion
  title={"Formación y Empleo en Tecnologías de Datos: Descubre Power Bi"}
  disabled={true}
  isOpen={open}
>
  <div slot="content">
    <div class="animate-slide-in-up">
      <img
           src={imageUrl}
           alt="Prototipo de imagen"
            class="transition-all duration-300 hover:scale-105 w-full rounded-lg mb-4 ml-4  max-w-[800px]"
      />
 </div>

    <h1>{courseTitle}</h1>
    <p>INICIO DE CLASES: {startDate} | {modality}</p>

    <h2>Docentes a cargo</h2>
    <ul>
      {#each professors as professor}
        <li>{professor}</li>
      {/each}
    </ul>

    <h2>Objetivos</h2>
    <h3>Objetivo General</h3>
    <p>{objectivesGeneral}</p>

    <h3>Objetivos Específicos</h3>
    <ul>
      {#each objectivesSpecific as objective}
        <li>{objective}</li>
      {/each}
    </ul>

    <h2 class="text-2xl font-bold mb-2">
      Programación de Actividades y Carga Horaria
    </h2>
    <p>
      Fecha de inicio: {startDate}. Modalidad a distancia, {schedule.totalClasses}
      clases de {schedule.classDuration} cada una ({schedule.weeks} semanas en total).
      Carga horaria total de {schedule.totalHours} hs, incluyendo {schedule.synchronousHours}
      hs de tutorías (sincrónico) y {schedule.asynchronousHours} hs (asincrónico).
    </p>
    <p>Plataforma de cursado: {schedule.platform}</p>

    <h2>Metodología</h2>
    <ul>
      {#each methodology as method}
        <li>{method}</li>
      {/each}
    </ul>

    <h2>Modalidad de Evaluación</h2>
    <ul>
      {#each evaluationCriteria as criterion}
        <li>{criterion}</li>
      {/each}
    </ul>

    <h2>Destinatarios</h2>
    <ul>
      {#each targetAudience as audience}
        <li>{audience}</li>
      {/each}
    </ul>

    <h2>Requisitos de Admisión</h2>
    <ul>
      {#each admissionRequirements as requirement}
        <li>{requirement}</li>
      {/each}
    </ul>

    <h2>Resultados Esperados</h2>
    <p>{expectedOutcomes}</p>

    <h2>Modalidad y Fechas de Dictado</h2>
    <p>Inicio: {startDate}.</p>
    <p>Duración: {schedule.weeks} semanas</p>
    <p>Días: Martes y Jueves, 19:00 a 21:00 hs</p>

    <h2>Costos</h2>
    <p>Dos (2) pagos de {cost.paymentAmount}.</p>
    <p>Formas de Pago: {cost.paymentMethod}</p>
    <p><strong>Datos Bancarios:</strong></p>
    <p>Alias: {cost.bankDetails.alias}</p>
    <p>Número de cuenta: {cost.bankDetails.accountNumber}</p>
    <p>CBU: {cost.bankDetails.cbu}</p>
    <p>Nombre: {cost.bankDetails.name}</p>
    <p>CUIT: {cost.bankDetails.cuit}</p>

    <h2>Inscripciones</h2>
    <p>Reservá tu cupo pagando hasta el {inscriptionDeadline}.</p>
    <p>
      Los comprobantes de pago, junto con la documentación de inscripción,
      deberán ser enviados al correo electrónico: {contacts.inscriptionEmail} con
      el asunto "PAGO", detallando Apellido y Nombres del Alumno, DNI y nombre del
      Curso a inscribirse.
    </p>

      <a href="https://acortar.link/fx2G2i" target="_blank" style="color:red"
        >► FORMULARIO DE INSCRIPCIÓN</a
      >

    <div class="animate-slide-in-up">
      <img src={qrCode} alt="Prototipo de imagen" />
    </div>
    <h2>Contactos</h2>
    <p>Unidad de Formación Continua. Secretaría de Posgrado</p>
    <p>Email: {contacts.email}</p>
    <p>Dirección: {contacts.address}</p>
  </div>
</Accordion>

<style>
  h1 {
    /*text-lg font-semibold text-[#6d0205]*/
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
</style>
