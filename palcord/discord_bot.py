import discord
from util import get_global_ip, get_ini_config, palcord_config

bot = discord.Bot()


@bot.slash_command(
    description="Show Palworld Server information",
    description_localizations={"ja": "Palworldサーバーの情報を表示します"},
)
async def info(ctx):
    palworld_config = get_ini_config()
    server_name = palworld_config.get("ServerName", "")
    server_description = palworld_config.get("ServerDescription", "")
    server_password = palworld_config.get("ServerPassword", "")
    if not server_password:
        server_password = "-No Password-"
    else:
        server_password = f"`{server_password}`"
    server_ip = palworld_config.get("PublicIP", "")
    if not server_ip:
        server_ip = get_global_ip()
    server_port = palworld_config.get("PublicPort", "")
    embed = discord.Embed(title=server_name, description=server_description, color=discord.Colour.blue())
    embed.add_field(name="Address", value=f"{server_ip}:{server_port}", inline=True)
    embed.add_field(name="Password", value=server_password, inline=True)
    await ctx.respond(embed=embed)


# @bot.slash_command()
# async def change_topic(ctx, contents, id):
#     channel: discord.channel.GuildChannel = bot.get_channel(int(id))
#     await channel.edit(topic=contents)
#     await ctx.respond("done.")


@bot.slash_command(
    description="Add Steam user to Palworld Server",
    description_localizations={"ja": "PalworldサーバーにSteamユーザーを追加します"},
    options=[
        discord.Option(
            name="steam-id", description="Player's Steam ID", description_localizations={"ja": "プレイヤーのSteam ID"}
        )
    ],
)
async def register(ctx, steam_id: int):
    await ctx.respond(f"Steam ID {steam_id} is added.")


bot.run(palcord_config["DiscordBOT-Token"])
