from client.digestor_client import DigestorClient

if __name__ == '__main__':

	print('************* Using gRPC *******************')
	curr_client = DigestorClient()
	print(curr_client.get_digest("Test Message"))
	print('************* SUCCESS *******************')

	print('************* Using RestGateway *******************')
	try:
		import requests
		import json
		payload_str = '{"Test Message"}'
		payload_json = json.dumps(payload_str)
		requests.post(url='http://localhost:46001/v1/digest', data=payload_json)
	except Exception as e:
		print("Got Exception" + e.message)
