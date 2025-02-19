# from umd_api.planet_terp import Search

# search = Search()

# search.search("Raluca")

from umd_api.general import Bus

bus = Bus()

routes = bus.get_specific_stops(["elk"])

print(routes)