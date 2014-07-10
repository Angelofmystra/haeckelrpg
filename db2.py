from worldbuilder.models import Area, Room, Mob, Character, Equipment, Weapon, Shield, Armor, House, Noble
import json
from django.core import serializers

### These functions effectively provide a public interface for the server to access simply by importing this file.###
def area():
	return Area.objects.all()
# This function requires a way to validate the data
def make_character(character_name, ip_address, character_alignment, max_hp, character_ac, character_fort, character_ref, character_will, character_spot, character_listen, new_or_not):
	c = Character(
			name=character_name, 
			ipAddress=ip_address, 
			alignment=character_alignment, 
			maxHealth=max_hp,
			ac=character_ac,
			fort=character_fort,
			ref=character_ref,
			will=character_will,
			spot=character_spot,
			listen=character_listen,
			newOrNot=new_or_not,
			title="the Fresh Meat",
			currentHealth=max_hp) # This should fail because room has not been set.
# This function should get the current character, then look at the room of which the character is in, and then look at the description as well as contents of the room.
# If this function has parameters, then it should check the current character's room, check to see who else is in it, if the target is in the room, then it should get the target's description.
#      Else, it should state something along the lines of: You dont see it.
def look(this_character_name):
	#c = Character.objects.filter(name=this_character_name).values('room')
	#return Room.objects.filter(pk=c).values('desc')
	return Room.objects.filter(pk=Character.objects.filter(name=this_character_name).values('room')).values('desc')

print look("Vulukyr")

def observe(this_character_name, target_object_name):
	# This block of code indicates that the player is specifying which object to look at (in the vast majority of cases when many are in the room)
	if "." in target_object_name:
		quantity = target_object_name[-2:]
		# This deals with the corner case where you have 10 or more objects in a room. It should be rare to have this, and even rarer to have a 3 digit number so that corner case is not handled.
		if "." in quantity:
			quantity.replace(".","")
		else:
			quantity = target_object_name[-1:]+quantity

	#get the current character's room id
	local_room_id = Room.objects.filter(pk=Character.objects.filter(name=this_character_name).values('room')).values('id')
	#check to see if mob the character is looking at is in the room
	a = Mob.objects.filter(rooms=local_room_id).filter(name=target_object_name).values('desc')
	# The effect of this code block is such that is, for example, if Vulukyr looks at himself, he will see himself. If he looks at others in the room, he will not see himself.
	b = Character.objects.filter(room=local_room_id)
	if this_character_name is not target_object_name:
		b = b.exclude(name=this_character_name)
	b = b.filter(name=target_object_name).values('desc')

	c = Equipment.objects.filter(rooms=local_room_id).filter(name=target_object_name).values('desc')
	
	d = Weapon.objects.filter(rooms=local_room_id).filter(name=target_object_name).values('desc')

	e = Armor.objects.filter(rooms=local_room_id).filter(name=target_object_name).values('desc')

	if len(a) > 0:
		if len(a) == 1:
			return a
		else:
			return "There are a number of things with that name in this room."
	elif len(b) > 0:
		if len(b) == 1:
			return b
		else:
			return "There are a number of things with that name in this room."
	elif len(c) > 0:
		if len(c) == 1:
			return c
		else:
			return "There are a number of things with that name in this room."
	elif len(d) > 0:
		if len(d) == 1:
			return d
		else:
			return "There are a number of things with that name in this room."
	elif len(e) > 0:
		if len(e) == 1:
			return e
		else:
			return "There are a number of things with that name in this room."
	else:
		return "Unable to see what you are looking for"

print observe("Vulukyr", "Vulukyr")

# data = serializers.serialize('json',objectQuerySet, fields=('name', 'desc'))

