<script lang="ts">
	import { onMount } from 'svelte';
	let piData: any = null;
	let error: any = null;

	// Fetch data from the API when the component mounts
	async function fetchData() {
		try {
			//const response = await fetch('https://your-app.onrender.com/api/pi');
			const response = await fetch('http://127.0.0.1:5001/api/pi');
			if (response.ok) {
				piData = await response.json(); // Parse JSON response
			} else {
				error = 'Failed to fetch data';
			}
		} catch (err: any) {
			error = 'An error occurred: ' + err.message;
		}
	}

	let intro_count: number;
	let intro: boolean;
	let intro_sequence: number[];
	let intro_count_sequence: number[];
	function introCount() {
		intro_sequence = [
			0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
			1,  1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3.1, 3.1, 3.1, 3.1, 3.14, 3.14, 3.14,
			3.141, 3.1415, 3.14159, 3.141592, 3.1415926, 3.14159265, 3.1415926544, 3.141592654439,
			3.141592654498854, 3.14159265449885456, 3.14159265449885456038, 
		];
		intro_count = 0;
		intro = true;
		const interval = setInterval(() => {
			if (intro_count < intro_sequence.length - 1) {
				intro_count++;
			} else {
				intro = false;
				clearInterval(interval);
			}
		}, 30);
	}

	onMount(() => {
		introCount();

		setInterval(() => {
			fetchData();
		}, 1000);
	});
</script>

<div
	class="flex h-screen items-center justify-center bg-gradient-to-b from-black to-blue-950 text-white"
>
	<div class="font-mono text-4xl font-bold">
		{#if intro}
			<div>
				<span class="">
					<p class="">Current π approximation: {intro_sequence[intro_count]}</p>
					<br />
				</span>
			</div>
		{:else if piData}
			<span class="">
				<p>Current π approximation: {piData.pi}</p>
				<p>Calculated iterations: {piData.iterations}</p>
			</span>
		{:else if error}
			<p>{error}</p>
		{:else}
			<p>Loading...</p>
		{/if}
	</div>

	<a
		class="fixed bottom-5 right-5 w-10 max-sm:hidden"
		href="https://github.com/Nikolai-Grytvik-Borbe"
	>
		<img class="hover:scale-105" src="/../github_logo.png" alt="GITHUB" />
	</a>
</div>
