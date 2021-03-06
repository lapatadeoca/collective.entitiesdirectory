"""Base class for integration tests, based on ZopeTestCase and PloneTestCase.

Note that importing this module has various side-effects: it registers a set of
products with Zope, and it sets up a sandbox Plone site with the appropriate
products installed.
"""

from Testing import ZopeTestCase
from Products.Five import zcml
from Products.Five import fiveconfigure

# Import PloneTestCase - this registers more products with Zope as a side effect
from Products.PloneTestCase.PloneTestCase import PloneTestCase
from Products.PloneTestCase.PloneTestCase import FunctionalTestCase
from Products.PloneTestCase.PloneTestCase import setupPloneSite
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_entitiesdirectory():
    fiveconfigure.debug_mode = True
    import collective.entitiesdirectory
    zcml.load_config('configure.zcml', collective.entitiesdirectory)
    fiveconfigure.debug_mode = False
    
    # Let Zope know about the products we require above-and-beyond a basic
    # Plone install (PloneTestCase takes care of these).
    ZopeTestCase.installPackage('collective.entitiesdirectory')

# Set up a Plone site, and quick-install the relevant products
setup_entitiesdirectory()
setupPloneSite(products=('collective.entitiesdirectory',))

class EntitiesDirectoryTestCase(PloneTestCase):
    """Base class for integration tests. 
    
    This may provide specific set-up and tear-down operations, or provide 
    convenience methods.
    """
    
class EntitiesDirectoryFunctionalTestCase(FunctionalTestCase):
    """Base class for functional integration tests. 
    
    This may provide specific set-up and tear-down operations, or provide 
    convenience methods.
    """