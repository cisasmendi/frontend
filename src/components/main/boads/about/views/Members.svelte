<script>
  import BoardLayout from "$BoardLayout";
  export let title = "";
  export let categories = [
    {
      title: "Consejo Directivo - Profesores",
      groups: [
        {
          title: "Titulares",
          members: [
            "Rivas, Juan Marcelo",
            "Juri, Marisa Rosana",
            "Barcat, Miguel",
            "Leiva, Raúl Eduardo",
          ],
        },
        {
          title: "Suplentes",
          members: [
            "Carrizo Safe, Oscar Eduardo",
            "Gilyam, Fabio Alejandro",
            "Gallo, Leticia Inés",
            "Degani, Jorge Sebastián",
          ],
        },
      ],
    },
    {
      title: "Auxiliares",
      groups: [
        {
          title: "Titulares",
          members: [
            "Teme, Mirian Rosana",
            "Sarmiento, Gustavo David",
            "Chacur, Walter Edgardo",
          ],
        },
        {
          title: "Suplentes",
          members: [
            "Arévalo Boggio, Ana Laura",
            "Lascano, Braian Martín",
            "Karamanef, Adriana Paola",
          ],
        },
      ],
    },
    {
      title: "No Docentes",
      groups: [
        {
          title: "Titular",
          members: ["Rivas López, Rodolfo Alejandro"],
        },
        {
          title: "Suplente",
          members: ["Pozywilko, Susana Marilyn"],
        },
      ],
    },
    {
      title: "Estudiantes",
      groups: [
        {
          title: "Titulares",
          members: [
            "Casimiro, Jorge Elías",
            "Dolcemascolo, Patricia Alejandra",
            "Vizzoni, Enzo Daniel",
            "Aybar Hidalgo, Erika Johana",
            "Barrionuevo, Maira",
          ],
        },
        {
          title: "Suplentes",
          members: [
            "Ríos, Carolina",
            "Nieva, Rocío Anahí",
            "Romero, Julieta Virginia",
            "Sánchez, Facundo Ezequiel",
            "Tapia, Andrea Melina",
          ],
        },
      ],
    },
    {
      title: "Egresados",
      groups: [
        {
          title: "Titular",
          members: ["Aguero, Mirtha Celia Elisa"],
        },
        {
          title: "Suplente",
          members: ["Parra Ceballos, Eugenia Mónica Andrea"],
        },
      ],
    },

  ];
</script>

<BoardLayout {title}>
  <div class="p-4 space-y-8">
    {#each categories as category}
      <div>
        <h2 class="text-2xl font-bold text-[#6d0205] mb-6">{category.title}</h2>
        <div class="grid gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
          {#each category.groups as group}
            <div class="bg-white rounded-lg shadow-lg p-6">
              <h3 class="text-xl font-semibold text-[#942c2e] mb-4">
                {group.title}
              </h3>
              <ul class="list-disc list-inside">
                {#each group.members as member}
                  <li class="ml-4 text-gray-700">{member}</li>
                {/each}
              </ul>
            </div>
          {/each}
        </div>
      </div>
    {/each}
  </div>
</BoardLayout>
