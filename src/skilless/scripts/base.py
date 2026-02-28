"""Base tool class for Skilless tools."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class DoctorResult:
    """Result of a tool health check."""

    status: str  # "OK", "FAIL", "OFF"
    detail: str


class BaseTool(ABC):
    """Base class for all Skilless tools.

    Each tool provides:
    - doctor(): health check
    - run(): execute the tool
    - troubleshooting: common problem/solution pairs
    """

    name: str = ""
    description: str = ""
    usage: str = ""
    how: str = ""

    @abstractmethod
    def doctor(self) -> DoctorResult:
        """Check if this tool is available and working."""
        ...

    @abstractmethod
    def run(self, args: list[str]) -> str:
        """Execute the tool. Returns plain text output."""
        ...

    @property
    def troubleshooting(self) -> list[tuple[str, str]]:
        """Return list of (problem, solution) pairs."""
        return []
