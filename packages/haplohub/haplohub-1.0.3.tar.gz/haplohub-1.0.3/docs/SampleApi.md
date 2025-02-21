# haplohub.SampleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hgvs_dosage**](SampleApi.md#hgvs_dosage) | **GET** /api/v1/sample/ | Fetch the dosage of a given allele for a sample based on the hgvs nomenclature. For example &#39;NC_000001.11:g.11794419T&gt;G&#39;


# **hgvs_dosage**
> GetHgvsResponse hgvs_dosage(sample_id, description)

Fetch the dosage of a given allele for a sample based on the hgvs nomenclature. For example 'NC_000001.11:g.11794419T>G'

### Example

* Bearer Authentication (ApiAuthBearer):
```python
import time
import os
import haplohub
from haplohub.models.get_hgvs_response import GetHgvsResponse
from haplohub.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: 
configuration = haplohub.Configuration(
    access_token=os.environ["API_KEY"]
)

# Enter a context with an instance of the API client
with haplohub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = haplohub.SampleApi(api_client)
    sample_id = 'sample_id_example' # str | 
    description = 'description_example' # str | 

    try:
        # Fetch the dosage of a given allele for a sample based on the hgvs nomenclature. For example 'NC_000001.11:g.11794419T>G'
        api_response = api_instance.hgvs_dosage(sample_id, description)
        print("The response of SampleApi->hgvs_dosage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->hgvs_dosage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **str**|  | 
 **description** | **str**|  | 

### Return type

[**GetHgvsResponse**](GetHgvsResponse.md)

### Authorization

[ApiAuthBearer](../README.md#ApiAuthBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

