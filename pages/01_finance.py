import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(page_title="📈 글로벌 시가총액 Top 10 주가 추이", layout="wide")

# 헤더
st.title("🌍 글로벌 시가총액 Top 10 기업 주가 변화 (최근 1년)")
st.markdown("Plotly를 활용한 인터랙티브 차트로 주가 추이를 확인하세요!")

# 주식 목록
top10_stocks = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "TSMC": "TSM",
    "Tesla": "TSLA"
}

# 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 사용자 선택 (멀티 셀렉트)
selected_companies = st.multiselect("🔎 기업 선택", options=list(top10_stocks.keys()), default=list(top10_stocks.keys()))

# 데이터 수집
if selected_companies:
    fig = go.Figure()
    for company in selected_companies:
        symbol = top10_stocks[company]
        try:
            data = yf.download(symbol, start=start_date, end=end_date)
            fig.add_trace(go.Scatter(
                x=data.index,
                y=data["Adj Close"],
                mode="lines",
                name=company
            ))
        except:
            st.warning(f"{company}의 데이터를 불러올 수 없습니다.")

    # 차트 설정
    fig.update_layout(
        title="📊 최근 1년간 주가 변화",
        xaxis_title="날짜",
        yaxis_title="주가 (USD)",
        template="plotly_dark",
        hovermode="x unified",
        legend_title="기업"
    )

    # 차트 출력
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("👆 위에서 하나 이상의 회사를 선택해주세요.")
