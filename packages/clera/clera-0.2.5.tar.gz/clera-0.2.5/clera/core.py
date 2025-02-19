from PySide6.QtCore import QSize, QPoint, QEvent
from PySide6.QtGui import QIcon, QMouseEvent, QScreen, QSyntaxHighlighter, QShortcut
from PySide6.QtWidgets import QMainWindow, QToolBar, QStatusBar, QGroupBox, QButtonGroup
from PySide6.QtWidgets import QWidget,  QHBoxLayout, QVBoxLayout,  QGridLayout, QTabWidget, QMenu
from PySide6.QtWidgets import QDialog, QFileDialog, QStyleFactory, QStackedWidget
################################
################################
from .utils import *
from .widgets import *
from .database import *
# from .scripts import *


__all__ = [
    'Window', 'Box', 'Grid', 'fieldset', 'Column', 'column', 'Group', 'group', 'Toolbar', 'toolbar',
    'Menubar', 'menubar', 'Statusbar', 'statusbar', 'GET', 'get', 'Button', 'button', 'Input',
    'input', 'Text', 'text', 'Image', 'image', 'CheckBox', 'checkbox', 'RadioButton', 'radiobutton',
    'Textarea', 'textarea', 'item', 'empty', 'separator', 'Exit', 'exit', 'Copy', 'copy', 'Cut', 'cut',
    'Paste', 'paste', 'Undo', 'undo', 'Redo', 'redo', 'link', 'ListWidget', 'listwidget', 'ListItem',
    'tab', 'TabWidget', 'tabwidget', 'Select', 'select', 'option', 'ProgressBar', 'progressbar',
    'Slider', 'slider', 'Dial', 'dial', 'Popup', 'popup', 'call', 'Titlebar', 'titlebar', 'File', 'file',
    'Folder', 'folder', 'ScrollArea', 'scrollarea', 'minimize', 'maximize', 'close', 'title', 'Highlight',
    'r', 'Stack', 'stack', 'expand', 'fixed', 'vertical', 'horizontal', 'top', 'bottom', 'left', 'right', 'center',
    'vcenter', 'hcenter', 'justify', 'static', 'normal', 'standard', 'password', 'noecho', 'extended',
    'noselection', 'multi', 'single', 'windows', 'windows11', 'fusion', 'curve', 'breeze', 'oxygen','circle', 'square',
    'encode', 'decode', 'colorpicker', 'ColorPicker', 'Database', 'database', 'null', 'blob',
    'thread', 'screen', 'screenshot', 'shortcut', 'Table', 'td'
]


# Initialize the Qt application
app = start()

# Default window layout object (empty QWidget, can be customized later)
DEFAULT_WINDOW_LAYOUT = QWidget()



def init_window_css(css_string):
    """
    Initializes CSS styles for the window by parsing the provided CSS string.
    It handles custom CSS and applies it to the correct widgets.
    """
    custom, builtins = console_css(css_string)
    
    # Iterate over custom styles to apply to corresponding widgets
    for name, property in custom:
        # Attempt to find the widget in WIDGET_ID_SAFE dictionary using the name
        widget = WIDGET_ID_SAFE.get(name)

        # Only proceed if the widget exists
        if widget:
            for value in compr:
                value = value.split('::')
                _type = value[1]

                # Ensure widget type matches expected type from CSS
                if any(typ in str(type(widget)) for typ in (value[0], value[1])):
                    property = property.replace(TYPE_MARKER, _type)
                    widget.setStyleSheet(property)  # Apply the modified CSS to the widget
                    break  # No need to check other types once matched

    # Apply the built-in CSS to the application
    app.setStyleSheet(builtins)


def link(href: str = None):
    """
    Adds a linked file to the list of included links if the file path is valid and ends with '.cx'.
    This is useful for dynamically linking CSS or configuration files to the application.
    """
    if href and href.strip().endswith('.cx'):
        LINK_ITEMS_INCLUDED.append(href)  # Add the link to the global list of included items


def init_linked_files():
    """
    Loads and applies all linked CSS files from the LINK_ITEMS_INCLUDED list.
    For each valid file path, it reads the content and applies the CSS styles to the window.
    """
    for LINK_ITEM in LINK_ITEMS_INCLUDED:
        file_path = path.abspath(LINK_ITEM)

        # Check if the file exists and is a valid file
        if path.isfile(file_path):
            try:
                # Open the file and read its content
                with open(file_path, 'r') as file:
                    file_content = file.read()

                # Apply the CSS content to the window
                init_window_css(file_content)
            except Exception as e:
                # Log more informative error
                print(f"Error loading file {file_path}: {e}")
        else:
            print(f"Invalid file path: {file_path}")  # Provide feedback for invalid paths


