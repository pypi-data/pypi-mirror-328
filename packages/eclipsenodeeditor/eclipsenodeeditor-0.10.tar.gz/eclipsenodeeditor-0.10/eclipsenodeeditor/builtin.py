from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QCoreApplication
QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)
from PyQt6 import QtWebEngineWidgets  # Import early to initialize WebEngine

from .core import EclipseNodeEditor, node, Node, socket, Socket, tool, Tool, NodeUtils, Reroute, SocketConnection, NodeEditorObject, Event
from typing import Callable


class NodeMovingTool(Tool):
    def __init__(self):
        super().__init__()
        self.is_moving = False
        self.grabbed_reroute = None
        self.grabbed_connection = None
        self.start_mouse_x = 0
        self.start_mouse_y = 0

    def input(self, editor: EclipseNodeEditor):
        mouse_x, mouse_y = editor.get_mouse_pos()
        nodes = editor.get_objects_of_type(Node)

        if editor.left_mouse_pressed:
            if not editor.get_key(Qt.Key.Key_Shift):
                for node in nodes:
                    node: Node
                    node.is_selected = False
                    for socket in node.sockets:
                        socket: Socket
                        for connection in socket.connections:
                            connection: SocketConnection
                            for reroute in connection.reroutes:
                                reroute.is_selected = False

            # Check for Ctrl+left-click on reroutes
            if editor.get_key(Qt.Key.Key_Control):
                for node in nodes:
                    node: Node
                    for socket in node.sockets:
                        socket: Socket
                        for connection in socket.connections:
                            connection: SocketConnection
                            for reroute in connection.reroutes:
                                if reroute.is_hovered:
                                    editor.lock_tool(self)
                                    self.is_moving = True
                                    self.grabbed_reroute = reroute
                                    self.grabbed_connection = connection
                                    self.start_mouse_x = mouse_x
                                    self.start_mouse_y = mouse_y
                                    reroute.start_x = reroute.x
                                    reroute.start_y = reroute.y
                                    reroute.is_selected = True

                                    # Store initial positions of all selected nodes if shift is held
                                    if editor.get_key(Qt.Key.Key_Shift):
                                        for node in nodes:
                                            if node.is_selected:
                                                node.start_x = node.x
                                                node.start_y = node.y
                                                node.start_mouse_x = mouse_x
                                                node.start_mouse_y = mouse_y
                                    return

            # Regular node grabbing logic
            grabbed_node = editor.grabbed_object
            if isinstance(grabbed_node, Node):
                if grabbed_node.is_over_header:
                    editor.lock_tool(self)
                    self.is_moving = True
                    grabbed_node.start_mouse_x = mouse_x
                    grabbed_node.start_mouse_y = mouse_y
                    grabbed_node.start_x = grabbed_node.x
                    grabbed_node.start_y = grabbed_node.y
                    grabbed_node.is_selected = True

        if self.is_moving:
            if editor.left_mouse_down:
                # Handle reroute movement
                if self.grabbed_reroute:
                    dx = mouse_x - self.start_mouse_x
                    dy = mouse_y - self.start_mouse_y
                    # Move all selected reroutes
                    for node in nodes:
                        # If shift is held, also move selected nodes
                        if editor.get_key(Qt.Key.Key_Shift):
                            if node.is_selected:
                                node.x = node.start_x + dx
                                node.y = node.start_y + dy

                        for socket in node.sockets:
                            for connection in socket.connections:
                                for reroute in connection.reroutes:
                                    if reroute.is_selected:
                                        reroute.x = reroute.start_x + dx
                                        reroute.y = reroute.start_y + dy
                else:
                    # Handle node movement
                    reroutes = set()
                    if editor.grabbed_object:
                        if isinstance(editor.grabbed_object, Node):
                            for obj in nodes:
                                obj: Node
                                if obj.is_selected:
                                    obj.x = obj.start_x + mouse_x - editor.grabbed_object.start_mouse_x
                                    obj.y = obj.start_y + mouse_y - editor.grabbed_object.start_mouse_y

                                for socket in obj.sockets:
                                    socket: Socket
                                    for connection in socket.connections:
                                        connection: SocketConnection
                                        for reroute in connection.reroutes:
                                            if reroute.is_selected:
                                                if reroute not in reroutes:
                                                    reroutes.add(reroute)
                                                    reroute.x = reroute.start_x + mouse_x - editor.grabbed_object.start_mouse_x
                                                    reroute.y = reroute.start_y + mouse_y - editor.grabbed_object.start_mouse_y

        if editor.left_mouse_released:
            self.is_moving = False
            self.grabbed_reroute = None
            self.grabbed_connection = None
            for node in nodes:
                node: Node
                node.start_mouse_x = mouse_x
                node.start_mouse_y = mouse_y
                node.start_x = node.x
                node.start_y = node.y

                for socket in node.sockets:
                    socket: Socket
                    for connection in socket.connections:
                        connection: SocketConnection
                        for reroute in connection.reroutes:
                            reroute.start_x = reroute.x
                            reroute.start_y = reroute.y

            editor.unlock_tool()


