<script>
  import Accordion from "$utilsMain/Accordion.svelte";

  let qrCode = "https://eco.unca.edu.ar/assets2/users/paginaeco/posgrado/Cursos de Posgrado/20_qr.png";
  export const courseTitle =
    "EXPOSICIÓN, ANÁLISIS Y PROYECCIÓN DE LA INFORMACIÓN CONTABLE";
  let startDate = "27 de marzo de 2026";
  let modality = "Virtual";
  let professors = [
    {
      name: "Mg. Ana María Campo",
    },
  ];

  let objectives = [
    "Comprender la incidencia de la coyuntura económica en la definición de los modelos contables.",
    "Conocer los factores que determinan las diferencias en la información contable en los ámbitos nacionales e internacionales.",
    "Comprender las normas contables de exposición vigentes en el país sobre cuestiones de aplicación general y particular, comparándolas con las normas de otros países.",
    "Realizar un análisis crítico de la doctrina y las normas contables vigentes.",
    "Acceder a las Normas Internacionales de Información Financiera en su última versión internacional y analizar su aplicación a través de casos reales.",
    "Aplicar los conceptos adquiridos en la resolución de casos de situaciones reales y/o simuladas planteadas.",
    "Realizar trabajos de investigación en materia contable sobre cuestiones planteadas en los contenidos del módulo.",
  ];

  let analyticalContents =
    "Exposición de la información contable. Estados contables básicos e información complementaria. Estados contables proyectados. Aspectos particulares de la Normativa Internacional. Casos especiales de medición del patrimonio, determinación de resultados y exposición.";

  let practicalTraining = [
    "Se propicia la formación de grupos de trabajo para resolver casos, problemas y ejercitaciones prácticas en general, seleccionar bibliografía (fuentes) e investigar temas controvertidos.",
    "Dentro del proceso de enseñanza-aprendizaje, los casos prácticos constituyen una herramienta para que los alumnos se capaciten en la resolución de situaciones que puedan presentarse en la realidad y, por lo tanto, en su práctica profesional. Los casos que se propongan, las situaciones que eventualmente surjan de cada clase pretenden cubrir aspectos de una gama de situaciones diferentes que la práctica ha de presentar, con la guía del docente.",
  ];

  let schedule = {
    totalClasses: 4,
    classDuration: "4 encuentros",
    dates: [
      "Fechas: 27, 28 de marzo; 10 y 11 de abril",
      "Horario: viernes de 16 a 21 hs; sábados de 8 a 13 hs",
    ],
  };

  let cost = {
    amount: "1 pago de $80.000",
    bankDetails: {
      name: "FC.CS.ECON.Y ADM.",
      cuit: "30641870931",
      accountNumber: "31554660081889",
      alias: "FCEyA.UNCA",
      cbu: "0110466420046600818894",
    },
  };

  let contacts = {
    area: "Unidad de Formación Continua | Secretaría de Posgrado",
    email: "formacioncontinua@eco.unca.edu.ar",
    address: "Av. José Figueroa 257",
    inscriptionLink: "https://forms.gle/K4izicLWXTLsPtfp7",
  };

  export let open = false;
</script>

<Accordion title={courseTitle} isOpen={open}>
  <div slot="content" class="course-content">
    <h1>{courseTitle}</h1>
    <p><strong>Inicio:</strong> {startDate}</p>
    <p><strong>Modalidad:</strong> {modality}</p>

    <h2>Docente</h2>
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

    <h2>Cronograma</h2>
    <div style="padding-left: 2rem;">
      {#each schedule.dates as date}<p>{date}</p>{/each}
      <p>Total de encuentros: {schedule.totalClasses}</p>
      <p>Duración: {schedule.classDuration}</p>
    </div>

    <h2>Valor del Curso</h2>
    <p>Valor del Curso: {cost.amount}</p>

    <h2>Inscripción</h2>
    <a href={contacts.inscriptionLink} target="_blank" style="color:blue"
      >► FORMULARIO DE INSCRIPCIÓN</a
    >
    <div class="animate-slide-in-up">
      <img src={qrCode} alt="Código QR de inscripción" class="qr-image" />
    </div>
    <h2>Datos Bancarios</h2>
    <p><strong>Nombre:</strong> {cost.bankDetails.name}</p>
    <p><strong>CUIT:</strong> {cost.bankDetails.cuit}</p>
    <p><strong>Número de cuenta:</strong> {cost.bankDetails.accountNumber}</p>
    <p><strong>Alias:</strong> {cost.bankDetails.alias}</p>
    <p><strong>CBU:</strong> {cost.bankDetails.cbu}</p>
    <p>
      <strong>Envío de comprobante de pago:</strong>
      <a href="mailto:{contacts.email}">{contacts.email}</a>
    </p>

    <h2>Objetivos</h2>
    <ul class="objective-list">
      {#each objectives as objective}
        <li>{objective}</li>
      {/each}
    </ul>

    <h2>Contenidos Mínimos</h2>
    <p>{analyticalContents}</p>

    <h2>Formación Práctica</h2>
    {#each practicalTraining as paragraph}
      <p>{paragraph}</p>
      <br />
    {/each}

    <br />

    <h2>Informes</h2>
    <p>{contacts.area}</p>
    <p>{contacts.address}</p>
    <p>Correo electrónico: {contacts.email}</p>
  </div>
</Accordion>

<style>
  .course-content {
    font-size: 1rem;
  }

  .course-content p,
  .course-content li {
    font-size: 1rem;
  }

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

  .objective-list {
    list-style: disc;
    padding-left: 1.25rem;
    margin: 0.5rem 0;
  }

  .objective-list li {
    margin-bottom: 0.35rem;
  }

  .qr-image {
    width: 180px;
    max-width: 100%;
    height: auto;
  }
</style>
