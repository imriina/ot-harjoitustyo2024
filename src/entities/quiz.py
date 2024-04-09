import uuid

class Quiz:
    """Luokka, joka kuvaa yksittäistä tehtävää

    Attributes:
        content: Merkkijonoarvo, joka kuvaa tehtävän sisältöä.
        done: Boolean-arvo, joka kuvastaa, onko tehtävä jo tehty.
        user: User-olio, joka kuvaa tehtävän omistajaa.
        todo_id: Merkkijonoarvo, joku kuvaa tehtävän id:tä.
    """

    def __init__(self, content, done=False, user=None, todo_id=None):

        self.content = content
        self.done = done
        self.user = user
        self.id = todo_id or str(uuid.uuid4())