import discord
import responses
from _handle_verification_ import handle_verification
import gitgud
from paginator import table
client = None
async def send_message(ctx,user_message,is_private):                                      #giving back response to the user
    try:
        response= await responses.handle_response(str(user_message),ctx)                            #fetching response
        await ctx.author.send(response) if is_private else await ctx.channel.send(response)     #sending response in dm if private or in channel if not
    except Exception as e:
        print(e)

async def run_discord_bot():
    global client
    TOKEN='MTA0ODIzNTAxMjcxMTAxMDM2NA.G6wi4q.6AE7Q3otjPtQ-Hu9JJ0C6hNnVDEc_M9xSsmLTc'    #bot id
    print('hello')
    client = discord.Client(intents=discord.Intents.all())                              #giving permissions and intents to the bot
    guild_id=1048212913539784805        #guild id
    guild=client.get_guild(guild_id)
    @client.event
    async def on_ready():                                                               #logged in successfully
        print('We have logged in')
    
    @client.event
    async def on_message(ctx):
        print(ctx)

        if ctx.author == client.user:                                               #will keep messaging itself without this
            return
        user_message=str(ctx.content)
        if (user_message.startswith(';identify')):
            await handle_verification(ctx)
        if user_message[0]=='?':                                                        #checking if message is private
            user_message=user_message[1:]
            await send_message(ctx,user_message,is_private=True) #message is private
        if user_message.split()[0]==";gitlog":
             mydict =  await gitgud.gitlog(ctx)
             await table(ctx,client,['Problem Name','Problem Rating','Points'], mydict)
        else:
            await send_message(ctx,user_message,is_private=False)#message is not private


    client.run(TOKEN)