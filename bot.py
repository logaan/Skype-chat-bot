import Skype4Py

skype = Skype4Py.Skype()
if not skype.Client.IsRunning:
	skype.Client.Start()
skype.FriendlyName = 'logans-chat-bot'
skype.Attach()

print "1. Friends"
for u in skype.Friends:
	print u.Handle

print "2. Chat"
c = skype.Chats[0]
print "Chat with", c.FriendlyName
for m in c.RecentMessages:
	print m.Body
c.SendMessage("Build's broken")
