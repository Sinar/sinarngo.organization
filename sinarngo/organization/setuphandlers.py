from collective.grok import gs
from sinarngo.organization import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.organization', 
    title=_('sinarngo.organization import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.organization.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
