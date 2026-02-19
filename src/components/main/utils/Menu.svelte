<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  export let menuItems = [];
  export let expand = false;
  let openMenus = [];
  let openSubMenus = [];
  let openSubSubMenus = [];

  // Initialize arrays based on the structure of menuItems
  $: openMenus = menuItems.map(() => expand);
  $: openSubMenus = menuItems.map((item) => item.submenu ? item.submenu.map(() => expand) : [], );
  $: openSubSubMenus = menuItems.map((item) => item.submenu ? item.submenu.map((subItem) => subItem.submenu ? subItem.submenu.map(() => expand) : [],  ) : [],  );

  function handleClick(item, index, subIndex = null, subSubIndex = null) {
    if (typeof item !== "string") {
      if (subSubIndex === null) {
        if (subIndex === null) {
          // Toggle the main submenu
          openMenus = openMenus.map((isOpen, i) =>
            i === index ? !isOpen : isOpen,
          );
        } else {
          // Toggle the sub-submenu
          openSubMenus[index] = openSubMenus[index].map((isOpen, i) =>
            i === subIndex ? !isOpen : isOpen,
          );
        }
      } else {
        // Toggle the sub-sub-submenu
        openSubSubMenus[index][subIndex] = openSubSubMenus[index][subIndex].map(
          (isOpen, i) => (i === subSubIndex ? !isOpen : isOpen),
        );
      }
    }
    // Dispatch the event regardless of menu/submenu level

    // recontrur path a patrir de item

    let path = "";

    if (typeof item === "string") {
      path = item;
    } else {
      if (subSubIndex === null) {
        if (subIndex === null) {
          path = item.title;
        } else {
          path = item.submenu[subIndex];
        }
      } else {
        path = item.submenu[subIndex].submenu[subSubIndex];
      }
    }
    dispatch("click", item);
  }
</script>

<nav
  class="animate-slide-in-left w-full lg:w-60 bg-[#fafafa] p-8 p-4 rounded-lg shadow-lg transition-colors duration-300"
>
  <ul>
    {#each menuItems as item, index}
      {#if typeof item === "string"}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
        <li
          class="menu-item py-2 border-b border-[#6d0205] text-[#333] cursor-pointer text-sm lg:text-base rounded transition-colors duration-200"
          on:click={() => handleClick(item, index)}
        >
          {item}
        </li>
      {:else}
        <li
          class="py-2 border-b border-[#6d0205] text-[#333] cursor-pointer text-sm lg:text-base rounded transition-colors duration-200"
        >
          <!-- svelte-ignore a11y-click-events-have-key-events -->
          <!-- svelte-ignore a11y-no-static-element-interactions -->
          <div on:click={() => handleClick(item, index)}>
            <span class="font-semibold text-lg">{item.title}</span>
          </div>
          {#if openMenus[index]}
            <ul class="ml-2 mt-1 text-xs lg:text-sm">
              {#each item.submenu as subitem, subIndex}
                {#if typeof subitem === "string"}
                  <!-- svelte-ignore a11y-click-events-have-key-events -->
                  <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
                  <li
                    class="menu-item py-1 border-b border-gray-300 text-[#333] cursor-pointer rounded transition-colors duration-200"
                    on:click={() => handleClick(subitem, index, subIndex)}
                  >
                    {subitem}
                  </li>
                {:else}
                  <li
                    class="py-1 border-b border-gray-300 text-[#333] cursor-pointer rounded transition-colors duration-200"
                  >
                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                    <!-- svelte-ignore a11y-no-static-element-interactions -->
                    <div on:click={() => handleClick(subitem, index, subIndex)}>
                      <span class="font-semibold">{subitem.title}</span>
                    </div>
                    {#if openSubMenus[index][subIndex]}
                      <ul class="ml-2 mt-1 text-xs lg:text-sm">
                        {#each subitem.submenu as subsubitem, subSubIndex}
                          {#if typeof subsubitem === "string"}
                            <!-- svelte-ignore a11y-click-events-have-key-events -->
                            <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
                            <li
                              class="menu-item py-1 border-b border-gray-300 text-[#333] cursor-pointer rounded transition-colors duration-200"
                              on:click={() =>
                                handleClick(
                                  subsubitem,
                                  index,
                                  subIndex,
                                  subSubIndex,
                                )}
                            >
                              {subsubitem}
                            </li>
                          {:else}
                            <li
                              class="py-1 border-b border-gray-300 text-[#333] cursor-pointer rounded transition-colors duration-200"
                            >
                              <!-- svelte-ignore a11y-click-events-have-key-events -->
                              <!-- svelte-ignore a11y-no-static-element-interactions -->
                              <div
                                on:click={() =>
                                  handleClick(
                                    subsubitem,
                                    index,
                                    subIndex,
                                    subSubIndex,
                                  )}
                              >
                                <span class="font-semibold"
                                  >{subsubitem.title}</span
                                >
                              </div>
                              {#if openSubSubMenus[index][subIndex][subSubIndex]}
                                <ul class="ml-2 mt-1 text-xs lg:text-sm">
                                  {#each subsubitem.submenu as subsubsubitem}
                                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                                    <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
                                    <li
                                      class="py-1 border-b border-gray-300 text-[#333] cursor-pointer rounded transition-colors duration-200"
                                      on:click={() =>
                                        handleClick(
                                          subsubsubitem,
                                          index,
                                          subIndex,
                                          subSubIndex,
                                        )}
                                    >
                                      {subsubsubitem}
                                    </li>
                                  {/each}
                                </ul>
                              {/if}
                            </li>
                          {/if}
                        {/each}
                      </ul>
                    {/if}
                  </li>
                {/if}
              {/each}
            </ul>
          {/if}
        </li>
      {/if}
    {/each}
  </ul>
</nav>

<style>
   .menu-item {
    position: relative;
    overflow: hidden;
  }

  .menu-item::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    height: 2px;
    width: 0%;
    background-color: #6d0205; /* Color del borde animado */
    transition: width 0.3s ease;
  }

  .menu-item:hover::after {
    width: 100%;
  }
  nav {
    background-color: #fafafa; /* Color de fondo del menú */
    transition:
      background-color 0.3s ease,
      box-shadow 0.3s ease;
  }

  nav:hover {

    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Efecto de sombra al pasar el mouse */
  }

  /* Estilos para la tipografía */
  li {
    font-family: "Arial", sans-serif; /* Tipografía más moderna */
  }

  /* Responsividad */
  @media (max-width: 768px) {
    nav {
      width: 100%; /* El menú ocupará todo el ancho en pantallas pequeñas */
    }

    ul {
      padding: 0; /* Quita el padding extra para ajustar el menú */
    }

    li {
      font-size: 14px; /* Reduce el tamaño de las fuentes en pantallas pequeñas */
    }

    .ml-2 {
      margin-left: 10px; /* Ajusta el margen para submenús en pantallas pequeñas */
    }
  }
</style>
