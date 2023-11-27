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

from sailpoint.beta.models.account_aggregation_completed import AccountAggregationCompleted  # noqa: E501


class TestAccountAggregationCompleted(unittest.TestCase):
    """AccountAggregationCompleted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountAggregationCompleted:
        """Test AccountAggregationCompleted
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountAggregationCompleted`
        """
        model = AccountAggregationCompleted()  # noqa: E501
        if include_optional:
            return AccountAggregationCompleted(
                source = sailpoint.beta.models.account_aggregation_completed_source.AccountAggregationCompleted_source(
                    type = 'SOURCE', 
                    id = '2c9180835d191a86015d28455b4b232a', 
                    name = 'HR Active Directory', ),
                status = Success,
                started = '2020-06-29T22:01:50.474Z',
                completed = '2020-06-29T22:02:04.090Z',
                errors = [
                    'Accounts unable to be aggregated.'
                    ],
                warnings = [
                    'Account Skipped'
                    ],
                stats = sailpoint.beta.models.account_aggregation_completed_stats.AccountAggregationCompleted_stats(
                    scanned = 200, 
                    unchanged = 190, 
                    changed = 6, 
                    added = 4, 
                    removed = 3, )
            )
        else:
            return AccountAggregationCompleted(
                source = sailpoint.beta.models.account_aggregation_completed_source.AccountAggregationCompleted_source(
                    type = 'SOURCE', 
                    id = '2c9180835d191a86015d28455b4b232a', 
                    name = 'HR Active Directory', ),
                status = Success,
                started = '2020-06-29T22:01:50.474Z',
                completed = '2020-06-29T22:02:04.090Z',
                errors = [
                    'Accounts unable to be aggregated.'
                    ],
                warnings = [
                    'Account Skipped'
                    ],
                stats = sailpoint.beta.models.account_aggregation_completed_stats.AccountAggregationCompleted_stats(
                    scanned = 200, 
                    unchanged = 190, 
                    changed = 6, 
                    added = 4, 
                    removed = 3, ),
        )
        """

    def testAccountAggregationCompleted(self):
        """Test AccountAggregationCompleted"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
