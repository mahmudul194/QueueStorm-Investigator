import json
import requests
import time

def test_api():
    # Wait for server to start
    time.sleep(2)
    
    with open('SUST_Preli_Sample_Cases.json', 'r', encoding='utf-8') as f:
        cases = json.load(f)
        
    for i, case in enumerate(cases['cases']):
        input_data = case['input']
        response = requests.post('http://localhost:8000/analyze-ticket', json=input_data)
        
        print(f"Case {i + 1}: Status Code {response.status_code}")
        if response.status_code != 200:
            print(f"Error on case {i + 1}: {response.text}")

if __name__ == '__main__':
    test_api()
