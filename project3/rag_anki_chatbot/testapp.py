import os
import requests
import streamlit as st
from io import BytesIO
from PIL import Image

# ===== Tavily 설정 =====
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
TAVILY_ENDPOINT = "https://api.tavily.com/search"


def tavily_top_image_url(query: str) -> str | None:
    """Tavily에서 가장 관련도 높은 이미지 URL 1장 반환"""
    if not TAVILY_API_KEY:
        st.error("⚠️ TAVILY_API_KEY 환경변수를 먼저 설정하세요.")
        return None

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "include_images": True,
        "search_depth": "advanced",
        "max_results": 5,
    }
    try:
        r = requests.post(TAVILY_ENDPOINT, json=payload, timeout=25)
        r.raise_for_status()
        st.write("🔎 Raw response text:", r.text)
        data = r.json()
        images = data.get("images") or data.get("image_results") or []
        if not images:
            return None
        images_sorted = sorted(images, key=lambda x: x.get("score", 0), reverse=True)
        return images_sorted[0].get("url")
    except Exception as e:
        st.error(f"❌ Tavily 호출 실패: {e}")
        return None


def show_image_safely(url: str, caption: str = ""):
    """Streamlit에서 URL 이미지를 안전하게 표시"""
    if not url:
        st.warning("이미지 URL이 없습니다.")
        return

    st.write("🔗 URL:", url)

    # (1) URL 직접 표시
    try:
        st.image(url, caption=caption or "검색 결과", use_column_width=True)
        return
    except Exception as e:
        st.info(f"URL 직접 표시 실패 → bytes로 시도: {e}")

    # (2) 직접 다운로드 후 표시 (User-Agent 헤더 추가)
    try:
        headers = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.google.com/"}
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content))
        st.image(img, caption=caption or "검색 결과", use_column_width=True)
        return
    except Exception as e:
        st.error(f"이미지 다운로드 실패: {e}")


# ===== Streamlit UI =====
st.title("🖼️ Tavily 이미지 검색")

query = st.text_input("검색어를 입력하세요", "한강 야경")
if st.button("검색"):
    with st.spinner("검색 중..."):
        url = tavily_top_image_url(query)
        if url:
            show_image_safely(url, caption=query)
        else:
            st.warning("이미지 결과를 찾지 못했습니다.")
