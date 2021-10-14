import datetime
from typing import Any, Optional


class Client:
    def __init__(self):
        self.presenter: Optional[Presenter] = None
        self.dj: Optional[MusicDJ] = None

    def hire_presenter(self, presenter):
        presenter.sign_contract(self)
        self.presenter = presenter
        print('Hiring presenter')

    def hire_dj(self, dj):
        dj.sign_contract(self)
        self.dj = dj
        print('Hiring DJ')

    def book_restaurant(self, restaurant):
        restaurant.sign_contract(self)
        date = datetime.datetime.today()
        restaurant.book_date(self, date)
        print(f'Book restaurant on {date.strftime("%d %B %Y")}')

    def choose_songs(self, songs: list[str]):
        self.dj.discuss_music(songs, self)


class Presenter:
    def __init__(self):
        self.contracts: list[Client] = []
        self.songs: list[str] = []

    def sign_contract(self, client):
        self.contracts.append(client)

    def fetch_processed_songs(self, dj, client):
        self.songs = dj.fetch_actual_songs(client)
        print(self.songs)
        print('Presenter gets songs from DJ')


class MusicDJ:
    def __init__(self):
        self.contracts: list[Client] = []
        self.white_lists_songs: list[dict[str, Any]] = []
        self.equipment: list[dict[str, Any]] = []

    def sign_contract(self, client):
        self.contracts.append(client)

    def fetch_actual_songs(self, client):
        for song_list in self.white_lists_songs:
            if song_list['client'] == client:
                return song_list['songs']

    def discuss_music(self, songs: list[str], client):
        capitalize_songs = []
        for song in songs:
            capitalize_songs.append(song.capitalize())
        self.white_lists_songs.append({'client': client, 'songs': capitalize_songs})

    def add_equipment(self, restaurant, equipment):
        self.equipment.append({'restaurant': restaurant, 'equipment': equipment})


class Restaurant:
    def __init__(self, equipment):
        self.contracts: list[Client] = []
        self.receipts: list[dict[str, Any]] = []
        self.equipment: list[str] = equipment

    def sign_contract(self, client):
        self.contracts.append(client)

    def book_date(self, client, date: datetime):
        self.receipts.append({'client': client, 'date': date})

    def provide_dj_with_equipment(self, dj):
        dj.add_equipment(self, self.equipment)
        equipment_to_str = ', '.join(self.equipment) if len(self.equipment) else self.equipment[0]
        print(f'Provide dj with equipment: {equipment_to_str}')


if __name__ == '__main__':
    client = Client()
    presenter = Presenter()
    dj = MusicDJ()
    restaurant = Restaurant(['lighting equipment'])

    client.hire_presenter(presenter)
    client.hire_dj(dj)
    client.book_restaurant(restaurant)

    client.choose_songs(['thriller', 'shape of my heart'])
    presenter.fetch_processed_songs(dj, client)
    restaurant.provide_dj_with_equipment(dj)