class SelectingTool(Tool):
    def __init__(self):
        super().__init__()
        self.is_selecting = False
        self.start_mouse_x = 0
        self.start_mouse_y = 0
        self.already_selected_nodes: list[Node] = []
        self.already_selected_reroutes: set[Reroute] = set()

        self.selection_region_color = QColor(20, 130, 219, 26)
        self.selection_region_outline_color = QColor(20, 130, 219, 179)

    def setup(self, editor: EclipseNodeEditor):
        """Setup the tool's input bindings"""
        editor.register_binding(
            "selecting",
            201,  # Base priority for right-click
            lambda: editor.left_mouse_pressed and editor.get_key(
                Qt.Key.Key_Shift),
            "Select nodes with left-click"
        )

    def input(self, editor: EclipseNodeEditor):
        mouse_x, mouse_y = editor.get_mouse_pos()
        if editor.get_binding("selecting"):
            editor.lock_tool(self)
            self.is_selecting = True
            self.start_mouse_x = mouse_x
            self.start_mouse_y = mouse_y
            self.already_selected_nodes = []
            self.already_selected_reroutes = set()
            nodes = editor.get_objects_of_type(Node)
            for node in nodes:
                node: Node
                if node.is_selected:
                    self.already_selected_nodes.append(node)

                for socket in node.sockets:
                    socket: Socket
                    for connection in socket.connections:
                        connection: SocketConnection
                        for reroute in connection.reroutes:
                            if reroute.is_selected:
                                self.already_selected_reroutes.add(reroute)

        if self.is_selecting:
            if editor.left_mouse_down:
                nodes = editor.get_objects_of_type(Node)
                # Calculate selection bounds regardless of drag direction
                min_x = min(self.start_mouse_x, mouse_x)
                max_x = max(self.start_mouse_x, mouse_x)
                min_y = min(self.start_mouse_y, mouse_y)
                max_y = max(self.start_mouse_y, mouse_y)

                for node in nodes:
                    node: Node
                    # Check if node overlaps with selection rectangle
                    node_left = node.x
                    node_right = node.x + node.width
                    node_top = node.y
                    node_bottom = node.y + node.height

                    # Check for overlap in both axes
                    overlap_x = (node_left < max_x) and (node_right > min_x)
                    overlap_y = (node_top < max_y) and (node_bottom > min_y)

                    if node not in self.already_selected_nodes:
                        if overlap_x and overlap_y:
                            node.is_selected = True
                        else:
                            node.is_selected = False

                    for socket in node.sockets:
                        socket: Socket
                        for connection in socket.connections:
                            connection: SocketConnection
                            for reroute in connection.reroutes:
                                if reroute not in self.already_selected_reroutes:
                                    if reroute.x >= min_x and reroute.x <= max_x and reroute.y >= min_y and reroute.y <= max_y:
                                        reroute.is_selected = True
                                    else:
                                        reroute.is_selected = False

        if editor.left_mouse_released:
            self.is_selecting = False
            editor.unlock_tool()
            editor.clear_active_binding()
            self.already_selected_nodes = []
            self.already_selected_reroutes = set()

    def render(self, editor: EclipseNodeEditor):
        if self.is_selecting:
            def render_selecting_rectangle():
                mouse_x, mouse_y = editor.get_mouse_pos()
                # Calculate rectangle dimensions regardless of drag direction
                rect_x = min(self.start_mouse_x, mouse_x)
                rect_y = min(self.start_mouse_y, mouse_y)
                rect_width = abs(mouse_x - self.start_mouse_x)
                rect_height = abs(mouse_y - self.start_mouse_y)

                editor.draw_rectangle(
                    rect_x, rect_y, rect_width, rect_height,
                    self.selection_region_color
                )

                editor.draw_rectangle_outline(
                    rect_x, rect_y, rect_width, rect_height,
                    self.selection_region_outline_color, 2
                )

            editor.add_render_group(100, render_selecting_rectangle)


