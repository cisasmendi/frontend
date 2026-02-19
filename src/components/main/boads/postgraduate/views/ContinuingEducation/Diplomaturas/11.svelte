<script>
  // @ts-ignore

  import Accordion from "$utilsMain/Accordion.svelte";
  export let open = false;
  export const courseTitle = "Diplomatura en Gestión Turística Sustentable";
  let director = "Lic. Raúl Mura";
  let sedeBelenInicio = "Septiembre 2025";
  let sedeLosAltosInicio = "Septiembre 2025";

  let schedule = {
    duration: "6 meses",
    totalHours: 180,
    sedeBelen: "Sábados de 09 a 12 y 13 a 16 hs",
    sedeLosAltos: "Sábados de 14 a 20 hs",
  };

  let objectives = [
    "Que el alumno en su proceso de formación académica adquiera aquellas competencias consideradas como fundamentales para su desenvolvimiento en la organización y gestión de emprendimientos turísticos. Que el alumno adquiera conocimientos básicos sobre el turismo como actividad económica y su contribución al desarrollo, visualizando la importancia de la articulación público-privado. Que el alumno reconozca a la empresa turística como unidad central de análisis en sus estudios y como lugar en el que desarrollará su trabajo. El alumno debe reconocer sus principales características, los distintos subsistemas que conforman su funcionamiento y sus relaciones con los elementos del entorno, todo ello desde el punto de vista de la dirección de la empresa turística. Que el alumno sea capaz de distinguir la importancia de la calidad y la excelencia en el sector turístico, y conocer la forma de gestionar tanto a personas como a equipos para alcanzar la competitividad de la empresa en el mercado. Que el alumno incorpore aspectos conceptuales y herramentales de marketing tradicional y digital aplicado al sector turístico para entender el funcionamiento del mercado, diseñar, posicionar y comercializar productos turísticos en forma adecuada..",
  ];

  let methodology = [
    "Cursado 100% presencial.",  
    "Material y tutorías en aula virtual (www.economicasvirtual.edu.ar).",
  ];

  let evaluation =
    "Trabajo Final: Plan de Negocios turístico o Plan de Desarrollo de destino.";

  let graduateProfile =
    "El egresado de la diplomatura obtendrá calificaciones para comprender los conceptos y las herramientas de gestión destinadas a la administración de los emprendimientos turísticos, aplicando los conocimientos conceptuales, técnicos, estratégicos e instrumentales en las diferentes dimensiones de la actividad turística. Las competencias que se espera alcancen, se desagregan en el aprendizaje de contenidos metodológico-conceptuales para la construcción de nuevos saberes y capacidad para su interpretación y traducción operativa en el desempeño profesional bajo un marco de pensamiento creativo, crítico, analítico y estratégico frente a los problemas que presentan las actividades de los cursantes, habilidades específicas acerca de la dinámica empresarial turística, actitudinales y aptitudinales promoviendo una adecuada aplicación de los conceptos incorporados en el proceso de administración de los emprendimientos turísticos.";

  let targetAudience = [
    "Ciudadanos interesados en la gestión turística o emprendedores que deseen planificar el desarrollo de su negocio. Se contemplarán especialmente los casos de quienes posean experiencia laboral en el sector turismo.",
  ];

  let modules = [
    "Módulo 01. Turismo como actividad económica. La revolución 4.0 en los negocios y el turismo.Concepto. Importancia económica del turismo y del asociativismo. Análisis y construcción de la cadena de valor del Turismo. Impactos económicos, socioculturales y territoriales del turismo. La planta Turística: conceptualización y componentes. La infraestructura general de un destino. La transformación digital: retos y oportunidades para los negocios. Tecnologías disruptivas y tecnologías emergentes. Cambio de paradigma: de organizaciones basadas en funciones a organizaciones orientadas a procesos. Herramientas para el fortalecimiento institucional y la gestión estratégica de las organizaciones. Mapa de procesos: operativo, estratégico, de apoyo. BPMN. La administración de recursos humanos: la importancia del up-: skilling y reskilling digital. Co-creación de aprendizaje, gestión del cambio y desarrollo de nuevos talentos. Planificación estratégica aplicada a los negocios digitales.",
    "Módulo 02. Planificación del desarrollo de un destino turístico. Comunidad anfitriona. Turismo, sostenibilidad y comunidad local. Turismo y comunidad local. La participación de la comunidad en los procesos de desarrollo turístico: la comunidad anfitriona y sus características. Modalidades de construcción. Fundamentos de la planificación estratégica aplicada al desarrollo turístico sostenible en el ámbito local. Planta Turística: conceptualización, componentes, características, modalidades de relevamiento y registro. Infraestructura turística: conceptualización, características, componentes, actores involucrados. Ordenación territorial y competitividad turística. El concepto de impacto en relación con la actividad turística. Técnicas, procedimientos y métodos.",
    "Módulo 03. Organización y Gestión de empresas turísticas. Empresa, empresario y sector turístico. Los subsistemas de la empresa turística. El entorno de la empresa turística. La administración de la empresa turística. La toma de decisiones. Planificación y control organizativo. La estructura y diseño organizativo en la empresa Turística. Motivación. Liderazgo. La dirección de grupos de trabajo. Comunicación, conflicto y negociación. Gestión de la calidad en el servicio turístico. Administración de las operaciones: hotelería, gastronomía, transporte y agencia de viaje.",
    "Módulo 04. Marketing turístico: Plan de negocios en la empresa turística. Introducción al Emprendedurismo. Proceso de Desarrollo para crear la Idea de Negocio. Creación de la Idea de Negocio. De la Idea de Negocio a la planificación: Metodologías. Fundamentos de marketing. Análisis de los conceptos básicos de marketing. Marketing de servicios. Marketing turístico. La planificación comercial y el análisis del entorno. La naturaleza del mercado turístico. Análisis del entorno turístico y el mercado turístico. El análisis de la demanda turística. El comportamiento del consumidor turístico. Análisis del proceso de decisión de compra. La segmentación del mercado turístico. Marketing electrónico: Posibilidades de uso de Internet. Comercio electrónico en turismo. Conceptualización de Plan de Negocios: Importancia; Gestión Estratégica; Gestión de Marketing; Gestión de Producción; Gestión de la Organización; Gestión Económica Financiera. El Plan de Negocios. La implantación de la estrategia. Gestión del Riesgo - Comunicación de Riesgos. Plan de Contingencia.",
    "Módulo 05. Calidad y competitividad turística. Introducción a la Calidad. Teorías y princ1p1os de la gestión de la Calidad. Herramientas de Gestión de la Calidad. Sistemas de calidad turística: infraestructura, atención al turista, modelos de información sobre satisfacción del cliente. Normalización y Certificación de la Calidad (Nacional e internacional). Componentes de un sistema de Calidad: procesos, procedimientos, mejora continua, indicadores, documentación, auditorias. Conformidad, medidas preventivas y correctivas en la cultura organizacional. La seguridad turística en un destino. Adopción y cumplimiento de estándares de seguridad y prácticas en instalaciones y lugares turísticos; política de información y educación destinada a conseguir la transparencia y a hacer frente a las crisis; y, acceso efectivo a medidas, instalaciones y servicios institucionales públicos y privados de que se dispone para atender a los visitantes en casos de emergencia o en apuros.",
    "Módulo 06. Taller de integración y tutorías. Se plantea que los alumnos puedan integrar los contenidos desarrollados a lo largo del curso logrando desarrollar un proyecto para poder aplicarlo posteriormente en su vida profesional o laboral. Para ello se plantea la tutoría y el apoyo del cuerpo docente de la Diplomatura. El resultado esperado es que logre la construcción de una planificación estratégica de un destino o un proyecto de plan de negocios en el sector turístico. Además del proyecto, se promoverá una discusión sobre las posibilidades que ofrece la articulación público-privada en el desarrollo de la actividad turística. El proyecto sobre el cual deben trabajar puede ser la planificación de un destino o de un plan de negocios de un emprendimiento turístico, inserto dentro de la realidad y características propias del lugar previsto como localización.",
  ];

  let cost = {
    amount: "$50.000",
    installments: "6 cuotas",
    method: "Transferencia",
    bank: {
      alias: "FCEyA.UNCA",
      account: "31554660081889",
      cbu: "0110466420046600818894",
      name: "FC.CS.ECON.Y ADM.",
      cuit: "30641870931",
    },
  };

  let inscriptions = [
    {
      sede: "Sede Belén",
      link: "https://forms.gle/TnUUcvXVmc2dRh2U7",
      qrCode: "/assets/posgrado/Diplomatura/belen.jpg",
      tel: "3834528604",
      email: "sedebelen@unca.edu.ar",
    },
    {
      sede: "Sede Los Altos",
      link: "https://forms.gle/yekpt18ui7xvSuS86",
      qrCode: "/assets/posgrado/Diplomatura/losaltos.jpg",
      tel: "3834636596",
      email: "uncacasapueblolosaltos@gmail.com",
    },
  ];
