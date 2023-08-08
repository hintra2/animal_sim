
class Square():
    def __init__(self, id:int, value:int):
        self.id = 1 if id == 100 else 0
        self.value=value
    id:int
    """
    determines type of terrain on board
    0=grass
    1=water
    """
    value:int
    animals_in_square=None

    def get_id(self) -> int:
        return self.id

    def get_value(self) -> int:
        return self.value

    def get_animals(self):
        if self.animals_in_square:
            return self.animals_in_square
        return None

    def add_animal_to_square(self, new_animal) -> bool:
        if not self.animals_in_square:
            self.animals_in_square=new_animal
            return True
        else:
            return False

    def update_id(self, value):
        self.id = value

    def remove_animal_from_square(self, animal):
        if animal == self.animals_in_square:
            self.animals_in_square=None
