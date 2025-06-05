import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Global Top 10 Stocks", layout="wide")

st.title("🌍 글로벌 시가총액 TOP 10 기업 주가 변화")
st.markdown("최근 1년간 주요 글로벌 기업들의 주가 변화를 시각화한 그래프입니다.")

# 안정적으로 작동하는 글로벌 시가총액 상위 10개 기업 티커
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Meta (Facebook)": "META",
    "Tesla": "TSLA",
    "TSMC": "TSM",
    "Eli Lilly": "LLY",
    "Visa": "V"
}

# 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 주가 데이터 가져오기 함수 (캐싱)
@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data["Adj Close"]

# Plotly 그래프 생성
fig = go.Figure()

for name, ticker in top10_tickers.items():
    try:
        data = load_data(ticker)
        if data.empty:
            raise ValueError("데이터가 없습니다.")
        fig.add_trace(go.Scatter(x=data.index, y=data, mode='lines', name=name))
    except Exception as e:
        st.warning(f"⚠️ {name} ({ticker}) 데이터 로드 실패: {e}")

# 그래프 스타일 설정
fig.update_layout(
    title="최근 1년간 주가 변화 (Adjusted Close)",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    hovermode="x unified",
    template="plotly_white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)
