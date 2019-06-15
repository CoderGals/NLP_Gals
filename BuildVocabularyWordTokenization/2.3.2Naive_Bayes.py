from nlpia.data.loaders import get_data

moview = get_data('hutto_movies')

print(moview.head().round(2))