class NodeConnectionTool(Tool):
    def __init__(self):
        super().__init__()
        self.from_node_and_socket: tuple[Node, Socket] | None = None
        self.to_node_and_socket: tuple[Node, Socket] | None = None
        self.from_reroute: tuple[Reroute, SocketConnection] | None = None
        self.to_reroute: tuple[Reroute, SocketConnection] | None = None

        self.connection_color = QColor(255, 255, 255)

    def check_connection_exists(self, socket1: Socket, socket2: Socket) -> bool:
        """Check if a connection already exists between these two sockets"""
        for connection in socket1.connections:
            if (connection.from_socket == socket1 and connection.to_socket == socket2) or \
               (connection.from_socket == socket2 and connection.to_socket == socket1):
                return True
        return False

    def input(self, editor: EclipseNodeEditor):
        mouse_x, mouse_y = editor.get_mouse_pos()

        if editor.left_mouse_pressed:
            nodes = editor.get_objects_of_type(Node)
            self.from_node_and_socket = None
            self.from_reroute = None

            # First check for reroute clicks
            for node in nodes:
                node: Node
                for socket in node.sockets:
                    for connection in socket.connections:
                        for reroute in connection.reroutes:
                            if reroute.is_hovered:
                                self.from_reroute = (reroute, connection)
                                editor.lock_tool(self)
                                return

            # Then check for socket clicks
            for node in reversed(nodes):
                node: Node
                for socket in node.sockets:
                    if socket.is_pin_hovered:
                        self.from_node_and_socket = (node, socket)
                        editor.lock_tool(self)
                        break

        if self.from_node_and_socket or self.from_reroute:
            if editor.left_mouse_released:
                nodes = editor.get_objects_of_type(Node)
                self.to_node_and_socket = None
                self.to_reroute = None

                # First check for reroute clicks
                for node in nodes:
                    node: Node
                    for socket in node.sockets:
                        for connection in socket.connections:
                            for reroute in connection.reroutes:
                                if reroute.is_hovered:
                                    self.to_reroute = (reroute, connection)
                                    break

                # Then check for socket clicks if no reroute was clicked
                if not self.to_reroute:
                    for node in reversed(nodes):
                        node: Node
                        for socket in node.sockets:
                            if socket.is_pin_hovered:
                                self.to_node_and_socket = (node, socket)
                                break

                # Handle the different connection cases
                if self.from_node_and_socket:
                    from_node, from_socket = self.from_node_and_socket

                    # Socket to Socket
                    if self.to_node_and_socket:
                        to_node, to_socket = self.to_node_and_socket
                        if from_node != to_node:  # Don't connect to same node
                            if not self.check_connection_exists(from_socket, to_socket):
                                if from_socket.pin_type == "input" and to_socket.pin_type == "output":
                                    NodeUtils.create_input_output_connection(
                                        to_node, to_socket, from_node, from_socket)
                                elif from_socket.pin_type == "output" and to_socket.pin_type == "input":
                                    NodeUtils.create_output_input_connection(
                                        from_node, from_socket, to_node, to_socket)

                    # Socket to Reroute
                    elif self.to_reroute:
                        reroute, connection = self.to_reroute
                        # Find reroute index
                        reroute_index = connection.reroutes.index(reroute)

                        # If connecting output to reroute
                        if from_socket.pin_type == "output":
                            # Check if connection already exists
                            if not self.check_connection_exists(from_socket, connection.to_socket):
                                # Create new connection from output to input
                                new_connection = SocketConnection()
                                new_connection.from_node = from_node
                                new_connection.from_socket = from_socket
                                new_connection.to_node = connection.to_node
                                new_connection.to_socket = connection.to_socket
                                # Include reroutes at and after the clicked one
                                new_connection.reroutes = connection.reroutes[reroute_index:]
                                from_socket.connections.append(new_connection)
                                connection.to_socket.connections.append(
                                    new_connection)

                        # If connecting input to reroute
                        elif from_socket.pin_type == "input":
                            # Check if connection already exists
                            if not self.check_connection_exists(from_socket, connection.from_socket):
                                # Create new connection from output to input
                                new_connection = SocketConnection()
                                new_connection.from_node = connection.from_node
                                new_connection.from_socket = connection.from_socket
                                new_connection.to_node = from_node
                                new_connection.to_socket = from_socket
                                # Include reroutes up to and including the clicked one
                                new_connection.reroutes = connection.reroutes[:reroute_index + 1]
                                connection.from_socket.connections.append(
                                    new_connection)
                                from_socket.connections.append(new_connection)

                elif self.from_reroute:
                    reroute, connection = self.from_reroute
                    reroute_index = connection.reroutes.index(reroute)

                    # Reroute to Socket
                    if self.to_node_and_socket:
                        to_node, to_socket = self.to_node_and_socket
                        if to_socket.pin_type == "input":
                            # Check if connection already exists
                            if not self.check_connection_exists(connection.from_socket, to_socket):
                                # Create new connection from output to input
                                new_connection = SocketConnection()
                                new_connection.from_node = connection.from_node
                                new_connection.from_socket = connection.from_socket
                                new_connection.to_node = to_node
                                new_connection.to_socket = to_socket
                                # Include reroutes up to and including the clicked one
                                new_connection.reroutes = connection.reroutes[:reroute_index + 1]
                                connection.from_socket.connections.append(
                                    new_connection)
                                to_socket.connections.append(new_connection)

                # Reset state
                self.from_node_and_socket = None
                self.to_node_and_socket = None
                self.from_reroute = None
                self.to_reroute = None

        if editor.left_mouse_released:
            editor.unlock_tool()

    def render(self, editor: EclipseNodeEditor):
        def render_temp_connection():
            mouse_x, mouse_y = editor.get_mouse_pos()
            if self.from_node_and_socket:
                from_node, from_socket = self.from_node_and_socket
                socket_x, socket_y = from_node.get_socket_pos(from_socket)
                editor.draw_line(socket_x, socket_y, mouse_x,
                                 mouse_y, 2, self.connection_color)
            elif self.from_reroute:
                reroute, _ = self.from_reroute
                editor.draw_line(reroute.x, reroute.y, mouse_x,
                                 mouse_y, 2, self.connection_color)

        editor.add_render_group(10, render_temp_connection)


