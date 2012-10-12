# -*- coding: utf-8 -*-
import unittest2 as unittest

import ExtensionClass
import Acquisition
from Acquisition import aq_chain

from zope.interface import implements

from Products.CMFCore.interfaces import IFolderish


# IMPLEMENTATION

def update_document_title_when_object_is_modified(obj, event):
    """Traverse acquision chain until a folderish object is found.
       Include the title of this folderish object as prefix in the
       title of the current object.
    """
    traverse_folder = [
        x for x in aq_chain(obj)
        if IFolderish.providedBy(x)
    ]
    if len(traverse_folder) > 0:
        obj.title = "%s: %s" % (
            traverse_folder[0].title,
            obj.title,
        )


# TESTS

class MockFolder(ExtensionClass.Base):
    implements(IFolderish)

    def __init__(self, title):
        self.title = title

    def Title(self):
        return self.title


class MockDocument(Acquisition.Implicit):

    def __init__(self, title):
        self.title = title


class UpdateDocumentTitleUnitTest(unittest.TestCase):

    def setUp(self):
        folder = MockFolder("Test Folder")
        document = MockDocument("Test Document")
        document.__of__(folder)
        document.__parent__ = folder
        self.folder = folder
        self.document = document

    def test_document_title_should_contain_folder_title(self):
        update_document_title_when_object_is_modified(self.document, None)
        self.assertTrue("Test Document" in self.document.title)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
