from filobot.filobot import config, bot
from filobot.tasks import update_game, update_hunts, start_server

bot.loop.create_task(update_hunts())
bot.loop.create_task(update_game())
bot.loop.create_task(start_server())

bot.run(config.get('Bot', 'Token'))
