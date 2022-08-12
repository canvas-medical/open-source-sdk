from canvas_workflow_kit.protocol import (
    ClinicalQualityMeasure,
    ProtocolResult,
    STATUS_DUE,
    STATUS_SATISFIED,
)
from canvas_workflow_kit.constants import CHANGE_TYPE
from canvas_workflow_kit.recommendation import ImmunizationRecommendation
from canvas_workflow_kit.value_set import ValueSet
from canvas_workflow_kit.timeframe import Timeframe

from canvas_workflow_kit.value_set.v2022.immunization import InfluenzaVaccine as FluShot
"""
This will be used as the patient.immunizations.find() parameter to identify if a patient has
received any of these immmunizations. A single immunization from this list on record will satisfy
the protocol.
"""



"""
A protocol that tests whether an individual has received a flu shot in the last year.
"""



class FluShotRec(ValueSet):
    """
    Creates a class from the Value set that includes the value code and name of the immunization.
    This will be used to populate the immunize command on the Canvas UI. If more than one code is used, the
    last item in the list (after normalization) will be used. Because you cannot specify the ordering of the
    list, we strongly recommend only adding a single code here to ensure expected behavior.
    """
    VALUE_SET_NAME = 'Influenza, seasonal, injectable'
    CVX ={'141'}  # Influenza, seasonal, injectable

class Rotavirus(ValueSet):
    VALUE_SET_NAME = 'Rotavirus Vaccine (3 dose schedule) Administered'
    CPT ={'90680',}


class ImmunizationProtocol(ClinicalQualityMeasure):

    class Meta:
        """
        title: String that describes the recommendation. It will be displayed in bold at the top of the protocol
        box.

        description: String that contains additional information about the recommendation. It will be displayed under the
        title in the populations view.

        version: String that tracks the version of the protocol. It must be unique each time the protocol is uploaded.
        If it is not updated, the upload will error. To get around updating the version for an upload, you can use the
        --force command at the end of the upload command (e.g. canvas-cli upload imagingProtocol.py --force).

        information: This is for the URL that populates in the More Info link for each Protocol listed on the
        Populations section of the UI.

        identifiers: This is a list of identifiers associated with the Protocol. These are sometimes populated with
        eCQI codes (i.e. CMS125v6), but can also be populated with strings of your choice to identify your custom
        Protocols. In the Canvas UI, these are populated underneath the Protocol title in a patient's chart.

        types: List that contains the abbreviation of a type of protocol. These are populated in parentheses next to
        identifiers in the Protocols section of a patient's chart.

        compute_on_change_type: a list of change types that signal the protocol to re-run against a patient. supported
        change types can be found here (https://docs.canvasmedical.com/docs/event-types). This protocol re-computes on any
        immunization that is administered to a patient.

        references: this is a list of URLs that show up under the information button on the protocol tab of the patient's
        page.
        """

        title = 'Annual Flu Shot'

        description = 'Reminder for all patients to get a flu shot annually.'

        version = '2022-07-07v7'

        information = 'https://www.cdc.gov/flu/prevent/flushot.htm'

        identifiers = ['ACM02']

        types = ['CQM']

        compute_on_change_types = [
            CHANGE_TYPE.IMMUNIZATION,
        ]

        references = [
            'https://www.mayoclinic.org/diseases-conditions/flu/in-depth/flu-shots/art-20048000'
        ]

    def in_denominator(self):
        """
        Patients in the initial population. Since all patients qualify for an annual flu shot,
        it always returns true.
        """
        return True

    def in_numerator(self):
        """
        Determines which patients who are a part of the initial population have already satisfied the recommendation.
        If a patient has received a flu shot, it will return true. Otherwise, it will return false.
        """
        last_immunization_timeframe = Timeframe(self.now.shift(years=-1), self.now)
        immunization_completed = self.patient.immunizations.find(
            FluShot
        ).within(last_immunization_timeframe)
        return bool(immunization_completed)


    def compute_results(self):
        """
        An immunization recommendation is created with the following attributes:

        - key is used as a unique code to access the recommendation.

        - rank is utilized if there are multiple recommendations within a single protocol. Since this protocol only has
        one recommendation, rank is set to 1.

        - button stores a string that will display on the protocol window. Since we are recommending a vaccine, it has been
        set to 'immunize'

        - patient is always going to be set to self.patient

        - immunization is a class that contains codings that map to specific immunizations. The valueset must be imported.
        A valid coding will result in the immunization command being autofilled with this vaccine. If multiple codes are
        entered, the autofill feature will default to the item that is ordered last in the list.

        - title is used to display next to the button.

        - narrative displays under the title of the protocol on the patient's protocols page via line 196
        (result.add_narrative(immunization_recommendation.narrative)). Without this, it will not display on the UI.

        - context is a dictionary that optionally may include a 'sig' key that maps to a string. This string, if included
        will populate the sig field within the immunize command.

        """
        immunization_recommendation = ImmunizationRecommendation(
            key='RECOMMEND_INFLUENZA_VACCINE',
            rank=1,
            button='Immunize',
            patient=self.patient,
            immunization=FluShotRec, #ValueSet with a single code in it
            title='Perform a Influenza Immunization',
            narrative='Administer an annual flu vaccine',
            context={'sig': 'This the sig'}
        )
        result = ProtocolResult()
        if self.in_denominator(): # All patients qualify to be part of this population
            if self.in_numerator(): # Has already received a flu vaccine this year
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f'{self.patient.first_name} has already been immunized this year.'
                )
            else: # Has not gotten the flu shot this year.
                result.status = STATUS_DUE
                result.due_in = -1
                result.add_recommendation(
                    immunization_recommendation
                )
                result.add_narrative(immunization_recommendation.narrative)
        return result
