# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from sailpoint.beta.models.certification_signed_off_certification import CertificationSignedOffCertification  # noqa: E501


class TestCertificationSignedOffCertification(unittest.TestCase):
    """CertificationSignedOffCertification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self,
                      include_optional) -> CertificationSignedOffCertification:
        """Test CertificationSignedOffCertification
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationSignedOffCertification`
        """
        model = CertificationSignedOffCertification()  # noqa: E501
        if include_optional:
            return CertificationSignedOffCertification(
                id = '2c91808576f886190176f88caf0d0067',
                name = 'Manager Access Review for Alice Baker',
                created = '2020-02-16T03:04:45.815Z',
                modified = '2020-02-16T03:06:45.815Z',
                campaign_ref = sailpoint.beta.models.campaign_reference.CampaignReference(
                    id = 'ef38f94347e94562b5bb8424a56397d8', 
                    name = 'Campaign Name', 
                    type = 'CAMPAIGN', 
                    campaign_type = 'MANAGER', 
                    description = 'A description of the campaign', 
                    correlated_status = CORRELATED, 
                    mandatory_comment_requirement = 'NO_DECISIONS', ),
                phase = 'ACTIVE',
                due = '2018-10-19T13:49:37.385Z',
                signed = '2018-10-19T13:49:37.385Z',
                reviewer = sailpoint.beta.models.reviewer.Reviewer(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', 
                    email = 'reviewer@test.com', ),
                reassignment = sailpoint.beta.models.reassignment.Reassignment(
                    from = sailpoint.beta.models.certification_reference.CertificationReference(), 
                    comment = 'Please review', ),
                has_errors = False,
                error_message = 'The certification has an error',
                completed = False,
                decisions_made = 20,
                decisions_total = 40,
                entities_completed = 5,
                entities_total = 10
            )
        else:
            return CertificationSignedOffCertification(
                id = '2c91808576f886190176f88caf0d0067',
                name = 'Manager Access Review for Alice Baker',
                created = '2020-02-16T03:04:45.815Z',
                campaign_ref = sailpoint.beta.models.campaign_reference.CampaignReference(
                    id = 'ef38f94347e94562b5bb8424a56397d8', 
                    name = 'Campaign Name', 
                    type = 'CAMPAIGN', 
                    campaign_type = 'MANAGER', 
                    description = 'A description of the campaign', 
                    correlated_status = CORRELATED, 
                    mandatory_comment_requirement = 'NO_DECISIONS', ),
                phase = 'ACTIVE',
                due = '2018-10-19T13:49:37.385Z',
                signed = '2018-10-19T13:49:37.385Z',
                reviewer = sailpoint.beta.models.reviewer.Reviewer(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', 
                    email = 'reviewer@test.com', ),
                has_errors = False,
                completed = False,
                decisions_made = 20,
                decisions_total = 40,
                entities_completed = 5,
                entities_total = 10,
        )
        """

    def testCertificationSignedOffCertification(self):
        """Test CertificationSignedOffCertification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
