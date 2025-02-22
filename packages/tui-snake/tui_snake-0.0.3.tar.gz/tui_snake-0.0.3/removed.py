

# class GameState:
#     def __init__(self, width: int, height: int, snake_speed: float):
#         self.width = width
#         self.height = height
#         self.snake_speed = snake_speed
#         self.walls_set = self.generate_walls_set()
#         self.all_coords_set = self.generate_all_coords()
#         self.snake_body: list[Coord2D] = [
#             Coord2D(self.width // 2, self.height // 2),
#             Coord2D(self.width // 2 - 1, self.height // 2),
#             Coord2D(self.width // 2 - 2, self.height // 2),
#         ]
#         self.snake_head = SnakeHead(
#             last_rotation=SnakeHeadRotation.RIGHT,
#             current_rotation=SnakeHeadRotation.RIGHT,
#             coords=Coord2D(self.width // 2, self.width // 2)
#         )
#         self.game_board = self.generate_game_board()
#         self.points: int = 0
#
#         # Init game
#         self.turn_cells_into_walls()
#         self.turn_cell_into_food()
#
#     def generate_game_board(self) -> list[list[BoardObject]]:
#         return [
#             [BoardObjectType.NULL for _ in range(self.width)]
#             for _ in range(self.height)
#         ]
#
#     def generate_all_coords(self) -> set[Coord2D]:
#         return {
#             Coord2D(x, y) for x, y in
#             product(range(self.width), range(self.height))
#         }
#
#     def generate_walls_set(self) -> set[Coord2D]:
#         cords = set()
#         cords |= {
#             Coord2D(x, y)
#             for x, y in product(range(self.width), range(1))
#         }
#         cords |= {
#             Coord2D(x, y) for x, y in
#             product(range(self.width), range(self.height - 1, self.height))
#         }
#         cords |= {
#             Coord2D(x, y) for x, y in
#             product(range(1), range(1, self.height - 1))
#         }
#         cords |= {
#             Coord2D(x, y) for x, y in
#             product(range(self.width - 1, self.width), range(1, self.height - 1))
#         }
#         return cords
#
#     def generate_new_food_coords(self) -> Coord2D:
#         self.all_coords_set -= self.walls_set
#         self.all_coords_set -= set(self.snake_body)
#         return choice(tuple(self.all_coords_set))
#
#     def turn_cells_into_walls(self) -> None:
#         for cord in self.walls_set:
#             self.game_board[cord.y][cord.x] = self.game_board[cord.y][cord.x].WALL
#
#     def turn_cell_into_food(self) -> None:
#         self.all_coords_set -= self.walls_set
#         self.all_coords_set -= set(self.snake_body)
#         cell: Coord2D = choice(tuple(self.all_coords_set))
#         self.game_board[cell.y][cell.x] = BoardObjectType.FOOD