class MainWindow(QMainWindow):
    def __init__(self, title, icon, size, fixed_size, geometry, style, frame, movable, win_top, spacing, content_margin, move, tool, cursor):
        super().__init__()

        # Initialize window properties from arguments
        self._qwidget = DEFAULT_WINDOW_LAYOUT
        self._title = title
        self._size = size
        self._fixed_size = fixed_size
        self._icon = icon
        self._geometry = geometry
        self._movable = movable
        self._frame = frame
        self._top = win_top
        self._spacing = spacing
        self._content_margin = content_margin
        self._move = move
        self._tool = tool
        self._cursor = cursor

        self._query_fixed_size = False
        self._custom_title_bar = False

        if self._cursor == False:
            self.setCursor(Qt.BlankCursor)
        
        # Set window flag if it is a tool window
        if self._tool == True:
            self.setWindowFlag(Qt.Tool)
    
        # Resize the window if a valid size is provided
        if self._size != (None, None):
            self.resize(*map(int, self._size))

        # Move the window if valid position is provided
        if self._move != (None, None):
            self.move(*self._move)

        # Set geometry (position and size) if provided
        if self._geometry:
            self.setGeometry(*self._geometry) if len(self._geometry) == 4 else None

        # Set window title
        self.setWindowTitle(self._title)

        # Set the window to always stay on top if specified
        if self._top:
            self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # Apply the style to the window
        app.setStyle(style)
    
        # Set fixed size if provided
        if self._fixed_size != (None, None):
            self._query_fixed_size = True
            self.setFixedSize(QSize(*map(int, self._fixed_size)))

        
        # Initialize layout for content
        global layout
        layout = QVBoxLayout()
        layout.setSpacing(self._spacing)


        # Set content margins based on the provided configuration
        if type(self._content_margin) != int:
            if len(self._content_margin) == 4:
                left, top, right, bottom = self._content_margin
                layout.setContentsMargins(left, top, right, bottom)
            elif len(self._content_margin) == 2:
                top_bottom, left_right = self._content_margin
                layout.setContentsMargins(
                    left_right, top_bottom, left_right, top_bottom)
        else:
            layout.setContentsMargins(
                self._content_margin, self._content_margin, self._content_margin, self._content_margin)

        # Apply the layout to the central widget
        self._qwidget.setLayout(layout)

        # Set window to frameless if frame is False
        if not self._frame:
            self.setWindowFlag(Qt.FramelessWindowHint)

            # make window transparent and border cornered

            # self.setAttribute(Qt.WA_TranslucentBackground)
            # DEFAULT_WINDOW_LAYOUT.setWindowOpacity(1)
            # DEFAULT_WINDOW_LAYOUT.setStyleSheet('''
            #     border-bottom-left-radius: 10px; 
            #     border-bottom-right-radius: 10px; 
            #     border-top-left-radius: 0px;
            #     border-top-right-radius: 0px;
            #     ''')
            # self.setStyleSheet('border-top-left-radius: 10px; border-top-right-radius: 10px;')


        # Set the window icon if provided
        self.setWindowIcon(QIcon(init_image(self._icon)))

    def WindowMenubar(self, menu_item, actions: list | None = None):
        """
        Creates and adds a menubar to the window.
        :param menu_item: Name of the menu (e.g., "File", "Edit")
        :param actions: List of actions (menu items) to add under the menu
        """
        if menu_item != None:
            menu_bar = self.menuBar()
            parent = menu_bar.addMenu(menu_item)

            # Add actions to the menu if provided
            if actions:
                for item in actions:
                    item_type = item[0]
                    if item_type == ELEM_TYPE_ITEM:
                        item_label = item[1]
                        if item_label != DEFAULT_SEPARATOR_MARKER:
                            parent.addAction(INIT_ITEM(self, item))
                        else:
                            parent.addSeparator()
                    elif item_type == ELEM_TYPE_SEPARATOR:
                        parent.addSeparator()
                    else:
                        pass
                        # DO NOTHING FOR NOW. SETUP LATER

    def WindowToolbar(self, name, tool_items, movable, position, ID, size, border, orientation, newline, toggle_view):
        """
        Creates and adds a toolbar to the window.
        :param name: Name of the toolbar
        :param tool_items: List of items (buttons, actions) to add to the toolbar
        :param movable: Whether the toolbar is movable
        :param position: Position of the toolbar (top, bottom, left, right)
        :param ID: Unique identifier for the toolbar
        :param size: Size of the toolbar icons
        :param border: Whether the toolbar has a border
        :param orientation: Orientation of the toolbar (vertical/horizontal)
        :param newline: Whether to add a new line before the toolbar
        :param toggle_view: Whether to toggle the visibility of the toolbar
        """
        toolbar = INIT_WIDGET(ID, QToolBar(name))
        
        # Add a break if required (i.e., a gap between toolbars)
        if newline:
            self.addToolBarBreak()

        if size != (None, None):
            # Set icon size of the toolbar
            toolbar.setIconSize(QSize(*size))


        # Define toolbar positions for various screen edges
        positions = {
            'top'     : Qt.TopToolBarArea,
            'bottom'  : Qt.BottomToolBarArea,
            'left'    : Qt.LeftToolBarArea,
            'right'   : Qt.RightToolBarArea
        }

        try:
            self.addToolBar(positions[position.lower()], toolbar)
        except:
            raise ValueError(f"Invalid position: {position}")

        # Add tool items to the toolbar
        if tool_items:
            for item in tool_items:
                if not isinstance(item, list):
                    widget_type, widget_items = check_func(item)
                    LayItOut(toolbar, widget_type, widget_items)
                    # toolbar.addWidget(widget)
                else:
                    item_type = item[0]
                    if item_type == ELEM_TYPE_ITEM:
                        item_label = item[1]
                        if item_label != DEFAULT_SEPARATOR_MARKER:
                            toolbar.addAction(INIT_ITEM(self, item))
                        else:
                            toolbar.addSeparator()
                    elif item_type == ELEM_TYPE_SEPARATOR:
                        toolbar.addSeparator()
                    else:
                        pass
                        # DO NOTHING FOR NOW. SETUP LATER

        # Set toolbar movability and orientation
        toolbar.setMovable(movable)
        toolbar.toggleViewAction().setVisible(toggle_view)
        
        orientations = {
            vertical: Qt.Vertical,
            horizontal: Qt.Horizontal
        }

        try:
            if orientation.lower() in ['v', 'h']:
                change = {
                    'v': vertical,
                    'h': horizontal
                }

                orientation = change[orientation.lower()]

            toolbar.setOrientation(orientations[orientation.lower()])
        except:
            raise ValueError(orientation)

        # Remove border styling if border is False
        if border == False:
            toolbar.setStyleSheet('border-bottom: 0px')

    # Status bar functions
    def init_status(self):
        """Initializes the status bar for the window."""
        self.setStatusBar(QStatusBar(self))

    def ADD_PERMANENT_WIDGET(self, widget_type, widget_items):
        """Adds a permanent widget to the status bar."""
        lyt = self.statusBar()
        LayItOut([lyt, 'addPermanentWidget'], widget_type, widget_items)

    def ADD_NORMAL_WIDGET(self, widget_type, widget_items):
        """Adds a normal widget (non-permanent) to the status bar."""
        lyt = self.statusBar()
        LayItOut([lyt, 'addWidget'], widget_type, widget_items)

    def SHOW_STATUSBAR_MESSAGE(self, text, time):
        """Displays a message on the status bar."""
        if time != None:
            self.statusBar().showMessage(text, time * 1000)
        else:
            self.statusBar().showMessage(text)

    def CLEAR_STATUSBAR_MESSAGE(self):
        """Clears the message from the status bar."""
        self.statusBar().clearMessage()

    def REMOVE_STATUSBAR_WIDGET(self, ID):
        """Removes a widget from the status bar by its ID."""
        if ID in WIDGET_ID_SAFE:
            self.statusBar().removeWidget(WIDGET_ID_SAFE[ID])
        else:
            raise IdError(f'id "{ID}" does not exist')

    def mousePressEvent(self, event):
        if self._movable == True:
            window.setCursor(Qt.SizeAllCursor)

        self.old_position = event.globalPos()
        return self.old_position

    def mouseMoveEvent(self, event):
        try:
            omega = QPoint(event.globalPos() - self.old_position)

            if self._custom_title_bar == False and self._movable == True and self._frame == False:
                self.move(self.x() + omega.x(), self.y() + omega.y())
                self.old_position = event.globalPos()
            else:
                return omega
        except:
            pass
        
    def mouseReleaseEvent(self, event: QMouseEvent):
        window.setCursor(Qt.ArrowCursor)

    # Title bar management
    def WindowTitlebar(self, title, icon, widgets, alignment, backgound_color,  text_color, default):
        """
        Manages the custom title bar for the window.
        """
        current_window_style = window.style().name().lower()
        title_buttons = []

        # Initialize controls based on window style
        if default == False:
            if current_window_style == SYSTEM_PLATFORM_FUSION:
                title_buttons = FUSION_CONTROLS()
            elif current_window_style == windows or windows in current_window_style:
                title_buttons = WINDOWS_CONTROLS()
        else:
            # Default system control buttons
            title_buttons = CLERA_CONTROLS()

        [
            CONTROL_MINIMIZED, 
            CONTROL_RESTORE, 
            CONTROL_MAXIMIZED, 
            CONTROL_CLOSE,
            CLOSE_EMPTY,
            MAXIMIZE_EMPTY,
            MINIMIZE_EMPTY,
            RESTORE_EMPTY
        ] = title_buttons

        if self._custom_title_bar == False and self._frame == False:
            if alignment != None:
                if alignment.lower() == 'center':
                    align = 'center'
                else:
                    align = None
            else:
                align = None

            def window_state():
                state = str(self.windowState())
                state = state.split('.')
                state = state[1].lower()
                return state

            def control_action(key: str = ''):
                state = window_state()
                max = GET(MAXIMIZE_BUTTON_ID)

                if key == 'max':
                    if state == 'windowmaximized':
                        self.setWindowState(Qt.WindowNoState)
                    elif state == 'windownostate':
                        max.icon(RESTORE_EMPTY)
                        self.setWindowState(Qt.WindowMaximized)
                elif key == 'min':
                    # Change Minimize Icon To Empty... [BUG]
                    self.setWindowState(Qt.WindowMinimized)
                

            if icon != None:
                titlebar_icon = Image(icon, id=ICON_IMAGE_ID, size=20)
            else:
                titlebar_icon = empty()

            # valid_styles = [SYSTEM_PLATFORM_FUSION, SYSTEM_PLATFORM_WINDOWS, 'windowsvista']
            def icon_controls(slot_one, slot_two, slot_three, size):
                def change_appearance(id, icon):
                    GET(id).icon(icon)   
                
                def change_appearance_maximize(status: str):
                    state = window_state()
                    max = GET(MAXIMIZE_BUTTON_ID)

                    if status == 'leave':
                        if state == 'windowmaximized':
                            max.icon(RESTORE_EMPTY)
                        elif state == 'windownostate':
                            max.icon(MAXIMIZE_EMPTY)
                    elif status == 'enter':
                        if state == 'windowmaximized':
                            max.icon(CONTROL_RESTORE)
                        elif state == 'windownostate':
                            max.icon(CONTROL_MAXIMIZED)
                        
                close_switch = (
                    call(change_appearance, CLOSE_BUTTON_ID, CONTROL_CLOSE),
                    call(change_appearance, CLOSE_BUTTON_ID, CLOSE_EMPTY)
                )

                minimize_switch = (
                    call(change_appearance, MINIMIZE_BUTTON_ID, CONTROL_MINIMIZED),
                    call(change_appearance, MINIMIZE_BUTTON_ID, MINIMIZE_EMPTY)
                )
                
                maximize_switch = (
                    call(change_appearance_maximize, 'enter'),
                    call(change_appearance_maximize, 'leave')
                )
                
                
                control_buttons = [
                    Button(icon=MAXIMIZE_EMPTY, id=MAXIMIZE_BUTTON_ID,
                        func=call(control_action, 'max'), focus=False, icon_size=size, hover=maximize_switch),
                    Button(icon=MINIMIZE_EMPTY, id=MINIMIZE_BUTTON_ID,
                        func=call(control_action, 'min'), focus=False, icon_size=size, hover=minimize_switch),
                    Button(icon=CLOSE_EMPTY, id=CLOSE_BUTTON_ID,
                        func=Window.quit, focus=False, icon_size=size, hover=close_switch)
                ]

                if align != center:
                    if widgets == None:
                        policy = expand
                    else:
                        policy = fixed
                else:
                    policy = expand

                items = [
                    titlebar_icon,
                    Text(title, id=TITLE_TEXT_ID,
                        sizepolicy=(policy, fixed), alignment=align),
                    control_buttons[slot_one],
                    control_buttons[slot_two],
                    control_buttons[slot_three]
                    
                ]

                return items

            if default == False:
                if current_window_style == SYSTEM_PLATFORM_FUSION:
                    title_items = icon_controls(1, 0, 2, 18) 
                else:
                    title_items = icon_controls(1, 0, 2, 40) 
            else:
               title_items = icon_controls(0, 1, 2, 18) 


            # Initialize titlebar
            container = INIT_WIDGET(
                '-clera_titlebar_container-', QToolBar('Container'))
            titlebar = INIT_WIDGET('titlebar', QToolBar('Titlebar'))

            class init_titlebar(QWidget):
                def __init__(self):
                    super().__init__()
                    cs_layout = QHBoxLayout()
                    self.setLayout(cs_layout)
                    cs_layout.setContentsMargins(0, 0, 0, 0)
                    cs_layout.addWidget(titlebar)
                    window.setCentralWidget(self)

                def mousePressEvent(self, event: QMouseEvent):
                    self.old_position = window.mousePressEvent(event)
                    window.setCursor(Qt.SizeAllCursor)

                def mouseMoveEvent(self, event: QMouseEvent):
                    try:
                        omega = window.mouseMoveEvent(event)
                        window.move(window.x() + omega.x(), window.y() + omega.y())
                        self.old_position = window.mousePressEvent(event)
                    except:
                        pass

                def mouseReleaseEvent(self, event: QMouseEvent):
                    window.setCursor(Qt.ArrowCursor)

                def mouseDoubleClickEvent(self, event: QMouseEvent):
                    if window._fixed_size == (None, None):
                        control_action('max')

            container_socket = init_titlebar()
            container_socket.setContentsMargins(0, 0, 0, 0)

            container.addWidget(container_socket)
            container.setStyleSheet('margin: 0; padding: 0; border: 0px;')

            container.setMovable(False)
            titlebar.setMovable(False)

            self.addToolBar(Qt.TopToolBarArea, container)

            container.toggleViewAction().setVisible(False)
            titlebar.toggleViewAction().setVisible(False)

            titlebar.setIconSize(QSize(20, 20))

            # self.addToolBar(Qt.TopToolBarArea, titlebar)

            self.addToolBarBreak()

            if widgets != None:
                titlebar_widget = []

                def init_titlebar_items(start, stop):
                    for _index in range(start, stop):
                        titlebar_widget.append(title_items[_index])

                if align == center:
                    for widget in widgets:
                        # titlebar_widget.append(widget)
                        append_items(titlebar_widget, widget)
                    else:
                        init_titlebar_items(0, 5)             
                else:
                    init_titlebar_items(0, 2)
                    for widget in widgets:
                        # titlebar_widget.append(widget)
                        append_items(titlebar_widget, widget)
                    else:
                        init_titlebar_items(2, 5)
                        # print(titlebar_widget)

                title_items = titlebar_widget

            for item in title_items:
                if type(item) != type(list()):
                    widget_type, widget_items = check_func(item)
                    LayItOut(titlebar, widget_type, widget_items)
                    # titlebar.addWidget(widget)

            titlebar.setOrientation(Qt.Horizontal)

            # button_style_query = button_style.lower()

            # button_styles = {
            #     circle: CONTROL_BUTTON_CIRCLE,
            #     square: CONTROL_BUTTON_SQUARE 
            # }

            # try:
            #     control_button_style = button_styles[button_style_query]
            # except:
            #     ...
            #     # raise an error

            title = GET(TITLE_TEXT_ID)
            minimize = GET(MINIMIZE_BUTTON_ID)
            maximize = GET(MAXIMIZE_BUTTON_ID)
            close = GET(CLOSE_BUTTON_ID)

            def init_title_icon(icon, value: str = 'left'):
                if icon != None:
                    icon = GET(ICON_IMAGE_ID)
                    icon.style(f'margin-{value}: 10px;')

            init_title_icon(icon)

            titlebar_padding = "7px"

            if default == False:
                if current_window_style == SYSTEM_PLATFORM_FUSION:
                    fusion_style(minimize, maximize, close)
                elif current_window_style == SYSTEM_PLATFORM_WINDOWS or windows in current_window_style:
                    windows_style(minimize, maximize, close)
                    titlebar_padding = 0
                else:
                    ...
            else:
                clera_style(minimize, maximize, close)

            title.style(
                f'color: {text_color}; margin: 0 4px;')
            container.setStyleSheet(
                f'border-bottom: 0px; background: {backgound_color}; max-height: 30px; color: {text_color}; padding: {titlebar_padding} 0')

            self._custom_title_bar = True


