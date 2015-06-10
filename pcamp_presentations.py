from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

from util_wrappers import *
from util_scripts import *

patches_budget = [
	# Include wages of camp troops in budget report; this is also what determines actual expenses
	[
		SD_OP_BLOCK_INSERT,
		str(ti_on_presentation_load),
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(assign, ":garrison_troop", 0), 0,

		[
			(party_get_template_id, ":party_template",":party_no"),
		]
	],
	[
		SD_OP_BLOCK_INSERT,
		str(ti_on_presentation_load),
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(this_or_next|eq, ":party_no", "p_main_party"), 0,

		[
			(this_or_next|eq, ":party_template", "pt_player_camp"),
		]
	],
	[
		SD_OP_BLOCK_INSERT,
		str(ti_on_presentation_load),
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(assign, ":garrison_troop", 0), 1,

		[
			(party_get_template_id, ":party_template",":party_no"),
		]
	],
	[
		SD_OP_BLOCK_INSERT,
		str(ti_on_presentation_load),
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(this_or_next|eq, ":party_no", "p_main_party"), 1,

		[
			(this_or_next|eq, ":party_template", "pt_player_camp"),
		]
	],
]

new_presentations = [
]


def apply_patches(orig_presentations, name, patches):
    find_r1 = list_find_first_match_i(orig_presentations, name)
    ops = PresentationWrapper(orig_presentations[find_r1]).GetTriggers()
    tmp = []
    i = 0
    while (i < len(ops)):
        tmp.append((str(ops[i][0]), ops[i][1]))
        i += 1
    process_script_directives(tmp, patches)

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "presentations"

        #swy--append the rest of scripts at the end
        orig_presentations = var_set[var_name_1]

        try:
          apply_patches(orig_presentations, "budget_report", patches_budget)

        except:
          import sys
          print "Injection failed:", sys.exc_info()[1]
          raise

        orig_presentations.extend(new_presentations)

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
