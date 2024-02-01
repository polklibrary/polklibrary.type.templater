# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from polklibrary.type.templater.testing import POLKLIBRARY_TYPE_TEMPLATER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that polklibrary.type.templater is properly installed."""

    layer = POLKLIBRARY_TYPE_TEMPLATER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if polklibrary.type.templater is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('polklibrary.type.templater'))

    def test_browserlayer(self):
        """Test that IPolklibraryTypeTemplaterLayer is registered."""
        from polklibrary.type.templater.interfaces import IPolklibraryTypeTemplaterLayer
        from plone.browserlayer import utils
        self.assertIn(IPolklibraryTypeTemplaterLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLKLIBRARY_TYPE_TEMPLATER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['polklibrary.type.templater'])

    def test_product_uninstalled(self):
        """Test if polklibrary.type.templater is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('polklibrary.type.templater'))

    def test_browserlayer_removed(self):
        """Test that IPolklibraryTypeTemplaterLayer is removed."""
        from polklibrary.type.templater.interfaces import IPolklibraryTypeTemplaterLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPolklibraryTypeTemplaterLayer, utils.registered_layers())
