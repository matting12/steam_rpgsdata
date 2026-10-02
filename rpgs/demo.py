"""Hardcoded sample data, used when Steam can't be reached so the app (and its demo bugs) work offline."""


def _g(rank, app_id, title, price, discount="", free=False):
    return {
        "rank": rank,
        "steam_app_id": app_id,
        "title": title,
        "url": "https://store.steampowered.com/",
        "image": "",
        "discount": discount,
        "price": price,
        "is_free": free,
    }


DEMO_GAMES = [
    _g(1, 9000001, "Baldur's Gate 3", "$59.99"),
    _g(2, 9000002, "Elden Ring", "$59.99"),
    _g(3, 9000003, "Cyberpunk 2077", "$20.99", "-65%"),
    _g(4, 9000004, "The Witcher 3: Wild Hunt", "$7.99", "-80%"),
    _g(5, 9000005, "The Elder Scrolls V: Skyrim Special Edition", "$9.99", "-75%"),
    _g(6, 9000006, "Dragon's Dogma 2", "$49.99"),
    _g(7, 9000007, "Persona 3 Reload", "$39.99", "-33%"),
    _g(8, 9000008, "Starfield", "$44.99", "-25%"),
    _g(9, 9000009, "Path of Exile 2", "Free", free=True),
    _g(10, 9000010, "Divinity: Original Sin 2", "$22.49", "-50%"),
]
