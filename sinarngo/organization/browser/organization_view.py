from five import grok
from plone.directives import dexterity, form
from sinarngo.organization.content.organization import IOrganization

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IOrganization)
    grok.require('zope2.View')
    grok.template('organization_view')
    grok.name('view')

