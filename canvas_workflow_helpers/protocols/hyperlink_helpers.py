from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import STATUS_DUE, ClinicalQualityMeasure, ProtocolResult
from canvas_workflow_kit.recommendation import HyperlinkRecommendation


class HyperlinkHelpers(ClinicalQualityMeasure):
    """
    Protocol that creates external dynamic hyperlinks at the top of the protocol list
    """

    class Meta:
        title = 'External Links'

        version = 'v1.0.0'

        description = 'Creates external dynamic hyperlinks at the top of the protocol list'

        information = 'https://canvasmedical.com/'

        identifiers = ['ExternalLinks']

        types = ['Links']

        references = ['Links to external resources about the patient']

        responds_to_event_types = [
            events.HEALTH_MAINTENANCE,
        ]

        authors = ['Canvas Medical']

        funding_source = ''

        can_be_snoozed = False

    def patient_external_id(self):
        if self.patient.patient.get('externalIdentifiers'):
            external_identifiers = self.patient.patient['externalIdentifiers']
            if len(external_identifiers):
                return external_identifiers[0]['value']
        return ''

    def compute_results(self):
        result = ProtocolResult()

        external_id = self.patient_external_id

        result.add_recommendation(
            HyperlinkRecommendation(
                key='EXTERNAL_LINK_1',
                rank=1,
                button='Open',
                href=f'https://www.google.com/search?q=broccoli+{external_id}',
                title='Meal plan',
            ))
        result.add_recommendation(
            HyperlinkRecommendation(
                key='EXTERNAL_LINKS2',
                rank=2,
                button='Open',
                href=f'https://www.google.com/search?q=medicine+{external_id}',
                title='Medicine plan',
            ))

        result.add_recommendation(
            HyperlinkRecommendation(
                key='EXTERNAL_LINKS3',
                rank=3,
                button='Open',
                href=f'https://www.google.com/search?q=limousine+{external_id}',
                title='Transportation plan',
            ))

        result.status = STATUS_DUE

        return result