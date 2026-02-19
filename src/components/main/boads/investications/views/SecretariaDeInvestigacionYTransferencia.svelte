<script>
  export let title = "";
  import BoardLayout from "$BoardLayout";
  let imageUrl = "/assets/logos/logo-campus2.png";
</script>

<BoardLayout {title}>
  <!--<img src={imageUrl} alt="Logo Campus de Entrenamiento Laboral" class="w-40 md:w-48 h-auto" />
  <div
    class="rounded-lg p-6 shadow-md bg-[#222A59] flex flex-col md:flex-row items-center md:items-start gap-6 mb-6"
  >
    <img
      src={imageUrl}
      alt="Logo Campus de Entrenamiento Laboral"
      class="w-40 md:w-48 h-auto"
    />
    <div class="flex-1 text-white text-center md:text-left">
      <h4 class="text-xl md:text-2xl font-semibold mb-2">
        Conocé el Campus de Entrenamiento Laboral
      </h4>
      <p class="mb-4 text-sm md:text-base">
        Accedé a capacitaciones y recursos útiles para mejorar tus habilidades
        laborales.
      </p>
      <a
        href="https://share.google/JrmqBb9c3xaCiboS4"
        target="_blank"
        class="inline-block px-5 py-2 bg-white text-[#222A59] font-semibold rounded hover:bg-gray-200 transition-colors"
      >
        Ir al Campus
      </a>
    </div>
  </div>
-->
  <p class="mb-4">
    La Secretaría de Investigación, Innovación y Transferencia de la Facultad de
    Ciencias Económicas y Administración (SIIT FCEyA) tiene la misión de
    promover y coordinar programas, proyectos y actividades tendientes al
    fortalecimiento y desarrollo de la actividad científica y tecnológica de la
    Facultad, con el fin de contribuir a la generación de conocimientos, la
    formación de capital humano dedicado a la investigación, la articulación de
    la investigación con las funciones sustantivas previstas en el Estatuto
    Universitario y la transferencia de conocimientos, innovación y tecnología
    en el campo de las Ciencias Económicas, con el objeto de alcanzar la
    excelencia académica y reafirmar el compromiso social universitario.
  </p>

  <p class="mb-4">
    <strong>Secretaria de Investigación, Innovación y Transferencia:</strong><br
    />
    Mg. CPN Andrea Morales<br />
    <a
      href="mailto:andream@eco.unca.edu.ar"
      class="text-blue-500 hover:underline">andream@eco.unca.edu.ar</a
    >
  </p>

  <p class="mb-4">
    <strong
      >Edificio de Profesores, Facultad de Ciencias Económicas y de
      Administración.</strong
    >
    <br />
    Av. José Figueroa 275. San Fernando del Valle de Catamarca (4700). Catamarca,
    Argentina.
  </p>
  <h3 class="text-xl font-semibold text-[#6d0205]">Contacto:</h3>

  <p class="mb-4">
    <strong>Email:</strong>
    <a href="mailto:" class="text-blue-500 hover:underline"
      >secretariainvestigacion@eco.unca.edu.ar</a
    ><br />
   
    <strong>Teléfono:</strong> +54 383 4434645 interno 161
  </p>

  <h3 class="text-xl font-semibold text-[#6d0205]">Horarios de atención:</h3>

  <p class="mb-4">Lunes a Viernes de 8:30 a 12:30 y de 18:00 a 20:30</p>

  <h3 class="text-xl font-semibold text-[#6d0205]">Estructura Organizativa:</h3>
  <p class="mb-4">
    Dependen de la Secretaría las Unidades de Investigación y Desarrollo y la
    Unidad de Vinculación y Transferencia.
  </p>
  <img
    src={"/assets/boards/investications/estructura.png"}
    alt="Prototipo de imagen"
    class=" h-auto mb-4"
  />
</BoardLayout>
