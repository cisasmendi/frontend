<script>
    import Index from "./Index.svelte";
    export let title = "Diplomatura";
    export let course = 10;
    // @ts-ignore
    import Menu from "$utilsMain/Menu.svelte";
    import { onMount } from "svelte";

    onMount(async () => {
        let max_height = window.innerHeight;
        window.scrollTo(0, max_height);
    });
</script>

<main class=" mx-auto flex flex-col lg:flex-row w-full lg:w-auto">
    <Menu />
    <Index {title} {course} />
</main>
