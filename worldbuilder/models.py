from django.db import models
from django.contrib.auth.models import User


class CommonInfo(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

    class Meta:
        abstract = True
        ordering = ['name']

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    def name_count(self, keyword):
        return self.filter(name__icontains=keyword).count()


class Area(CommonInfo):
    author = models.ForeignKey(User, related_name='created_by')
    edited_by = models.ForeignKey(User, related_name='edited_by')
    starting_level = models.IntegerField(default=0)
    end_level = models.IntegerField(default=0)
    geography = models.TextField(default="blank")
    history = models.TextField(default="blank")
    arcana = models.TextField(default="blank")
    local = models.TextField(default="blank")


class Room(CommonInfo):
    TERRAIN_TYPE = (
        ('P', 'Plains'),
        ('M', 'Mountain'),
        ('F', 'Forest'),
        ('S', 'Swamp'),
        ('B', 'Island'),
        ('X', 'Civilisation'),
        ('D', 'Dungeon'),
        ('C', 'Cave'),
        ('T', 'Desert'),
        ('G', 'Graveyard'),
        ('H', 'Hills'),
        ('A', 'Aquatic'),
    )
    area = models.ForeignKey('Area')
    terrain = models.CharField(max_length=1, choices=TERRAIN_TYPE)

    class Meta:
        ordering = ['area']


class Mob(CommonInfo):
    veteran = models.BooleanField("Veteran of many battles.", default=False)
    # Admittedly bad db design, but good for the model
    sheet = models.TextField()
    rooms = models.ManyToManyField(Room)
    # drops = models.ManyToMany(null=True,blank=True)


class Character(CommonInfo):
    ALIGNMENT = (
        ('CE', 'Chaotic Evil'),
        ('NE', 'Neutral Evil'),
        ('LE', 'Lawful Evil'),
        ('CN', 'Chaotic Neutral'),
        ('TN', 'True Neutral'),
        ('LN', 'Lawful Neutral'),
        ('CG', 'Chaotic Good'),
        ('NG', 'Neutral Good'),
        ('LG', 'Lawful Good'),
    )
    user = models.OneToOneField(User)
    ipAddress = models.IPAddressField()
    role = models.TextField(default="")
    rooms = models.ManyToManyField(Room)
    title = models.CharField(max_length=200)
    alignment = models.CharField(max_length=2, choices=ALIGNMENT)
    maxHealth = models.IntegerField()
    currentHealth = models.IntegerField()  # Not sure if this is a good idea
    ac = models.IntegerField()
    fort = models.IntegerField()
    ref = models.IntegerField()
    will = models.IntegerField()
    spot = models.IntegerField()
    listen = models.IntegerField()
    newOrNot = models.BooleanField(
        "Are you new to D&D or roleplaying in general?")


class ItemInfo(CommonInfo):  # Saves alot of coding work
    STONE = 1
    BRONZE = 2
    IRON = 3
    CLASSICAL = 4
    DARK = 5
    EMEDIEVAL = 6
    LMEDIEVAL = 7
    CHIVALRIC = 8
    RENAISSANCE = 9

    CULTURE_LEVEL = (
        (STONE, 'Stone Age'),
        (BRONZE, 'Bronze Age'),
        (IRON, 'Iron Age'),
        (CLASSICAL, 'Classical'),
        (DARK, 'Dark Age'),
        (EMEDIEVAL, 'Early Medieval'),
        (LMEDIEVAL, 'Medieval'),
        (CHIVALRIC, 'Chivalric'),
        (RENAISSANCE, 'Renaissance'),
    )
    category = models.CharField(max_length=200)
    copper = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    culture = models.IntegerField(choices=CULTURE_LEVEL, default=1)
    rooms = models.ManyToManyField(Room)

    class Meta(CommonInfo.Meta):
        abstract = True


class Equipment(ItemInfo):
    mechanics = models.TextField()


class GearInfo(ItemInfo):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    HUGE = 4

    ORGANIC = 0
    STEEL = 1
    IRON = 2
    MITHRIL = 3
    BONE = 4
    GRANITE = 5
    ENERGY = 6
    ADAMANTINE = 7
    SILVER = 8
    WOOD = 9

    NOAURA = 0
    BLESSED = 1
    PROFANE = 2

    SIZE = (
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (HUGE, 'Huge'),
    )
    MATERIAL = (
        (ORGANIC, 'Organic'),
        (STEEL, 'Steel'),
        (IRON, 'Iron'),
        (MITHRIL, 'Mithril'),
        (BONE, 'Bone'),
        (GRANITE, 'Granite'),
        (ENERGY, 'Energy'),
        (ADAMANTINE, 'Adamantine'),
        (SILVER, 'Silver'),
        (WOOD, 'Wood')
    )
    ALIGNMENTAURA = (
        (NOAURA, 'No alignment Aura'),
        (BLESSED, 'Blessed'),
        (PROFANE, 'Profane'),
    )
    material = models.CharField(
        max_length=200,
        choices=MATERIAL,
        default=STEEL)
    size = models.IntegerField(max_length=1, choices=SIZE, default=MEDIUM)
    craftsmanship = models.CharField(
        max_length=200,
        default="Its craftsmanship is not of notable quality.")
    history = models.TextField(
        default="It has no meaningful history to speak of.")

    glowing = models.BooleanField(default=False)
    humming = models.BooleanField(default=False)
    powerful = models.BooleanField(default=False)
    limited = models.BooleanField(default=False)
    noremove = models.BooleanField(default=False)
    nodrop = models.BooleanField(default=False)
    magical = models.BooleanField(default=False)
    radiance = models.IntegerField(
        max_length=1,
        choices=ALIGNMENTAURA,
        default=0)
    goodallowed = models.BooleanField(default=True)
    neutralallowed = models.BooleanField(default=True)
    evilallowed = models.BooleanField(default=True)

    class Meta(CommonInfo.Meta):
        abstract = True


class Weapon(GearInfo):
    HANDEDNESS = (
        (1, 'One Handed'),
        (2, 'Two Handed'),
        (3, 'Light'),
    )
    # Chose not to use inheritence for glowing, humming, powerful
    damage = models.CharField(max_length=200, default="1d6")
    handedness = models.IntegerField(max_length=1, choices=HANDEDNESS)

    nodisarm = models.BooleanField(default=False)
    piercing = models.BooleanField(default=False)
    slashing = models.BooleanField(default=False)
    crushing = models.BooleanField(default=False)
    rotDeath = models.BooleanField(default=False)
    aggro = models.BooleanField(default=False)


class DefensiveInfo(GearInfo):
    NOTAPPLICABLE = 0
    MOVEACTION = 1
    FIVEROUNDS = 2
    ONEMINUTE = 3
    TWOMINUTES = 4
    ONEDFOURPLUSONEMINUTES = 5
    FOURMINUTES = 6
    IMPOSSIBLE = 7
    DON = (
        (NOTAPPLICABLE, 'Not Applicable'),
        (MOVEACTION, 'Move Action'),
        (FIVEROUNDS, '5 Rounds'),
        (ONEMINUTE, '1 Minute'),
        (TWOMINUTES, '2 Minutes'),
        (ONEDFOURPLUSONEMINUTES, '1d4+1 Minutes'),
        (FOURMINUTES, '4 Minutes'),
        (IMPOSSIBLE, 'Impossible'),
    )
    ac = models.PositiveIntegerField(max_length=2)
    acp = models.IntegerField("armor check penalty", max_length=2)
    # Problematic. Due to data model of armor and shield.
    mdb = models.IntegerField("Max Dex Bonus", max_length=1, default=0)
    scfc = models.IntegerField("spellcasting failure chance", max_length=2)
    don = models.IntegerField("Don without help", choices=DON)
    don_hastily = models.IntegerField("Don hastily without help", choices=DON)
    remove = models.IntegerField("Remove without help", choices=DON)
    don_with_help = models.IntegerField("Don with help", choices=DON)
    don_hastily_with_help = models.IntegerField(
        "Don hastily with help",
        choices=DON)
    remove_with_help = models.IntegerField("Remove with help", choices=DON)
    spikes = models.BooleanField(default=False)

    class Meta(CommonInfo.Meta):
        abstract = True


class Shield(DefensiveInfo):
    tower_shield = models.BooleanField(default=False)
    heraldry = models.TextField(default="It lacks heraldry.")


class Armor(DefensiveInfo):
    speed_reduction = models.BooleanField(default=False)


class House(models.Model):
    UNKNOWN = 0
    THE_DAWN_AGE = 1
    AGE_OF_HEROES = 2
    GOLDEN_AGE = 3
    DARK_AGE = 4

    ERA = (
        (UNKNOWN, 'Unknown'),
        (THE_DAWN_AGE, 'The Dawn Age'),
        (AGE_OF_HEROES, 'Age of Heroes'),
        (GOLDEN_AGE, 'Golden Age'),
        (DARK_AGE, 'Dark Age'),
    )
    name = models.CharField(max_length=200)
    legacy = models.TextField()
    coat_of_arms = models.CharField(max_length=200)
    seat = models.CharField(max_length=200)
    words = models.CharField(max_length=200)
    overlord = models.OneToOneField(
        'self',
        null=True,
        blank=True,
        related_name="overlord_set")
    cadet_branch = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name="cadet_branches_set")
    ancestral_weapon = models.OneToOneField(Weapon, null=True, blank=True)
    founded = models.IntegerField(
        max_length=1,
        choices=ERA,
        null=True,
        blank=True)


class Noble(CommonInfo):
    MALE = 1
    FEMALE = 2
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.IntegerField(max_length=1, choices=GENDER)
    house = models.ForeignKey(House)
    lord = models.BooleanField(default=False)
    founder = models.BooleanField(default=False)
    mother = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name="mother_of_set")
    father = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name="father_of_set")
