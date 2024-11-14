<script>
	import GridBeam from "../components/GridBeam.svelte";

	let imText = "Michael O'Sullivan";

	import * as THREE from 'three';
	import * as SC from 'svelte-cubed';

	let width = 1;
	let height = 1;
	let depth = 1;

	let spin = 0;

	SC.onFrame(() => {
		spin += 0.01;
	});
</script>

<GridBeam>
<main class="grid grid-cols-5 h-screen w-screen text-white bg-[radial-gradient(#3e3e3e_1px,transparent_1px)] [background-size:16px_16px]">
	
	<div class="col-span-1"></div>
	<div class="p-10 col-span-3">
		<div class="backdrop-blur-[3px] rounded-lg p-6 m-3">
			<h1 class="text-3xl text-white font-bold text-start">
				<span class="text-[#66F217] inline">michael@0sullivan $</span> Hello, I'm {imText}!<span class="text-[#66F217] animate-pulse inline">_</span>
			</h1>
		</div>
		<div class="grid grid-cols-2">
			<div>
				<div class="backdrop-blur-[3px] rounded-lg p-6 m-3">
					<h1 class="text-4xl font-bold text-start text-[#66F217]">
						Bio:<hr>
					</h1>
					<h1 class="text-xl text-white font-bold text-start">
						⋅ I'm a senior in high school at Keefe Tech, in Framingham, MA.<br>
						⋅ 4+ years of coding experience.<br>
						⋅ Flask (Python) + Svelte is my favorite tech stack.<br>
						⋅ Managed Twitter accounts with 1+ million followers.<br>
						⋅ I have certs for several programming languages.<br>
					</h1>
				</div>
				<div class="backdrop-blur-[3px] rounded-lg p-6 m-3 mt-6">
					<h1 class="text-4xl text-white font-bold text-start rounded p-3">
						<a href="https://github.com/m0sullivan"><span class="hover:text-[#66F217]">-> Github</span></a>
					</h1>
				</div>
			</div>
			
			<div class="backdrop-blur-[3px] rounded-lg p-6 m-3">
				<h1 class="text-4xl text-[#66F217] font-bold text-start">
					Notable Links:<hr>
				</h1>
				<h1 class="text-4xl text-white font-bold text-start rounded p-3">
					<a href="/about"><span class="hover:text-[#66F217]">-> About me</span></a>
					<br>
					<a href="https://github.com/m0sullivan/Twitter-Bot-Framework"><span class="hover:text-[#66F217]">-> Twitter Bot</span></a>
					<br>
				</h1>
				<div class="backdrop-blur-[3px] rounded-lg p-6 m-3 py-28">
					​<SC.Canvas antialias background={new THREE.Color(null, null, null)}>
						<SC.Mesh
							geometry={new THREE.BoxGeometry()}
							material={new THREE.MeshStandardMaterial({ color: 0x66F217 })}
							scale={[width, height, depth]}
							rotation={[0, spin, 0]}
						/>
						<SC.PerspectiveCamera position={[1, 1, 3]} />
						<SC.OrbitControls enableZoom={false} />
						<SC.AmbientLight intensity={0.6} />
						<SC.DirectionalLight intensity={1} position={[-2, 3, 2]} />
					​</SC.Canvas>
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
		background-color: black;
		font-family: monospace;
		overflow-x: hidden;
	}
</style>
