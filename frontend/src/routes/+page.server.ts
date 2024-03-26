import PocketBase from 'pocketbase';

import { PB_URL, PB_ADMIN_PASSWORD, PB_ADMIN_USERNAME } from '$env/static/private';

export async function load() {
	const pb = new PocketBase(PB_URL);
	// !authenticate as admin
	pb.admins.authWithPassword(PB_ADMIN_USERNAME, PB_ADMIN_PASSWORD);

	// !Query data
	const feeData = await pb.collection('fee_data').getFullList({
		sort: '-created'
	});
	// !send data to frontend
	return { feeData };
}
