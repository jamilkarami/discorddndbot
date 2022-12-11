import os
from discord import Embed

API_URL = os.getenv('API_URL')

class DndObject:
    vals: dict

    def get_vals(self):
        raise NotImplementedError 
    
    def get_embed(self):
        embed = Embed(title = self.name if self.name else self.embedtitle)
        vals: dict = self.get_vals()
        if 'Image' in vals:
            embed.set_image(url=API_URL+vals['Image'])
            vals.pop('Image')
        for k,v in vals.items():
            inline = k!="Description"
            if v:
                if type(v) is str:
                    v = v[0].upper() + v[1:]
                    if len(v) > 256:
                        inline = False
                    if len(v) > 1024:
                        v = v[:1021]+"..."
                embed.add_field(name=k, value=v, inline=inline)
        return embed
