<script>
// @ts-nocheck

	import Header from "./components/layout/Header.svelte";
	import Navbar from "./components/layout/Navbar.svelte";
	import Footer from "./components/layout/Footer.svelte";
	import Home from "./components/main/boads/init/Index.svelte";
	import About from "./components/main/boads/about/Index.svelte";
	import Offer from "./components/main/boads/offer/Index.svelte";
	import Investigation from "./components/main/boads/investications/Index.svelte";
	import Community from "./components/main/boads/community/Index.svelte";
	import Extensions from "./components/main/boads/extensions/Index.svelte";
	import Postgraduate from "./components/main/boads/postgraduate/Index.svelte";
	import Library from "./components/main/boads/library/Index.svelte";
	import New from "./components/main/boads/new/Index.svelte";
	import Contact from "./components/main/boads/contact/Index.svelte";
	import OfferQuery from "./components/main/boads/offerQuery/Index.svelte";
	import ADistancia from "./components/main/boads/Others/ADistancia.svelte";
	import Terms from "./components/main/PageAux/Terms.svelte";
	// @ts-ignore	
	import { Router, Route } from "svelte5-router";// manejo de rutas
	// @ts-ignore
	export let url = "";
</script>

<svelte:head>
	<title>Facultad de Ciencias Económicas y de Administración</title>
</svelte:head>

<div class="min-h-screen bg-gray-100">
	<Header />
	<Router {url} >
		<Navbar />
		<Route path="/" component={Home} />
		<Route path="/about" component={About} />
		<Route path="/:id" >{#snippet children(params)}<OfferQuery id={params.id}/> {/snippet} </Route>
		<Route path="/offer" component={Offer} />
		<Route path="/investigation" component={Investigation} />
		<Route path="/community" component={Community} />
		<Route path="/community/:id" > {#snippet children(params)}<Community id={params.id}/> {/snippet}  </Route>
		<Route path="/extension" component={Extensions} />
		<Route path="/posgrado" component={Postgraduate} />
		<Route path="/library" component={Library} />
		<Route path="/news" component={New} />
		<Route path="/contact" component={Contact} />
		<Route path="/distancia" component={ADistancia} />
		<Route path="/terms" component={Terms} />
	</Router>
	<Footer />
</div>
