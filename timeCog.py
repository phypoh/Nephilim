import discord
import asyncio
import time
from discord.ext import commands

class timeCog(commands.Cog):
    def __init__(self, _commands):
        self.msglist = []
        self.timelist = []

    @commands.command()
    async def test(self, ctx):
        """Check if the time cog is loaded."""
        await ctx.send("Testing, testing. Cog is working!")

    @commands.command()
    async def remind(self, ctx, *, message:str):
        """Set a reminder: !remind <X> <minutes/hours> <message>"""
        try:
            [num, period, msg] = message.split(' ', 2)
            num = int(num)

            if "hour" in period:
                seconds = num*3600
                self.timelist.append("{} hrs".format(num))
            elif "min" in period:
                seconds = num*60
                self.timelist.append("{} mins".format(num))
            elif "sec" in period:
                seconds = num
                self.timelist.append("{} secs".format(num))
            else:
                await ctx.send("Please send a valid period")

            output = "Reminder has been set to recur every {num} {period} for the following message: \n{msg}".format(num=num, period=period, msg=msg)
            await ctx.send(output)

            self.msglist.append(msg)

            await self.recurr(ctx, seconds, msg)

        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    async def recurr(self, ctx, seconds, msg):
        if msg in self.msglist:
            await asyncio.sleep(seconds)
            embedVar = discord.Embed(title=msg, color=0x00ff00)
            await ctx.send(embed=embedVar)
            # await ctx.send(msg)
            await self.recurr(ctx, seconds, msg)

    @commands.command()
    async def show(self, ctx):
        """Show reminders set so far"""
        if len(self.msglist) == 0:
            await ctx.send("There are no reminders set!")

        else:
            output = "List of reminders:\n"
            for i in range(len(self.msglist)):
                output += "{}) ".format(i+1)
                output += self.msglist[i]
                output += " ("
                output += self.timelist[i]
                output += ")\n"
            await ctx.send(output)

    @commands.command()
    async def remove(self, ctx, *, num:int):
        """Remove a reminder from the !show list. !remove <number>"""
        output = "The following reminder has been removed: \n" + self.msglist[num-1]
        del self.msglist[num-1]
        del self.timelist[num-1]
        await ctx.send(output)



def setup(bot):
    bot.add_cog(timeCog(bot))