# TODO: Have a think of how to approach this to enable entrance rando without too much effort


# this is a very primitive region system just so I can start working on logic
# it's not usable yet since I had to stop working on it half way through
region_locations = {
  "0 Cubes": {
    golden_cubes: 0,
    cube_bits: 8,
    anti_cubes: 2,
    heart_cubes: 0,
    keys: 2,
    owls: 0
  },
  "1 Cube": {
    golden_cubes: 0,
    cube_bits: 8,
    anti_cubes: 0,
    heart_cubes: 0,
    keys: 0,
    owls: 0
  },
}:

def create_region(world: "APSkeletonWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    # When we create the region we go through all the locations we made and check if they are in that region
    # If they are and are valid, we attach it to the region
    for (key, data) in location_table.items():
        if data.region == name:
            if not is_valid_location(world, key):
                continue
            location = APSkeletonLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    
    world.multiworld.regions.append(reg)
    return reg
