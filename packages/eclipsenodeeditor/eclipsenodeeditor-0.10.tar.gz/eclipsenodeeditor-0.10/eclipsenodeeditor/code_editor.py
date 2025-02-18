from PyQt6.QtCore import Qt, QUrl, pyqtSlot, QObject
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSplitter
from PyQt6 import QtWebEngineWidgets
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile, QWebEngineSettings
import os
import json
import inspect
import importlib
import sys
from typing import Any, Dict, List, Optional
import builtins
import pkgutil
from . import core
from .environment import EnvironmentAnalyzer
import logging

# Set up logging with more detailed format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger('CodeEditor')

# List of core classes and functions we want to expose
CORE_EXPORTS = {
    'Node', 'Socket', 'EclipseNodeEditor', 'node', 'socket', 'tool', 'Tool',
    'NodeUtils', 'Reroute', 'SocketConnection', 'NodeEditorObject', 'Event'
}

class EditorPage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, message, line, source):
        # Only log warnings and errors
        if level in [QWebEnginePage.JavaScriptConsoleMessageLevel.WarningMessageLevel,
                    QWebEnginePage.JavaScriptConsoleMessageLevel.ErrorMessageLevel]:
            logger.warning(f"JS: {message}")

    def certificateError(self, error):
        # Accept all certificates for CDN access
        return True

