import requests
from bs4 import BeautifulSoup


def print_secret_message(doc_url):
    message_grid = build_message_grid(doc_url)
    for row in message_grid:
        print(''.join(row))

def build_message_grid(doc_url):
    response = requests.get(doc_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    input_rows = table.find_all('tr')

    input_data = []
    max_x, max_y = 0, 0

    for row in input_rows[1:]:
        cells = row.find_all('td')

        x_cord = int(cells[0].get_text(strip=True))
        char = cells[1].get_text(strip=True)
        y_cord = int(cells[2].get_text(strip=True))

        input_data.append((x_cord, y_cord, char))
        max_x = max(max_x, x_cord)
        max_y = max(max_y, y_cord)

    message_grid = []
    for _ in range(max_y + 1): 
        base_row = [' '] * (max_x + 1)
        message_grid.append(base_row)

    for x, y, char in input_data:
        message_grid[max_y - y][x] = char

    return message_grid

print_secret_message("")
