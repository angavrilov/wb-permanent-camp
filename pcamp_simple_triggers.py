from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *

from module_constants import *

from util_wrappers import *
from util_scripts import *

import sys

# Patches in second list are applied to first trigger that contains all operations from first list:

patches = [
	# Let lords escape from camps
	([
		(call_script, "script_randomly_make_prisoner_heroes_escape_from_party", ":center_no", ":chance"),
	 ],[
		[
			SD_OP_BLOCK_INSERT, "",
			D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_AFTER,
			0, 0,
			[
				(try_for_range, ":chest", pcamp_chests_begin, pcamp_chests_end),
					(troop_get_slot, ":party", ":chest", slot_pcamp_chest_party),
					(gt, ":party", 0),
					(party_is_active, ":party"),
					(call_script, "script_randomly_make_prisoner_heroes_escape_from_party", ":party", pcamp_lord_escape_chance),
				(try_end),
			]
		],
	 ]),
]

new_triggers = [
]

def apply_patches(orig_triggers, patches):
    for patch in patches:
        found = False
        for trigger in orig_triggers:
            matches = True
            for restriction in patch[0]:
                if restriction not in trigger[1]:
                    matches = False
                    break
            if matches:
                found = True
                tmp = [("", trigger[1])]
                process_script_directives(tmp, patch[1])
                #print_script(tmp, "")
                break
        if not found:
            print "Could not find simple trigger: ", patch[0]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "simple_triggers"

        #swy--append the rest of scripts at the end
        orig_triggers = var_set[var_name_1]

        try:
          apply_patches(orig_triggers, patches)

        except:
          import sys
          print "Injection failed:", sys.exc_info()[1]
          raise

        orig_triggers.extend(new_triggers)

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
