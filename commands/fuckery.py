# encoding=utf8
import asyncio

import cat
import random
import os
import wikipedia
import time

#from cleverwrap import CleverWrap
#from utils.config import Config #for cleverwrap's key
from discord.ext import commands

from utils.logger import log
from utils.tools import *
from utils.unicode import *
from utils.fun.lists import *
from utils import checks

class Fuckery(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx):
        """Make the bot say whatever you want it to say"""
        try:
            await ctx.message.delete()
        except:
            pass
        if ctx.author is not ctx.author.bot:
            triggers = ['.', "r.", "hey dragon, ", "hey derg, ", "hey batzz, "]
            msg = ctx.message.clean_content
            for trigger in triggers:
                msg = msg.replace(trigger + "say", "")
            await ctx.send(msg)
        else:
            return

    #from codex  pls dont kill
    @commands.command()
    async def dadjoke(self, ctx):
        """!joke - Get random dad joke."""
        r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'text/plain'})
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as error:
            return print(f'[ERROR] {error}')

        await ctx.send(r.text)

    @commands.command()
    async def test(self, ctx):
        """No context."""
        await ctx.send("( ͡° ͜ʖ ͡°) I love you")

    @commands.command()
    async def cat(self, ctx):
        """Sends a random cute cat gifs because cats are soooo cuteeee <3 >.< -Seth, 2016"""
        await ctx.channel.trigger_typing()
        cat.getCat(directory="data", filename="cat", format="gif")
        await asyncio.sleep(1) # This is so the bot has enough time to download the file
        await ctx.send(file=discord.File("data/cat.gif"))
        # Watch Nero spam this command until the bot crashes

    @commands.command()
    async def f(self, ctx):
        """Press F to pay your respects"""
        await ctx.send("Guess what? {} just paid their respects! Amount paid: {}".format(ctx.author, random.randint(0, 10000)))

    @commands.command()
    async def nicememe(self, ctx):
        """Nice Meme!"""
        await ctx.send("http://niceme.me")

    @commands.command()
    async def dab(self, ctx):
        """Dab for me squiddy"""
        await ctx.send("http://i.giphy.com/lae7QSMFxEkkE.gif")

    @commands.command()
    async def rekt(self, ctx):
        """#REKT"""
        await ctx.channel.trigger_typing()
        await ctx.send(file=discord.File("assets/imgs/rekt.gif"))

    @commands.command()
    async def roasted(self, ctx):
        """MY NIGGA YOU JUST GOT ROASTED!"""
        await ctx.channel.trigger_typing()
        await ctx.send(file=discord.File("assets/imgs/roasted.gif"))

    @commands.command()
    async def yiffinhell(self, ctx):
        """snek yiff"""
        await ctx.channel.trigger_typing()
        await ctx.send(file=discord.File("assets/imgs/yiffinhell.png"))

    @commands.command()
    async def spam(self, ctx):
        """SPAM SPAM SPAM"""
        await ctx.channel.trigger_typing()
        await ctx.send(file=discord.File("assets/imgs/spam.png"))

    @commands.command()
    async def internetrules(self, ctx):
        """The rules of the internet"""
        await ctx.channel.trigger_typing()
        #this is how you create a memory leak
        gayrule = random.choice(open('assets/InternetRules.txt', encoding="utf8").readlines())
        await ctx.send(gayrule)

