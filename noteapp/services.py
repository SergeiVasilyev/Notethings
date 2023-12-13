from noteapp.models import Note


def create_note(name=None, text=None, creator=None, category=None, folder=None):
    note = Note.create_note(name, text, creator, category, folder)
    return note