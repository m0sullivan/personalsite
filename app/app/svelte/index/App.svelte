<script>
	import { Router, Route, Link } from "svelte-navigator";
	import Home from "./Home.svelte";
</script>
<Router>
	<main>
		<Route>
			<Home/>
		</Route>
	</main>
</Router>
<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

	body {
		background-color: black;
		font-family: monospace;
		overflow-x: hidden;
	}
</style>