class ConnectionCuttingTool(Tool):
    def __init__(self):
        super().__init__()
        self.start_mouse_x = 0
        self.start_mouse_y = 0
        self.is_cutting = False
        # connection is the key, intersections is the value
        self.connections_to_cut_data: dict[SocketConnection,
                                           list[tuple[float, float]]] = {}

        self.cutting_color = QColor(255, 0, 0)

    def setup(self, editor: EclipseNodeEditor):
        """Setup the tool's input bindings"""
        editor.register_binding(
            "connection_cut",
            200,  # Base priority for right-click
            lambda: editor.right_mouse_pressed and editor.get_key(
                Qt.Key.Key_Shift),
            "Cut connections"
        )

    def input(self, editor: EclipseNodeEditor):
        mouse_x, mouse_y = editor.get_mouse_pos()

        if editor.get_binding("connection_cut"):
            editor.lock_tool(self)
            self.start_mouse_x = mouse_x
            self.start_mouse_y = mouse_y
            self.is_cutting = True

        if editor.right_mouse_down:
            self.update_connection_data(editor)

        if editor.right_mouse_released:
            self.is_cutting = False
            self.update_connection_data(editor)
            for connection, intersections in self.connections_to_cut_data.items():
                if len(intersections) > 0:
                    NodeUtils.remove_connection(connection)
            editor.unlock_tool()
            editor.clear_active_binding()

    def update_connection_data(self, editor: EclipseNodeEditor):
        self.connections_to_cut_data = {}
        mouse_x, mouse_y = editor.get_mouse_pos()
        nodes = editor.get_objects_of_type(Node)
        for node in nodes:
            node: Node
            for socket in node.sockets:
                for connection in socket.connections:
                    intersections = NodeUtils.get_intersections_with_connection(
                        self.start_mouse_x, self.start_mouse_y, mouse_x, mouse_y, connection)
                    if intersections:
                        self.connections_to_cut_data[connection] = intersections

    def render(self, editor: EclipseNodeEditor):
        def render_cutting_line():
            if self.is_cutting:
                mouse_x, mouse_y = editor.get_mouse_pos()
                editor.draw_line(self.start_mouse_x, self.start_mouse_y, mouse_x,
                                 mouse_y, 2, self.cutting_color)

                for connection, intersections in self.connections_to_cut_data.items():
                    for intersection in intersections:
                        editor.draw_circle(
                            intersection[0], intersection[1], 5, self.cutting_color)

        editor.add_render_group(100, render_cutting_line)


