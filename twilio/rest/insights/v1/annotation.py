# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class AnnotationList(ListResource):

    def __init__(self, version):
        """
        Initialize the AnnotationList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.insights.v1.annotation.AnnotationList
        :rtype: twilio.rest.insights.v1.annotation.AnnotationList
        """
        super(AnnotationList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, call_sid):
        """
        Constructs a AnnotationContext

        :param call_sid: The call_sid

        :returns: twilio.rest.insights.v1.annotation.AnnotationContext
        :rtype: twilio.rest.insights.v1.annotation.AnnotationContext
        """
        return AnnotationContext(self._version, call_sid=call_sid, )

    def __call__(self, call_sid):
        """
        Constructs a AnnotationContext

        :param call_sid: The call_sid

        :returns: twilio.rest.insights.v1.annotation.AnnotationContext
        :rtype: twilio.rest.insights.v1.annotation.AnnotationContext
        """
        return AnnotationContext(self._version, call_sid=call_sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.AnnotationList>'


class AnnotationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AnnotationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.annotation.AnnotationPage
        :rtype: twilio.rest.insights.v1.annotation.AnnotationPage
        """
        super(AnnotationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AnnotationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.annotation.AnnotationInstance
        :rtype: twilio.rest.insights.v1.annotation.AnnotationInstance
        """
        return AnnotationInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.AnnotationPage>'


class AnnotationContext(InstanceContext):

    def __init__(self, version, call_sid):
        """
        Initialize the AnnotationContext

        :param Version version: Version that contains the resource
        :param call_sid: The call_sid

        :returns: twilio.rest.insights.v1.annotation.AnnotationContext
        :rtype: twilio.rest.insights.v1.annotation.AnnotationContext
        """
        super(AnnotationContext, self).__init__(version)

        # Path Solution
        self._solution = {'call_sid': call_sid, }
        self._uri = '/Voice/{call_sid}/Annotation'.format(**self._solution)

    def update(self, answered_by=values.unset, connectivity_issue=values.unset,
               quality_issues=values.unset, spam=values.unset,
               call_score=values.unset, comment=values.unset,
               incident=values.unset):
        """
        Update the AnnotationInstance

        :param AnnotationInstance.AnsweredBy answered_by: The answered_by
        :param AnnotationInstance.ConnectivityIssue connectivity_issue: The connectivity_issue
        :param unicode quality_issues: The quality_issues
        :param bool spam: The spam
        :param unicode call_score: The call_score
        :param unicode comment: The comment
        :param unicode incident: The incident

        :returns: The updated AnnotationInstance
        :rtype: twilio.rest.insights.v1.annotation.AnnotationInstance
        """
        data = values.of({
            'AnsweredBy': answered_by,
            'ConnectivityIssue': connectivity_issue,
            'QualityIssues': quality_issues,
            'Spam': spam,
            'CallScore': call_score,
            'Comment': comment,
            'Incident': incident,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return AnnotationInstance(self._version, payload, call_sid=self._solution['call_sid'], )

    def fetch(self):
        """
        Fetch the AnnotationInstance

        :returns: The fetched AnnotationInstance
        :rtype: twilio.rest.insights.v1.annotation.AnnotationInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AnnotationInstance(self._version, payload, call_sid=self._solution['call_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.AnnotationContext {}>'.format(context)


class AnnotationInstance(InstanceResource):

    class AnsweredBy(object):
        UNKNOWN_ANSWERED_BY = "unknown_answered_by"
        HUMAN = "human"
        MACHINE = "machine"

    class ConnectivityIssue(object):
        UNKNOWN_CONNECTIVITY_ISSUE = "unknown_connectivity_issue"
        NO_CONNECTIVITY_ISSUE = "no_connectivity_issue"
        INVALID_NUMBER = "invalid_number"
        CALLER_ID = "caller_id"
        DROPPED_CALL = "dropped_call"
        NUMBER_REACHABILITY = "number_reachability"

    class QualityIssues(object):
        UNKNOWN_QUALITY_ISSUE = "unknown_quality_issue"
        NO_QUALITY_ISSUE = "no_quality_issue"
        LOW_VOLUME = "low_volume"
        CHOPPY_ROBOTIC = "choppy_robotic"
        ECHO = "echo"
        DTMF = "dtmf"
        LATENCY = "latency"
        OWA = "owa"
        STATIC_NOISE = "static_noise"

    def __init__(self, version, payload, call_sid=None):
        """
        Initialize the AnnotationInstance

        :returns: twilio.rest.insights.v1.annotation.AnnotationInstance
        :rtype: twilio.rest.insights.v1.annotation.AnnotationInstance
        """
        super(AnnotationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'call_sid': payload.get('call_sid'),
            'account_sid': payload.get('account_sid'),
            'answered_by': payload.get('answered_by'),
            'connectivity_issue': payload.get('connectivity_issue'),
            'quality_issues': payload.get('quality_issues'),
            'spam': payload.get('spam'),
            'call_score': deserialize.integer(payload.get('call_score')),
            'comment': payload.get('comment'),
            'incident': payload.get('incident'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'call_sid': call_sid or self._properties['call_sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: AnnotationContext for this AnnotationInstance
        :rtype: twilio.rest.insights.v1.annotation.AnnotationContext
        """
        if self._context is None:
            self._context = AnnotationContext(self._version, call_sid=self._solution['call_sid'], )
        return self._context

    @property
    def call_sid(self):
        """
        :returns: The call_sid
        :rtype: unicode
        """
        return self._properties['call_sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def answered_by(self):
        """
        :returns: The answered_by
        :rtype: AnnotationInstance.AnsweredBy
        """
        return self._properties['answered_by']

    @property
    def connectivity_issue(self):
        """
        :returns: The connectivity_issue
        :rtype: AnnotationInstance.ConnectivityIssue
        """
        return self._properties['connectivity_issue']

    @property
    def quality_issues(self):
        """
        :returns: The quality_issues
        :rtype: list[unicode]
        """
        return self._properties['quality_issues']

    @property
    def spam(self):
        """
        :returns: The spam
        :rtype: bool
        """
        return self._properties['spam']

    @property
    def call_score(self):
        """
        :returns: The call_score
        :rtype: unicode
        """
        return self._properties['call_score']

    @property
    def comment(self):
        """
        :returns: The comment
        :rtype: unicode
        """
        return self._properties['comment']

    @property
    def incident(self):
        """
        :returns: The incident
        :rtype: unicode
        """
        return self._properties['incident']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, answered_by=values.unset, connectivity_issue=values.unset,
               quality_issues=values.unset, spam=values.unset,
               call_score=values.unset, comment=values.unset,
               incident=values.unset):
        """
        Update the AnnotationInstance

        :param AnnotationInstance.AnsweredBy answered_by: The answered_by
        :param AnnotationInstance.ConnectivityIssue connectivity_issue: The connectivity_issue
        :param unicode quality_issues: The quality_issues
        :param bool spam: The spam
        :param unicode call_score: The call_score
        :param unicode comment: The comment
        :param unicode incident: The incident

        :returns: The updated AnnotationInstance
        :rtype: twilio.rest.insights.v1.annotation.AnnotationInstance
        """
        return self._proxy.update(
            answered_by=answered_by,
            connectivity_issue=connectivity_issue,
            quality_issues=quality_issues,
            spam=spam,
            call_score=call_score,
            comment=comment,
            incident=incident,
        )

    def fetch(self):
        """
        Fetch the AnnotationInstance

        :returns: The fetched AnnotationInstance
        :rtype: twilio.rest.insights.v1.annotation.AnnotationInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.AnnotationInstance {}>'.format(context)