from modules.conway import Universe


def print_universe(u):
    h, w = u.dim
    for i in range(h):
        print(u.space[i])

if __name__ == "__main__":
    u = Universe((10, 10))
    u.random_reset(50)
    print_universe(u)
    while input() != 'q':
        u.next_generation()
        print_universe(u)

