<script>
  import Accordion from "$utilsMain/Accordion.svelte";

  let qrCode = "/assets/posgrado/Cursos de Posgrado/19_qr.png";
  let imageUrl = null; //"/assets/posgrado/Cursos de Posgrado/19.jpg";
  export const courseTitle = "AUDITORÍA Y CONTROL FISCAL";
  let startDate = "6 de marzo de 2026";
  let modality = "Híbrida";
  let professors = [
    {
      name: "Esp. CP. Horacio Ludueña",
    },
  ];

  let objectivesGeneral = "Lograr que los alumnos profundicen sus conocimientos con respecto al diseño y control de las administraciones fiscales, como así también la conducción y demás cuestiones referidas al factor humano."
   let objectivesSpecific = [
    "Comprender la dinámica histórica del fenómeno de la Administración fiscal",
    "Conocer las interrelaciones de la administración fiscal con las ciencias sociales afines.",
    "Analizar las taxonomías de los subsistemas principales incluidos en el funcionamiento de un organismo de administración fiscal.",
    "Conocer las características básicas y relaciones recíprocas de los distintos subsistemas identificados.",
    "Profundizar en particular en las características específicas del subsistema de recursos humanos en los organismos de Administración fiscal.",
    "Comprender la importancia fundamental del cumplimiento voluntario de los contribuyentes para el logro del objetivo final de la administración fiscal.",
    "Reconocer los principales desafíos futuros a los que se enfrenta la Administración fiscal en el Siglo XXI.",
  ];

  let analyticalContents = [
    "Aspectos sociológicos y psicológicos del personal de la administración fiscal, factores de riesgos del control de cumplimiento de los tributos, los límites de las administraciones fiscales, el marketing de los entes fiscales, consideraciones generales de diseño de la administración tributaria, recursos humanos, el control de gestión"
  ];

  let schedule = {
    totalClasses: 4,
    classDuration: "5 horas por encuentro",
    dates: [
      "Inicio: 6 de marzo de 2026",
      "Fechas: 6, 7, 13, 14 de marzo",
      "Horario: viernes de 16 a 21 hs; sábados de 8 a 13 hs",
    ],
    totalHours: "20 horas presenciales (modalidad híbrida)",
  };


  let cost = {
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
    inscriptionLink: "https://forms.gle/Ad8YZJfY6pAYkZpD8",
  };

  let evaluationModality = "Se evalúa con dos tipos de actividades que se promedian entre ambas, resultando de esa forma la nota final del módulo. Un examen final de preguntas que incluye todos los puntos relevantes del programa, lo cual obliga al alumno a conocer y aprender la totalidad de los mismos; y la resolución de un caso práctico sobre los temas del módulo; se considera asimismo una evaluación complementaria que consiste en el concepto de trabajo y nivel de participación en clase, el desarrollo y enfoque de casos prácticos trabajados en clase.";

  export let open = false;
</script>

<Accordion title={courseTitle} isOpen={open}>
  <div slot="content">
    <h1>{courseTitle}</h1>
    <!--
    <div class="animate-slide-in-up">
      <img
        src={imageUrl}
        alt="Imagen del curso Power BI"
        class="transition-all duration-300 hover:scale-105 w-full rounded-lg mb-4 ml-4 max-w-[800px]"
      />
    </div>-->
    <p>INICIO: {startDate} | MODALIDAD: {modality}</p>

    <h2>Docentes</h2>
    <ul class="professor-list">
      {#each professors as professor}
        <li class="professor-item">
          <div class="professor-info">
            <strong>{professor.name}</strong>
            {#if professor.descript}
              <p>{professor.descript}</p>
            {/if}
          </div>
        </li>
      {/each}
    </ul>

    <h2>Objetivos</h2>
    <h3>General</h3>
    <p>{objectivesGeneral}</p>
    <br />
    <h3>Específicos</h3>
    <ul>
      {#each objectivesSpecific as objective}<p>- {objective}</p>
        <br />{/each}
    </ul>

    <h2>Cronograma</h2>
    <div style="padding-left: 2rem;">
      {#each schedule.dates as date}<p>{date}</p>{/each}
      <p>Total de encuentros: {schedule.totalClasses}</p>
      <p>Duración: {schedule.classDuration}</p>
      <p>Carga horaria total: {schedule.totalHours}</p>
    </div>



    <h2>Contenidos Mínimos</h2>
    <ul>
      {#each analyticalContents as content}
        <li><p>{content}</p></li>
        <br />
      {/each}
    </ul>

    <h2>Modalidad de Evaluación</h2>
    <p>{evaluationModality}</p>

    <h2>Valor del Curso</h2>
    <div style="padding-left: 2rem;">
      <p>Valor: $80.000 (pago único)</p>
      <p>Forma de Pago: {cost.paymentMethod}</p>
      <p><strong>Datos Bancarios:</strong></p>
      <p>Alias: {cost.bankDetails.alias}</p>
      <p>Número de cuenta: {cost.bankDetails.accountNumber}</p>
      <p>CBU: {cost.bankDetails.cbu}</p>
      <p>Nombre: {cost.bankDetails.name}</p>
      <p>CUIT: {cost.bankDetails.cuit}</p>
      <p>
        Enviar comprobante a <a
          href="mailto:formacioncontinua@eco.unca.edu.ar"
          style="color:#007bff;text-decoration:none;"
          >formacioncontinua@eco.unca.edu.ar</a
        >
        detallando Apellido y nombre del alumno, nombre del curso a inscribirse.
      </p>
    </div>

    <h2>Inscripciones</h2>
    <a href={contacts.inscriptionLink} target="_blank" style="color:blue"
      >► FORMULARIO DE INSCRIPCIÓN</a
    >

    <div class="animate-slide-in-up">
      <img src={qrCode} alt="Código QR de inscripción" />
    </div>

    <br />

    <h2>Contactos</h2>
    <p>Unidad de Formación Continua | Secretaría de Posgrado</p>
    <p>Email: {contacts.email}</p>
    <p>Dirección: {contacts.address}</p>
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

  .professor-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .professor-item {
    margin-bottom: 1.5rem;
    overflow: auto;
  }

  .professor-info {
    text-align: justify; /* Para que se vea más prolijo */
  }

  .professor-info p {
    margin: 0 0 0;
  }
</style>
