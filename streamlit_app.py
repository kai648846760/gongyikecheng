# import streamlit as st
# import requests

# def get_xueqi():
#     headers = {
#         'Accept': 'application/json, text/plain, */*',
#         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/json',
#         'Origin': 'https://lianmeng.hetao101.com',
#         'Referer': 'https://lianmeng.hetao101.com/',
#         'Sec-Fetch-Dest': 'empty',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Site': 'same-site',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
#         'authorization': st.secrets['token'],
#         'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"macOS"',
#     }

#     params = ''

#     response = requests.get(
#         'https://api.hetao101.com/ug-agent-back/v1/token/star/mobile/btoc/terms',
#         params=params,
#         headers=headers,
#     )
#     return response.json()['data']

# def get_people(xueqi):
#     headers = {
#         'Accept': 'application/json, text/plain, */*',
#         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/json',
#         'Origin': 'https://lianmeng.hetao101.com',
#         'Referer': 'https://lianmeng.hetao101.com/',
#         'Sec-Fetch-Dest': 'empty',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Site': 'same-site',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
#         'authorization': st.secrets['token'],
#         'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"macOS"',
#     }

#     json_data = {
#         'team_id': '12628952',
#         'b2c_term_tag_names': [
#             xueqi,
#         ],
#     }

#     response = requests.post(
#         'https://api.hetao101.com/ug-agent-back/v1/token/star/mobile/btoc/term/sumOnline',
#         headers=headers,
#         json=json_data,
#     )
#     return response.json()

# people_list = [ get_people(x['termTagName'])['data'] for x in get_xueqi() ]

# st.title("🎈 公益课程人数展示")
# for i in people_list:
#     if i:
#         st.write(
#             f"当前季度 {i[0]['b2c_term_tag_name']} .  该季度当前公益课人数：{i[0]['get_account_num_str']} 人"
#         )
#     else:
#         pass
import streamlit as st
import requests


# 设置页面配置
st.set_page_config(
    page_title="公益课程人数展示",
    page_icon="🎈",
    layout="centered"
)


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


# 显示加载提示
with st.spinner('正在获取数据...'):
    people_list = [get_people(x['termTagName'])['data'] for x in get_xueqi()]

# 美化标题
st.markdown("<h1 style='text-align: center; color: #007BFF; text-shadow: 2px 2px 4px #ccc;'>🎈 公益课程人数展示</h1>", unsafe_allow_html=True)

# 定义卡片样式（支持暗黑模式）
card_style = """
<style>
/* 亮色主题样式 */
@media (prefers-color-scheme: light) {
    .card {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #f9f9f9;
        color: #333;
    }
    .separator {
        border-top: 1px solid #e0e0e0;
        margin: 20px 0;
    }
}
/* 暗黑主题样式 */
@media (prefers-color-scheme: dark) {
    .card {
        border: 1px solid #444;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        background-color: #333;
        color: #fff;
    }
    .separator {
        border-top: 1px solid #444;
        margin: 20px 0;
    }
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# 显示每个人数信息
for i in people_list:
    if i:
        st.markdown(
            f'<div class="card">季度 <strong>{i[0]["b2c_term_tag_name"]}</strong> .  该季度当前公益课人数：<strong>{i[0]["get_account_num_str"]}</strong> 人</div>',
            unsafe_allow_html=True
        )
        st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
    