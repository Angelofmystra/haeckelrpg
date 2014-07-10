from django.db import models

PRIORITY_CHOICES = [(1, 'Critical'), (2, 'High'), (3, 'Medium'), (4, 'Low')]


class Todo(models.Model):
    ART = 1
    FEATUREREQ = 2
    BUG = 3
    MISC = 4
    WORLDBUILDING = 5

    TODOTYPE = (
        (ART, 'Art'),
        (FEATUREREQ, 'Feature Request'),
        (BUG, 'Bug'),
        (MISC, 'Misc'),
        (WORLDBUILDING, 'World Building'),
    )
    todotype = models.IntegerField(choices=TODOTYPE, default=4)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=4)
    content = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User')

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s \t %s" % (self.todotype, self.content)
