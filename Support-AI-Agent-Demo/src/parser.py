# Demo parser for sample tickets
import json

def load_tickets(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
