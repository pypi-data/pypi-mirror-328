from __future__ import annotations
import sys
import os
import inspect
import importlib
import pkgutil
import logging
from typing import Any, Dict, List, Optional, Set, Tuple, Callable
from dataclasses import dataclass
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

logger = logging.getLogger('Environment')
logger.setLevel(logging.INFO)

@dataclass
class CompletionItem:
    """Represents a single completion item with all its metadata"""
    name: str
    kind: str  # 'class', 'function', 'method', 'property', 'variable', 'module'
    detail: str
    documentation: str
    signature: Optional[str] = None
    type_hint: Optional[str] = None

class ModuleChangeHandler(FileSystemEventHandler):
    """Handles file system events for module changes"""
    def __init__(self, analyzer: 'EnvironmentAnalyzer'):
        self.analyzer = analyzer
        self.last_reload = {}  # Track last reload time per file
        
    def on_modified(self, event):
        if event.is_directory:
            return
            
        if not event.src_path.endswith('.py'):
            return
            
        # Debounce reloads (prevent multiple reloads within 1 second)
        current_time = time.time()
        if event.src_path in self.last_reload:
            if current_time - self.last_reload[event.src_path] < 1:
                return
                
        self.last_reload[event.src_path] = current_time
        
        # Convert file path to module path
        rel_path = os.path.relpath(event.src_path, self.analyzer.project_root)
        if rel_path.startswith('eclipsenodeeditor'):
            module_path = rel_path.replace(os.path.sep, '.')[:-3]  # Remove .py
            logger.warning(f"File changed: {event.src_path}")  # Make this visible
            self.analyzer.reload_module(module_path)