</script>

<Accordion title={courseTitle} isOpen={open}>
  <div slot="content">
    <h1>{courseTitle}</h1>
    <p><strong>Director:</strong> {director}</p>

    <h2>Inicio de Clases</h2>
    <p><strong>Sede Belén:</strong> {sedeBelenInicio}</p>
    <p><strong>Sede Los Altos:</strong> {sedeLosAltosInicio}</p>

    <h2>Programación de Actividades y Carga Horaria</h2>
    <p><strong>Duración:</strong> {schedule.duration}</p>
    <p><strong>Carga horaria total:</strong> {schedule.totalHours} horas</p>
    <p><strong>Frecuencia:</strong> Semanal clase presenciales, dias sábado </p>
    <p><strong>Sede Belén:</strong> {schedule.sedeBelen}</p>
    <p><strong>Sede Los Altos:</strong> {schedule.sedeLosAltos}</p>

    <h2>Objetivos</h2>
    <ul>
      {#each objectives as obj}<li>{obj}</li>{/each}
    </ul>

    <h2>Metodología</h2>
    <ul>
      {#each methodology as m}<li>{m}</li>{/each}
    </ul>

    <h2>Evaluación</h2>
    <p>{evaluation}</p>

    <h2>Perfil del Egresado</h2>
    <p>{graduateProfile}</p>

    <h2>Destinatarios</h2>
    <ul>
      {#each targetAudience as dest}<li>{dest}</li>{/each}
    </ul>

    <h2>Plan de Estudios</h2>
    <ol>
      {#each modules as mod}
        <li>{mod}</li>
        <br />
      {/each}
    </ol>

    <h2>Costos y Formas de Pago</h2>
    <p>{cost.installments} de {cost.amount}</p>
    <p><strong>Método:</strong> {cost.method}</p>
    <p><strong>Alias:</strong> {cost.bank.alias}</p>
    <p><strong>Cuenta:</strong> {cost.bank.account}</p>
    <p><strong>CBU:</strong> {cost.bank.cbu}</p>
    <p><strong>Nombre:</strong> {cost.bank.name}</p>
    <p><strong>CUIT:</strong> {cost.bank.cuit}</p>
    <p>
      <strong>Nota:</strong> El pago se realiza a través de transferencia bancaria.
      Una vez realizado, envía el comprobante al correo electrónico de la sede correspondiente.
    </p>

    <h2>Inscripciones</h2>
    <p>
      Para inscribirte, escanea el código QR o haz clic en el enlace
      correspondiente a tu sede.
    </p>
    <div class="qr-container">
      {#each inscriptions as ins}
        <div class="qr">
          <p><strong>{ins.sede}</strong></p>
          <img src={ins.qrCode} alt="QR Belén" />
          <h2>Contactos</h2>
          <a href={ins.link} target="_blank">{ins.link}</a>
          <p>Tel: {ins.tel}</p>
          <p>Email: <a href="mailto:{ins.email}">{ins.email}</a></p>
        </div>
      {/each}
    </div>
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
  .qr-container {
    display: flex;
    gap: 2rem;
    margin-top: 1rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
  }
  .qr {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .qr img {
    max-width: 200px;
    height: auto;
    border: 1px solid #ccc;
    padding: 0.5rem;
    background: #fff;
    border-radius: 8px;
  }
</style>
