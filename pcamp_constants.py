from module_constants import *

# Cost to build a camp
pcamp_build_cost = 100

# Max allowed distance to nearest center
pcamp_max_center_distance = 10

# Chance for a lord to escape from camp (default for party - 50)
pcamp_lord_escape_chance = 40

# Number of additional troops per commander leadership level and charisma
pcamp_commander_leadership_size_bonus = 5
pcamp_commander_charisma_size_bonus = 1

# Number of prisoner slots per commander skill and num troops to gain 1 slot
pcamp_commander_prisoner_skill_bonus = 5
pcamp_troop_count_prisoner_divisor = 5

# Internal constants

pcamp_chests_begin = "trp_player_camp_chest_1"
pcamp_chests_end = "trp_player_camp_chest_end"

slot_pcamp_camp_commander = slot_town_elder
slot_pcamp_camp_chest = slot_town_merchant
slot_pcamp_camp_initialized = slot_center_player_relation

slot_pcamp_chest_commander = slot_troop_guardian
slot_pcamp_chest_party = slot_troop_home
slot_pcamp_chest_center = slot_troop_cur_center
slot_pcamp_chest_items = slot_troop_renown
slot_pcamp_chest_value = slot_troop_wealth
