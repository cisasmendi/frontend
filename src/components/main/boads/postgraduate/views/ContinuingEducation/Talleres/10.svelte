<script>
  import Accordion from "$utilsMain/Accordion.svelte";
  let qrCode = "/assets/posgrado/Taller/10_qr.png";
  export const courseTitle = "Taller de Interpretación Jurisprudencial";
  export let course = {
    start_date: "25 de Octubre 2024",
    mode: "Virtual",
    teacher: "Dr. Daniel Malvestiti",
    objectives: [
      "Comprender la importancia de la jurisprudencia como fuente del derecho.",
      "Identificar los elementos que componen una decisión judicial.",
      "Analizar adecuadamente el fallo y sus fundamentos.",
    ],
    min_content:
      "Se trabajará la modalidad de taller, desmenuzando los contenidos de las interpretaciones administrativas, como de los fallos judiciales, y analizando las resoluciones que pueden haber existido en las distintas instancias...",
    analytic_content: [
      "Interpretación de la Ley Tributaria...",
      "La jurisprudencia como fuente del Derecho...",
      "Órgano Administrativo y Judicial...",
      "La Sentencia: Estructura de la sentencia...",
    ],
    methodology: [
      "Clases Teórico-Prácticas: desarrollando ejemplos prácticos.",
      "Clases Prácticas: Los alumnos desarrollarán ejercicios prácticos.",
    ],
    evaluation:
      "Examen final, que podrá ser oral o escrito e incluirá temas teóricos y prácticos.",
    audience: "Profesionales en Ciencias Económicas.",
    schedule: {
      mode: "Virtual",
      start_date: "25 de Octubre de 2024",
      duration: "4 encuentros en Octubre y Noviembre",
      days: ["25, 26 de Octubre", "01, 02 de Noviembre 2024"],
      hours: ["Viernes de 17:00 a 21:00hs", "Sábados de 09:00 a 13:00hs"],
    },
    certification: {
      attendance: "Asistencia al 80% de las clases.",
      approval: "Aprobación del examen final.",
    },
    documentation: [
      "DNI, Pasaporte o Cédula Extranjera",
      "Título de Grado o Certificado de Título en trámite",
    ],
    costs: {
      amount: "$30.000 (Pesos Treinta mil)",
      payment_methods: [
        "Transferencia o Depósito",
        "Alias: FCEyA.UNCA",
        "Número de cuenta: 31554660081889",
        "CBU: 0110466420046600818894",
        "CUIT: 30641870931",
      ],
    },
    contacts: {
      email: "formacioncontinua@eco.unca.edu.ar",
      address: "Av. José Figueroa 257. SFV de Catamarca. Catamarca.",
    },
  };
  export let open = false; // Controla si el acordeón está abierto o cerrado
</script>

<Accordion title={"Taller de Interpretación Jurisprudencial"} isOpen={open}>
  <div slot="content">
    <h1>{courseTitle}</h1>
    <p>
      <strong>INICIO DE CLASES:</strong>
      {course.start_date} | <strong>Modalidad:</strong>
      {course.mode}
    </p>

    <h2>Docente</h2>
    <p>{course.teacher}</p>

    <h2>Objetivos</h2>
    <ul>
      {#each course.objectives as objective}
        <li>{objective}</li>
      {/each}
    </ul>

    <h2>Contenidos Mínimos</h2>
    <p>{course.min_content}</p>

    <h2>Contenidos Analíticos</h2>
    <ul>
      {#each course.analytic_content as content}
        <li>{content}</li>
      {/each}
    </ul>

    <h2>Metodología</h2>
    <ul>
      {#each course.methodology as method}
        <li>{method}</li>
      {/each}
    </ul>

    <h2>Formas de Evaluación</h2>
    <p>{course.evaluation}</p>

    <h2>Destinatarios</h2>
    <p>{course.audience}</p>

    <h2>Modalidad y Fechas de Dictado</h2>
    <ul>
      <li><strong>Modalidad:</strong> {course.schedule.mode}</li>
      <li><strong>Fecha de inicio:</strong> {course.schedule.start_date}</li>
      <li><strong>Duración:</strong> {course.schedule.duration}</li>
      <li><strong>Días:</strong> {course.schedule.days.join(", ")}</li>
      <li><strong>Horarios:</strong> {course.schedule.hours.join(", ")}</li>
    </ul>

    <h2>Certificación a Entregar</h2>
    <ul>
      <li>{course.certification.attendance}</li>
      <li>{course.certification.approval}</li>
    </ul>

    <h2>Documentación a enviar</h2>
    <ul>
      {#each course.documentation as doc}
        <li>{doc}</li>
      {/each}
    </ul>

    <h2>Costos</h2>
    <p><strong>Monto:</strong> {course.costs.amount}</p>
    <ul>
      {#each course.costs.payment_methods as method}
        <li>{method}</li>
      {/each}
    </ul>

    <h2>Contactos</h2>
    <p>Email: {course.contacts.email}</p>
    <p>Dirección: {course.contacts.address}</p>
    <h2>Inscripciones</h2>
    <a href="https://acortar.link/8F1IaR" target="_blank" style="color:red"
      >► FORMULARIO DE INSCRIPCIÓN</a
    >
    <div class="animate-slide-in-up">
      <img src={qrCode} alt="Prototipo de imagen" />
    </div>
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
