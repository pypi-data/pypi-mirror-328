import importlib.util
import json
import logging
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph

logger = logging.getLogger(__name__)


@dataclass
class GraphConfig:
    name: str
    path: str
    file_path: str
    graph_var: str
    _graph: Optional[Union[StateGraph, CompiledStateGraph]] = None

    @classmethod
    def from_config(cls, name: str, path: str) -> "GraphConfig":
        file_path, graph_var = path.split(":")
        return cls(name=name, path=path, file_path=file_path, graph_var=graph_var)

    def load_graph(self) -> Union[StateGraph, CompiledStateGraph]:
        """Load graph from the specified path"""
        try:
            if self.file_path.startswith("."):
                abs_file_path = os.path.abspath(self.file_path)
            else:
                abs_file_path = self.file_path

            if not os.path.exists(abs_file_path):
                raise FileNotFoundError(f"Script not found: {abs_file_path}")

            module_name = Path(abs_file_path).stem
            spec = importlib.util.spec_from_file_location(module_name, abs_file_path)

            if not spec or not spec.loader:
                raise ImportError(f"Could not load module from: {abs_file_path}")

            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)

            graph = getattr(module, self.graph_var, None)
            if not isinstance(graph, (StateGraph, CompiledStateGraph)):
                raise TypeError(
                    f"Expected StateGraph or CompiledStateGraph, got {type(graph)}"
                )

            self._graph = graph
            return graph

        except Exception as e:
            logger.error(f"Failed to load graph {self.name}: {str(e)}")
            raise

    def get_input_schema(self) -> Dict[str, Any]:
        """Extract input schema from graph"""
        if not self._graph:
            self._graph = self.load_graph()

        if hasattr(self._graph, "input_schema"):
            return self._graph.input_schema
        return {}


class LangGraphConfig:
    def __init__(self, config_path: str = "langgraph.json"):
        self.config_path = config_path
        self._config: Optional[Dict[str, Any]] = None
        self._graphs: List[GraphConfig] = []

    @property
    def exists(self) -> bool:
        """Check if langgraph.json exists"""
        return os.path.exists(self.config_path)

    def load_config(self) -> Dict[str, Any]:
        """Load and validate langgraph configuration"""
        if not self.exists:
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        try:
            with open(self.config_path, "r") as f:
                config = json.load(f)

            required_fields = ["graphs"]
            missing_fields = [field for field in required_fields if field not in config]
            if missing_fields:
                raise ValueError(
                    f"Missing required fields in langgraph.json: {missing_fields}"
                )

            self._config = config
            self._load_graphs()
            return config
        except Exception as e:
            logger.error(f"Failed to load langgraph.json: {str(e)}")
            raise

    def _load_graphs(self):
        """Load all graph configurations"""
        if not self._config:
            return

        self._graphs = [
            GraphConfig.from_config(name, path)
            for name, path in self._config["graphs"].items()
        ]

    @property
    def graphs(self) -> List[GraphConfig]:
        """Get all graph configurations"""
        if not self._graphs:
            self.load_config()
        return self._graphs

    def get_graph(self, name: str) -> Optional[GraphConfig]:
        """Get a specific graph configuration by name"""
        return next((g for g in self.graphs if g.name == name), None)

    @property
    def dependencies(self) -> List[str]:
        """Get project dependencies"""
        return self._config.get("dependencies", []) if self._config else []

    @property
    def env_file(self) -> Optional[str]:
        """Get environment file path"""
        return self._config.get("env") if self._config else None