#    @commands.command()
#    async def perf(self, ctx):
#        """the return of the furry bullshit"""
#        rt = random.choice(tweetsthatareokhand)
#        ctx.send(rt)

    @commands.command(aliases=['emily'])
    async def santropez(self, ctx):
        """:~)"""
        sppt = random.choice(santropez)
        if sppt == "spt":
            await ctx.send(file=discord.File("assets/imgs/spt.png"))
        if sppt == "spt2":
            await ctx.send(file=discord.File("assets/imgs/spt2.png"))
        await ctx.send(sppt)

    @commands.command(aliases=['zekurt'])
    async def kurt(self, ctx):
        """viva la poutine"""
        poutine = random.choice(zekurt)
        await ctx.send(poutine)
    
    @commands.command()
    async def fionn(self, ctx):
        """rawr xd nuzzles u"""
        m35 = random.choice(fionn)
        await ctx.send(m35)

    @commands.command()
    async def nero(self, ctx):
        """learn from a NYer"""
        hoe = random.choice(nero)
        await ctx.send(hoe)

    @commands.command()
    async def seth(self, ctx):
        """wannabe thug"""
        weeb = random.choice(seth)
        await ctx.send(weeb)

    @commands.command(aliases=['sks'])
    async def kae(self, ctx):
        """no friends"""
        yeehaw = random.choice(kae)
        await ctx.send(yeehaw)

    @commands.command(aliases=['sand'])
    async def ryan(self, ctx):
        """actually sand"""
        sand = random.choice(ryan)
        await ctx.send(sand)

    @commands.command(aliases=['patrick'])
    async def mibbzz(self, ctx):
        """jihadist commentaries"""
        cse = random.choice(patrick)
        await ctx.send(cse)

    @commands.command()
    async def derek(self, ctx):
        """japan is my life"""
        fakeweeb = random.choice(derek)
        await ctx.send(fakeweeb)

    @commands.command()
    async def troy(self, ctx):
    	"""boy troy who used to live in detroit who's also a weeb"""
    	nani = random.choice(troy)
    	await ctx.send(nani)

    @commands.command()
    async def speed(self, ctx):
        """ m """
        m = random.choice(speed)
        await ctx.send(m)

    @commands.command(aliases=['ajax'])
    async def super(self, ctx):
        """lion co"""
        lioncompany = random.choice(soopor)
        await ctx.send(lioncompany)

    @commands.command(aliases=['ahegao', 'ron'])
    async def rhymix(self, ctx):
        """and that's the tea"""
        tea = random.choice(rhyfomos)
        await ctx.send(tea)

    @commands.command(aliases=['bruh'])
    async def square(self, ctx):
        """remove emo european"""
        emo = random.choice(square)
        await ctx.send(emo)

    @commands.command()
    async def chaotix(self, ctx):
        """british tf2 meme yeah"""
        tf2 = random.choice(chaotix)
        await ctx.send(tf2)

    @commands.command()
    async def randomimage(self, ctx):
        """Gives you a randomized link from prnt.sc, you've been warned"""
        num = random.randint(1000,9999)
        let = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        let2 = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        await ctx.send(f"https://prnt.sc/{let}{let2}{num}")

    @commands.command(aliases=[':regional_indicator_NWORD:'])
    async def n(self, ctx):
        await ctx.send("<:whatgorilla:553035221474476053> NO N WORD.....")

    @commands.command()
    async def quote(self, ctx):
        """Don't quote me on that"""
        await ctx.channel.trigger_typing()
        await ctx.send(file=discord.File("assets/imgs/quotes/{}.png".format(random.randint(1, len([file for file in os.listdir("assets/imgs/quotes")])))))

    @commands.command()
    async def delet(self, ctx):
        """Delet this"""
        await ctx.channel.trigger_typing()
        await ctx.send(file=discord.File("assets/imgs/delet_this.jpg"))

    @commands.command()
    async def roll(self, ctx, sides: int):
        """Roll the fuck out of this shit."""
        rolling = random.randint(1, sides)
        await ctx.send("You got a {} out of the {} sided die.".format(rolling, str(sides)))

    @commands.command()
    async def lenny(self, ctx):
        """<Insert lenny face here>"""
        await ctx.send(lenny)
        #they're back fuck yeah
        
    @commands.command()
    async def psat(self, ctx):
        """You know he had to do it to her. PSAT Memes from Oct 11, 2017."""
        await ctx.send(random.choice(psat_memes))

    @commands.command(name="8ball")
    async def ball(self, ctx, *, question:str):
        """It's just python random don't take it seriously kthx"""
        await ctx.send("{}: {}".format(ctx.author.name, random.choice(magic_conch_shell)))

    @commands.command()
    async def insult(self, ctx):
        """Insult those ass wipes"""
        thememe = ctx.message.clean_content.replace(".insult", "")
        await ctx.send("{} {}".format(thememe, random.choice(insults)))

    @commands.command()
    async def compliment(self, ctx):
        """I love you."""
        await ctx.send("{}".format(random.choice(compliments)))

    @commands.command()
    async def fish(self, ctx):
        """bird"""
        await ctx.send(":bird:")
        
    @commands.command()
    async def epicman(self, ctx):
        """EPICMAN"""
        await ctx.send("i,m epicman")

    @commands.command()
    async def bird(self, ctx):
        """fish"""
        await ctx.send(":fish:")

    @commands.command()
    async def wattpad(self, ctx):
        """Hello hello 👋 fellow viewers!!! First I want to apologize to some of my grammatical error.. I'm not perfect lolz, aaaaand this story is still in progressed soooo you can judge freeeely. And I'm so excited for this series because..! . . . . . . [ERR..."""
        await ctx.send(random.choice(wattpad))

    @commands.command(aliases=['mentionseth', '<@!169597963507728384>', 'nigato'])
    @checks.is_dev()
    async def ms(self, ctx):
        """@nigato @nigato @nigato"""
        for i in range(5):
            #await ctx.channel.trigger_typing
            await ctx.send(f"<@319679435194368000> {ctx.author} needs you thanks")
            await asyncio.sleep(2)
            print(i) # you want to be used? ill use u alright

    @commands.command()
    async def trico(self, ctx):
        """KREYGASM absolute KREYGASM"""
        await ctx.send("trico... <:hyperkreygasm:460417913837322271>")

    @commands.command()
    async def actdrunk(self, ctx):
        """I got drunk on halloween in 2016 it was great"""
        await ctx.send(random.choice(drunkaf))

    """@commands.command()
    async def talk(self, ctx, *, pussy:str):
        #talk to the bot
        config = Config()
        api_key = config.cb_api_key
        cw = CleverWrap(api_key)
        themessage = cw.say(pussy)
        result = themessage
        try:
            await ctx.send(str(ctx.author) + " >> " + cw.say(result))
        except UnicodeDecodeError:
            await ctx.send("Error has occured trying to decode the Cleverbot message.")"""

    @commands.command()
    async def ship(self, ctx, user1:discord.User=None, user2:discord.User=None):
        """Treat yourself to shipping to FedEx, DHL, UPS, USPS, and more. Nah not really. Ship yourself with someone if you could."""
        if user2 is None:
            await ctx.send("I see you haven't shipped yourself with anyone. Sad.")
        else:
            await ctx.send("I hereby ship {} and {} officially by bot code.".format(user1.mention, user2.mention))

    @commands.command()
    async def rate(self, ctx, *, user):
        """Have the bot rate yourself or another user"""
        if user is None:
            await ctx.send("I rate you a `{}`/`10`".format(random.randint(0, 10)))
        else:
            await ctx.send("I rate {} a `{}`/`10`".format(user, random.randint(0, 10)))

    @commands.command()
    async def coinflip(self, ctx):
        """Make the bot flip either heads or tails."""
        result = random.randint(0, 1)
        if result == int(0):
            await ctx.send("You flipped a coin as high as you could. It falls on the floor since you can't catch it. Surprise, it's heads!")
        elif result == int(1):
            await ctx.send("You flip the coin. You catch it somehow, and interestingly enough, it's tails!")

    @commands.command()
    async def wiki(self, ctx, *, query: str):
        """
        Search the infinite pages of wikipedia!
        """
        #Holy fucking shit, how long has that mistake been here?
        if ("kenya" or "Kenya") in query:
            return await ctx.send("not real sorry")
        cont = re.sub("\s+", '_', query)
        q = wikipedia.page(cont)
        await ctx.channel.trigger_typing()
        em = discord.Embed(description="")
        try:
            if ctx.me.color == None:
                maybe = None
            else:
                maybe = ctx.me.color
            em.title = "Wikipedia"
            em.color = maybe
            em.description = q.url
            em.add_field(name=q.title, value=wikipedia.summary(query, sentences=4))
        except wikipedia.exceptions.PageError:
            em.title = "Error"
            em.add_field(name=cont, value="The phrase you have inputted does not resolve any pages.")
        except wikipedia.exceptions.DisambiguationError:
            em.title = "Error"
            await ctx.send("Looks like there's more than one result. This may refer to the below: \n{}".format(wikipedia.exceptions.DisambiguationError.may_refer_to[:1985]))
        await ctx.send(embed=em)

    @commands.command()
    async def time(self, ctx):
        """Tells the current time from the server"""
        d = time.strftime("%A, %B %d, %Y")
        t = time.strftime("%I:%M:%S %p %Z")
        linemedaddy = "```ruby\nCurrent Date: " + d + '\nCurrent Time: ' + t + "\n" + "```"
        await ctx.send(linemedaddy)

    @commands.command()
    async def memegen(self, ctx, template: str, *, lines: str):
        """
        Attempt on trying to create a meme command, .memeg (template/line1/line2)
        List: http://memegen.link/templates/
        """
        if len(template) and len(lines) != 0:
            memeg = str(template) + " " + str(lines)
            await ctx.send("http://memegen.link/" + re.sub(r"\s+", '-', memeg) + ".jpg")
        else:
            await ctx.send("You didn't enter a message. Templates: http://memegen.link/templates/")

    @commands.command()
    async def honk(self, ctx):
        """Honk honk mother fucker. yes this came back lukkan."""
        await ctx.send(random.choice(honkhonkfgt))

    @commands.command()
    async def plzmsgme(self, ctx, *, message:str):
        """Seriously, why the fuck are you doing this to yourself?"""
        await ctx.author.dm_channel.send(message)
        await ctx.send(":ok_hand: check your DMs")

    @commands.command()
    async def lameme(self, ctx):
        """la meme my bro xdddddddddddddddddd"""
        await ctx.channel.trigger_typing()
        await ctx.send("la meme xd xd")
        await ctx.send(file=discord.File( "assets/imgs/lameme.jpg"))

    @commands.command()
    async def msgquote(self, ctx, id:int):
        """Quotes a message with the specified message ID"""
        message = await ctx.channel.get_message(id)
        if message is None:
            await ctx.send("Can't find {} in here.".format(id))
            return
        embed = make_message_embed(message.author, message.author.color, message.content, formatUser=True)
        await ctx.send(None, embed=embed)
        
    @commands.command()
    async def timer(self, ctx, timer: float, *, message: str):
        await ctx.send("Timer has been set.")
        log.info(str(ctx.author) + " has set the timer for " + str(timer) + " seconds")
        await asyncio.sleep(timer)
        await ctx.send("m its ready\nmessage that came with it {}".format(message.replace("@everyone", "at everyone fuckers ")))

def setup(bot):
    bot.add_cog(Fuckery(bot))
