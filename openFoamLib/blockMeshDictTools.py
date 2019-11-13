class VertexList:
    """Collects the vertex list for a given blockMeshDict and writes it to a buffer.

    Progressively or parametrically add vertices to the vertex list and then return a buffer with the vertex information.
    This buffer may then be written to the desired dictionary.
    """

    # Vector component lists
    comp_x = []
    comp_y = []
    comp_z = []

    def addVertex(self, comp_0_, comp_1_, comp_2_):
        self.comp_x.append(comp_0_)
        self.comp_y.append(comp_1_)
        self.comp_z.append(comp_2_)

    def printVertexList(self):
        print(len(self.comp_x))
        for ii in range(0, len(self.comp_x)):
            print('(', self.comp_x[ii], ', ', self.comp_y[ii], ', ', self.comp_z[ii], ')')

    def getVertexList(self):
        vertex_buffer = []

        vertex_open = '\nvertices' + '\n(\n'
        vertex_close = '\n);\n\n'

        vertex_buffer.append(vertex_open)

        for ii in range(0, len(self.comp_x)):
            vertex_buffer.append('\t(' + str(self.comp_x[ii]) + ' ' + str(self.comp_y[ii]) + ' ' + str(self.comp_z[ii]) + ')\n')

        vertex_buffer.append(vertex_close)

        return (vertex_buffer)


class Block():
    """Collects information for a given blockMesh block and writes it to a buffer.

    Progressively or parametrically add blocks and then return a buffer with the block information.
    This buffer may then be written to the desired dictionary.
    """

    # Vertex IDs corresponding to those in the VertexList
    vertex_list = []
    block_type = 'hex'
    grading = 'simpleGrading'
    num_cells = []
    num_grading = []

    def __init__(self, vertex_list_, block_name_, num_cells_, num_grading_):
        self.block_id = -1
        self.vertex_list = vertex_list_
        self.block_name = block_name_
        self.num_cells = num_cells_

        self.num_grading = num_grading_

    def getBlock(self):
        block_buffer = []

        # Format the vertex list
        block_buffer.append('\n' + '\t' + self.block_type + ' (')
        for ii in range(0, len(self.vertex_list)):
            block_buffer.append(' ' + str(self.vertex_list[ii]))
        block_buffer.append(')')

        # Add block name, number of cells, and grading
        block_buffer.append('\n' + '\t' + self.block_name)
        block_buffer.append('\n' + '\t' + '(' + str(self.num_cells[0]) + ' ' + str(self.num_cells[1]) + ' ' + str(self.num_cells[2]) + ')')
        block_buffer.append('\n' + '\t' + self.grading + ' (' + str(self.num_grading[0]) + ' ' + str(self.num_grading[1]) + ' ' + str(self.num_grading[2]) + ')')
        block_buffer.append('\n')

        return (block_buffer)

class Edge():
    vertex_list = []
    interp_point = []
    edge_type = 'arc'

    def __init__(self, vertex_list_, interp_point_):
        self.vertex_list = vertex_list_
        self.interp_point = interp_point_

    def getEdge(self):
        edge_buffer = []

        edge_buffer.append('\n' + '\t' + self.edge_type)

        # Start and end vertices for the arc
        for ii in range(0, len(self.vertex_list)):
            edge_buffer.append(' ' + str(self.vertex_list[ii]))
        edge_buffer.append(' (')

        # Coordinates of interpolation point
        edge_buffer.append(' ' + str(self.interp_point[0]) + ' ' + str(self.interp_point[1]) + ' ' + str(self.interp_point[2]))
        edge_buffer.append(')')

        return (edge_buffer)
