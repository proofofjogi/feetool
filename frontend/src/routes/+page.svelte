<script lang="ts">
	// data from server load function
	export let data;
	console.log(data.feeData);
</script>

<svelte:head>
	<!-- !FOR PWA -->
</svelte:head>

<!-- Take full height (mobile first), center, is simple SPA anyway -->
<main class="h-[100dvh] flex justify-center items-center">
	<div class="flex flex-col gap-3">
		<h1 class="text-center text-4xl font-bold text-secondary">Fee Tool</h1>
		<p class="text-center text-xl">a bitcoin transaction fee tool</p>
		<div class="grid grid-cols-2 gap-8">
			<div class="px-8 py-4 bg-base-300 rounded-3xl">
				<h2 class="text-center text-xl font-bold mb-2 text-primary">Conservative</h2>
				<div class="flex flex-col gap-3">
					<div class="flex gap-3 justify-between">
						<div>Blocks</div>
						<div>Fee Rate</div>
					</div>
					{#each data?.feeData as entry}
						{#if entry.type === 'CONSERVATIVE'}
							<div class="flex gap-3 justify-between">
								<div>{entry.target_blocks}</div>
								<div>{parseInt(entry.fee_rate)} sats/vbyte</div>
							</div>
						{/if}
					{/each}
				</div>
			</div>
			<div class="px-8 py-4 bg-base-300 rounded-3xl">
				<h2 class="text-center text-xl font-bold mb-2 text-primary">Economical</h2>
				<div class="flex flex-col gap-3">
					<div class="flex justify-between">
						<div>Blocks</div>
						<div>Fee Rate</div>
					</div>
					{#each data?.feeData as entry}
						{#if entry.type === 'ECONOMICAL'}
							<div class="flex justify-between">
								<div>{entry.target_blocks}</div>
								<div>{parseInt(entry.fee_rate)} sats/vbyte</div>
							</div>
						{/if}
					{/each}
				</div>
			</div>
		</div>
		<p class="text-center text-xl">Fees taken from bitcoin core</p>
	</div>
</main>
