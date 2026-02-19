<script>
    import { onMount } from "svelte";

    onMount(async () => {
        let max_height = window.innerHeight;
        window.scrollTo(0, max_height);
    });

    export let title = "";
    export let imageUrl = "";
</script>


<div class="w-full p-10">
    {#if imageUrl !== ""}
        <div class="animate-slide-in-right">
            <img
                src={imageUrl}
                alt="Prototipo de imagen"
                class="transition-all duration-300 hover:scale-105 w-full lg:w-1/2 rounded-lg mb-4 float-right ml-4"
            />
        </div>
    {/if}
    {#if title !== ""}
        <h2 class="text-2xl font-semibold text-[#6d0205] animate-fade-in-down">
            {title}
        </h2>
    {/if}
    <div class="animate-slide-in-up">
        <slot />
    </div>
</div>
