class CellSet:
    def __init__(self, cells):
        self.cells = cells

    def is_contiguous(self):
        self.accounted_cells = []
        self.verify(self.cells[0])
        return len(self.accounted_cells) == len(self.cells)

    def verify(self, cell):
        self.accounted_cells.append(cell)
        for neighbor in self.straight_neighbors(cell):
            if not neighbor in self.accounted_cells:
                self.verify(neighbor)

    def straight_neighbors(self, center_cell):
        neighbors = []
        points = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        center_cell_x = center_cell.x
        center_cell_y = center_cell.y
        for point in points:
            x = center_cell_x + point[0]
            y = center_cell_y + point[1]
            neighbor = self.cell_at(x, y)
            if neighbor is not None:
                neighbors.append(neighbor)
        return neighbors

    def cell_at(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell
