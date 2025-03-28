import streamlit as st
import requests

def get_xueqi():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://lianmeng.hetao101.com',
        'Referer': 'https://lianmeng.hetao101.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
        'authorization': st.secrets['token'],
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = ''

    response = requests.get(
        'https://api.hetao101.com/ug-agent-back/v1/token/star/mobile/btoc/terms',
        params=params,
        headers=headers,
    )
    return response.json()['data']

def get_people(xueqi):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://lianmeng.hetao101.com',
        'Referer': 'https://lianmeng.hetao101.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
        'authorization': st.secrets['token'],
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    json_data = {
        'team_id': '12628952',
        'b2c_term_tag_names': [
            xueqi,
        ],
    }

    response = requests.post(
        'https://api.hetao101.com/ug-agent-back/v1/token/star/mobile/btoc/term/sumOnline',
        headers=headers,
        json=json_data,
    )
    return response.json()

people_list = [ get_people(x['termTagName'])['data'] for x in get_xueqi() ]

st.title("🎈 公益课程人数展示")
for i in people_list:
    if i:
        st.write(
            f"当前季度 {i[0]['b2c_term_tag_name']} .  该季度对应人数：{i[0]['get_account_num_str']} 人"
        )
    else:
        pass
