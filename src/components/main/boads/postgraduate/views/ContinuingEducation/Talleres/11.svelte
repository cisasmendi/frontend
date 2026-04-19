<script>
  import Accordion from "$utilsMain/Accordion.svelte";
  let qrCode = "https://eco.unca.edu.ar/assets2/users/paginaeco/posgrado/Taller/11_qr.png";
  export const courseTitle = "Taller de Tesis";
  export let course = {
    teachers: ["Dr. Daniel Esteban Quiroga", "Dr. Rafael Ponzo Florimonte"],
    audience:
      "Profesionales graduados de carreras universitarias de más de 4 años de duración.",
    start_date: "23 de abril de 2026",
    mode: "Híbrida",
    schedule: {
      encounter_1: [
        "23 de abril | 16 a 21 hs.",
        "24 de abril | 16 a 21 hs.",
        "25 de abril | 9 a 14 hs.",
      ],
      encounter_2: [
        "21 de mayo | 16 a 21 hs.",
        "22 de mayo | 16 a 21 hs.",
        "23 de mayo | 9 a 14 hs.",
      ],
    },
    objectives:
      "El curso busca brindar elementos conceptuales y prácticos para la elaboración de un trabajo científico orientado a las ciencias económicas, el cual se plasmará en un proyecto de tesis del doctorado. Se realizará un acompañamiento en las distintas instancias del diseño de la investigación para la realización del proyecto de investigación. Se pretende presentar y debatir criterios metodológicos y epistemológicos necesarios al momento de la elaboración de la investigación en ciencias económicas. Se procura acompañar a las y los estudiantes en el proceso de investigación que deben llevar adelante para formular el problema de investigación. De ese modo, el curso ofrecerá un espacio para definir y desarrollar un proyecto de investigación a partir de un ejercicio que combina la reflexión teórico-metodológica y la labor práctica.",
    certification:
      "Certificado de aprobación o asistencia según corresponda.",
    costs: {
      amount: "2 pagos de $70.000.",
      bank_data: [
        { label: "CUIT", value: "30-64187093-1" },
        { label: "Razón social", value: "UNIVERSIDAD NACIONAL DE CATAMARCA" },
        { label: "Tipo de cuenta", value: "CC $" },
        { label: "Número de cuenta", value: "31554660219296" },
        { label: "CBU", value: "0110466420046602192961" },
        { label: "Alias", value: "fceyaunca" },
      ],
      receipt_email: "mluduena@eco.unca.edu.ar",
    },
    documentation: [
      "DNI, Pasaporte o Cédula Extranjera",
      "Título de Grado o Certificado de Título en trámite",
    ],
    documentation_email: "formacioncontinua@eco.unca.edu.ar",
    inscription:
      "https://forms.gle/t5yFKvS8TSXW7d8n7",
    contacts: {
      unit: "Unidad de Formación Continua | Secretaría de Posgrado",
      email: "formacioncontinua@eco.unca.edu.ar",
      address: "Av. José Figueroa 257. SFV de Catamarca. Catamarca.",
    },
  };
  export let open = false; // Controla si el acordeón está abierto o cerrado
</script>

<Accordion title={"Taller de Tesis"} isOpen={open}>
  <div slot="content">
    <h1>{courseTitle}</h1>
    <h2>Docentes</h2>
    <ul>
      {#each course.teachers as teacher}
        <li>{teacher}</li>
      {/each}
    </ul>

    <h2>Destinatarios</h2>
    <p>{course.audience}</p>

    <h2>Inicio</h2>
    <p>{course.start_date}</p>

    <h2>Modalidad</h2>
    <p>{course.mode}</p>

    <h2>Fechas y Horarios</h2>
    <h3>Encuentro 1</h3>
    <ul>
      {#each course.schedule.encounter_1 as date}
        <li>{date}</li>
      {/each}
    </ul>
    <h3>Encuentro 2</h3>
    <ul>
      {#each course.schedule.encounter_2 as date}
        <li>{date}</li>
      {/each}
    </ul>

    <h2>Objetivos</h2>
    <p>{course.objectives}</p>

    <h2>Certificación a Entregar</h2>
    <p>{course.certification}</p>

    <h2>Valor del Curso y Forma de Pago</h2>
    <p><strong>Monto:</strong> {course.costs.amount}</p>
    <p><strong>Datos Bancarios:</strong></p>
    <ul>
      {#each course.costs.bank_data as bankItem}
        <li><strong>{bankItem.label}:</strong> {bankItem.value}</li>
      {/each}
    </ul>
    <p>
      Los comprobantes de pago deberán ser enviados al correo electrónico:
      <a href={`mailto:${course.costs.receipt_email}`} class="email-highlight"
        >{course.costs.receipt_email}</a
      >.
      Con el asunto "PAGO", detallando Apellido y Nombres del Alumno, DNI y
      nombre del Curso a inscribirse.
    </p>

    <h2>Documentación a Enviar</h2>
    <ul>
      {#each course.documentation as doc}
        <li>{doc}</li>
      {/each}
    </ul>
    <p>
      La documentación deberá ser enviada al correo electrónico:
      <a href={`mailto:${course.documentation_email}`} class="email-highlight"
        >{course.documentation_email}</a
      > indicando el nombre del curso.
    </p>

    <h2>Inscripciones</h2>
    <a
      href={course.inscription}
      target="_blank"
      rel="noopener noreferrer"
      style="color:red"
    >► FORMULARIO DE INSCRIPCIÓN</a>
    <div class="animate-slide-in-up">
      <img src={qrCode} alt="Prototipo de imagen" class="qr-image" />
    </div>

    <h2>Contactos</h2>
    <p>{course.contacts.unit}</p>
    <p>
      Correo electrónico:
      <a href={`mailto:${course.contacts.email}`} class="email-highlight"
        >{course.contacts.email}</a
      >
    </p>
    <p>{course.contacts.address}</p>


  </div>
</Accordion>

<style>

 p, li {
 
    font-size: 1rem;
    color: #333;
    line-height: 1.5;
  }
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

  .qr-image {
    width: 180px;
    max-width: 100%;
    height: auto;
  }

  .email-highlight {
    color: #7a1c0b;  
    text-decoration: underline;
  }
</style>
