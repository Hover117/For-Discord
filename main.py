import discord
from discord.ext import commands

TOKEN = "YOUR_BOT_TOKEN"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def edit(ctx, message_id: int, *, new_content: str):
    """Command to edit a specific message in the same channel."""
    try:
        message = await ctx.channel.fetch_message(message_id)
        await message.edit(content=new_content)
        await ctx.send("✅ Message edited successfully!", delete_after=5)
    except discord.NotFound:
        await ctx.send("❌ Message not found!", delete_after=5)
    except discord.Forbidden:
        await ctx.send("❌ I don’t have permission to edit this message!", delete_after=5)
    except discord.HTTPException as e:
        await ctx.send(f"❌ Failed to edit message: {e}", delete_after=5)

bot.run(TOKEN)
