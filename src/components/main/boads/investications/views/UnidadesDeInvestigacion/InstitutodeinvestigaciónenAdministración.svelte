<script>
  export let title = "";
  import BoardLayout from "$BoardLayout";
</script>

<BoardLayout {title}>
  <!-- Descripción del instituto -->
  <p class="mb-4">
    Tiene la misión de abordar conocimientos vinculados con la acción de los
    recursos humanos y materiales dentro de la empresa, sea esta pública o
    privada, como así también lo atinente al desarrollo de sistemas de
    información que permitan reducir el aspecto incertidumbre para una mejor
    toma de decisiones.
  </p>



  <!-- Sección Contacto -->
  <h3 class="text-xl font-semibold text-[#6d0205] pt-4">Contacto</h3>
  <p>
    <strong>Email:</strong><br />
    <a class="text-blue-600" href="mailto:secretariainvestigacion@eco.unca.edu.ar"
      >secretariainvestigacion@eco.unca.edu.ar</a
    >
  </p>

  <!-- Dirección del edificio -->
  <p class="mt-2">
    Edificio de Profesores, Facultad de Ciencias Económicas y de Administración.
    UNCA<br />
    Av. José Figueroa 275, San Fernando del Valle de Catamarca (4700), Catamarca,
    Argentina.
  </p>
</BoardLayout>