# ------------------------------------------------------------------------#

###########################################################################
############################## WINDOWS CLASS ##############################
###########################################################################

# ------------------------------------------------------------------------#


class Window:
    def __init__(self, title: str = DEFAULT_WINDOW_TITLE, icon: str = DEFAULT_WINDOW_ICON, size: tuple = DEFAULT_WINDOW_SIZE,
                 geometry: tuple = DEFAULT_WINDOW_GEOMETRY, style: str = DEFAULT_WINDOW_STYLE, fixed_size: tuple = DEFAULT_WINDOW_FIXED_SIZE, frame: bool = True,
                 movable: bool = False, top: bool = False, spacing: int = 5, margin: tuple = (5, 5, 5, 5), move: tuple = (None, None), tool: bool = False, cursor: bool = True):
        '''
        Initializes the window with various configuration parameters like title, icon, size, and more.
        These properties are later used to create the actual window in the `MainWindow` class (assigned to `window`).
        '''

        global window

        self.window_title = title
        self.window_icon = icon
        self.window_size = size
        self.window_fixed_size = fixed_size
        self.window_geometry = geometry
        self.window_style = style
        self.frame = frame
        self.movable = movable
        self.top = top
        self.spacing = spacing
        self.content_margin = margin
        self.move = move
        self.tool = tool
        self.cursor = cursor

        # Create an instance of MainWindow, passing the parameters to configure it
        window = MainWindow(self.window_title, self.window_icon,
                            self.window_size, self.window_fixed_size, self.window_geometry, self.window_style, self.frame,
                            self.movable, self.top, self.spacing, self.content_margin, self.move, self.tool, self.cursor)
    
    def __register_cursor__(self):
        '''Registers the cursor for the window by overriding the default cursor with the specified cursor type.'''
        app.setOverrideCursor(window.cursor())
        app.changeOverrideCursor(window.cursor())

    def run(self, css: None = None):
        '''Starts the application and shows the window. Optionally applies CSS styling and initializes linked files.'''
        # if self.splashscreen != None:
        #     self.init_splashscreen()

        window.show()
        # self.__register_cursor__() # block cursor

        # Apply CSS styles if provided
        if css:
            init_window_css(css)

        # Initialize linked files if any
        if LINK_ITEMS_INCLUDED:
            init_linked_files()

        state = self.window_state()
       
        try:
            max = GET(MAXIMIZE_BUTTON_ID)

            if state == 'windowmaximized':
                max.value(CONTROL_RESTORE)

            if window._query_fixed_size:
                max.delete()

            if window._custom_title_bar:
                menu_bar = window.menuBar()
                menu_bar.clear()
        except Exception:
            pass

        # Start the application event loop
        app.exec()
        self.quit()

    def close(self):
        '''Closes the window by quitting the application.'''
        self.quit()

    def quit(self):
        '''Safely terminates the app.'''
        app.quit()

    def update(self, remove_id, widget):
        '''
        Replaces an existing widget in the layout with a new one.

        :param remove_id: The ID of the widget to be removed.
        :param widget: The new widget to replace the old one.
        '''

        try:
            replace_widget = WIDGET_ID_SAFE[remove_id]
            widget_type, widget_items = check_func(widget)

            if layout.indexOf(replace_widget) != -1:
                LayItOut([layout, replace_widget, 'replaceWidget'], widget_type, widget_items)
                layout.removeWidget(replace_widget)
                replace_widget.deleteLater()
        except Exception:
            pass

    def normal(self):
        '''Resets the window state to normal (not maximized or minimized).'''
        window.setWindowState(Qt.WindowNoState)

    def minimize(self):
        '''Minimizes the window.'''
        window.setWindowState(Qt.WindowMinimized)

    def maximize(self):
        '''Maximizes the window.'''
        window.setWindowState(Qt.WindowMaximized)
    
    def window_state(self):
        '''Checks and returns the window state (e.g., maximized, minimized).'''
        state = str(window.windowState()).split('.')[1].lower()
        return state
    
    def details(self):
        '''
        Returns detailed information about the window, including its position, size, style, and screen size.

        :return: A dictionary with the window's details.
        '''
        screen = window.screen().virtualSize()
        title = window.windowTitle()
        size = window.size()

        if len(title) == 0:
            title = None

        return {
            'position': window.geometry().getCoords()[:2],
            'screen': (screen.width(), screen.height()),
            'style': window.style().name(),
            'size': (size.width(), size.height()),
            'title': title,
            'system_styles': QStyleFactory().keys(),
            'style_reference': FILE_LINKS
        }


    def title(self, value: any = None):
        '''Sets or returns the window title.'''
        if value != None:
            window.setWindowTitle(value)

        return window.windowTitle()

        
    def resize(self, size: tuple, fixed: bool=False):
        '''
        Resizes the window to the specified size. Optionally, makes the window size fixed.

        :param size: The new size as a tuple (width, height).
        :param fixed: If True, the window size is fixed and cannot be resized by the user.
        '''
        width, height = size

        if width is not None and height is not None:
            window_size = QSize(int(width), int(height))
            if fixed:
                window.setFixedSize(window_size)
            else:
                window.resize(window_size)

    def screenshot(self, filename: str):
        '''Takes a screenshot of the window and saves it to the specified file.'''
        details = self.details()
        x, y = details['position']
        w, h = details['size']
        
        if window.isHidden() == False:
            window.screen().grabWindow(x=x, y=y, w=w, h=h).save(filename)

    def _cursor(self, hide: bool = False):
        '''Hides or shows the cursor based on the `hide` flag.'''
        if hide == True:
            window.setCursor(Qt.BlankCursor)
        elif hide == False:
            window.unsetCursor()

        self.__register_cursor__()

    def _move(self, position: tuple = (None, None), top: bool = None):
        '''Moves the window to the specified position (x, y) and optionally keeps it on top.'''
        if position != (None, None):
            window.move(*position)

        if top is not None:
            if top:
                window.setWindowFlag(Qt.WindowStaysOnTopHint)
            else:
                window.setWindowFlags(window.windowFlags() & ~Qt.WindowStaysOnTopHint)

            window.show()


    # def init_splashscreen(self):
    #     splash_screen = QSplashScreen(QPixmap(init_image(self.splashscreen)), Qt.WindowStaysOnTopHint)
    #     splash_screen.show()
        
    #     if self.splash_function != None:
    #     # Perform a function during splash screen
    #         self.splash_function() 
        
    #     splash_screen.finish(DEFAULT_WINDOW_LAYOUT)
    
    def style(self, css: None=None, reset: bool = False):
        '''Applies CSS styles to the window, optionally resetting the current styles.'''
        set_style(window, css, reset)

    # def _tool(self):
    #     window.setWindowFlag(~Qt.Tool)


    # def frames(self, value):
    #     # if value != window.frame:

    #     if value == False:
    #         window.setWindowFlag(Qt.FramelessWindowHint)
    #     elif value == True:
    #         window.setWindowFlag(~Qt.FramelessWindowHint)

    #     print(window.windowFlags())
    #     window.show()


