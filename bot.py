import discord
from discord import app_commands

id_do_servidor = 1233414963557826701
arquivo_saida = "registros.txt"

class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        self.voice_states = {}  # Dicionário para rastrear o tempo dos membros no canal de voz

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=id_do_servidor))
            self.synced = True
        print(f"Entramos como {self.user}.")

    async def on_voice_state_update(self, member, before, after):
        if before.channel != after.channel:
            if before.channel:
                time_spent = discord.utils.utcnow().timestamp() - self.voice_states.pop(member.id, 0)
                if time_spent > 0:
                    hours = int(time_spent) // 3600
                    minutes = int(time_spent) % 3600 // 60
                    with open(arquivo_saida, "a") as f:
                        f.write(f"{member.name} saiu do canal de voz após {hours} horas e {minutes} minutos.\n")
            if after.channel:
                self.voice_states[member.id] = discord.utils.utcnow().timestamp()

aclient = Client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild=discord.Object(id=id_do_servidor), name='ping', description='Testando')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Estou funcionando!", ephemeral=True)

aclient.run('MTIzMzQxNDA3OTIwNTQ3ODQ5MQ.GDbCVt.kMHPD9tG6HKw7vkWxB_1q27jdWgp2XJTJEv_dk')
