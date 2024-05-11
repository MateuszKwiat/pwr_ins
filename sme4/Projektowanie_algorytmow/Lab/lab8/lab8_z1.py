import numpy as np
import ast

def generate_robot():
    return (
        *np.random.choice(('AGV', 'AFV', 'ASV', 'AUV'), 1),
        round(np.random.uniform(0, 10_000), 2),
        np.random.randint(0, 101),
        np.random.randint(0, 2)
    )


def generate_robots_list(N):
    return [generate_robot() for _ in range(N)]


def write_read_robots(operation='r', robots_list=None):
    if operation == 'r':
        with open('robots.txt') as f:
            return ast.literal_eval(f.readline())
        
    elif operation == 'w':
        with open('robots.txt', 'w') as f:
            f.write(str(robots_list))


ls = generate_robots_list(20)

for i in ls:
    print(i)

print()
write_read_robots(operation='w', robots_list=ls)
ls1 = write_read_robots()

for i in ls1:
    print(i)