class ConnectionRerouteTool(Tool):
    def __init__(self):
        super().__init__()
        self.start_mouse_x = 0
        self.start_mouse_y = 0
        self.is_rerouting = False
        # connection is the key, intersections is the value
        self.connections_to_reroute_data: dict[SocketConnection,
                                               list[tuple[float, float]]] = {}

        self.rerouting_color = QColor(0, 255, 255)

    def setup(self, editor: EclipseNodeEditor):
        """Setup the tool's input bindings"""
        editor.register_binding(
            "connection_reroute",
            100,  # Higher priority than cut for shift+right-click
            lambda: editor.right_mouse_pressed,
            "Reroute connections"
        )

    def input(self, editor: EclipseNodeEditor):
        mouse_x, mouse_y = editor.get_mouse_pos()

        if editor.get_binding("connection_reroute"):
            editor.lock_tool(self)
            self.start_mouse_x = mouse_x
            self.start_mouse_y = mouse_y
            self.is_rerouting = True

        if editor.right_mouse_down:
            self.update_connection_data(editor)

        if editor.right_mouse_released:
            self.is_rerouting = False
            self.update_connection_data(editor)
            for connection, intersections in self.connections_to_reroute_data.items():
                if len(intersections) > 0:
                    # Sort intersections by index to maintain correct order
                    sorted_intersections = sorted(
                        intersections, key=lambda x: x[2])
                    # Add all reroutes, adjusting indices as we insert
                    offset = 0
                    for x, y, index in sorted_intersections:
                        # Insert at the original index plus offset from previous insertions
                        new_reroute = Reroute(x, y)
                        new_reroute.color = connection.from_socket.pin_color
                        connection.reroutes.insert(index + offset, new_reroute)
                        offset += 1
            editor.unlock_tool()
            editor.clear_active_binding()

    def update_connection_data(self, editor: EclipseNodeEditor):
        self.connections_to_reroute_data = {}
        mouse_x, mouse_y = editor.get_mouse_pos()
        nodes = editor.get_objects_of_type(Node)
        for node in nodes:
            node: Node
            for socket in node.sockets:
                for connection in socket.connections:
                    intersections = NodeUtils.get_intersections_with_connection(
                        self.start_mouse_x, self.start_mouse_y, mouse_x, mouse_y, connection)
                    if intersections:
                        self.connections_to_reroute_data[connection] = intersections

    def render(self, editor: EclipseNodeEditor):
        def render_rerouting_line():
            if self.is_rerouting:
                mouse_x, mouse_y = editor.get_mouse_pos()
                editor.draw_line(self.start_mouse_x, self.start_mouse_y, mouse_x,
                                 mouse_y, 2, self.rerouting_color)

                for connection, intersections in self.connections_to_reroute_data.items():
                    for intersection in intersections:
                        editor.draw_circle(
                            intersection[0], intersection[1], 5, self.rerouting_color)

        editor.add_render_group(100, render_rerouting_line)


class RemoveNodeTool(Tool):
    def __init__(self):
        super().__init__()

    def setup(self, editor: EclipseNodeEditor):
        editor.register_binding(
            "remove_node",
            100,
            lambda: editor.get_key_down(Qt.Key.Key_Delete),
            "Remove node"
        )

    def input(self, editor: EclipseNodeEditor):
        if editor.get_binding("remove_node"):
            nodes = editor.get_objects_of_type(Node)
            nodes_to_remove = set()

            # First pass: identify nodes to remove and remove selected reroutes
            for node in nodes:
                if node.is_selected:
                    nodes_to_remove.add(node)
                else:
                    # For non-removed nodes, clean up selected reroutes
                    for socket in node.sockets:
                        # Create a copy to modify during iteration
                        for connection in socket.connections[:]:
                            # Remove selected reroutes from the connection
                            connection.reroutes = [
                                r for r in connection.reroutes if not r.is_selected]

            # Second pass: remove connections to nodes that will be removed
            for node in nodes:
                if node not in nodes_to_remove:
                    for socket in node.sockets:
                        # Remove any connections that connect to nodes being removed
                        socket.connections = [
                            conn for conn in socket.connections
                            if (conn.from_node not in nodes_to_remove and
                                conn.to_node not in nodes_to_remove)
                        ]

            # Finally, remove the selected nodes
            for node in nodes_to_remove:
                editor.remove_object(node)

            editor.clear_active_binding()


