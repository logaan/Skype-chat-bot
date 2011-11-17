# python bot.py '#l0gaan/$echo123;f8415547db7af82e' 'duuude lol'
import Skype4Py
import sys

# Pull in args
if len(sys.argv) != 3:
	print "usage: python bot.py chatid 'message to send'"
	sys.exit(1)
else:
	chat_id = sys.argv[1]
	message_to_send = sys.argv[2]

# Connect to skype
skype = Skype4Py.Skype()
if not skype.Client.IsRunning:
	skype.Client.Start()
skype.FriendlyName = 'logans-chat-bot'
skype.Attach()

# Find the chat and send the message
find_group_chat = lambda chat: chat.Name == chat_id
group_chat = filter(find_group_chat, skype.Chats)[0]
group_chat.SendMessage(message_to_send)

