"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    new_l = each_wagons_id[2], missing_wagons[0], *missing_wagons[1:], *each_wagons_id[3:], *each_wagons_id[0:2]
    return list(new_l)


def add_missing_stops(*args, **kwargs):
    slownik = dict()
    slownik.update(*args)
    slownik.update({"stops": list(kwargs.values())})
    return slownik


def extend_route_information(route, more_route_information):
    slownik = dict()
    slownik.update(route)
    slownik.update(more_route_information)
    return slownik


def fix_wagon_depot(wagons_rows):
    nowa_macierz = [[wagons_rows[j][i] for j in range(len(wagons_rows))] for i in range(len(wagons_rows[0]))]
    return nowa_macierz

print(fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ]))

# [
# [(2, "red"), (5, "blue"), (3, "orange")],
# [(4, "red"), (9, "blue"), (7, "orange")],
# [(8, "red"), (13,"blue"), (11, "orange")]
# ]