class ControlMenu(NodeEditorObject):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 300
        self.height = 400
        self.title = "Control Menu"
        self.title_color = QColor(255, 255, 255)
        self.header_size = 40
        self.header_color = QColor(75, 75, 75)
        self.background_color = QColor(51, 51, 51)
        self.is_hovered = False
        self.option_hover_color = QColor(75, 75, 75)
        self.option_title_color = QColor(255, 255, 255)
        self.separator_color = QColor(255, 255, 255)

        # Options
        self.options = []
        self.hovered_option_index = 2

    def add_option(self, name: str, callback: Callable):
        event = Event()
        if callback:
            event.on(callback)
        self.options.append((name, event))
        return event

    def add_separator(self):
        self.options.append(("separator", None))

    def raycast_reset(self, editor: EclipseNodeEditor):
        self.is_hovered = False
        self.hovered_option_index = -1

    def raycast(self, editor: EclipseNodeEditor):
        mouse_x, mouse_y = editor.get_mouse_pos()

        has_hit = False
        # Check if mouse is within menu bounds
        if (mouse_x >= self.x and mouse_x <= self.x + self.width and
                mouse_y >= self.y and mouse_y <= self.y + self.height):
            self.is_hovered = True
            has_hit = True

            # Options
            option_y = self.y + self.header_size + 10
            for i, option in enumerate(self.options):
                if option[0] == "separator":
                    pass
                else:
                    if mouse_x >= self.x and mouse_x <= self.x + self.width and mouse_y >= option_y and mouse_y <= option_y + 25:
                        self.hovered_option_index = i

                if option[0] == "separator":
                    option_y += 10
                else:
                    option_y += 25

        return has_hit

    def input(self, editor: EclipseNodeEditor):
        if editor.left_mouse_pressed:
            if self.hovered_option_index != -1:
                event: Event = self.options[self.hovered_option_index][1]
                if event:
                    event.trigger(editor)

    def render(self, editor: EclipseNodeEditor):
        def render_main():
            editor.draw_raised_rectangle(self.x, self.y,
                                         self.width, self.height, self.background_color)

            # Draw Header
            editor.draw_rectangle(self.x, self.y, self.width, self.header_size,
                                  self.header_color)

            # Draw Title
            editor.draw_text(self.x - 45 + self.width / 2,
                             self.y + 20, self.title, self.title_color)

            # Draw Options
            option_y = self.y + self.header_size + 10
            for i, option in enumerate(self.options):
                if option[0] == "separator":
                    editor.draw_rectangle(
                        self.x + 10, option_y + 3, self.width - 20, 2, self.separator_color)
                else:
                    hovered = i == self.hovered_option_index
                    if hovered:
                        editor.draw_rectangle(
                            self.x, option_y, self.width, 25, self.option_hover_color)
                    editor.draw_text(self.x + 10, option_y + 12,
                                     option[0], self.option_title_color, font_size=12 if hovered else 10)

                if option[0] == "separator":
                    option_y += 10
                else:
                    option_y += 25

        editor.add_render_group(100, render_main)


