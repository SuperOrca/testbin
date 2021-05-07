from rstr import xeger

from . import db


def createPaste(text: str) -> str:
    table = db.pull('pastes')
    IDS = [paste['ID'] for paste in table]
    while True:
        ID = xeger(r'[A-Za-z0-9]{8}')
        if ID not in IDS:
            break
    db.append('pastes', {"ID": ID, "text": text})
    return ID


def getPaste(ID: str) -> str:
    for paste in db.pull('pastes'):
        if paste['ID'] == ID:
            return paste['text']
    return 'null'
