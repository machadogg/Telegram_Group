from telethon import TelegramClient, sync

api_id = 'your_ID'
api_hash = 'your_hash'

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

my_group = groups['your_group_name']

ids = []

for u in client.get_participants(my_group):
    ids.append([u.username, u.first_name, u.last_name])




with open ('output.csv','w') as file:

    file.write('Username, First Name, Last Name\n')
    for usr in ids:
        
        temp = str(usr)
        temp = temp.strip('[]')
        temp = temp.replace("'","")
        try:
            file.write(temp+'\n')
        except:
            loc = []
            for i in range(len(temp)):
                if temp[i] == ',':
                    loc.append(i)
            temp2 = temp[0:loc[0]]
            file.write(temp2+',----------,----------\n')

print('Task complete')
