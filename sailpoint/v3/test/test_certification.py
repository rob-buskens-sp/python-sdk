# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from v3.models.certification import Certification  # noqa: E501

class TestCertification(unittest.TestCase):
    """Certification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Certification:
        """Test Certification
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Certification`
        """
        model = Certification()  # noqa: E501
        if include_optional:
            return Certification(
                id = '2c9180835d2e5168015d32f890ca1581',
                name = 'Source Owner Access Review for Employees [source]',
                campaign = v3.models.campaign_reference.CampaignReference(
                    id = 'ef38f94347e94562b5bb8424a56397d8', 
                    name = 'Campaign Name', 
                    type = 'CAMPAIGN', 
                    campaign_type = 'MANAGER', 
                    description = 'A description of the campaign', 
                    correlated_status = CORRELATED, 
                    mandatory_comment_requirement = 'NO_DECISIONS', ),
                completed = True,
                identities_completed = 5,
                identities_total = 10,
                created = '2018-06-25T20:22:28.104Z',
                modified = '2018-06-25T20:22:28.104Z',
                decisions_made = 20,
                decisions_total = 40,
                due = '2018-10-19T13:49:37.385Z',
                signed = '2018-10-19T13:49:37.385Z',
                reviewer = v3.models.reviewer.Reviewer(
                    id = 'ef38f94347e94562b5bb8424a56397d8', 
                    name = 'Reviewer Name', 
                    email = 'reviewer@test.com', 
                    type = 'IDENTITY', 
                    created = '2018-06-25T20:22:28.104Z', 
                    modified = '2018-06-25T20:22:28.104Z', ),
                reassignment = v3.models.reassignment.Reassignment(
                    from = v3.models.certification_reference.CertificationReference(
                        id = 'ef38f94347e94562b5bb8424a56397d8', 
                        name = 'Certification Name', 
                        type = 'CERTIFICATION', 
                        reviewer = v3.models.reviewer.Reviewer(
                            id = 'ef38f94347e94562b5bb8424a56397d8', 
                            name = 'Reviewer Name', 
                            email = 'reviewer@test.com', 
                            type = 'IDENTITY', 
                            created = '2018-06-25T20:22:28.104Z', 
                            modified = '2018-06-25T20:22:28.104Z', ), ), 
                    comment = 'Reassigned for a reason', ),
                has_errors = False,
                error_message = 'The certification has an error',
                phase = 'ACTIVE'
            )
        else:
            return Certification(
        )
        """

    def testCertification(self):
        """Test Certification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
