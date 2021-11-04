from fbchat import Client
from fbchat.models import Message

# Facebook user credentials:
username = "username.or.email"
password = "password"

# login
client = Client(username, password)

# get the 20 recent users you talked to:
users = client.fetchThreadList()
print(users)