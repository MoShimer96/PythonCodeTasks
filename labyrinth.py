from collections import deque

def count(r):
    #Helpointa on kuvitella, että tää kaksiulotteisena listana(?).
    n = len(r)
    m = len(r[0])

    # Etsitään ruudut A ja B, jotta voidaan vertailla näitä tuloksia matkan varrella saataviin tuloksiin
    start, end = None, None
    for i in range(n):
        for j in range(m):
            if r[i][j] == 'A':
                start = (i, j)
            elif r[i][j] == 'B':
                end = (i, j)
    
    if not start or not end:
        return -1  # A tai B puuttuu labyrintista

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps  # Saavutettiin B, palautetaan reitin pituus

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < m and r[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), steps + 1)) #Jono merkkien käsittelyä varten.
                visited.add((new_x, new_y))

    return -1  # Ei reittiä A:sta B:hen 

if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r))  # 7