# ------------------------------------------------------------------------#

###########################################################################
############################## CORE HANDLERS ##############################
###########################################################################

# ------------------------------------------------------------------------#


def handle_group(widgets, grouplayout, strict, parent):
    if widgets != None:
        if grouplayout.lower() in DEFAULT_HORIZONTAL_TYPES:
            group_element_layout = QHBoxLayout()
        elif grouplayout.lower() in DEFAULT_VERTICAL_TYPES:
            group_element_layout = QVBoxLayout()
        else:
            raise ValueError(grouplayout)

        parent.addLayout(group_element_layout)

        # Create a QButtonGroup once for the layout
        groupcontent = QButtonGroup(group_element_layout)
        
        # Use a set to track added widgets for faster membership check
        
        for items in widgets:
            WidgetType, items = check_func(items)
            
            # Only add the widget if it's not already added to avoid redundancy
            groupcontent.addButton(LayItOut(group_element_layout, WidgetType, items))
        
        groupcontent.setExclusive(strict)


def init_column(hbox, vbox, property):
    '''
    Optimized column layout initialization to avoid deep recursion.
    
    - Uses an iterative approach to handle column layouts more efficiently.
    '''
    hbox.addLayout(vbox)  # Add the main vertical box layout to horizontal layout
    
    # Stack to hold properties to process, replacing recursion
    layout_stack = [(vbox, property[1])]  # Initial properties to process
    
    while layout_stack:
        parent_layout, current_properties = layout_stack.pop()
        
        for properties in current_properties:
            col_hbox = QHBoxLayout()  # Create a horizontal layout for this column
            parent_layout.addLayout(col_hbox)
            
            for property in properties:
                WidgetType, property = check_func(property)
                
                # If it's not a column, add it to the current layout
                if WidgetType != ELEM_TYPE_COLUMN:
                    LayItOut(col_hbox, WidgetType, property)
                else:
                    # If it is a column, add the vertical layout to the stack to process
                    layout_stack.append((col_hbox, property[1]))  # Add nested columns to the stack


def init_menubar(menu_items):
    if menu_items:  # Check if menu_items is not empty
        for items in menu_items:
            # Use tuple unpacking to simplify the menu item processing
            if len(items) == 2:
                name, actions = items
            else:
                name = items[0] if isinstance(items[0], str) else None
                actions = items[0] if isinstance(items[0], list) else None
            
            # Add the menu item directly
            window.WindowMenubar(name, actions)


# ------------------------------------------------------------------------#

###########################################################################
############################# LAYOUT PROCESSOR ############################
###########################################################################

# ------------------------------------------------------------------------#


def Box(widgets, margin: tuple | int = None, spacing: int = None, _parent: any = None):
    containers = {ELEM_TYPE_COLUMN, ELEM_TYPE_FIELDSET, ELEM_TYPE_GROUP}  # Set for O(1) membership check
    box_layout = QVBoxLayout()

    # Use provided parent or default if not specified
    box_widget = _parent if _parent else QWidget()

    # If the parent is not provided, check for the default layout
    if not _parent and get_parent(BOX_IDENTIFIER):
        box_widget = DEFAULT_WINDOW_LAYOUT
        box_layout = layout
        window.setCentralWidget(box_widget)

    box_widget.setLayout(box_layout)

    for items in widgets:
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        box_layout.addLayout(hbox)

        for item in items:
            widget_type, widget_items = check_func(item)

            # Directly process widgets that are not containers
            if widget_type not in containers:
                LayItOut(hbox, widget_type, widget_items)
            elif widget_type == ELEM_TYPE_COLUMN:
                init_column(hbox, vbox, widget_items)
            elif widget_type == ELEM_TYPE_FIELDSET:
                # Use dicts to avoid redundant checks
                Notrequired, name, fieldset_widgets, id, fieldset_layout = widget_items
                if fieldset_widgets is not None:
                    groupbox = INIT_WIDGET(id, QGroupBox(name))
                    hbox.addWidget(groupbox)

                    groupbox_layout = QVBoxLayout() if fieldset_layout.lower() in DEFAULT_VERTICAL_TYPES else QHBoxLayout()
                    groupbox.setLayout(groupbox_layout)

                    for items in fieldset_widgets:
                        widget_type, widget_items = check_func(items)
                        if widget_type == ELEM_TYPE_GROUP:
                            handle_group(widget_items[1], widget_items[2], widget_items[3], groupbox_layout)  # Avoid unnecessary unpacking
                        else:
                            LayItOut(groupbox_layout, widget_type, widget_items)
            elif widget_type == ELEM_TYPE_GROUP:
                handle_group(widget_items[1], widget_items[2], widget_items[3], box_layout)

    # Apply margin and spacing in a batch
    is_margin = init_content_margin(box_layout, margin)
    init_spacing(box_layout, spacing)

    return [box_widget, box_layout, is_margin]


def Grid(widgets, margin: tuple | int=None, spacing: int=None):
    grid_widget = QWidget()
    grid = QGridLayout()

    grid_layout = QVBoxLayout()

    if get_parent(GRID_IDENTIFIER):
        grid_widget = DEFAULT_WINDOW_LAYOUT
        grid_layout = layout

        window.setCentralWidget(grid_widget)
        grid_layout.addLayout(grid)

    grid_widget.setLayout(grid)

    grid_pos_x = 0
    grid_pos_y = 0

    for items in widgets:
        for item in items:
            widget_type, widget_items = check_func(item)
            LayItOut(grid, widget_type, widget_items, grid_pos_x, grid_pos_y)
            grid_pos_y += 1
        grid_pos_y = 0
        grid_pos_x += 1

    is_margin = init_content_margin(grid_layout, margin)
    init_spacing(grid_layout, spacing)
    return [grid_widget, grid_layout, is_margin]


class ScrollArea:
    def __init__(self, widgets: None = None, id: None = None, contain: bool = True):
        '''
        ScrollArea class to create a scrollable area for widgets.
        '''

        elem_type = ELEM_TYPE_SCROLL_AREA
        self.scroll_widget = QWidget()

        # Only set central widget if it’s required
        if  get_parent(ELEM_TYPE_TAB) and get_parent(SCROLL_AREA_IDENTIFIER):
            # layout.addWidget(scroll_area)
            window.setCentralWidget(self.scroll_widget)

        scroll_layout = QVBoxLayout()

        scroll_area = INIT_WIDGET(id, QScrollArea())
        scroll_layout.addWidget(scroll_area)
        self.scroll_widget.setLayout(scroll_layout)
        
        if widgets != None:
            widgets = widgets[0]
            scroll_area.setWidget(widgets)

        scroll_area.setAlignment(Qt.AlignBottom)
        scroll_area.setWidgetResizable(contain)

    def __repr__(self):
        return [self.scroll_widget]

    def __call__(self):
        return [self.scroll_widget]
        

