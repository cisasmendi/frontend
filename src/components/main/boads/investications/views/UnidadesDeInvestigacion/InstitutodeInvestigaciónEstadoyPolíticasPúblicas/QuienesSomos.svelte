<script>
  export let title = "";
  export let imageUrl = "";
  import BoardLayout from "$BoardLayout";
</script>

<BoardLayout>
    <img
      src={imageUrl}
      alt="Prototipo de imagen"
      class="w-10 h-10 lg:w-10 lg:h-10 rounded-lg mb-4 float-left mr-4"
    />
    <h2 class="text-2xl font-semibold text-[#6d0205]">{title}</h2>
    <p class="mb-4 mt-6">
      A partir del año 2022, con la ordenanza CD Nº001-22 FCEyA, nace el
      Instituto de Investigación Estado y Políticas Públicas. Dicho ordenamiento
      permite la reorganización y posicionamiento como Instituto de
      Investigación al, por aquel entonces, Centro de Estudio de Políticas
      Públicas, creado en el año 2006, quien desde su conformación ha
      desarrollado innumerables labores académicas y técnicas, consolidándose
      para generar, administrar y fortalecer el desarrollo de un espacio para la
      reflexión, el intercambio de experiencias, la investigación, la formación
      y fortalecimiento de redes comunicacionales y sociales, la extensión
      universitaria, y toda actividad comprendida en el campo de la producción
      de conocimiento en políticas públicas que fortalezcan y propicien la
      construcción de una sociedad más justa para todos, mediante la
      articulación entre las demandas de la sociedad y el Estado.
    </p>

    <h3 class="text-xl font-semibold text-[#6d0205]">Titular</h3>

    <p class="mb-4">
      <strong>Director:</strong><br />
      Lic. Raúl Mura
    </p>

    <!-- Sección Eventos -->
    <h3 class="text-xl font-semibold text-[#6d0205] pt-4">Eventos</h3>

    <!-- 1er Congreso Regional Estado y Administración -->
    <p>
      <strong
        >1er Congreso Regional Estado y Administración: “El Estado Pos-Pandemia”</strong
      ><br />
      18 y 19 de mayo 2023<br />
      FCEyA - UNCA
    </p>

    <!-- 1ra. Jornada Provincial Estado y Administración -->
    <p>
      <strong
        >1ra. Jornada Provincial Estado y Administración: “El Estado
        Pos-Pandemia”</strong
      ><br />
      31 de mayo y 01 junio 2022<br />
      FCEyA - UNCA<br />
      <strong>Libro del evento:</strong><br />
      ISBN 978-987-661-438-2<br />
      Editorial Científica Universitaria de la Universidad Nacional de Catamarca,
      2022. Libro digital, PDF
    </p>

    <!-- II Congreso Regional en Políticas Públicas -->
    <p>
      <strong
        >II Congreso Regional en Políticas Públicas: “Desarrollo, Ciudadanía e
        Inclusión Social”</strong
      ><br />
      8 al 10 de octubre 2014<br />
      FCEyA - UNCA
    </p>

    <!-- 1er Congreso Regional de Políticas Públicas -->
    <p>
      <strong
        >1er Congreso Regional de Políticas Públicas: “Demandas Sociales y
        Legitimidad Política”</strong
      ><br />
      25, 26 y 27 de octubre de 2006<br />
      FCEyA - UNCA
    </p>

    <!-- Sección Proyectos -->
    <h3 class="text-xl font-semibold text-[#6d0205] pt-4">Proyectos</h3>

    <p>
      “Un proyecto de investigación es un plan definido y concreto de una
      indagación a realizar, donde se encuentran especificadas todas sus
      características básicas”. Sabino (2006).
    </p>

    <p>
      Según Sierra Bravo (1991), el proyecto de investigación “es la
      especificación organizativa, temporal y económica de las distintas fases y
      operaciones del proceso de investigación, en relación con un caso concreto
      de estudio”.
    </p>

    <p>
      El primer paso para implementar cualquier estrategia de intervención es un
      proyecto. La investigación es un recorrido que permite describir lo que se
      propone el investigador, expresa el qué y cómo se investigará.
    </p>

    <p>
      Los proyectos de investigación necesitan plantear un problema, plasmando
      qué se desea indagar y fundamentado por un marco teórico. Presenta
      alternativas de soluciones y la metodología que se utilizará en el
      proceso.
    </p>

    <p>
      <strong>En los proyectos de investigación que hemos trabajado son:</strong
      >
    </p>

    <ul class="list-disc pl-5">
      <li>Proyectos de Innovación y Desarrollo</li>
      <li>Proyectos de Transferencia</li>
      <li>Proyectos de Extensión</li>
    </ul>

    <h3 class="text-xl font-semibold text-[#6d0205] pt-10">Contacto</h3>

    <p class="mb-4">
      <strong>Email:</strong>
      <a href="mailto:" class="text-blue-500 hover:underline"
        >raulmura@eco.unca.edu.ar</a
      ><br />
      <strong>Teléfono y WhatsApp:</strong> +54 9 383 471 3890<br />
      <strong
        >Edificio de Profesores, Facultad de Ciencias Económicas y de
        Administración. UNCA</strong
      ><br />
      Av. José Figueroa 275. San Fernando del Valle de Catamarca (4700). Catamarca,
      Argentina.
    </p>
</BoardLayout>
