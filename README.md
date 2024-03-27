# What is feetool?

Feetool is a tool that is going to help you understand if bitcoin transaction fees are high or low or anything in between compared to what they have been before.

If you do frequent bitcoin transactions this tool might help you.

Feetool is FOSS and will remain FOSS forever.

## Project status

Frontend has some code written for simple display of the latest fee rate. That's the initial hosted version. Not very useful but that's because the tool needs to gather data first. We need a baseline to compare against.

This isn't hosted anywhere yet either.

## Project specs:

These specs are needed to make this work

- Fees: First and foremost, the project needs a fee source. This could come from a prunded node running on the server for the productino site via RCP. This could also come from mempool (if they have a fee API, author is not clear on that).

- Backend: Cronjob that updates fees regularly, say 5 minute intervals. Store in Pocketbase for API calls on frontend

- Frontend: Svelte kit app, make it as a PWA so it's platform agnostic and censorship proof, dispatch notifications for logged in users (nostr login).

- FOSS at all time
