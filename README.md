# Dnd Bot
A Discord bot to query the Dnd 5e API found [here](https://github.com/5e-bits/5e-srd-api).

# Usage
You need to either use the DnD API linked above or host it locally (along with the database). Instructions are in the linked repo.

# Requirements
Package requirements are in ```requirements.txt```. In addition, you need to set the ```DND_5E_API_URL``` environment variable (it should end in ```/api```), as well as the ```DISCORD_TOKEN``` environment variable.

# TODO
- Implement ```equipment``` module.
- Perhaps implement functionality to add entries into the DB.