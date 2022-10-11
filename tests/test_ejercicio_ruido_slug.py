#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ejercicio_ruido_slug` package."""


import unittest
from click.testing import CliRunner

from ejercicio_ruido_slug import ejercicio_ruido_slug
from ejercicio_ruido_slug import cli


class TestEjercicio_ruido_slug(unittest.TestCase):
    """Tests for `ejercicio_ruido_slug` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        pass

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_000_something(self):
        """Test something."""
        pass

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'ejercicio_ruido_slug.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

if __name__ == "__main__":
    unittest.main()
