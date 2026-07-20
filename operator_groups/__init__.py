from collections import OrderedDict

from .coral import get_coral_groups
from .dynamic import get_dynamic_groups
from .lets_fly import get_lets_fly_groups
from .paks import get_paks_groups
from .pegast_tez import get_pegast_tez_groups
from .russ_express import get_russ_express_groups
from .space_travel import get_space_travel_groups
from .sunmar import get_sunmar_groups


def get_operator_profiles():
    return OrderedDict({
        "1": ("Пегас/ТезТур", get_pegast_tez_groups),
        "2": ("Coral", get_coral_groups),
        "3": ("Sunmar", get_sunmar_groups),
        "21": ("Paks", get_paks_groups),
        "22": ("RussExpress", get_russ_express_groups),
        "45": ("SpaceTravel", get_space_travel_groups),
        "78": ("Динамика", get_dynamic_groups),
        "95": ("Lets Fly", get_lets_fly_groups),
    })


def resolve_operator_profile(choice: str):
    profiles = get_operator_profiles()
    choice_norm = (choice or "").strip().casefold()
    aliases = {
        "pegas": "1",
        "pegast": "1",
        "пегас": "1",
        "tez": "1",
        "teztour": "1",
        "тез": "1",
        "тезтур": "1",
        "dyn": "78",
        "dynamic": "78",
        "dynamics": "78",
        "динамика": "78",
        "coral": "2",
        "корал": "2",
        "sunmar": "3",
        "санмар": "3",
        "paks": "21",
        "пакс": "21",
        "russexpress": "22",
        "russ express": "22",
        "russ_express": "22",
        "руссэкспресс": "22",
        "русс экспресс": "22",
        "space": "45",
        "spacetravel": "45",
        "space travel": "45",
        "спейстревел": "45",
        "спейс тревел": "45",
        "letsfly": "95",
        "lets fly": "95",
        "let's fly": "95",
        "летс флай": "95",
    }
    profile_key = aliases.get(choice_norm, choice_norm)
    if profile_key not in profiles:
        return None, None
    return profiles[profile_key]
