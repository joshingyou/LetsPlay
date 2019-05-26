import uuid
from django.db import models


# Create your models here.
class PlayerInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = " ".join([last_name, first_name])
    birth_year = models.PositiveSmallIntegerField()
    joined_date = models.DateField(auto_now_add=True)
    start_rating = models.DecimalField(max_digits=2, decimal_places=1)
    dynamic_current_rating = start_rating

    def __str__(self):
        return self.full_name


class GenericMatchesHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    match_date = models.DateField()
    is_finished = models.BooleanField(default=False)

    set_1_is_tiebreak = models.BooleanField(default=False)
    side_1_set_1_score = models.PositiveSmallIntegerField(default=0)
    side_1_set_1_tiebreak = models.PositiveSmallIntegerField(default=0)
    side_2_set_1_score = models.PositiveSmallIntegerField(default=0)
    side_2_set_1_tiebreak = models.PositiveSmallIntegerField(default=0)

    set_2_is_tiebreak = models.BooleanField(default=False)
    side_1_set_2_score = models.PositiveSmallIntegerField(default=0)
    side_1_set_2_tiebreak = models.PositiveSmallIntegerField(default=0)
    side_2_set_2_score = models.PositiveSmallIntegerField(default=0)
    side_2_set_2_tiebreak = models.PositiveSmallIntegerField(default=0)

    set_3_is_tiebreak = models.BooleanField(default=False)
    side_1_set_3_score = models.PositiveSmallIntegerField(default=0)
    side_1_set_3_tiebreak = models.PositiveSmallIntegerField(default=0)
    side_2_set_3_score = models.PositiveSmallIntegerField(default=0)
    side_2_set_3_tiebreak = models.PositiveSmallIntegerField(default=0)


class SinglesMatchesHistory(GenericMatchesHistory):
    player_1_id = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)  # side 1
    player_2_id = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)  # side 2

    match_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.match_id


class DoublesMatchesHistory(GenericMatchesHistory):
    player_1_id = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)  # side 1
    player_2_id = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)  # side 1
    player_3_id = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)  # side 2
    player_4_id = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)  # side 2

    match_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.match_id
