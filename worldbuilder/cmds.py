from worldbuilder.models import Character, Room, Mob
from django.contrib.auth.models import User


def make_character(username, password, conn):
    userN = User.objects.create_user(username, password)
    userN.save()

    c = Character(
    name=username,
    desc="",
    user=userN,#User.objects.get(username="robin"),
    connection=conn,
    role="",
    title="the fresh meat",
    alignment="TN",
    maxHealth=1,
    currentHealth=1,
    ac=10,
    fort=0,
    ref=0,
    will=0,
    spot=0,
    listen=0,
    newOrNot=True,
    ).save()
    c.rooms.add(Room.objects.get(id=1))
    return "blah"

def check_if_character_exists(name):
    '''
    If the username exists, return True, else return false
    '''
    if not User.objects.get(username=name):
        return False
    else:
        return True

def login(name, password, conn):
    user = User.objects.get(username=name)
    if not user.check_password(password):
        return False
    else: # if correct
        return True
#print
#print check_if_character_exists("robin")
#print login("robin", "pass", "swag")

def look(this_character_name):
    #c = Character.objects.filter(name=this_character_name).values('room')
    #return Room.objects.filter(pk=c).values('desc')
    return Room.objects.filter(pk=Character.objects.filter(name=this_character_name).values('rooms')).values('desc')

print look("johann")

def _get_pk_of_room_character_is_in(this_character_name):
    return Character.objects.all().filter(name=this_character_name).values('rooms')

def _parse_list(query_set):
    return '\n'.join([str(i) for i in query_set.values_list('name', flat=True)])

def look2(this_character_name):
    room_description = Room.objects.filter(pk=Character.objects.filter(name=this_character_name).values('rooms')).values('desc')
    characters_in_room = Character.objects.all().filter(rooms=Room.objects.filter(pk=Character.objects.filter(name="Vulukyr").values('rooms')))
    mobs_in_room = Mob.objects.all().filter(rooms=Room.objects.filter(pk=_get_pk_of_room_character_is_in(this_character_name)))
    return _parse_list(room_description)+_parse_list(characters_in_room)+_parse_list(mobs_in_room)
    #mobs_in_room = Mob.objects.filter(name=Room.objects.filter(pk=Character.objects.filter(name=this_character_name).values('rooms'))).values('name')

print look2("johann")
