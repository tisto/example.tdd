from plone.testing.z2 import ZSERVER_FIXTURE

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig


class ExampleTddLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import example.tdd
        xmlconfig.file(
            'configure.zcml',
            example.tdd,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.tdd:default')

EXAMPLE_TDD_FIXTURE = ExampleTddLayer()
EXAMPLE_TDD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EXAMPLE_TDD_FIXTURE,),
    name="ExampleTddLayer:Integration")
EXAMPLE_TDD_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(EXAMPLE_TDD_FIXTURE, ZSERVER_FIXTURE),
    name="ExampleTDD:Acceptance"
)
