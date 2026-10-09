from . import Enums

intent_map = {
    Enums.Intent.Remove.name: "removal, subtract, checking out, taking out",
    Enums.Intent.Add.name: "addition, putting back, adding",
    Enums.Intent.Multiple.name: "multiple intents",
    Enums.Intent.Other.name: "neither removing or adding a item, unknown"
}