# Aliasing the ScrollArea class as 'scrollarea' for potential readability or legacy reasons.
class scrollarea(ScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Stack:
    def __init__(self, widgets: None = None, id: None = None, current_changed: None = None, widget_removed: None = None):
        '''
        Stack Widget to display multiple widgets, switching between them (like a tab view).

        :param widgets: List of widgets or widget data to be added to the stack.
        :param id: ID of the stacked widget.
        :param current_changed: Callback function when the current widget in the stack changes.
        :param widget_removed: Callback function when a widget is removed from the stack.
        '''

        # Create the stacked widget container.
        self.stacked_widget = INIT_WIDGET(id, QStackedWidget())
        
        layout_default = QVBoxLayout()
        stack_default = QWidget()

        # Function to initialize and add widgets to the stack.
        def init_stack(widget):
            '''
            Initialize each widget that will be added to the stack.
            :param widget_data: A tuple containing the widget and layout configuration.
            '''
            stack_layout = widget[1]
            is_margin = widget[2]
            
            try:
                widget = widget[0]
            except:
                widget = widget()[0]
            
            if is_margin != True:
                init_content_margin(stack_layout, 0)
            self.stacked_widget.addWidget(widget)

        if widgets != None:
            if process_request(ELEM_TYPE_SCROLL_AREA, str(type(widgets)).lower()):
                widgets = widgets()
            
            if type(widgets[0]) == sample_list:
                for widget in widgets:
                    init_stack(widget)    
            else:
                init_stack(widgets)    
        
        # Set up the layout for the stacked widget
        layout_default.addWidget(self.stacked_widget)
        stack_default.setLayout(layout_default)

        self.stacked_widget.currentChanged.connect(current_changed)
        self.stacked_widget.widgetRemoved.connect(widget_removed)
        
        layout_default.setContentsMargins(0, 0, 0, 0)
        window.setCentralWidget(stack_default)

    def set(self, index):
        '''
        Set the currently displayed widget by index.
        :param index: The index of the widget to display.
        '''
        self.stacked_widget.setCurrentIndex(index)

    def show(self, widget):
        '''
        Show a specific widget in the stack.
        :param widget: A tuple (widget, layout) to display.
        '''
        widget, layout = widget
        self.stacked_widget.setCurrentWidget(widget)


# Alias for backward compatibility or easier readability.
class stack(Stack):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# ------------------------------------------------------------------------#

###########################################################################
############################## CORE ELEMENTS ##############################
###########################################################################

# ------------------------------------------------------------------------#


class Menubar:
    def __init__(self, menu_items: list | None = None):
        '''
        Menu Bar to create a menu system for the window.

        :param menu_items: A list of menu items to populate the menu bar. Defaults to None.
        '''

        # Initialize the menu bar with the provided items.
        init_menubar(menu_items)


# Alias for Menubar for backward compatibility or readability.
class menubar(Menubar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Titlebar:
    def __init__(self, title: str = path.basename(sys.argv[0]), icon: str = None, widgets: list = None, alignment: None = None, text_color: str = 'white',
                 background_color: str = 'rgb(32, 32, 32)', default: bool = False):
        '''
        Titlebar to display a title bar for the window.

        :param title: Title text for the window. Defaults to the basename of the script.
        :param icon: Icon for the window (optional).
        :param widgets: List of widgets to display on the title bar (optional).
        :param alignment: Alignment of the title text (optional).
        :param text_color: Color for the title text (default is white).
        :param background_color: Background color for the title bar (default is dark gray).
        :param default: Boolean to set a default title bar (optional).
        '''
        # Initialize the title bar with the specified parameters.
        window.WindowTitlebar(title, icon, widgets, alignment,
                              background_color, text_color, default)


# Alias for Titlebar for backward compatibility or readability.
class titlebar(Titlebar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Toolbar:
    def __init__(self, name, tool_items: list | None = None, movable: bool = False,
                 position: str = top, id: None = None, iconsize: tuple = (None, None),
                 border: bool = True, orientation: str = SET_HORIZONTAL, newline: bool = False, toggle_view: bool = True):
        '''
        Toolbar element to create a toolbar with tools for the window.

        :param name: Name of the toolbar.
        :param tool_items: List of items (tools) to add to the toolbar (optional).
        :param movable: Boolean to specify if the toolbar is movable.
        :param position: Position of the toolbar (default is top).
        :param id: ID for the toolbar (optional).
        :param iconsize: Tuple to define the icon size (optional).
        :param border: Boolean to define if the toolbar has a border (default is True).
        :param orientation: Orientation of the toolbar (default is horizontal).
        :param newline: Boolean to specify whether the toolbar should create a new line (optional).
        :param toggle_view: Boolean to toggle the toolbar visibility (optional).
        '''

        # Initialize the toolbar with the specified parameters.
        window.WindowToolbar(name,  tool_items, movable,  position,  id,  iconsize,  border,
                             orientation, newline, toggle_view)


# Alias for Toolbar for backward compatibility or readability.
class toolbar(Toolbar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Statusbar:
    def __init__(self):
        '''
        Statusbar to show a status message area at the bottom of the window.
        Initializes the status bar.
        '''
        window.init_status()

    def message(self, text: str = '', time: None = None):
        '''
        Display a temporary status message in the status bar.

        :param text: The message text to be displayed.
        :param time: Time in seconds for which the message will be displayed (optional).
        '''
        window.SHOW_STATUSBAR_MESSAGE(text, time)

    def clear(self):
        '''
        Clear the current status message in the status bar.
        '''
        window.CLEAR_STATUSBAR_MESSAGE()

    def add(self, widget, type: str = SET_NORMAL):
        '''
        Add a widget to the status bar.

        :param widget: The widget to be added to the status bar.
        :param type: Type of widget (normal or static) to be added.
        '''
        type = type.upper()
        widget_type, widget_items = check_func(widget)
        
        if type == SET_NORMAL:
            window.ADD_NORMAL_WIDGET(widget_type, widget_items)
        elif type == SET_STATIC:
            window.ADD_PERMANENT_WIDGET(widget_type, widget_items)
        else:
            raise ValueError(f'"{type}" is an invalid type value')

    def remove(self, id):
        '''
        Remove a widget from the status bar.

        :param id: The ID of the widget to be removed.
        '''
        window.REMOVE_STATUSBAR_WIDGET(id)


class statusbar(Statusbar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class File(QFileDialog):
    def __init__(self):
        ...

    def open(self: None = QFileDialog, caption: str = None, filter: str = '(All Files: *)', directory: str = None, type: str = DEFAULT_OPEN_FILE_TYPE):
        '''
        Open File Dialog

        :param caption: The caption for the dialog.
        :param filter: Filter for file types (default is all files).
        :param directory: Directory to start the dialog from.
        :param file_type: Type of open dialog (single or multiple).
        :return: The selected file(s).
        '''
        open_type = type.lower()

        if open_type == OPEN_FILE_TYPE_SINGLE:
            return self.getOpenFileName(
                caption=caption,
                dir=directory,
                filter=get_filter(filter))

            # file_names = file[0]
        elif open_type == OPEN_FILE_TYPE_MULTI:
            return self.getOpenFileNames(
                caption=caption,
                dir=directory,
                filter=get_filter(filter))
        else:
            raise ValueError(f'Invalid file_type "{type}"')


    def save(self: None = QFileDialog, filter: str = '(All Files: *)'):
        '''
        Save File Dialog

        :param filter: Filter for file types (default is all files).
        :return: The selected file.
        '''

        return self.getSaveFileName(filter=get_filter(filter))


class file(File):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Folder(QFileDialog):
    def __init__(self, caption: str = None, directory: str = None):
        '''
        Folder Dialog to select a directory.

        :param caption: The caption for the dialog.
        :param directory: Directory to start the dialog from.
        '''
        
        self.folder = self.getExistingDirectory(caption=caption,
                                                dir=directory)

    def __repr__(self):
        '''
        Return the selected folder path.
        '''
        return self.folder


class folder(Folder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Popup:
    def __init__(self, title: None = None, widgets: None = None, id: None = None, size: tuple = (None, None), fixed_size: tuple = (None, None), move: tuple = (None, None),
                 modal: bool = False, frame: bool = True, lock: bool = False, center: bool = True, margin: tuple | int = None, spacing: int = None):
        '''
        Popup Window

        :param title: Title for the popup window.
        :param widgets: Widgets to be added to the popup.
        :param id: ID for the popup.
        :param size: Size of the popup (width, height).
        :param fixed_size: Fixed size for the popup (optional).
        :param move: Position to move the popup.
        :param modal: Whether the popup is modal or not.
        :param frame: Whether the popup has a frame.
        :param lock: Lock the popup to the main window.
        :param center: Whether to center the popup on the screen.
        :param margin: Margin inside the popup.
        :param spacing: Spacing between widgets in the popup.
        '''

        parent = DEFAULT_WINDOW_LAYOUT if lock else None
        self.popup = INIT_WIDGET(id, QDialog(parent))

        elem_type = ELEM_TYPE_POPUP

        self.popup.setWindowTitle(title)

        if widgets:
            Box(widgets, margin, spacing, self.popup)

        self.popup.setModal(modal)

        width, height = size
        if width != None and height != None:
            self.popup.resize(int(width), int(height))
        
        fixed_width, fixed_height = fixed_size
        if fixed_width != None and fixed_height != None:
            self.popup.setFixedSize(QSize(int(fixed_width), int(fixed_height)))

        
        def center_self():
            '''Centers the popup window on the screen'''
            screen_center = window.geometry().center()
            popup_size = self.popup.size()
            
            x = screen_center.x() - popup_size.width() // 2
            y = screen_center.y() - popup_size.height() // 2
            
            self.popup.move(x, y)

        position_x, position_y = move
        if position_x != None and position_y != None:
            self.popup.move(position_x, position_y)


        if frame == False:
            self.popup.setWindowFlag(Qt.FramelessWindowHint)

        # Decide on modal behavior
        if modal:
            self.popup.show()  # Shows window if modal
        else:
            self.popup.exec()  # Executes dialog in non-modal mode


        position_x, position_y = move
        if position_x != None and position_y != None:
            self.popup.move(position_x, position_y)
        else:
            if center == True:
                center_self()


        self.rtn = [elem_type, id, self.popup]

    def __call__(self):
        return self.rtn

    def result(self):
        '''Returns the result of the popup interaction'''
        return self.popup.result()

    def close(self):
        '''Closes the popup window'''
        self.popup.close()
    

class popup(Popup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ColorPicker:
    def __init__(self, title: None = None, id: None = None, modal: bool = False, 
                 frame: bool = True, lock: bool = False, color_selected: None = None, 
                 native: bool = True, current: str | None = None):
        '''
        Popup window for selecting a color.
        
        :param title: Title of the popup.
        :param id: Identifier for the popup.
        :param modal: Whether the popup is modal or not.
        :param frame: Whether the popup has a frame (default is True).
        :param lock: If True, locks the popup to the main window (default is False).
        :param color_selected: Callback function when a color is selected.
        :param native: Whether to use native dialog (default is True).
        :param current: The current color, which can be a string (e.g., 'rgb(255, 0, 0)').
        '''

        parent = DEFAULT_WINDOW_LAYOUT if lock else None
        elem_type = ELEM_TYPE_POPUP

        popup = INIT_WIDGET(id, QColorDialog(parent))
        self.popup = popup

        popup.setWindowTitle(title or "Color Picker")
        popup.setModal(modal)

        # popup.resize(200, 120)

        if not frame:
            popup.setWindowFlag(Qt.FramelessWindowHint)

        if not native:
            popup.setOption(QColorDialog.DontUseNativeDialog)
        
        popup.setOption(QColorDialog.ShowAlphaChannel)
        popup.colorSelected.connect(color_selected)

        if popup.isModal:
            popup.show()
        else:
            popup.exec()

        def get_rgb_value(mode, current):
            current = current.removeprefix(f'{mode}(').removesuffix(')')
            current = current.split(',')

            current = [int(value) for value in current]

            if len(current) == 3:
                r, g, b = current
                current = QColor(r, g, b)
            else:
                r, g, b, a = current
                current = QColor(r, g, b, a)
            
            popup.setCurrentColor(current)


        if current.startswith('rgba'):
            get_rgb_value('rgba', current)
        elif current.startswith('rgb'):
            get_rgb_value('rgb', current)
        else:
            popup.setCurrentColor(current)
            
        self.rtn = [elem_type, id, popup]

    def __call__(self):
        return self.rtn


class colorpicker(ColorPicker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TabWidget:
    def __init__(self, tabs: None = None, id: None = None, movable: bool = False, closable: bool = False,
                 close_requested: None = None, clicked: None = None, current_changed: None = None):
        '''
        Initializes a tab widget with optional tabs, closable/movable functionality, and event handlers.
        
        :param tabs: List of tabs to be added to the tab widget (default is None).
        :param id: Identifier for the widget (default is None).
        :param movable: If True, allows the tabs to be moved (default is False).
        :param closable: If True, allows tabs to be closed (default is False).
        :param close_requested: Function to handle close request events (default is None).
        :param clicked: Function to handle tab bar click events (default is None).
        :param current_changed: Function to handle tab change events (default is None).
        '''

        elem_type = ELEM_TYPE_TAB
        tab_widget = INIT_WIDGET(id, QTabWidget())

        if tabs != None:
            add_tabs(tab_widget, tabs)

        tab_widget.setMovable(movable)
        tab_widget.setTabsClosable(closable)

        tab_widget.tabCloseRequested.connect(close_requested)
        tab_widget.tabBarClicked.connect(clicked)
        tab_widget.currentChanged.connect(current_changed)

        layout.addWidget(tab_widget)
        window.setCentralWidget(DEFAULT_WINDOW_LAYOUT)

        self.rtn = [elem_type, id]

    def __call__(self):
        return self.rtn


class tabwidget(TabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Highlighter(QSyntaxHighlighter):
    def __init__(self, mapping, parent=None):
        '''
        Applies syntax highlighting based on the provided patterns and formats.
        
        :param mapping: A dictionary of patterns to highlight and the corresponding format.
        :param parent: The parent widget for the highlighter (default is None).
        '''
        super().__init__(parent)
        self.mapping = mapping

    def highlightBlock(self, text):
        '''
        Highlights the text in the block according to the provided patterns and formats.

        :param text: The text in the document block to be highlighted.
        '''
        for pattern, format in self.mapping.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end-start, format)


class Highlight:
    def __init__(self, widget_id, synthax, id: None = None):
        '''
        Initializes syntax highlighting for a specific widget using defined patterns.
        
        :param widget_id: The ID of the widget to apply the syntax highlighting to.
        :param synthax: A dictionary of syntax patterns to highlight.
        :param id: The ID for the highlighter widget (default is None).
        '''
        mapping = {}

        # Prepare the mapping with syntax patterns and formats
        for pattern, format in synthax.items():
            _format = INIT_FORMAT(format)
            mapping[rf'{pattern}'] = _format
        
        self.widget = WIDGET_ID_SAFE[widget_id]
        self.synthax = INIT_WIDGET(id, Highlighter(mapping))
        self.synthax.setDocument(self.widget.document())
        self.synthax.document()


def thread(target, wait: bool = False, *args, **kwargs):
    '''
    Runs a target function in a separate thread, optionally waiting for it to finish.
    
    :param target: The function to execute in the thread.
    :param wait: If True, waits for the thread to finish before returning (default is False).
    :param args: Arguments to pass to the target function.
    :param kwargs: Keyword arguments to pass to the target function.
    '''
    if wait == True:
        return lambda: clera_multi_threading.start(target, *args, **kwargs)
    elif wait == False:
        clera_multi_threading.start(target, *args, **kwargs)


def screen():
    '''
    Returns the current screen’s width and height.
    
    :return: A tuple containing the width and height of the screen.
    '''
    
    try:
        core = window
    except:
        core = DEFAULT_WINDOW_LAYOUT

    size = core.screen().virtualSize()

    return (size.width(), size.height())


def screenshot(filename: str):
    '''
    Captures a screenshot of the current window and saves it to the specified file.
    
    :param filename: The file path where the screenshot will be saved.
    '''
    try:
        core = window
    except:
        core = DEFAULT_WINDOW_LAYOUT

    screenshot = core.screen().grabWindow()
    screenshot.save(filename)


def shortcut(keys: str, func: None = None):
    '''
    Binds a keyboard shortcut to a specified function.
    
    :param keys: The keys for the shortcut (e.g., "Ctrl+S").
    :param func: The function to be executed when the shortcut is triggered (default is None).
    '''
    # Ensure that the keys are in a valid format (e.g., "Ctrl+S")
    if not isinstance(keys, str):
        raise ValueError("keys parameter must be a string, like 'Ctrl+S'.")

    _shortcut = QShortcut(keys, window)
    _shortcut.activated.connect(func)


class GET:
    def __init__(self, id):

        '''
        GET ELEMENT
        
        :param id:

        :method value:
        :method update:
        :method delete:
        :method append:
        :method html:
        :method insert_html:
        :method plain_text:
        :method alignment:
        :method is_default:
        :method is_readonly:
        :method style:
        :method is_checked:
        :method hidden:
        :method hide:
        :method diabled:
        :method disable:
        :method enable:
        :method is_hidden:
        :method is_disabled:
        :method select_all:
        :method copy:
        :method cut:
        :method undo:
        :method redo:
        :method paste:
        :method clear:
        :method add:
        :method remove:
        :method current:
        :method count:
        :method selected_items:
        :method set:
        :method index:
        :method reset:
        :method minimum:
        :method maximum:
        :method is_text_visible:
        :method reject:
        :method accept:
        :method focus:
        :method cursor:
        :method setcursor:
        :method icon:
        :method show:
        :method scrollbar:
        :method checked:
        '''
        self.id = id
        # Safely get the widget from the WIDGET_ID_SAFE dictionary
        self.widget = WIDGET_ID_SAFE.get(self.id)
        if self.widget is None:
            raise ValueError(f"Widget with ID {self.id} not found.")
        self.widget_type = str(type(self.widget))

    def __repr__(self):
        '''
        Return a string representation of the widget depending on its type.

        :return: A string representation of the widget's current state.
        '''
        
        allowed_types = [
            GET_ELEM_TYPE_PROGRESS_BAR, 
            GET_ELEM_TYPE_SLIDER, 
            GET_ELEM_TYPE_DIAL
        ]

        # Process request based on allowed types
        if process_request(allowed_types, self.widget_type):
            return str(self.widget.value())

        if process_request(GET_ELEM_TYPE_TEXTAREA, self.widget_type):
            return self.widget.toPlainText()

        if process_request(GET_ELEM_TYPE_COLOR_POPUP, self.widget_type):
            return str(self.widget.selectedColor().name(QColor.HexRgb))

        # Default text for other widget types
        return self.widget.text()

    def value(self, value: str | None = None):
        '''
        Set or get the value of the widget.

        :param value: The value to set for the widget (if None, returns the current value).
        :return: The current value of the widget (if no value is passed).
        '''
        allowed = [
            GET_ELEM_TYPE_PROGRESS_BAR,
            GET_ELEM_TYPE_SLIDER,
            GET_ELEM_TYPE_DIAL
        ]

        if process_request(allowed, self.widget_type):
            self.widget.setValue(int(value))
        else:
            self.widget.setText(str(value))

    def update(self, widget):
        '''
        Replace the current widget with a new widget.

        :param widget: The new widget to replace the current one.
        '''
        widget_type, widget_items = check_func(widget)

        try:
            layout.indexOf(self.widget)
            LayItOut([layout, self.widget, 'replaceWidget'],
                     widget_type, widget_items)
            layout.removeWidget(self.widget)
            self.widget.deleteLater()
        except Exception as e:
            print(f"Error during update: {e}")

        # WIDGET_ID_SAFE.pop(self.id)

    def delete(self):
        '''
        Remove the widget from the layout and delete it.
        '''
        layout.removeWidget(self.widget)
        self.widget.deleteLater()

    def append(self, value: str = ''):
        '''
        Append a value to the widget (if supported, e.g., in a TextArea).

        :param value: The text value to append.
        '''
        allowed = [
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            self.widget.append(value)

    def html(self, value):
        '''
        Set the HTML content of the widget (if supported, e.g., in a TextArea).

        :param value: The HTML content to set.
        '''
        allowed = [GET_ELEM_TYPE_TEXTAREA]

        if process_request(allowed, self.widget_type):
            self.widget.setHtml(value)

    def insert_html(self, value):
        '''
        Insert HTML content at the current cursor position in the widget (if supported).

        :param value: The HTML content to insert.
        '''
        allowed = [
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            self.widget.insertHtml(value)

    def plain_text(self, value: None = None):
        '''
        Set or get the plain text content of the widget.

        :param value: The plain text to set (if None, returns the current plain text).
        :return: The current plain text (if no value is passed).
        '''
        allowed = [
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            if value != None:
                self.widget.setPlainText(value)
            else:
                return self.widget.toPlainText()

    def alignment(self, value: None = None):
        '''
        Set or get the alignment of the widget.

        :param value: The alignment to set (if None, returns the current alignment).
        :return: The current alignment of the widget (if no value is passed).
        '''
        if value != None:
            make_alignment(self.widget, value)
        else:
            return self.widget.alignment()

    def is_default(self):
        '''
        Check if the widget is set as the default.

        :return: True if the widget is the default, otherwise False.
        '''
        return self.widget.isDefault()

    def is_readonly(self):
        '''
        Check if the widget is set as read-only.

        :return: True if the widget is read-only, otherwise False.
        '''
        return self.widget.isReadonly()

    def style(self, css: None = None, reset: bool = False):
        '''
        Set or reset the CSS style of the widget.

        :param css: The CSS style to apply (if None, resets the style).
        :param reset: Whether to reset the style to the default.
        '''
        set_style(self.widget, css, reset)

    def is_checked(self):
        '''
        Check if the widget (e.g., checkbox or radio button) is checked.

        :return: True if the widget is checked, otherwise False.
        '''
        return self.widget.isChecked()

    def hidden(self, value: bool | None = None):
        '''
        Set or get the visibility of the widget.

        :param value: True to hide the widget, False to show it (if None, returns the visibility state).
        :return: The visibility state of the widget (if no value is passed).
        '''
        if value != None:
            self.widget.setHidden(value)

    def hide(self):
        '''
        Hide the widget.
        '''
        self.widget.setHidden(True)
    
    def disabled(self, value: bool | None = None):
        '''
        Set or get the disabled state of the widget.

        :param value: True to disable the widget, False to enable it (if None, returns the disabled state).
        :return: The disabled state of the widget (if no value is passed).
        '''
        if value != None:
            self.widget.setDisabled(value)

    def disable(self):
        '''
        Disable the widget.
        '''
        self.widget.setDisabled(True)

    def enable(self):
        '''
        Enable the widget.
        '''
        self.widget.setEnabled(True)

    def is_hidden(self):
        '''
        Check if the widget is hidden.

        :return: True if the widget is hidden, otherwise False.
        '''
        return self.widget.isHidden()

    def is_disabled(self):
        '''
        Check if the widget is disabled.

        :return: True if the widget is disabled, otherwise False.
        '''
        return self.widget.isDisabled()

    def select_all(self):
        '''
        Select all content in the widget (if supported, e.g., in a TextArea).
        '''
        allowed = [
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            self.widget.selectAll()

    def copy(self):
        '''
        Copy the selected content from the widget (if supported, e.g., in a TextArea).
        '''
        allowed = [
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            self.widget.copy()

    def cut(self):
        '''
        Cut the selected content from the widget (if supported, e.g., in a TextArea).
        '''
        allowed = [
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            self.widget.cut()

    def undo(self):
        '''
        Undo the last action in the widget (if supported, e.g., in a TextArea).
        '''
        allowed = [
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            self.widget.undo()

    def redo(self):
        '''
        Redo the last undone action in the widget (if supported, e.g., in a TextArea).
        '''
        allowed = [
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            self.widget.redo()

    def paste(self):
        '''
        Paste the clipboard content into the widget (if supported, e.g., in a TextArea).
        '''
        allowed = [
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            self.widget.paste()

    def clear(self):
        '''
        Clear the content of the widget.
        '''
        widget_type = self.widget_type
        if process_request([GET_ELEM_TYPE_TEXTAREA, GET_ELEM_TYPE_LISTWIDGET, 
                            GET_ELEM_TYPE_SELECT, GET_ELEM_TYPE_TAB_WIDGET], widget_type):
            self.widget.clear()
        elif process_request([GET_ELEM_TYPE_INPUT], widget_type):
            self.widget.setText('')

    def add(self, items):
        '''
        Add items to the widget (if supported, e.g., ListWidget, Select, TabWidget, StackedWidget).

        :param items: The items to add (can be a list of items depending on the widget type).
        '''
        widget_type = self.widget_type
        if process_request([GET_ELEM_TYPE_LISTWIDGET], widget_type):
            add_list_items(self.widget, items)
        elif process_request([GET_ELEM_TYPE_SELECT], widget_type):
            if isinstance(items[0], (sample_list, sample_string)):
                items = [items] if isinstance(items[0], sample_string) else items
        elif process_request([GET_ELEM_TYPE_TAB_WIDGET], widget_type):
            add_tabs(self.widget, items)
        elif process_request([GET_ELEM_TYPE_STACKED], widget_type):
            add_stacks(self.widget, items)

    def remove(self, items):
        allowed = [
            GET_ELEM_TYPE_LISTWIDGET,
            GET_ELEM_TYPE_SELECT,
            GET_ELEM_TYPE_TAB_WIDGET,
            GET_ELEM_TYPE_STACKED
        ]

        if process_request(allowed[0], self.widget_type):
            self.widget.takeItem(items)
        elif process_request(allowed[1], self.widget_type):
            self.widget.removeItem(items)
        elif process_request(allowed[2], self.widget_type):
            self.widget.removeTab(items)
        elif process_request(allowed[3], self.widget_type):
            def init_remove(widget):
                widget, layout = widget
                if widget is not None:
                    self.widget.removeWidget(widget)
            
            
            if isinstance(items, int):
                init_remove([self.widget.widget(items), None])
            elif isinstance(items[0], list):
                for item in items:
                    init_remove(item)
            else:
                init_remove(items)


    def current(self):
        '''
        Get the current item or index of the widget (e.g., ListWidget, Select, TabWidget, StackedWidget).

        :return: The current item or index based on the widget type.
        '''
        widget_type = self.widget_type
        if process_request([GET_ELEM_TYPE_LISTWIDGET], widget_type):
            return self.widget.currentRow()
        elif process_request([GET_ELEM_TYPE_SELECT], widget_type):
            return self.widget.currentText()
        elif process_request([GET_ELEM_TYPE_TAB_WIDGET, GET_ELEM_TYPE_STACKED], widget_type):
            return self.widget.currentIndex()

    def count(self):
        '''
        Get the count of items in the widget (e.g., ListWidget, Select, TabWidget, StackedWidget).

        :return: The number of items in the widget.
        '''
        allowed = [
            GET_ELEM_TYPE_LISTWIDGET,
            GET_ELEM_TYPE_SELECT,
            GET_ELEM_TYPE_TAB_WIDGET,
            GET_ELEM_TYPE_STACKED
        ]

        if process_request(allowed, self.widget_type):
            return self.widget.count()

    def selected_items(self):
        '''
        Get the list of selected items in the widget (if supported, e.g., ListWidget).

        :return: A list of selected items (as text) from the widget.
        '''
        allowed = [
            GET_ELEM_TYPE_LISTWIDGET,
        ]

        if process_request(allowed, self.widget_type):
            selected_items = [items.text()
                              for items in self.widget.selectedItems()]
            return selected_items

    def set(self, value):
        '''
        Set the current item or index of the widget (e.g., Select, StackedWidget).

        :param value: The item or index to set.
        '''
        allowed = [
            GET_ELEM_TYPE_SELECT,
            GET_ELEM_TYPE_STACKED
        ]

        if process_request(allowed, self.widget_type):
            self.widget.setCurrentIndex(value)


    def index(self):
        '''
        Get the current index of the widget (e.g., Select, StackedWidget).

        :return: The current index of the widget.
        '''
        allowed = [
            GET_ELEM_TYPE_SELECT,
            GET_ELEM_TYPE_STACKED
        ]

        if process_request(allowed, self.widget_type):
            return self.widget.currentIndex()

    def reset(self):
        '''
        Reset the widget to its default state (if supported, e.g., ProgressBar).
        '''
        allowed = [
            GET_ELEM_TYPE_PROGRESS_BAR,
        ]

        if process_request(allowed, self.widget_type):
            self.widget.reset()

    def minimum(self):
        '''
        Get the minimum value of the widget (if supported, e.g., ProgressBar).

        :return: The minimum value of the widget.
        '''
        allowed = [
            GET_ELEM_TYPE_PROGRESS_BAR,
        ]

        if process_request(allowed, self.widget_type):
            return self.widget.minimum()

    def maximum(self):
        '''
        Get the maximum value of the widget (if supported, e.g., ProgressBar).

        :return: The maximum value of the widget.
        '''
        allowed = [
            GET_ELEM_TYPE_PROGRESS_BAR,
        ]

        if process_request(allowed, self.widget_type):
            return self.widget.maximum()

    def is_text_visible(self):
        '''
        Check if the text is visible in the widget (if supported, e.g., ProgressBar).

        :return: True if the text is visible, otherwise False.
        '''
        allowed = [
            GET_ELEM_TYPE_PROGRESS_BAR,
        ]

        if process_request(allowed, self.widget_type):
            return self.widget.isTextVisible()

    def reject(self, result: int = None):
        '''
        Reject the widget (if supported, e.g., Popup).
        
        :param result: The result to set after rejection (optional).
        '''
        allowed = [
            GET_ELEM_TYPE_POPUP,
        ]

        if process_request(allowed, self.widget_type):
            self.widget.reject()
            if result != None:
                self.widget.setResult(result)

    def accept(self, result: int = None):
        '''
        Accept the widget (if supported, e.g., Popup).
        
        :param result: The result to set after acceptance (optional).
        '''
        allowed = [
            GET_ELEM_TYPE_POPUP,
        ]

        if process_request(allowed, self.widget_type):
            self.widget.accept()
            if result != None:
                self.widget.setResult(result)
    
    def focus(self, value: bool = True):
        '''
        Set or get the focus of the widget (e.g., Input, TextArea).
        
        :param value: True to set focus on the widget, False to remove focus (optional).
        :return: None if setting focus, otherwise True if the widget has focus.
        '''
        allowed = [
            GET_ELEM_TYPE_INPUT,
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            self.widget.setFocus()
    

    def has_focus(self, value: bool = True):
        allowed = [
            GET_ELEM_TYPE_INPUT,
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            return self.widget.hasFocus()

    def cursor(self):
        '''
        Get the current text cursor and position in the widget (if supported, e.g., Input, TextArea).
        
        :return: A tuple of the cursor and its position.
        '''
        allowed = [
            GET_ELEM_TYPE_INPUT,
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            cursor = self.widget.textCursor()
            position = cursor.position()

            return cursor, position

    
    def setcursor(self, cursor):
        '''
        Set the position of the text cursor in the widget.
        
        :param cursor: The cursor object with the desired position.
        '''
        cursor, position = cursor
        cursor.setPosition(position)
        self.widget.setTextCursor(cursor)

    def icon(self, path):
        '''
        Set the icon of the widget.
        
        :param path: The file path to the icon image.
        '''
        self.widget.setIcon(QIcon(init_image(path)))

    def show(self, widget):
        '''
        Show the given widget inside the current widget (if supported, e.g., StackedWidget, TabWidget).
        
        :param widget: The widget to show.
        '''
        allowed = [
            GET_ELEM_TYPE_STACKED,
            GET_ELEM_TYPE_TAB_WIDGET,
        ]

        if process_request(allowed[0], self.widget_type):
            widget, layout = widget
            self.widget.setCurrentWidget(widget)
        elif process_request(allowed[1], self.widget_type):
            self.widget.setCurrentIndex(widget)

    def scrollbar(self, scrollbar: None = None, bar_type: str = 'v', id: None = None):
        '''
        Set or get the scrollbar for the widget (if supported, e.g., TextArea).
        
        :param scrollbar: The scrollbar widget to set (optional).
        :param bar_type: The type of scrollbar ('v' for vertical, 'h' for horizontal).
        :param id: The identifier for the scrollbar widget (optional).
        :return: The scrollbar widget if not setting it, or None.
        '''
        allowed = [
            GET_ELEM_TYPE_TEXTAREA
        ]

        if process_request(allowed, self.widget_type):
            if scrollbar != None:
                if bar_type == 'v':
                    self.widget.setVerticalScrollBar(scrollbar)
                elif bar_type == 'h':
                    self.widget.setHorizontalScrollBar(scrollbar)
            else:
                if bar_type == 'v':
                    bar =  self.widget.verticalScrollBar()
                elif bar_type == 'h':
                    bar = self.widget.horizontalScrollBar()
                else:
                    bar = None

                if bar != None:
                    return INIT_WIDGET(id, bar)
                else:
                    return bar
                
    def hex(self):
        '''
        Get the selected color as a hexadecimal string (if supported, e.g., Color Popup).
        
        :return: The selected color in hexadecimal format.
        '''
        allowed = [
            GET_ELEM_TYPE_COLOR_POPUP
        ]

        if process_request(allowed, self.widget_type):
            return self.widget.selectedColor().name(QColor.HexRgb)

    
    def rgba(self):
        '''
        Get the selected color as an RGBA tuple (if supported, e.g., Color Popup).
        
        :return: A tuple representing the selected color in RGBA format.
        '''
        allowed = [
            GET_ELEM_TYPE_COLOR_POPUP
        ]

        if process_request(allowed, self.widget_type):
            return self.widget.selectedColor().getRgb()


    def checked(self, value: bool = True):
        '''
        Set or get the checked state of the widget (e.g., RadioButton, CheckBox).
        
        :param value: True to set the widget as checked, False to uncheck it.
        '''
        allowed = [
            GET_ELEM_TYPE_RADIO_BUTTON,
            GET_ELEM_TYPE_CHECK_BOX
        ]

        if process_request(allowed, self.widget_type):
            self.widget.setChecked(value)

class get(GET):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# ------------------------------------------------------------------------#

###########################################################################
############################## EASE OF ACCESS #############################
###########################################################################

# ------------------------------------------------------------------------#



class Exit(Button):
    def __init__(self, label: str = 'Exit', icon: None = None, id: None = None,
                 disabled: bool = False, default: bool = False, grid: tuple = (None, None),
                 sizepolicy: tuple = (None, None), checkable: bool = False, checked: bool = False, hidden: bool = False, focus: bool = True, 
                 icon_size: int = 20, statustip: str = None, tooltip: str = None, shortcut: str = None, hover: None = None):

        elem_type = ELEM_TYPE_BUTTON

        self.rtn = [elem_type, label, Window.quit, icon, id,
                    disabled, default, grid, sizepolicy, checkable, checked, hidden, focus, icon_size, statustip, tooltip, shortcut, hover]

    def __call__(self):
        return self.rtn


class exit(Exit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Copy(Button):
    def __init__(self, Target_ID, button_text: str = 'Copy', icon: None = None,
                 id: None = None, disabled: bool = False, default: bool = False,
                 grid: tuple = (None, None), sizePolicy: tuple = (None, None), checked: bool = False, hidden: bool = False, focus: bool = True, 
                 icon_size: int = 20, statustip: str = None, tooltip: str = None, shortcut: str = None, hover: None = None):

        elem_type = elem_type, id = pre_widget_process('copy')
        METHOD_COPY.append(f'{id}:{Target_ID}')

        self.rtn = [elem_type, button_text, action_copy, icon, id,
                    disabled, default, grid, sizePolicy, True, checked, hidden, focus, icon_size, statustip, tooltip, shortcut, hover]

    def __call__(self):
        return self.rtn


class copy(Copy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Cut(Button):
    def __init__(self, Target_ID, button_text: str = 'Cut', icon: None = None,
                 id: None = None, disabled: bool = False, default: bool = False,
                 grid: tuple = (None, None), sizePolicy: tuple = (None, None), checked: bool = False, hidden: bool = False, focus: bool = True, 
                 icon_size: int = 20, statustip: str = None, tooltip: str = None, shortcut: str = None, hover: None = None):

        elem_type, id = pre_widget_process('cut')
        METHOD_CUT.append(f'{id}:{Target_ID}')

        self.rtn = [elem_type, button_text, action_cut, icon, id,
                    disabled, default, grid, sizePolicy, True, checked, hidden, focus, icon_size, statustip, tooltip, shortcut, hover]

    def __call__(self):
        return self.rtn


class cut(Cut):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Paste(Button):
    def __init__(self, Target_ID, button_text: str = 'Paste', icon: None = None,
                 id: None = None, disabled: bool = False, default: bool = False,
                 grid: tuple = (None, None), sizePolicy: tuple = (None, None), checked: bool = False, hidden: bool = False, focus: bool = True, 
                 icon_size: int = 20, statustip: str = None, tooltip: str = None, shortcut: str = None, hover: None = None):

        elem_type, id = pre_widget_process('paste')
        METHOD_PASTE.append(f'{id}:{Target_ID}')

        self.rtn = [elem_type, button_text, action_paste, icon, id,
                    disabled, default, grid, sizePolicy, True, checked, hidden, focus, icon_size, statustip, tooltip, shortcut, hover]

    def __call__(self):
        return self.rtn


class paste(Paste):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Undo(Button):
    def __init__(self, Target_ID, button_text: str = 'Undo', icon: None = None,
                 id: None = None, disabled: bool = False, default: bool = False,
                 grid: tuple = (None, None), sizePolicy: tuple = (None, None), checked: bool = False, hidden: bool = False, focus: bool = True, 
                 icon_size: int = 20, statustip: str = None, tooltip: str = None, shortcut: str = None, hover: None = None):

        elem_type = elem_type, id = pre_widget_process('undo')
        METHOD_UNDO.append(f'{id}:{Target_ID}')

        self.rtn = [elem_type, button_text, action_undo, icon, id,
                    disabled, default, grid, sizePolicy, True, checked, hidden, focus, icon_size, statustip, tooltip, shortcut, hover]

    def __call__(self):
        return self.rtn


class undo(Undo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Redo(Button):
    def __init__(self, Target_ID, button_text: str = 'Redo', icon: None = None,
                 id: None = None, disabled: bool = False, default: bool = False,
                 grid: tuple = (None, None), sizePolicy: tuple = (None, None), checked: bool = False, hidden: bool = False, focus: bool = True, 
                 icon_size: int = 20, statustip: str = None, tooltip: str = None, shortcut: str = None, hover: None = None):

        elem_type = elem_type, id = pre_widget_process('redo')
        METHOD_REDO.append(f'{id}:{Target_ID}')

        self.rtn = [elem_type, button_text, action_redo, icon, id,
                    disabled, default, grid, sizePolicy, True, checked, hidden, focus, icon_size, statustip, tooltip, shortcut, hover]

    def __call__(self):
        return self.rtn


class redo(Redo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



# ------------------------------------------------------------------------#

###########################################################################
############################## CONTROL BUTTONS ############################
###########################################################################

# ------------------------------------------------------------------------#


def get_element_by_id(element_id: str):
    """
    Retrieves an element using its unique ID.

    :param element_id: The ID of the element to retrieve.
    :return: The element wrapped in a GET instance.
    """
    return GET(element_id)

def minimize():
    return get_element_by_id(MINIMIZE_BUTTON_ID)

def maximize():
    return get_element_by_id(MAXIMIZE_BUTTON_ID)

def close():
    return get_element_by_id(CLOSE_BUTTON_ID)

def title():
    return get_element_by_id(TITLE_TEXT_ID)


# ------------------------------------------------------------------------#

###########################################################################
############################### MANUAL WINDOW #############################
###########################################################################

# ------------------------------------------------------------------------#


# def main():
#     window = Window()
#     Box([[Button('UNAVAILABLE')]])
#     window.run()


# ------------------------------------------------------------------------#

###########################################################################
########################### CLERA STYLING EDITOR ##########################
###########################################################################

# ------------------------------------------------------------------------#

# def key():
#     print(QStyleFactory.keys())

# key()
