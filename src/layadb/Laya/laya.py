import laya

from laya import decide

from ..Schema.CriteriaMap import intent_map
from ..Schema.Enums import Intent

def get_intent_from_string(string: str) -> Intent:
    stripped_string = string.strip()
    agent = laya.Agent("convaiinnovations/laya", device=None)

    questions = {
        "intent": {
            "type": "choice",
            "instructions": "What is the intent of this statement?",
            "criteria": intent_map
        }
    }

    result = decide(agent, stripped_string, questions=questions)
    choice = result.get("intent", {}).get("choice")

    return choice and Intent[choice] or Intent.Other
