<script>
  import Accordion from "$utilsMain/Accordion.svelte";

  let qrCode = "/assets/posgrado/Cursos de Posgrado/16_qr.png";
  let imageUrl = null; //"/assets/posgrado/Cursos de Posgrado/16.jpg";
  export const courseTitle = "VISUALIZACIÓN Y ANÁLISIS DE DATOS CON POWER BI";
  let startDate = "1 de octubre de 2025";
  let modality = "Virtual";
  let professors = [
    {
      image: "/assets/posgrado/Cursos de Posgrado/16.jpg",
      name: "MG. Hernán Aruj",
      descript:
        "Es Licenciado en Relaciones Internacionales por la UNR y Magister en Economía y Desarrollo Industrial por la UNGS. Está certificado como Analista de Datos con Power Bi por Microsoft. Utilizó sus conocimientos en el campo de la analítica de datos de salud, primero en PAMI-INSSJP, y luego en Cober Salud. Se desempeña como profesor en el Nodo Tecnológico Catamarca, CoderHouse y PAMI-INSSJP. ",
    },
  ];

  let objectivesGeneral =
    "Capacitar a los participantes en la comprensión de las técnicas de visualización y análisis de datos mediante el uso de Power BI, a fin de transformar datos crudos en informes y gráficos que faciliten la toma de decisiones estratégicas en sus organizaciones.";
  let objectivesSpecific = [
    "Introducción a la Visualización de Datos: Comprender los principios fundamentales de la visualización de datos y la importancia de comunicar información de manera visualmente atractiva y comprensible.",
    "Transformación y Limpieza de Datos: Enseñar a los participantes cómo limpiar, transformar y preparar datos utilizando Power Query, una de las funciones más importantes de Power BI para asegurar la calidad y precisión de los análisis.",
    "Creación de Visualizaciones Dinámicas: Permitir a los participantes crear visualizaciones complejas como mapas geoespaciales, gráficos dinámicos, informes interactivos y utilizar funciones avanzadas de Power BI.",
    "Utilización de los Últimos Avances: Capacitar a los participantes en el uso práctico de Power BI, aplicando las actualizaciones mensuales que tiene la herramienta.",
  ];

  let analyticalContents = [
    "UNIDAD 1. Introducción a Power BI y fundamentos del análisis de datos: Instalación, análisis de datos, navegación e interfaz, importación y organización de los datos.",
    "UNIDAD 2. Modelado de datos en Power BI: Power Query y lenguaje M, creación de tabla calendario, medidas, funciones DAX, columnas calculadas, uso de filtros.",
    "UNIDAD 3. Creación de reportes interactivos: Fundamentos de la visualización de datos, estándar IBCS, tipos de gráficos, interactividad, navegación y creación de reportes.",
    "UNIDAD 4. Enriquecer la visualización: Datos geográficos, gráficos avanzados, uso de IA, integración con R y Python, trabajo final.",
  ];

  let schedule = {
    totalClasses: 16,
    classDuration: "2 horas por clase",
    dates: [
      "Inicio: 1 de octubre",
      "Finaliza: 1 de diciembre",
      "Días: Lunes y miércoles de 19 a 21 hs",
    ],
    totalHours: "60 horas (32 sincrónicas + 28 asincrónicas)",
  };

  let methodology = [
    "El curso se desarrollará en formato virtual sincrónico, con grabación de las clases y disponibilidad del material utilizado.",
    "Se trabajará con datos reales de Catamarca y la región NOA para contextualizar la experiencia.",
    "Se utilizará el campus virtual de la Facultad para materiales y actividades.",
  ];

  let evaluationCriteria = [
    "La evaluación se basará en la elaboración de un trabajo final: el armado de un dashboard. Este podrá desarrollarse a partir de información seleccionada por el alumno o sobre bases de datos propuestas por el docente, con el propósito de orientar y enriquecer el proceso de aprendizaje.",
  ];

  let targetAudience = [
    "Profesionales y estudiantes con manejo intermedio de Excel.",
  ];

  let expectedOutcomes =
    "Desarrollar la capacidad de crear reportes interactivos, dashboards y análisis de datos con Power BI aplicando buenas prácticas y técnicas avanzadas.";

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
    inscriptionLink: "https://forms.gle/CiQbxSRzqQ981ga36",
  };

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
          <img
            class="professor-image"
            src={professor.image}
            alt="Foto de {professor.name}"
          />
          <div class="professor-info">
            <strong>{professor.name}</strong>
            <p>{professor.descript}</p>
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
      <p>Total de clases: {schedule.totalClasses}</p>
    </div>

    <h2>Metodología</h2>
    <ul>
      {#each methodology as method}<li><p>{method}</p></li>{/each}
    </ul>

    <h2>Evaluación</h2>
    <ul>
      <p>
        {#each evaluationCriteria as criterion}
          <li>{criterion}</li>
        {/each}
      </p>
    </ul>

    <h2>Destinatarios</h2>
    <ul>
      <p>
        {#each targetAudience as audience}<li>{audience}</li>{/each}
      </p>
    </ul>

    <h2>Certificación:</h2>
    <ul>
     
        <li><p>• Certificación de Asistencia a quienes completen la cursada.</p></li>
        <li>
          <p>• Certificación de Aprobación a quienes, además, aprueben el trabajo
          final.</p>
        </li>
        <li>
          <p>
          La certificación se emitirá como actividad de posgrado para los
          participantes que acrediten carreras de grado con una duración mínima
          de cuatro (4) años. En los demás casos, se otorgará constancia de
          curso de capacitación.
          </p>
        </li>
     
    </ul>

    <h2>Contenidos Analíticos</h2>
    <ul>
      {#each analyticalContents as content}
        <li><p>{content}</p></li>
        <br />
      {/each}
    </ul>

    <h2>Resultados Esperados</h2>
    <p>{expectedOutcomes}</p>
    <h2>Requisitos</h2>
    <p>
      Se recomienda contar con manejo de Excel a nivel intermedio, a fin de
      facilitar la comprensión de los contenidos y el uso de Power BI.
    </p>
    <h2>Valor del Curso</h2>
    <div style="padding-left: 2rem;">
      <p>
        Promoción Inscripción Temprana: Hasta el 20/9 → $100.000 (pago único)
      </p>
      <p>
        Valor regular: $120.000 en 2 cuotas de $60.000, 1° cuota hasta el 24/9,
        2° cuota hasta el 24/10
      </p>
      <p>Forma de Pago: {cost.paymentMethod}</p>
      <p><strong>Datos Bancarios:</strong></p>
      <p>Alias: {cost.bankDetails.alias}</p>
      <p>Número de cuenta: {cost.bankDetails.accountNumber}</p>
      <p>CBU: {cost.bankDetails.cbu}</p>
      <p>Nombre: {cost.bankDetails.name}</p>
      <p>CUIT: {cost.bankDetails.cuit}</p>
      <p>
        Enviar comprobante a <a
          href="mailto:mluduena@eco.unca.edu.ar"
          style="color:#007bff;text-decoration:none;"
          >mluduena@eco.unca.edu.ar</a
        >
        con el asunto <strong>"PAGO"</strong> detallando Apellido y Nombres, DNI
        y nombre del curso.
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

  .professor-image {
    float: left;
    width: 100px;
    height: auto;
    border-radius: 8px;
    margin: 1rem 1rem 1rem 0;
  }

  .professor-info {
    text-align: justify; /* Para que se vea más prolijo */
  }

  .professor-info p {
    margin: 0 0 0;
  }

  /* ✅ Ocultar imagen en pantallas pequeñas */
  @media (max-width: 768px) {
    .professor-image {
      display: none;
    }
  }
</style>
