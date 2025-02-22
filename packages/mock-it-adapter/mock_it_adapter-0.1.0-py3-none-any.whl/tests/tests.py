from src.mock_it_adapter.client import MockITClient

client = MockITClient(base_url="http://localhost:20000")
# resource = client.create_mock(
#     method="POST",
#     endpoint="/test_adapter_2",
#     name="test_adapter_name",
#     response_body="Matcher_test",
#     matcher=Matcher(matcher_type=MatcherType.KEY_TO_VALUE, key="test_key2", value="111"),
# )

resource = client.create_mock(
    method="POST",
    endpoint="/test_adapter_3",
    response_body="Matcher_test"
)
print(resource)
