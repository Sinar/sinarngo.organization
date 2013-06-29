from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from collective import dexteritytextindexer

from sinarngo.organization import MessageFactory as _

# Interface class; used to define content-type schema.

class IOrganization(form.Schema, IImageScaleTraversable):
    """
    Organizations
    """

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(title=u'Name', 
                         description=u'Name of organization.')

    dexteritytextindexer.searchable('title')
    description = schema.Text(title=u'Description',
                                  description=u'Brief description '
                                  'of organization.'
                                  )

    dexteritytextindexer.searchable('details')
    details = RichText(
                title=_(u"Details"),
                required=False,
            ) 

    organization_type = schema.Choice(
        title=_(u'Type'),
        vocabulary = "ploneun.vocabularies.organizations.types"
    )

    website = schema.TextLine(title=u'Website',
            description=u'Enter url eg. http://sinarproject.org',
                              required=False)

    gpluspage = schema.TextLine(title=u'Google+ Page',
                                description=u'Enter url eg. https://plus.google.com/101396658148522528050 ',
                                required=False)
 
    fbpage = schema.TextLine(title=u'FaceBook Page',
            description=u'Enter url eg. '
            'https://www.facebook.com/organization',
                                required=False)

    twitter = schema.TextLine(title=u'Twitter',
            description=u'Enter url eg. '
            'https://twitter.com/sinarproject.org',
                                required=False)
