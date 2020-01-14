"""Enums representing Garmin Connect data types."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import enum
import logging

import Fit.field_enums as fe


logger = logging.getLogger(__file__)


class Event(enum.Enum):
    """Garmin Connect event types enum."""

    race            = 1
    recreation      = 2
    special_event   = 3
    training        = 4
    transportation  = 5
    touring         = 6
    geocaching      = 7
    fitness         = 8
    uncategorized   = 9

    @classmethod
    def from_json(cls, json_data):
        """Create a Event enum instance from Garmin Connect JSON data."""
        json_event = json_data['eventType']
        try:
            return cls(json_event['typeId'])
        except ValueError:
            logger.error("Unknown event type: %r", json_event)
            raise


class Sport(enum.Enum):
    """Garmin Connect sport types enum."""

    running                                 = 1
    cycling                                 = 2
    hiking                                  = 3
    other                                   = 4
    mountain_biking                         = 5
    trail_running                           = 6
    street_running                          = 7
    track_running                           = 8
    walking                                 = 9
    road_biking                             = 10
    indoor_cardio                           = 11
    strength_training                       = 13
    casual_walking                          = 15
    speed_walking                           = 16
    top_level                               = 17
    treadmill_running                       = 18
    cyclocross                              = 19
    downhill_biking                         = 20
    track_cycling                           = 21
    recumbent_cycling                       = 22
    indoor_cycling                          = 25
    swimming                                = 26
    lap_swimming                            = 27
    open_water_swimming                     = 28
    fitness_equipment                       = 29
    elliptical                              = 30
    stair_climbing                          = 31
    indoor_rowing                           = 32
    snow_shoe                               = 36
    mountaineering                          = 37
    rowing                                  = 39
    wind_kite_surfing                       = 41
    horseback_riding                        = 44
    driving_general                         = 49
    flying                                  = 52
    paddling                                = 57
    whitewater_rafting_kayaking             = 60
    skating                                 = 62
    inline_skating                          = 63
    resort_skiing_snowboarding              = 67
    backcountry_skiing_snowboarding         = 68
    boating                                 = 75
    sailing                                 = 77
    cross_country_skiing                    = 81
    stand_up_paddleboarding                 = 87
    golf                                    = 88
    bmx                                     = 131
    hunting_fishing                         = 133
    surfing                                 = 137
    wakeboarding                            = 138
    rock_climbing                           = 139
    hang_gliding                            = 140
    tennis                                  = 142
    gravel_cycling                          = 143
    diving                                  = 144
    yoga                                    = 149
    floor_climbing                          = 150
    virtual_ride                            = 152
    virtual_run                             = 153
    obstacle_run                            = 154
    indoor_running                          = 156
    safety                                  = 157
    assistance                              = 158
    incident_detected                       = 159
    ccr_diving                              = 161
    auto_racing                             = 162
    yoga_gym                                = 163
    breathwork                              = 164
    winter_sports                           = 165
    snow_shoe_ws                            = 167
    skating_ws                              = 168
    backcountry_skiing_snowboarding_ws      = 169
    skate_skiing_ws                         = 170
    cross_country_skiing_ws                 = 171
    resort_skiing_snowboarding_ws           = 172

    @classmethod
    def __activity_from_json(cls, json_data):
        return json_data['activityType']

    @classmethod
    def __activity_from_details_json(cls, json_data):
        return json_data['activityTypeDTO']

    @classmethod
    def __sport_from_json(cls, json_activity):
        return json_activity['parentTypeId']

    @classmethod
    def __subsport_from_json(cls, json_activity):
        return json_activity['typeId']

    @classmethod
    def from_json(cls, json_data):
        """Create a Sport enum instance from Garmin Connect JSON data."""
        json_activity = cls.__activity_from_json(json_data)
        try:
            return Sport(cls.__sport_from_json(json_activity))
        except ValueError:
            logger.error("Unknown sport type: %r", json_activity)

    @classmethod
    def from_details_json(cls, json_data):
        """Create a Sport enum instance from Garmin Connect JSON details data."""
        json_activity = cls.__activity_from_details_json(json_data)
        try:
            return Sport(cls.__sport_from_json(json_activity))
        except ValueError:
            logger.error("Unknown sport type: %r", json_activity)

    @classmethod
    def subsport_from_json(cls, json_data):
        """Create a Sport enum instance from Garmin Connect subsport JSON data."""
        json_activity = cls.__activity_from_json(json_data)
        try:
            return Sport(cls.__subsport_from_json(json_activity))
        except ValueError:
            logger.error("Unknown subsport type: %r", json_activity)

    @classmethod
    def subsport_from_details_json(cls, json_data):
        """Create a Sport enum instance from Garmin Connect subsport JSON details data."""
        json_activity = cls.__activity_from_details_json(json_data)
        try:
            return Sport(cls.__subsport_from_json(json_activity))
        except ValueError:
            logger.error("Unknown subsport type: %r", json_activity)


def convert_gc_sport_to_fit(gc_sport, gc_sub_sport):
    """Convert sport and subsport values from Garmin Connect to Fit values."""
    remap_gc_sub_sport_to_fit = {
        Sport.mountain_biking                         : fe.SubSport.mountain,
        Sport.trail_running                           : fe.SubSport.trail,
        Sport.street_running                          : fe.SubSport.street,
        Sport.track_running                           : fe.SubSport.track,
        Sport.road_biking                             : fe.SubSport.road,
        Sport.casual_walking                          : fe.SubSport.casual_walking,
        Sport.speed_walking                           : fe.SubSport.speed_walking,
        Sport.treadmill_running                       : fe.SubSport.treadmill,
        Sport.downhill_biking                         : fe.SubSport.downhill,
        Sport.track_cycling                           : fe.SubSport.track_cycling,
        Sport.recumbent_cycling                       : fe.SubSport.recumbent,
        Sport.indoor_cycling                          : fe.SubSport.indoor_cycling,
        Sport.strength_training                       : fe.SubSport.strength_training,
        Sport.cyclocross                              : fe.SubSport.cyclocross,
        Sport.lap_swimming                            : fe.SubSport.lap_swimming,
        Sport.open_water_swimming                     : fe.SubSport.open_water,
        Sport.elliptical                              : fe.SubSport.elliptical,
        Sport.stair_climbing                          : fe.SubSport.stair_climbing,
        Sport.indoor_rowing                           : fe.SubSport.indoor_rowing,
        Sport.bmx                                     : fe.SubSport.bmx,
        Sport.gravel_cycling                          : fe.SubSport.gravel_cycling,
        Sport.yoga                                    : fe.SubSport.yoga,
        Sport.obstacle_run                            : fe.SubSport.obstacle,
        Sport.indoor_running                          : fe.SubSport.indoor_running,
        Sport.yoga_gym                                : Sport.yoga_gym
    }
    remap_winter_sports = {
        Sport.snow_shoe_ws                            : fe.Sport.snowshoeing,
        Sport.skating_ws                              : fe.Sport.ice_skating,
        Sport.backcountry_skiing_snowboarding_ws      : Sport.backcountry_skiing_snowboarding,
        Sport.skate_skiing_ws                         : Sport.skate_skiing_ws,
        Sport.cross_country_skiing_ws                 : fe.Sport.cross_country_skiing,
        Sport.resort_skiing_snowboarding_ws           : Sport.resort_skiing_snowboarding
    }
    remap_gc_sport_to_fit = {
        Sport.running                                 : fe.Sport.running,
        Sport.cycling                                 : fe.Sport.cycling,
        Sport.hiking                                  : fe.Sport.hiking,
        Sport.walking                                 : fe.Sport.walking,
        Sport.indoor_cardio                           : Sport.indoor_cardio,
        Sport.swimming                                : fe.Sport.swimming,
        Sport.fitness_equipment                       : fe.Sport.fitness_equipment,
        Sport.snow_shoe                               : fe.Sport.snowshoeing,
        Sport.mountaineering                          : fe.Sport.mountaineering,
        Sport.rowing                                  : fe.Sport.rowing,
        Sport.wind_kite_surfing                       : fe.Sport.kitesurfing,
        Sport.horseback_riding                        : fe.Sport.horseback_riding,
        Sport.driving_general                         : fe.Sport.driving,
        Sport.flying                                  : fe.Sport.flying,
        Sport.paddling                                : fe.Sport.paddling,
        Sport.whitewater_rafting_kayaking             : Sport.whitewater_rafting_kayaking,
        Sport.skating                                 : fe.Sport.ice_skating,
        Sport.inline_skating                          : fe.Sport.inline_skating,
        Sport.resort_skiing_snowboarding              : Sport.resort_skiing_snowboarding,
        Sport.backcountry_skiing_snowboarding         : Sport.backcountry_skiing_snowboarding,
        Sport.boating                                 : fe.Sport.boating,
        Sport.sailing                                 : fe.Sport.sailing,
        Sport.cross_country_skiing                    : fe.Sport.cross_country_skiing,
        Sport.stand_up_paddleboarding                 : fe.Sport.stand_up_paddleboarding,
        Sport.golf                                    : fe.Sport.golf,
        Sport.hunting_fishing                         : Sport.hunting_fishing,
        Sport.surfing                                 : fe.Sport.surfing,
        Sport.wakeboarding                            : fe.Sport.wakeboarding,
        Sport.rock_climbing                           : fe.Sport.rock_climbing,
        Sport.hang_gliding                            : fe.Sport.hang_gliding,
        Sport.tennis                                  : fe.Sport.tennis,
        Sport.diving                                  : Sport.diving,
        Sport.floor_climbing                          : fe.Sport.floor_climbing,
        Sport.virtual_ride                            : Sport.virtual_ride,
        Sport.virtual_run                             : Sport.virtual_run,
        Sport.safety                                  : Sport.safety,
        Sport.assistance                              : Sport.assistance,
        Sport.incident_detected                       : Sport.incident_detected,
        Sport.ccr_diving                              : Sport.ccr_diving,
        Sport.auto_racing                             : Sport.auto_racing,
        Sport.breathwork                              : Sport.breathwork,
    }
    special_remaps = {
        Sport.other                                   : remap_gc_sport_to_fit.get(gc_sub_sport),
        Sport.top_level                               : remap_gc_sport_to_fit.get(gc_sub_sport),
        Sport.winter_sports                           : remap_winter_sports.get(gc_sub_sport),
    }
    if gc_sport in special_remaps.keys():
        return (special_remaps[gc_sport], fe.Sport.generic)
    return (remap_gc_sport_to_fit.get(gc_sport), remap_gc_sub_sport_to_fit.get(gc_sub_sport))


def get_details_sport(json_data):
    """Get the sport and sub-sport and convert to Fit values if possible."""
    sport = Sport.from_details_json(json_data)
    sub_sport = Sport.subsport_from_details_json(json_data)
    return convert_gc_sport_to_fit(sport, sub_sport)


def get_summary_sport(json_data):
    """Get the sport and sub-sport and convert to Fit values if possible."""
    sport = Sport.from_json(json_data)
    sub_sport = Sport.subsport_from_json(json_data)
    return convert_gc_sport_to_fit(sport, sub_sport)
