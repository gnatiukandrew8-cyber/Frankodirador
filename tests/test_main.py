"""
Tests for the main application module.
"""

import pytest
from src.main import Application, hello_world


class TestApplication:
    """Test cases for Application class."""

    def test_application_initialization(self):
        """Test that application initializes correctly."""
        app = Application("TestApp")
        assert app.name == "TestApp"
        assert app.running is False

    def test_application_start(self):
        """Test starting the application."""
        app = Application("TestApp")
        app.start()
        assert app.running is True

    def test_application_stop(self):
        """Test stopping the application."""
        app = Application("TestApp")
        app.start()
        app.stop()
        assert app.running is False

    def test_get_status_running(self):
        """Test getting status when application is running."""
        app = Application("TestApp")
        app.start()
        assert app.get_status() == "running"

    def test_get_status_stopped(self):
        """Test getting status when application is stopped."""
        app = Application("TestApp")
        assert app.get_status() == "stopped"


class TestHelloWorld:
    """Test cases for hello_world function."""

    def test_hello_world_default(self):
        """Test hello_world with default argument."""
        result = hello_world()
        assert result == "Hello, World!"

    def test_hello_world_custom_name(self):
        """Test hello_world with custom name."""
        result = hello_world("Alice")
        assert result == "Hello, Alice!"

    def test_hello_world_empty_string(self):
        """Test hello_world with empty string."""
        result = hello_world("")
        assert result == "Hello, !"