class CodeEditorBridge(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.project_root = os.path.dirname(os.path.dirname(__file__))
        if self.project_root not in sys.path:
            sys.path.insert(0, self.project_root)
        
        # Initialize environment analyzer
        self.environment = EnvironmentAnalyzer()
        # Register for reload notifications
        self.environment.add_reload_callback(self.on_module_reload)
        # Track current file
        self.current_file = None
        logger.info("Environment analyzer initialized")

    def on_module_reload(self, module_path: str):
        """Handle module reload events"""
        logger.warning(f"CodeEditorBridge notified of module reload: {module_path}")
        # Force clear Python's module cache to ensure fresh imports
        if module_path in sys.modules:
            logger.warning(f"Removing {module_path} from sys.modules cache")
            del sys.modules[module_path]
        # The environment analyzer already cleared its caches

    @pyqtSlot(str)
    def set_current_file(self, file_path: str):
        """Set the current file being edited"""
        self.current_file = file_path
        # Track if we explicitly opened core.py
        self._explicitly_opened_core = os.path.basename(file_path) == "core.py"
        logger.info(f"Current file set to: {file_path}")

    @pyqtSlot(str, result=bool)
    def save_file(self, content: str) -> bool:
        """Save the current file content to disk"""
        if not self.current_file:
            # Don't error log here since this is expected for new/unsaved files
            logger.debug("No current file set - editor has unsaved content")
            return False
            
        try:
            # Extra safety check - never allow saving to core.py unless explicitly opened
            if os.path.basename(self.current_file) == "core.py" and not getattr(self, '_explicitly_opened_core', False):
                logger.error("Prevented attempt to save to core.py when not explicitly opened")
                return False
                
            with open(self.current_file, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Saved file: {self.current_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to save file: {e}")
            return False

    @pyqtSlot(str, result=str)
    def get_completions(self, context_json: str) -> str:
        try:
            context = json.loads(context_json)
            
            # Log the type of completion request
            if context.get('type') == 'signature':
                logger.info("=== Starting Signature Help Request ===")
            else:
                logger.info("=== Starting Completion Request ===")
            
            line = context['line']
            position = context['position']
            file_content = context.get('fileContent', '')
            
            logger.info(f"Line {position['lineNumber']}, Column {position['column']}")
            logger.info(f"Line content: {line}")
            
            # Handle signature help requests
            if context.get('type') == 'signature':
                # Get the function name from the current line
                current_line = line[:position['column']]
                # Find the last opening parenthesis
                if '(' in current_line:
                    func_part = current_line[:current_line.rindex('(')].strip()
                    # If it's a method call, get the object
                    if '.' in func_part:
                        obj_part, func_name = func_part.rsplit('.', 1)
                        # Analyze context to get the object
                        obj, _ = self.environment.analyze_code_context(
                            file_content,
                            position['lineNumber'],
                            current_line.rindex(obj_part) + len(obj_part)
                        )
                        if obj:
                            signature = self.environment.get_signature_help(obj, func_name)
                            if signature:
                                return json.dumps(signature)
                    else:
                        # It's a direct function call, look in globals
                        obj, _ = self.environment.analyze_code_context(
                            file_content,
                            position['lineNumber'],
                            position['column']
                        )
                        if obj:
                            signature = self.environment.get_signature_help(obj, func_part)
                            if signature:
                                return json.dumps(signature)
                return json.dumps({})
            
            # Analyze the context to find what we're completing
            logger.info("Analyzing code context...")
            obj, remaining = self.environment.analyze_code_context(
                file_content, 
                position['lineNumber'], 
                position['column']
            )
            
            if obj is not None:
                logger.info(f"Found object of type: {type(obj).__name__}")
            else:
                logger.info("No object found, will provide module completions")
            
            suggestions = []
            if obj is not None:
                # Get completions for the object
                logger.info(f"Getting completions for object: {type(obj).__name__}")
                completions = self.environment.get_completions_for_object(obj, remaining)
                logger.info(f"Found {len(completions)} completions")
                
                # Convert CompletionItems to Monaco format
                for completion in completions:
                    kind = {
                        'class': 7,
                        'function': 2,
                        'method': 2,
                        'property': 10,
                        'variable': 5,
                        'module': 9
                    }.get(completion.kind, 0)
                    
                    suggestion = {
                        'label': completion.name,
                        'kind': kind,
                        'detail': completion.detail,
                        'documentation': completion.documentation,
                        'insertText': completion.signature or completion.name
                    }
                    suggestions.append(suggestion)
            else:
                # If no object found, provide module completions
                logger.info("Getting module completions")
                completions = self.environment.get_all_module_completions(remaining)
                logger.info(f"Found {len(completions)} module completions")
                for completion in completions:
                    suggestions.append({
                        'label': completion.name,
                        'kind': 9,  # Module
                        'detail': completion.detail,
                        'documentation': completion.documentation,
                        'insertText': completion.name
                    })
                
            logger.info(f"Returning {len(suggestions)} total suggestions")
            return json.dumps({'suggestions': suggestions})
            
        except Exception as e:
            logger.error(f"Failed to get completions: {e}")
            logger.error(f"Error details:", exc_info=True)  # This will log the full stack trace
            return json.dumps({'suggestions': []})

class CodeEditorWindow(QWidget):
    def __init__(self, parent=None, file_path=None):
        super().__init__(parent)
        self.setWindowTitle("Node Editor Code Editor")
        self.resize(1200, 800)
        
        # Store file path - only set if explicitly provided
        self.file_path = file_path
        
        # Create layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create splitter for editor and file tree
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Create web view for Monaco
        self.web_view = QWebEngineView()
        
        # Set up profile with network access
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.MemoryHttpCache)
        
        # Enable JavaScript and other required settings
        settings = profile.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.AllowRunningInsecureContent, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        
        # Set up custom page for console messages
        self.page = EditorPage(profile, self.web_view)
        self.web_view.setPage(self.page)
        
        # Set up web channel for communication
        self.channel = QWebChannel()
        self.bridge = CodeEditorBridge()
        self.channel.registerObject("bridge", self.bridge)
        self.web_view.page().setWebChannel(self.channel)
        
        # Only set current file if one was explicitly provided
        if self.file_path:
            self.bridge.set_current_file(self.file_path)
        
        # Load Monaco Editor
        editor_path = os.path.join(os.path.dirname(__file__), "static", "editor.html")
        if not os.path.exists(editor_path):
            logger.error(f"Could not find editor.html at {editor_path}")
        else:
            url = QUrl.fromLocalFile(editor_path)
            self.web_view.setUrl(url)
        
        splitter.addWidget(self.web_view)
        layout.addWidget(splitter)
        
    def show_editor(self):
        self.show()
        self.raise_()
        self.activateWindow() 