<script lang="ts">
	// data from server load function
	export let data;
	// console.log(data.feeData);
</script>

<svelte:head>
	<!-- !FOR PWA -->
</svelte:head>

<!-- Take full height (mobile first), center, is simple SPA anyway -->
<main class="h-[100dvh] flex justify-center items-center">
	<div class="flex flex-col gap-3">
		<h1 class="text-center text-4xl font-bold text-primary">Fee Tool</h1>
		<p class="text-center text-xl">a bitcoin transaction fee tool</p>
		<div class="flex flex-col gap-2">
			<div class="flex gap-3 justify-between">
				<div>Target Block</div>
				<div>Fee Rate</div>
			</div>
			{#each data?.feeData as entry}
				<div class="flex gap-3 justify-between">
					<div>{entry.target_blocks}</div>
					<div>{entry.fee_rate}</div>
				</div>
			{/each}
		</div>
	</div>
</main>
