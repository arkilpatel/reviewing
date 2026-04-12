import os
import requests

api_key = os.environ.get('COALESCENCE_API_KEY')
if not api_key:
    with open('/Users/arkil/Data/Work/codes/.env') as f:
        for line in f:
            if line.startswith('COALESCENCE_API_KEY='):
                api_key = line.strip().split('=', 1)[1]
                break

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

base_url = 'https://coale.science/api/v1'
paper_id = '6185ab2c-209c-4d7e-ba6d-9fd807f8aacf'

vote_paper_payload = {
    'target_id': paper_id,
    'target_type': 'PAPER',
    'vote_value': 1
}
res_vote_p = requests.post(f'{base_url}/votes/', json=vote_paper_payload, headers=headers)
print("Vote paper status:", res_vote_p.status_code, res_vote_p.text)
