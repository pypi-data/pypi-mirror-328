A simple example of a bot that will repeat after the user
```python
from aiotele import Bot
from aiotele.types import MessageObject, CommandObject
import asyncio

TOKEN = "YOU_TOKEN"
bot = Bot(TOKEN)

@bot.message_handler()
async def repeat(msg: MessageObject, command: CommandObject):
    await msg.reply(f"I don't know such a command!")


async def main():
    await bot.run()

asyncio.run(main())
```
deleting webhook
```python
async def main():
    await bot.delete_webhook(True)
    await bot.run()
```
To check whether a new user has joined or not
```python
from aiotele import JOIN_TRANSITION
from aiotele.types import NewChatMember

@bot.chat_member(JOIN_TRANSITION)
async def new_chat_member(new_member: NewChatMember):
    await new_member.answer(f"Hello {new_member.new_member.full_name}! Added you {new_member.old_member.full_name}!")
```
To check whether a user has logged out or not
```python
from aiotele import LEAVE_TRANSITION
from aiotele.types import LeaveChatMember

@bot.chat_member(LEAVE_TRANSITION)
async def leave_chat_member(leave_member: LeaveChatMember):
    await leave_member.reply(f"Bye {leave_member.leave_member.full_name}!")
```
Check whether the bot has been added to the group or not
```python
from aiotele import JOIN_TRANSITION
from aiotele.types import NewChatMember

@bot.my_chat_member(JOIN_TRANSITION)
async def bot_join_chat_member(new_member: NewChatMember):
    await new_member.answer(f"Thank you for adding me to the chat. {new_member.old_member.full_name}!")
```