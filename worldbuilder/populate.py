from worldbuilder.models import Area, Mob, Room, Equipment, Weapon


# This script has been made so that I can populate a database with sample data after flushing it.
# This allows me to modify the database structure while in development
# without worrying too much about dataloss.
a = Area(
    name="Roggeg",
    desc="A border town famous for its honey.",
    author="Bertrand",
    geograph="The region surrounding Roggeg is primarily forests. Travelling on foot is not only inefficient but highly dangerous. The roads are few in number, and poorly kept - many are ancient. Thus this region is perfect for adventuring in the wilderness.",
    history="Being a border town, it is close to the border of Ablon as well as Nosquam. The former is a trading ally of Nes, and the later is an enemy. ",
    arcana="You know nothing about the topic off hand. But you know where to look. There is a known witch who advises the Jarl Stin Gernerson. There is a gnome who is doing an architectural project. You heard in myth that gnomes have such backgrounds. ",
    local="Local (legends, personalities, inhabitants, laws, customs, traditions, humanoids).",
    starting_level=1,
    end_level=10)
a.save()
b = Mob(
    name="Roggeg Guard",
    desc="He looks tipsy.",
    sheet="Human Warrior 1 S 13 D 12 C 11 I 10 W 9 X 8")
b.save()
c = Room(
    name="Market Square",
    desc="Filled with merchants of all kinds. You hear bees.",
    area=a,
    terrain="X",
    mobs=b)
c.save()

e = Equipment(
    name="Torch",
    desc="A wooden stave with one end wrapped in linen which has been soaked in a fatty animal oil.",
    copper=1,
    weight=1,
    culture=1,
    category="Light",
    mechanics="A torch burns for 1 hour, clearly illuminating a 20-foot radius and providing shadowy illumination out to a 40-foot radius. If a torch is used in combat, treat it as a one-handed improvised weapon that deals bludgeoning damage equal to that of a gauntlet of its size, plus 1 point of fire damage.")
e.save()
f = Area(
    name="Nosquam",
    desc="Its not getting to the Land of the Dead thats the problem. Its getting back.",
    author="Bertrand")
f.save()

g = Weapon(
    name="Mermaid Whip",
    desc="An organic whip made from kelp and other materials of the ocean.",
    culture=1,
    category="whip",
    copper=0,
    weight=1,
    damage="1d4",
    handedness=3,
    size=2,
    craftsmanship="Mermaid",
    history="Very little is known about the Mermaid Whip.",
    material=9)

h = Room(name="Orbicular Granite Cove",
         desc="Orbicular Granite is... everywhere.",
         area=a,
         terrain='B',
         mobs=b)
i = Weapon(
    name="Blackbeard's Blade",
    desc="A wide-bladed broken machete with three ridges down the side. It can take control of ships.",
    culture=1,
    category="Sword",
    copper=0,
    weight=1,
    damage="1d10",
    handedness=1,
    size=2,
    craftsmanship="Undead",
    history="Very little is known about Blackbeard's Blade.",
    material=9)
