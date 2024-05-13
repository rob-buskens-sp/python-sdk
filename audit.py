import sailpoint
import sailpoint.v3
import sailpoint.beta
import logging

from sailpoint.configuration import Configuration
from sailpoint.paginator import Paginator
import sailpoint.v3.models
from sailpoint.v3.models.search import Search
from pprint import pprint
from urllib3 import Retry

# from http.client import HTTPConnection

if __name__ == '__main__':
    logging.basicConfig(filename='audit.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=getattr(logging, "DEBUG"))
                        
    # HTTPConnection.debuglevel = 1 # Low level, goes to stdout
    # Requests logging
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel('DEBUG')
    requests_log.propagate = True

    configuration = Configuration()
    configuration.retries = Retry(
            total = 5,
            respect_retry_after_header = True
        )

    with sailpoint.v3.ApiClient(configuration) as v3_client, \
        sailpoint.beta.ApiClient(configuration) as beta_client:

        search = sailpoint.v3.Search(
            indices=['events'], 
            query=sailpoint.v3.Query(query='type:*'),
            sort=['id'])
        
        searchDocuments = Paginator.paginate_search(sailpoint.v3.SearchApi(v3_client), search=search, increment=100, limit=1000)

        print(len(searchDocuments))

        print(f'{"created":<35} {"name":<40} {"actor name":<20} {"target name":<20}')

        for searchDocument in searchDocuments:
            if isinstance(searchDocument.actual_instance, sailpoint.v3.models.EventDocument):
                event = searchDocument.actual_instance
                created = event.created.isoformat()
                name = event.name
                actor_name = event.actor.name or ''
                target_name = event.target.name or ''

                print(f'{created:<35} {name:<40} {actor_name:<20} {target_name:<20}')
            else:
                print(type(searchDocument.actual_instance))


