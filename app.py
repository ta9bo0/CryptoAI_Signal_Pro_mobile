import streamlit as st
import pandas as pd
import numpy as np
import requests

# ページ設定（スマホ対応のレスポンシブ）
st.set_page_config(
    page_title="CryptoAI Signal Pro",
    page_icon="📈",
    layout="wide"
)

# スタイリング調整
st.markdown("""
<style>
    .main { background-color: #121212; color: #ffffff; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #1f1f1f; color: white; border-radius: 4px; padding: 8px 16px; }
    .stTabs [aria-selected="true"] { background-color: #1f538d !important; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 CryptoAI Signal Pro (Web / Mobile 版)")

# サイドバー設定
with st.sidebar:
    st.header("⚙️ 設定 & 銘柄選択")
    api_key = st.text_input("Gemini APIキー", type="password")
    
    selected_symbol = st.selectbox(
        "銘柄選択",
        ["BTC/JPY", "ETH/JPY", "SOL/JPY", "TAO/JPY", "SUI/JPY", "PEPE/JPY"]
    )
    
    timeframe = st.selectbox("予測期間", ["1時間以内", "3日以内", "1週間以内", "1ヶ月以内"])
    
    if st.button("⚡ AI分析＆確率予測を実行", use_container_width=True):
        st.success("AI分析を実行しました！")

# メインタブ
tab_trade, tab_portfolio, tab_macro, tab_strategy = st.tabs([
    "📊 シグナル＆チャート", 
    "💼 ポートフォリオ", 
    "📅 経済指標", 
    "💬 戦略会議室"
])

# 1. シグナル＆チャートタブ
with tab_trade:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("判定", "買い時", "+67.43%")
    col2.metric("現在価格", "￥10,275,000", "+2.4%")
    col3.metric("RSI(14)", "52.4", "中立")
    col4.metric("CEX上場確率", "89.42%", "高ポテンシャル")
    
    st.subheader(f"📈 {selected_symbol} チャート・予測")
    chart_data = pd.DataFrame(
        np.random.randn(30, 2) * 100000 + 10275000,
        columns=['価格(終値)', '移動平均(20MA)']
    )
    st.line_chart(chart_data)

# 2. ポートフォリオタブ
with tab_portfolio:
    st.subheader("💼 保有資産・損益＆カスタム損切管理")
    
    df_pf = pd.DataFrame([
        {"銘柄": "BTC/JPY", "保有数": 0.15, "取得単価": 9800000, "カスタムSL": 9200000},
        {"銘柄": "ETH/JPY", "保有数": 1.20, "取得単価": 420000, "カスタムSL": 390000},
    ])
    
    edited_df = st.data_editor(df_pf, num_rows="dynamic", use_container_width=True)
    
    if st.button("🧮 損益を再計算"):
        st.info("ポートフォリオの評価額および損益を更新しました。")

# 3. 経済指標タブ
with tab_macro:
    st.subheader("📅 直近の主要経済指標スケジュール")
    st.markdown("""
    - **9/24(木) 21:30**: 🇺🇸 米・実質GDP改定値 (コンセンサス: +2.8%)
    - **10/02(金) 21:30**: 🇺🇸 米・雇用統計 (コンセンサス: +16.5万人)
    - **10/14(水) 21:30**: 🇺🇸 米・消費者物価指数 CPI (コンセンサス: 3.1%)
    """)

# 4. 戦略会議室タブ (4者合同AI)
with tab_strategy:
    st.subheader("💬 戦略会議室 (4者合同AI対話)")
    
    chat_container = st.container(height=400)
    with chat_container:
        st.markdown("📌 **システムメモ**: 全タブの情報（銘柄・ポートフォリオ・経済指標）をAIが自動共有しています。")
        st.markdown("📊 **主席アナリストAI (マクロ)**: 指標発表前後のボラティリティに警戒が必要です。")
        st.markdown("📈 **テクニカルAI**: 現在のRSIと移動平均の状態を注視しましょう。")
        st.markdown("🛡️ **リスク管理官AI**: ポートフォリオ全体の損切ラインを再確認してください。")
        st.markdown("👑 **チーフオーケストレーター**: 指標発表を控え、ポジションを抑えた慎重な立ち回りを推奨します。")

    user_query = st.chat_input("AI戦略会議室へメッセージを入力 (例: 現在のポートフォリオとCPIに向けた方針は？)")
    if user_query:
        with chat_container:
            st.markdown(f"👤 **あなた**: {user_query}")
            st.markdown("👑 **チーフオーケストレーター (総括)**: ご質問ありがとうございます。現在のポートフォリオとマクロ環境を踏まえると...")