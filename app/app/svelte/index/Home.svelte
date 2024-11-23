<script>
	import GridBeam from "../components/GridBeam.svelte";
	import * as THREE from 'three';
	import * as SC from 'svelte-cubed';
	import Typewriter from 'typewriter-effect/dist/core';
	import { onMount, onDestroy } from 'svelte';

	let imText = "Michael O'Sullivan";

	let texts = ["Michael O'Sullivan", "Михайл О'Сулливан", "decent at coding", "behind you", "having a good time", "talking to myself", "a functional alcoholic", "neck deep in debt", "just alright", ".................", "afraid of heights", "a homo sapiens", "a natural", "being put down", "around", "buying a home in the Atlanta area", "graduating law school", "addicted to playing fortnite", "taking a break", "among us", "at 48°35'37.2\"N 37°52'09.4\"E", "washing my hands", "banned on chinese internet", "soooooo funny :)"];

	let width = 1;
	let height = 1;
	let depth = 1;

	let spin = 0;

	SC.onFrame(() => {
		spin += 0.01;
	});

	let typewriter;
	let element;
	
	onMount(() => {
		typewriter = new Typewriter(element, {
			strings: texts,
			autoStart: true,
			loop: true,
			cursor: `<span class="text-[#66F217] animate-pulse inline">_</span>`,
		});
	});
	
	onDestroy(() => {
		// Stop the effect when the element disappears
		if(typewriter) {
			typewriter.stop();
		}
	})
</script>

<GridBeam>
<main class="grid grid-cols-1 lg:grid-cols-5 min-h-screen w-screen text-white bg-[radial-gradient(#3e3e3e_1px,transparent_1px)] [background-size:16px_16px] [background-position:0_0]">
	<div class="col-span-1"></div>
	<div class="p-6 sm:p-10 col-span-3">
		<div class="backdrop-blur-[2px] bg-neutral-800/30 rounded-lg p-6 mt-3 mb-3">
			<h1 class="text-2xl sm:text-3xl md:text-3xl text-white font-bold text-start">
				<span class="text-[#66F217] inline">michael@0sullivan $</span> Hello, I'm <span bind:this={element}></span>
			</h1>
		</div>
		<div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
			<div>
				<div class="backdrop-blur-[2px] bg-neutral-800/30 rounded-lg p-6 mt-3">
					<h1 class="lg:text-4xl text-[#66F217] font-bold text-start">
						Bio:<hr>
					</h1>
					<p class="lg:text-xl text-white text-start font-bold">
						⋅ I'm a senior in high school at Keefe Tech, in Framingham, MA.<br>
						⋅ I have 4+ years of coding experience.<br>
						⋅ Flask (Python) + Svelte is my favorite tech stack.<br>
						⋅ I Managed Twitter accounts with 1+ million followers.<br>
						⋅ I have certs for Python, HTML + CSS, JavaScript, and Java.<br>
						⋅ I speak English, Spanish, and Russian.<br>
					</p>
				</div>
				<div class="backdrop-blur-[2px] bg-neutral-800/30 rounded-lg p-6 mt-6">
					<h1 class="lg:text-xl text-white font-bold text-start rounded p-3">
						<a href="https://github.com/m0sullivan" class="hover:text-[#66F217]">-> Github</a>
					</h1>
				</div>
			</div>
			
			<div class="backdrop-blur-[2px] bg-neutral-800/30 rounded-lg p-6 mt-3">
				<h1 class="lg:text-4xl text-[#66F217] font-bold text-start">
					Notable Links:<hr>
				</h1>
				<p class="lg:text-xl text-white text-start rounded p-3 font-bold">
					<a href="https://github.com/m0sullivan/Twitter-Bot-Framework" class="hover:text-[#66F217]">-> Twitter Bot</a><br>
					<a href="https://github.com/m0sullivan/funnychat" class="hover:text-[#66F217]">-> NoJS Chat App</a><br>
					<a href="https://github.com/m0sullivan/personalsite" class="hover:text-[#66F217]">-> This Website's Code</a><br>
				</p>
				<h1 class="lg:text-4xl text-[#66F217] font-bold text-start">
					Torus Knot (enable WebGL):<hr>
				</h1>
				<div class="backdrop-blur-[2px] bg-neutral-800/30 bg-neutral-800/30 p-6 m-3 py-28 outline outline-1">
					<SC.Canvas antialias background={new THREE.Color(null, null, null)}>
						<SC.Mesh
							geometry={new THREE.TorusKnotGeometry}
							material={new THREE.MeshStandardMaterial({ color: 0x66F217 })}
							scale={[width, height, depth]}
							rotation={[0, spin, spin]}
						/>
						<SC.PerspectiveCamera position={[1.5, 1.5, 4]} />
						<SC.OrbitControls enableZoom={false} />
						<SC.AmbientLight intensity={0.6} />
						<SC.DirectionalLight intensity={1} position={[-2, 3, 2]} />
					</SC.Canvas>
				</div>
			</div>
		</div>
	</div>
	<div class="col-span-1"></div>
</main>
</GridBeam>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

	body {
		font-family: monospace;
		overflow-x: hidden;
	}

	/* Add a wave animation for the background dots */
	@keyframes wave {
		0% {
			background-position: 0 0;
		}
		50% {
			background-position: 250px 250px;
		}
		100% {
			background-position: 0 0;
		}
	}

	main {
		animation: wave 50s ease-in-out infinite;
	}

	/* Custom styles for handling overflow on smaller screens */
	/* Ensure text doesn't overflow */
	.text-start {
		word-wrap: break-word;
		overflow-wrap: break-word;
	}
</style>