class ControlMenuTool(Tool):
    def __init__(self):
        super().__init__()
        self.menu = None
        self.start_mouse_x = 0
        self.start_mouse_y = 0

    def setup(self, editor: EclipseNodeEditor):
        editor.register_binding(
            "space_menu",
            100,
            lambda: editor.get_key_down(Qt.Key.Key_Space),
            "Space menu"
        )

    def input(self, editor: EclipseNodeEditor):
        if editor.get_binding("space_menu"):
            editor.lock_tool(self)
            self.start_mouse_x, self.start_mouse_y = editor.get_mouse_pos()
            self.open_menu(editor)

        if editor.get_key_up(Qt.Key.Key_Space):
            editor.unlock_tool()
            editor.clear_active_binding()

        # Handle menu interaction
        if self.menu:
            # Close menu if clicking outside of it
            if (editor.left_mouse_pressed or editor.right_mouse_pressed) and not self.menu.is_hovered:
                self.close_menu(editor)

    def open_menu(self, editor: EclipseNodeEditor):
        if self.menu != None:
            editor.remove_object(self.menu)

        self.menu = ControlMenu(self.start_mouse_x, self.start_mouse_y)
        self.menu.x = self.start_mouse_x - self.menu.width / 2
        self.menu.y = self.start_mouse_y - 20
        editor.add_object(self.menu)
        self.initialize_menu(editor)

    def close_menu(self, editor: EclipseNodeEditor):
        if self.menu:
            editor.remove_object(self.menu)
            self.menu = None

    def initialize_menu(self, editor: EclipseNodeEditor):
        self.menu.add_option("Create Custom Node", self.create_custom_node)

    def create_custom_node(self, editor: EclipseNodeEditor):
        # Create a new CustomNodeBuilder at the menu's starting position
        self.custom_node_builder = CustomNodeBuilder(
            self.start_mouse_x, self.start_mouse_y)
        self.custom_node_builder.x = self.start_mouse_x - \
            self.custom_node_builder.width / 2
        self.custom_node_builder.y = self.start_mouse_y - \
            self.custom_node_builder.height / 2
        editor.add_object(self.custom_node_builder)
        self.custom_node_builder.initialize(editor)

        # Find existing CustomNodeTool or create a new one
        custom_node_tool = self.find_specific_tool(editor, CustomNodeTool)
        if not custom_node_tool:
            # No existing tool found, create and add a new one
            self.custom_node_tool = CustomNodeTool()
            editor.add_tool(self.custom_node_tool)
        else:
            # Use existing tool
            self.custom_node_tool = custom_node_tool

        # Lock editor to the custom node tool and close the menu
        editor.lock_tool(self.custom_node_tool)
        self.close_menu(editor)

    def find_specific_tool(self, editor: EclipseNodeEditor, tool_class: type):
        for tool in editor.tools:
            if isinstance(tool, tool_class):
                return tool
        return None


class CustomNodeTool(Tool):
    def __init__(self):
        super().__init__()
        self.custom_node_builder = None

    def setup(self, editor: EclipseNodeEditor):
        editor.register_binding(
            "custom_node_tool",
            100,
            lambda: editor.left_mouse_pressed,
            "Custom node tool"
        )

    def input(self, editor: EclipseNodeEditor):
        if editor.get_binding("custom_node_tool"):
            node_builders = editor.get_objects_of_type(CustomNodeBuilder)
            for node_builder in node_builders:
                node_builder.is_targeted = False

            hovered_exists = False
            hovered_builder = None
            for node_builder in node_builders:
                if node_builder.is_hovered:
                    hovered_exists = True
                    hovered_builder = node_builder
                    break

            if hovered_exists:
                hovered_builder.is_targeted = True
                editor.remove_object(hovered_builder)
                editor.add_object(hovered_builder)
                editor.lock_tool(self)
            else:
                editor.unlock_tool()

        if editor.locked_tool == self:
            if editor.get_key_down(Qt.Key.Key_Delete):
                node_builders = editor.get_objects_of_type(CustomNodeBuilder)
                for node_builder in node_builders:
                    node_builder.is_targeted = False

                hovered_exists = False
                hovered_builder = None
                for node_builder in node_builders:
                    if node_builder.is_hovered:
                        hovered_exists = True
                        hovered_builder = node_builder
                        break

                if hovered_exists:
                    editor.remove_object(hovered_builder)
                    editor.unlock_tool()


