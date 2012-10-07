from plone.testing.z2 import ZSERVER_FIXTURE

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig

from mocker import Mocker
from mocker import ANY


class ExampleTddLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Mock postmonkey
        mocker = Mocker()
        postmonkey = mocker.replace("postmonkey")
        mailchimp = postmonkey.PostMonkey(ANY)
        mocker.count(0, 1000)
        # Lists
        mailchimp.lists()
        mocker.count(0, 1000)
        mocker.result({
            u'total': 2,
            u'data': [{
                    u'id': 625,
                    u'web_id': 625,
                    u'name': u'ACME Newsletter',
                    u'default_from_name': u'info@acme.com',
                },
                {
                    u'id': 626,
                    u'web_id': 626,
                    u'name': u'ACME Newsletter 2',
                    u'default_from_name': u'info@acme.com',
                },
            ]})
        mocker.replay()

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
