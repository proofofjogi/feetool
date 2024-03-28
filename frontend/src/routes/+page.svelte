<script lang="ts">
	// data from server load function
	export let data;
	// @ts-ignore
	let latestFees = data?.items;
</script>

<svelte:head>
	<!-- !FOR PWA -->
</svelte:head>

<!-- Take full height (mobile first), center, is simple SPA anyway -->
<main class="h-[100dvh] flex justify-center items-center">
	<div class="flex flex-col gap-3">
		<h1 class="text-center text-4xl font-bold text-secondary">Fee Tool</h1>
		<p class="text-center text-xl">a bitcoin transaction fee tool</p>

		<div class="px-8 py-4 bg-base-300 rounded-3xl">
			<h2 class="text-center text-xl font-bold mb-2 text-primary">Current Fees</h2>
			<div class="flex flex-col gap-3">
				<div class="flex justify-between">
					<div>Blocks</div>
					<div>Fee Rate</div>
				</div>
				{#each latestFees as feeData}
					<div class="flex justify-between gap-3">
						<div>{feeData.target_blocks}</div>
						<div>{parseInt(feeData.fee_rate)} sats/vbyte</div>
					</div>
				{/each}
			</div>
		</div>
		<p class="text-center text-xl">Fees data source is blockstream</p>
	</div>
</main>