class CustomNodeBuilder(NodeEditorObject):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 400
        self.height = 400
        self.color = QColor(35, 35, 35)
        self.is_hovered = False
        self.is_targeted = False

        self.buttons = []

    def initialize(self, editor: EclipseNodeEditor):
        self.open_code_editor_button = self.add_button(self.x + 10, self.y + 10, 150, 50,
                                                       "Open Code Editor", QColor(212, 130, 30))
        self.open_code_editor_button.title_offset_x = -62
        self.open_code_editor_button.title_offset_y = -2
        
        # Add callback for the code editor button
        self.code_editor_window = None
        self.open_code_editor_button.add_callback(self.open_code_editor)

    def add_button(self, x: int, y: int, width: int, height: int, text: str, color: QColor):
        button = Button(x, y, width, height, text, color)
        button.is_raised = True
        self.buttons.append(button)
        return button

    def raycast_reset(self, editor: EclipseNodeEditor):
        self.is_hovered = False
        for button in self.buttons:
            button.raycast_reset()

    def raycast(self, editor: EclipseNodeEditor):
        mouse_x, mouse_y = editor.get_mouse_pos()
        has_hit = False
        if mouse_x >= self.x and mouse_x <= self.x + self.width and mouse_y >= self.y and mouse_y <= self.y + self.height:
            self.is_hovered = True
            has_hit = True

        for button in self.buttons:
            if button.raycast(mouse_x, mouse_y):
                has_hit = True

        return has_hit

    def input(self, editor: EclipseNodeEditor):
        for button in self.buttons:
            button.input(editor)

    def render(self, editor: EclipseNodeEditor):
        def render_main():
            editor.draw_raised_rectangle(self.x, self.y, self.width,
                                         self.height, self.color)

            if self.is_targeted:
                editor.draw_rectangle_outline(self.x, self.y, self.width,
                                              self.height, QColor(255, 165, 0), 2)

            for button in self.buttons:
                button.render(editor)

        editor.add_render_group(100, render_main)

    def open_code_editor(self, editor: EclipseNodeEditor):
        from .code_editor import CodeEditorWindow
        if not self.code_editor_window:
            self.code_editor_window = CodeEditorWindow()
        self.code_editor_window.show_editor()


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, title: str, color: QColor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.title_offset_x = 0
        self.title_offset_y = 0
        self.color = color
        # Create lighter color by increasing brightness by 25%
        self.hover_color = color.lighter(125)
        # Create darker color by decreasing brightness by 25%
        self.pressed_color = color.darker(125)
        self.text_color = QColor(255, 255, 255)

        self.is_hovered = False
        self.is_pressed = False
        self.is_raised = False

        self.event = Event()

    def add_callback(self, callback: Callable):
        self.event.on(callback)

    def trigger(self, editor: EclipseNodeEditor):
        self.event.trigger(editor)

    def raycast_reset(self):
        self.is_hovered = False
        self.is_pressed = False

    def raycast(self, x: int, y: int):
        if x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height:
            self.is_hovered = True
            return True
        return False

    def input(self, editor: EclipseNodeEditor):
        if self.is_hovered:
            if editor.left_mouse_pressed:
                self.trigger(editor)

            if editor.left_mouse_down:
                self.is_pressed = True
            else:
                self.is_pressed = False

    def render(self, editor: EclipseNodeEditor):
        if self.is_raised:
            if self.is_pressed:
                editor.draw_rectangle(self.x, self.y + 3, self.width,
                                      self.height, self.pressed_color)
                editor.draw_text(self.x + self.width / 2 + self.title_offset_x, self.y + self.height / 2 + self.title_offset_y + 3,
                                 self.title, self.text_color, font_size=12)
            elif self.is_hovered:
                editor.draw_raised_rectangle(self.x, self.y, self.width,
                                             self.height, self.hover_color)
                editor.draw_text(self.x + self.width / 2 + self.title_offset_x, self.y + self.height / 2 + self.title_offset_y,
                                 self.title, self.text_color, font_size=12)
            else:
                editor.draw_raised_rectangle(self.x, self.y, self.width,
                                             self.height, self.color)
                editor.draw_text(self.x + self.width / 2 + self.title_offset_x, self.y + self.height / 2 + self.title_offset_y,
                                 self.title, self.text_color, font_size=12)
        else:
            if self.is_pressed:
                editor.draw_rectangle(self.x, self.y, self.width,
                                      self.height, self.pressed_color)
                editor.draw_text(self.x + self.width / 2 + self.title_offset_x, self.y + self.height / 2 + self.title_offset_y,
                                 self.title, self.text_color, font_size=12)
            elif self.is_hovered:
                editor.draw_rectangle(self.x, self.y, self.width,
                                      self.height, self.hover_color)
                editor.draw_text(self.x + self.width / 2 + self.title_offset_x, self.y + self.height / 2 + self.title_offset_y,
                                 self.title, self.text_color, font_size=12)
            else:
                editor.draw_rectangle(self.x, self.y, self.width,
                                      self.height, self.color)
                editor.draw_text(self.x + self.width / 2 + self.title_offset_x, self.y + self.height / 2 + self.title_offset_y,
                                 self.title, self.text_color, font_size=12)


@node()
class TestNode(Node):
    def __init__(self, x, y):
        super().__init__(x, y, "Test Node")
        self.add_input_socket(Socket())
        self.add_output_socket(Socket())
