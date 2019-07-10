from telethon import TelegramClient, sync
from re import sub as sub

def delete_emoji(weird):

    not_weird = sub(r'[^,ĖíДилшод\w]','',weird)
    

    return not_weird

api_id = 'your_ID'
api_hash = 'your_HASH'

client = TelegramClient('my_session', api_id, api_hash).start()

# # get all the channels that I can access
# channels = {d.entity.username: d.entity
#             for d in client.get_dialogs()
#             if d.is_channel}

# # choose the one that I want to list users from
# channel = channels[channel_name]

# # get all the users and print them
# for u in client.get_participants(channel):
#     print(u.id, u.first_name, u.last_name, u.username)

groups = {d.entity.username: d.entity for d in client.get_dialogs() if d.is_channel}

my_group = groups['yourgroup_name']

ids = []

for u in client.get_participants(my_group):
    ids.append([u.username, u.first_name, u.last_name])


with open ('output.csv','w') as file:

    file.write('Username, First Name, Last Name\n')
    for usr in ids:
        
        temp = sub(r"['\[\]]","",str(usr))
        
        try:
            file.write(delete_emoji(temp)+'\n')
        except:
            print(temp)
            file.write(temp[0:temp.find(',')]+',----------,----------\n')

print('Task complete')
