from discord import app_commands

def get_options(opts: dict):
    options = []
    for k,v in opts.items():
        options.append(app_commands.Choice(name=k, value=v))
    return options