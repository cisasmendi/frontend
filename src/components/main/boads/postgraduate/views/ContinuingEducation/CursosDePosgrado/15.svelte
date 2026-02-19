<script>
  import Accordion from "$utilsMain/Accordion.svelte";

  let qrCode = "/assets/posgrado/Cursos de Posgrado/15_qr.png";
  let imageUrl = "/assets/posgrado/Cursos de Posgrado/15.jpg";
  export const courseTitle = "METODOLOGÍA DE LA INVESTIGACIÓN 1";
  let startDate = "21 de agosto de 2025";
  let modality = "Híbrida";
  let professors = ["Dr. Cristian Emanuel Jara"];

  let objectivesGeneral =
    "Desarrollar en los estudiantes competencias avanzadas en metodología de investigación que les permitan diseñar, ejecutar y comunicar investigaciones rigurosas y socialmente relevantes en sus respectivos campos disciplinarios, mediante el dominio de fundamentos epistemológicos, métodos y herramientas de escritura académica.";
  let objectivesSpecific = [
    "Proporcionar a los estudiantes una comprensión sólida de los principios fundamentales que guían la producción de conocimiento científico, diferenciándola de otras formas de saberes.",
    "Analizar las fases de la producción de conocimiento científico, teniendo en cuenta los criterios de validez y confiabilidad que plantean los diversos posicionamientos epistemológicos. ",
    "Dar cuenta de problemas que se suelen presentar en la construcción de un objeto de investigación, aportando herramientas para su delimitación.",
    "Capacitar a los estudiantes en el uso de técnicas para la construcción, procesamiento, análisis y presentación de los datos.",
    "Desarrollar habilidades de escritura científica, brindando a los doctorandos estrategias para la redacción que se adecue a los estándares académicos.",
  ];
  let analyticalContents = [
    "UNIDAD 1. EL CONOCIMIENTO CIENTÍFICO: El conocimiento científico y la ecología de saberes. Diferentes tradiciones de investigación. El Paradigma Positivista y el escenario post-positivista: supuestos ontológicos, epistemológicos y metodológicos. Metodología y Método. Objetividad y Neutralidad. Investigación y ética.",
    "UNIDAD 2. EL PROCESO DE INVESTIGACIÓN: Etapas y fases. De la identificación de áreas de interés a la comunicación de los resultados. Revisión preliminar y exhaustiva de la literatura. Formulación de las preguntas de Investigación. La construcción de marcos teóricos y estrategias de metodológica. La construcción de la matriz de dato y los instrumentos. El trabajo de campo. Los procedimientos para el análisis y presentación de los datos. La discusión de los hallazgos.",
    "UNIDAD 3. LA CONSTRUCCIÓN DEL OBJETO DE ESTUDIO: Disciplina, tema, y problema. El proceso de identificación del problema: problema social, problema de conocimiento y problema de intervención. Tradiciones epistemológicas que fundamentan determinada construcción del objeto de estudio. El “árbol del problema” y las estrategias de delimitación. Las preguntas engañosas. Los componentes del problema de investigación. La formulación de los objetivos generales y específicos. La coherencia interna y la articulación entre el título, el problema y los objetivos. La formulación de las hipótesis y las anticipaciones de sentido. La fundamentación de las mismas. Errores frecuentes en la formulación de los objetivos.",
    "UNIDAD 4. LOS ANTECEDENTES Y EL PAPEL DE LA TEORÍA EN LA INVESTIGACIÓN: Diferencias entre marco teórico y antecedentes. Estrategias de búsqueda de bibliografía especializada y actualizada. El mundo de las revistas científicas. Revisión de literatura, criterios de selección y análisis crítico de fuentes bibliográficas relevantes.",
    "UNIDAD 5. LAS METODOLOGÍAS POSIBLES: Metodología, métodos y técnicas. Tipos de diseños. Estrategias cuantitativas y cualitativas, potenciales combinaciones. El uso de fuentes (primarias y secundarias). Fundamentación del procedimiento. La construcción, procesamiento, análisis y presentación de los datos.",
    "UNIDAD 6. INVESTIGAR Y ESCRIBIR COMO PROCESOS SIMULTÁNEOS: a) El punto de partida y el bloqueo de la página en blanco. Momentos de la escritura. Perfiles de escritores: la importancia de reconocer nuestras fortalezas y debilidades. d) El saber de oficio y la artesanalidad en Ciencias Sociales; aprendizajes en y desde la práctica de investigación. c) La planificación y la factibilidad: recursos disponibles, oportunidades y plazos. Lo inesperado: flexibilidad y resiliencia en el recorrido. d) Razones para citar y sistema de citado académico.",
  ];
  let schedule = {
    totalClasses: 2,
    classDuration: "Varias horas por encuentro",
    dates: [
      "21 de agosto | 17 a 21 hs",
      "22 de agosto | 9 a 13/14 a 18 hs",
      "18 de septiembre | 17 a 21 hs",
      "19 de septiembre | 17 a 21 hs",
      "20 de septiembre | 9 a 13 hs",
    ],
    totalHours: "No especificado",
    platform: "Presencial/videoconferencia",
  };

  let methodology = [
   "Los encuentros (presenciales o por videoconferencia) estarán orientadas a la comprensión teórica de los contenidos del curso y los trabajos en la plataforma a ejercitar los principales procesos cognitivos propuestos, promoviendo la retroalimentación. Los trabajos prácticos consistirán en elaboraciones escritas e individual, las cuales han sido pensadas como pasos previos e interconectados que deberán ser ajustadas y articuladas en el trabajo final del curso."
  ];

  let evaluationCriteria = [
    "Asistencia mínima al 75% de los encuentros",
    "Calificación promedio mínima de 6 puntos sobre 10",
    "La evaluación final consistirá en un trabajo escrito e individual, tendrán una guía con las consignas para la elaboración.  ",
  ];

  let targetAudience = [
    "Profesionales graduados de carreras universitarias de más de 4 años de duración",
  ];



  let expectedOutcomes =
    "Adquisición de herramientas metodológicas para diseñar e implementar investigaciones que contribuyan al conocimiento académico en el campo de las ciencias sociales y económicas.";

  let cost = {
    paymentAmount: "Dos(2) cuotas de $70.000. La primera, previo al inicio del curso. La segunda, antes del comienzo del 2° encuentro. ",
    paymentMethod: "Transferencia",
    bankDetails: {
      alias: "fceyaunca",
      accountNumber: "31554660219296",
      cbu: "0110466420046602192961",
      name: "UNIVERSIDAD NACIONAL DE CATAMARCA",
      cuit: "30-64187093-1",
    },
  };

  let contacts = {
    email: "formacioncontinua@eco.unca.edu.ar",
    address: "Av. José Figueroa 257. SFV de Catamarca. Catamarca.",
    inscriptionLink: "https://forms.gle/bb6LNRiFmXFkVXUy5",
  };

  export let open = false;
