import nextcord
from api import get_user_info, get_ouid
from nextcord.ext import commands

guild = 1310190580860715049
bot = commands.Bot()
Token = ""
#put bot token here ^

@bot.slash_command(description="Get information about a user")
async def getuser(interaction: nextcord.Interaction, username: str):
    
    user_info = get_user_info(username)
    if user_info:
        embed = nextcord.Embed(
            title="User Information",
            description=f"Here is the information for {user_info['username']}",
            color=nextcord.Color.blue()
        )
        embed.add_field(name="Username", value=user_info["username"], inline=False)
        embed.add_field(name="Platform", value=user_info["platformtype"], inline=True)
        embed.add_field(name="Mastery", value=user_info["mastery"], inline=True)
        embed.add_field(name="Language", value=user_info["language"], inline=True)
        embed.set_footer(text="Requested by " + interaction.user.name, icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed)

@bot.slash_command(description="Get ouid")
async def getouid(interaction: nextcord.Interaction, username: str):
    ouid = get_ouid(username)
    await interaction.response.send_message(f"OUID: `{ouid}`")

@bot.event
async def on_ready():
    print(f"Bot is online! Logged in as {bot.user}")

bot.run(Token)