class EnvironmentAnalyzer:
    """Analyzes and provides information about the Python environment"""
    
    def __init__(self):
        self.project_root = os.path.dirname(os.path.dirname(__file__))
        self.package_name = 'eclipsenodeeditor'
        self.module_cache: Dict[str, Any] = {}
        self.completion_cache: Dict[str, List[CompletionItem]] = {}
        self.reload_callbacks: List[Callable[[str], None]] = []  # List of callbacks to notify on reload
        
        # Add project root to path if not already there
        if self.project_root not in sys.path:
            sys.path.insert(0, self.project_root)
            
        # Initialize core package
        self.core_package = self._import_module(self.package_name)
        self.core_module = self._import_module(f"{self.package_name}.core")
        
        # Initialize environment
        self.initialize_environment()
        
        # Set up file watching
        self.observer = Observer()
        self.event_handler = ModuleChangeHandler(self)
        watch_path = os.path.join(self.project_root, 'eclipsenodeeditor')
        self.observer.schedule(self.event_handler, watch_path, recursive=True)
        self.observer.start()
        logger.warning(f"Started watching for changes in: {watch_path}")  # Make this visible
        
    def __del__(self):
        """Clean up file system observer"""
        if hasattr(self, 'observer'):
            self.observer.stop()
            self.observer.join()
            logger.warning("Stopped file system observer")
            
    def add_reload_callback(self, callback: Callable[[str], None]):
        """Add a callback to be notified when modules are reloaded"""
        self.reload_callbacks.append(callback)
            
    def reload_module(self, module_path: str):
        """Reload a module and update the environment"""
        try:
            logger.warning(f"Attempting to reload module: {module_path}")
            
            # Remove from cache
            if module_path in self.module_cache:
                del self.module_cache[module_path]
                logger.warning("Cleared module from cache")
                
            # Force reload of the module
            module = importlib.import_module(module_path)
            importlib.reload(module)
            
            # Update our cache
            self.module_cache[module_path] = module
            
            # If it's the core module, update our reference and force clear sys.modules
            if module_path == f"{self.package_name}.core":
                self.core_module = module
                # Force clear all package modules to ensure fresh imports
                for key in list(sys.modules.keys()):
                    if key.startswith(self.package_name):
                        logger.warning(f"Clearing {key} from sys.modules")
                        del sys.modules[key]
                logger.warning("Updated core module reference and cleared module cache")
                
            # Clear completion cache to force fresh analysis
            self.completion_cache.clear()
            
            # Notify all callbacks
            for callback in self.reload_callbacks:
                try:
                    callback(module_path)
                except Exception as e:
                    logger.error(f"Error in reload callback: {e}")
            
            logger.warning(f"Successfully reloaded module: {module_path}")
            
        except Exception as e:
            logger.error(f"Failed to reload module {module_path}: {e}")
            
    def _import_module(self, module_name: str) -> Optional[Any]:
        """Safely import a module and cache it"""
        try:
            if module_name in self.module_cache:
                return self.module_cache[module_name]
            
            module = importlib.import_module(module_name)
            self.module_cache[module_name] = module
            return module
        except Exception as e:
            logger.error(f"Failed to import module {module_name}: {e}")
            return None
            
    def initialize_environment(self):
        """Initialize the environment by scanning all relevant modules"""
        logger.info("Initializing environment analysis...")
        
        # Scan all submodules of our package
        package = self._import_module(self.package_name)
        if package:
            for _, name, _ in pkgutil.iter_modules(package.__path__):
                full_name = f"{self.package_name}.{name}"
                self._import_module(full_name)
                
        logger.info(f"Loaded {len(self.module_cache)} modules")
        
    def get_completions_for_object(self, obj: Any, prefix: str = '') -> List[CompletionItem]:
        """Get completion items for an object"""
        completions = []
        
        try:
            # Get all attributes including inherited ones
            members = []
            
            if inspect.isclass(obj):
                # For classes, always get fresh info
                if hasattr(obj, '__module__') and obj.__module__.startswith(self.package_name):
                    logger.info(f"Getting fresh class info for {obj.__name__}")
                    module = importlib.import_module(obj.__module__)
                    obj = getattr(module, obj.__name__)
                members = inspect.getmembers(obj)
            elif isinstance(obj, type):
                members = inspect.getmembers(obj)
            else:
                # For instances, get both instance and class attributes
                # Always get fresh class info for our package's classes
                cls = type(obj)
                if hasattr(cls, '__module__') and cls.__module__.startswith(self.package_name):
                    logger.info(f"Getting fresh class info for instance of {cls.__name__}")
                    module = importlib.import_module(cls.__module__)
                    fresh_cls = getattr(module, cls.__name__)
                    # Get instance members first
                    instance_members = inspect.getmembers(obj)
                    # Then get class members from fresh class
                    class_members = inspect.getmembers(fresh_cls)
                else:
                    instance_members = inspect.getmembers(obj)
                    class_members = inspect.getmembers(type(obj))
                
                # Combine both, preferring instance members
                seen = set()
                for name, member in instance_members + class_members:
                    if name not in seen and not name.startswith('_'):
                        seen.add(name)
                        members.append((name, member))
            
            logger.info(f"Found {len(members)} total members")
            
            for name, member in members:
                if name.startswith('_'):  # Skip private/internal
                    continue
                    
                if not prefix or name.startswith(prefix):
                    # Determine the kind
                    kind = 'variable'
                    if inspect.isclass(member):
                        kind = 'class'
                    elif inspect.ismethod(member) or inspect.isfunction(member):
                        kind = 'method' if hasattr(member, '__self__') else 'function'
                    elif isinstance(member, property):
                        kind = 'property'
                        
                    # Get documentation
                    doc = inspect.getdoc(member) or ''
                    
                    # Get type hint
                    type_hint = None
                    try:
                        if hasattr(member, '__annotations__'):
                            return_annotation = member.__annotations__.get('return')
                            if return_annotation:
                                type_hint = str(return_annotation)
                        elif isinstance(member, property) and member.fget:
                            return_annotation = member.fget.__annotations__.get('return')
                            if return_annotation:
                                type_hint = str(return_annotation)
                    except Exception:
                        pass
                    
                    # Get signature for callable objects
                    signature = None
                    if callable(member) and not inspect.isclass(member):
                        try:
                            sig = inspect.signature(member)
                            params = []
                            for param_name, param in sig.parameters.items():
                                if param_name != 'self':
                                    param_str = param_name
                                    if param.annotation != inspect._empty:
                                        param_str += f": {param.annotation.__name__}"
                                    if param.default != inspect._empty:
                                        param_str += f" = {param.default}"
                                    params.append(param_str)
                            signature = f"{name}({', '.join(params)})"
                        except Exception:
                            pass
                    
                    completion = CompletionItem(
                        name=name,
                        kind=kind,
                        detail=type_hint or str(type(member).__name__),
                        documentation=doc,
                        signature=signature,
                        type_hint=type_hint
                    )
                    
                    completions.append(completion)
                    
            logger.info(f"Returning {len(completions)} matching completions")
                    
        except Exception as e:
            logger.error(f"Failed to get completions: {e}")
            logger.error("Error details:", exc_info=True)
            
        return completions
    
    def analyze_code_context(self, code: str, line: int, column: int) -> Tuple[Optional[Any], str]:
        """
        Analyze code context up to a specific position
        Returns (object, remaining_text) where object is the object to get completions for
        and remaining_text is any remaining text after the last dot
        """
        try:
            # Create a fresh environment
            local_vars = {}
            global_vars = {}
            
            # Add our core exports
            if self.core_module:
                # Force reload the core module to get latest changes
                if f"{self.package_name}.core" in sys.modules:
                    logger.info(f"Reloading core module from sys.modules")
                    importlib.reload(sys.modules[f"{self.package_name}.core"])
                    self.core_module = sys.modules[f"{self.package_name}.core"]
                    logger.info(f"Core module reloaded, version: {getattr(self.core_module, '__version__', 'unknown')}")
                
                logger.info("Adding core exports to globals")
                for name, obj in inspect.getmembers(self.core_module):
                    if not name.startswith('_'):
                        global_vars[name] = obj
                logger.info(f"Added {len(global_vars)} items from core")
            
            # Split into lines and get the context
            lines = code.split('\n')
            current_line = lines[line][:column] if line < len(lines) else ""
            
            # Check if we're in an import statement
            if 'import ' in current_line or 'from ' in current_line:
                logger.info("Handling import statement completion")
                words = current_line.strip().split()
                if len(words) > 0:
                    if words[0] == 'from':
                        # We're in a 'from' statement
                        if len(words) == 2:  # Only 'from prefix' typed
                            logger.info(f"Completing 'from' statement with prefix: {words[1]}")
                            # Return None to trigger module completions
                            return None, words[1]
                        elif len(words) > 2 and words[-1] != 'import':
                            # After the 'import' keyword, completing module members
                            logger.info(f"Completing module members with prefix: {words[-1]}")
                            return self.core_module, words[-1]
                    elif words[0] == 'import':
                        # We're in an 'import' statement
                        logger.info(f"Completing 'import' statement with prefix: {words[-1]}")
                        # Return None to trigger module completions
                        return None, words[-1]
            
            # Find the last dot operator
            parts = current_line.split('.')
            if len(parts) > 1:
                obj_path = parts[-2].strip()
                remaining = parts[-1].strip()
                logger.info(f"Looking for object: {obj_path} with remaining: {remaining}")
                
                # Try to get the object directly from globals first
                if obj_path in global_vars:
                    logger.info(f"Found {obj_path} in globals")
                    return global_vars[obj_path], remaining
                
                # If not in globals, try to execute the context
                try:
                    # Add the current line without the part after the last dot
                    context_lines = lines[:line]
                    if current_line.strip():
                        context_lines.append(current_line[:current_line.rindex('.')])
                    
                    # Execute the context
                    context = '\n'.join(context_lines)
                    logger.info("Executing context to find object")
                    exec(context, global_vars, local_vars)
                    
                    # Try to get the object
                    if obj_path in local_vars:
                        logger.info(f"Found {obj_path} in local vars")
                        return local_vars[obj_path], remaining
                    elif obj_path in global_vars:
                        logger.info(f"Found {obj_path} in global vars after exec")
                        return global_vars[obj_path], remaining
                except Exception as e:
                    logger.debug(f"Failed to execute context: {e}")
                    # Even if execution fails, we might still have the object in globals
                    if obj_path in global_vars:
                        logger.info(f"Found {obj_path} in globals after exec failed")
                        return global_vars[obj_path], remaining
                    
            return None, parts[-1].strip()
            
        except Exception as e:
            logger.error(f"Failed to analyze context: {e}")
            return None, ""
            
    def get_all_module_completions(self, prefix: str = '') -> List[CompletionItem]:
        """Get completions for module imports"""
        completions = []
        
        # Clean up prefix
        prefix = prefix.strip()
        logger.info(f"Getting module completions with prefix: '{prefix}'")
        
        # Add our main package if it matches
        if not prefix or self.package_name.startswith(prefix):
            logger.info(f"Adding main package: {self.package_name}")
            completions.append(CompletionItem(
                name=self.package_name,
                kind='module',
                detail='Node Editor Package',
                documentation='The main Eclipse Node Editor package'
            ))
            
        # Add core exports if we're in an import context
        if self.core_module:
            logger.info("Adding core module exports")
            for name, obj in inspect.getmembers(self.core_module):
                if not name.startswith('_'):  # Skip private members
                    if not prefix or name.startswith(prefix):
                        kind = 'class' if inspect.isclass(obj) else 'function'
                        doc = inspect.getdoc(obj) or ''
                        
                        completions.append(CompletionItem(
                            name=name,
                            kind=kind,
                            detail=f"{self.package_name}.{name}",
                            documentation=doc
                        ))
        
        # Add all submodules of our package
        if self.core_package:
            logger.info("Adding package submodules")
            for _, name, _ in pkgutil.iter_modules(self.core_package.__path__):
                if not prefix or name.startswith(prefix):
                    full_name = f"{self.package_name}.{name}"
                    completions.append(CompletionItem(
                        name=name,
                        kind='module',
                        detail=full_name,
                        documentation=f'Submodule: {full_name}'
                    ))
        
        logger.info(f"Found {len(completions)} total module completions")
        return completions

    def get_signature_help(self, obj: Any, func_name: str) -> Optional[Dict]:
        """Get signature help for a function or method"""
        try:
            if inspect.isclass(obj):
                # For classes, look for constructor
                member = obj
            else:
                # For modules or instances, look for named member
                member = getattr(obj, func_name, None)
                if member is None:
                    return None

            if not callable(member):
                return None

            # Get signature
            sig = inspect.signature(member)
            
            # Build parameter info
            parameters = []
            for name, param in sig.parameters.items():
                if name == 'self':  # Skip self parameter
                    continue
                    
                # Get parameter type and default value
                param_type = param.annotation.__name__ if param.annotation != inspect._empty else 'Any'
                has_default = param.default != inspect._empty
                default_value = f" = {param.default}" if has_default else ""
                
                parameters.append({
                    'label': f"{name}: {param_type}{default_value}",
                    'documentation': ''  # Could add parameter documentation here
                })

            # Get function documentation
            doc = inspect.getdoc(member) or ''

            return {
                'signatures': [{
                    'label': f"{func_name}({', '.join(p['label'] for p in parameters)})",
                    'documentation': doc,
                    'parameters': parameters
                }],
                'activeParameter': 0  # Could be more sophisticated based on cursor position
            }

        except Exception as e:
            logger.error(f"Failed to get signature help: {e}")
            return None 