
from polls.models import Poll, Choice
g = Poll(question="Which is your favourite Culture Level?")
g.save()
Choice(poll=g, choice_text="Stone Age (10000-5000 B.C.)").save()
Choice(poll=g, choice_text="Bronze Age (5000-2500 B.C.)").save()
Choice(poll=g, choice_text="Iron Age (2500-1 B.C.)").save()
Choice(poll=g, choice_text="Classical (1-500 A.D.)").save()
Choice(poll=g, choice_text="Dark Age (500-800)").save()
Choice(poll=g, choice_text="Early Medieval (800-1200 A.D.)").save()
Choice(poll=g, choice_text="Medieval (1200-1400 A.D.)").save()
Choice(poll=g, choice_text="Chivalric (1400-1550 A.D.)").save()
Choice(poll=g, choice_text="Renaissance (1550-1700 A.D.)").save()