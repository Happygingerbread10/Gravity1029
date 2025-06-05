import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 시가총액 기준 글로벌 Top 10 기업 (2025년 기준 예상 티커)
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Meta (Facebook)": "META",
    "Berkshire Hathaway": "BRK-B",
    "TSMC": "TSM",
    "Tesla": "TSLA"
}

st.set_page_config(page_title="Global Top 10 Stocks Tracker", layout="wide")
st.title("📈 글로벌 시가총액 Top 10 기업 - 최근 1년 주가 변화")

# 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 데이터 수집
@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data["Adj Close"]

# Plotly 그래프 생성
fig = go.Figure()
for name, ticker in top10_tickers.items():
    try:
        data = load_data(ticker)
        fig.add_trace(go.Scatter(x=data.index, y=data, mode='lines', name=name))
    except Exception as e:
        st.warning(f"❗ {name} 데이터 로드 실패: {e}")

fig.update_layout(
    title="최근 1년간 주가 비교 (Adjusted Close)",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    hovermode="x unified",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