</script>

<Accordion title={courseTitle} isOpen={open}>
  <div slot="content">
    <h1>{courseTitle}</h1>
    <div class="animate-slide-in-up">
      <img
        src={imageUrl}
        alt="Prototipo de imagen"
        class="transition-all duration-300 hover:scale-105 w-full rounded-lg mb-4 ml-4 max-w-[800px]"
      />
    </div>
    <p>INICIO: {startDate} | MODALIDAD: {modality}</p>

    <h2>Docente</h2>
    <ul>
      {#each professors as professor}<li>{professor}</li>{/each}
    </ul>

    <h2>Objetivos</h2>
    <h3>General</h3>
    <p>{objectivesGeneral}</p>
    <h3>Específicos</h3>
    <ul>
      {#each objectivesSpecific as objective}<li>- {objective}</li>{/each}
    </ul>
    <h2>Cronograma</h2>



   

    <div style="padding-left: 2rem;">
      total de encuentros: {schedule.totalClasses} encuentros<br />
      <p>ENCUENTRO 1:</p>
      <ul>
        <li>{schedule.dates[0]}</li>
        <li>{schedule.dates[1]}</li>
      </ul>
      <p>ENCUENTRO 2:</p>
      <ul>
        <li>{schedule.dates[2]}</li>
        <li>{schedule.dates[3]}</li>
        <li>{schedule.dates[4]}</li>
      </ul>
    </div>

    <h2>Metodología</h2>
    <ul>
      {#each methodology as method}<li>{method}</li>{/each}
    </ul>

    <h2>Evaluación</h2>
    <ul>
      {#each evaluationCriteria as criterion}<li>{criterion}</li>{/each}
    </ul>

    <h2>Destinatarios</h2>
    <ul>
      {#each targetAudience as audience}<li>{audience}</li>{/each}
    </ul>

    <h2>Contenidos Analíticos</h2>
    <ul>
      {#each analyticalContents as content}<li>{content}</li> <br>{/each}
    </ul>
    <h2>Resultados Esperados</h2>
    <p>{expectedOutcomes}</p>

    <h2>Valor del Curso</h2>
    <div style="padding-left: 2rem;">
      <p>{cost.paymentAmount}</p>
      <p>Forma de Pago: {cost.paymentMethod}</p>
      <p><strong>Datos Bancarios:</strong></p>
      <p>Alias: {cost.bankDetails.alias}</p>
      <p>Número de cuenta: {cost.bankDetails.accountNumber}</p>
      <p>CBU: {cost.bankDetails.cbu}</p>
      <p>Nombre: {cost.bankDetails.name}</p>
      <p>CUIT: {cost.bankDetails.cuit}</p>
      <div>
        <p>
          Los comprobantes de pago deberán ser enviados a
          <a
            href="mailto:formacioncontinua@eco.unca.edu.ar"
            style="color: #007bff; text-decoration: none;"
            >formacioncontinua@eco.unca.edu.ar</a
          >
          con el asunto <strong>"PAGO"</strong>, detallando:
        </p>
        <ul>
          <li><strong>Apellido y Nombres</strong> del Alumno</li>
          <li><strong>DNI</strong></li>
          <li><strong>Nombre del Curso</strong> a inscribirse</li>
        </ul>
      </div>
    </div>
    <h2>Inscripciones</h2>
    <a href={contacts.inscriptionLink} target="_blank" style="color:blue"
      >► FORMULARIO DE INSCRIPCIÓN</a
    >

    <div class="animate-slide-in-up">
      <img src={qrCode} alt="Código QR de inscripción" />
    </div>

    <br />
    <h2>Documentación a Enviar</h2>
    <ul>
      <li>DNI, Pasaporte o Cédula Extranjera</li>
      <li>Título de Grado o Certificado de Título en trámite</li>
    </ul>
    <p>
      Deberán ser enviados al correo electrónico
      <a
        href="mailto:formacioncontinua@eco.unca.edu.ar"
        style="color: #007bff; text-decoration: none;"
        >formacioncontinua@eco.unca.edu.ar</a
      >
      indicando el nombre del curso.
    </p>

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
</style>
