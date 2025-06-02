import streamlit as st
from datetime import datetime

# 星座日期范围
zodiac_dates = [
    ("摩羯座", (1, 1), (1, 19)),
    ("水瓶座", (1, 20), (2, 18)),
    ("双鱼座", (2, 19), (3, 20)),
    ("白羊座", (3, 21), (4, 19)),
    ("金牛座", (4, 20), (5, 20)),
    ("双子座", (5, 21), (6, 20)),
    ("巨蟹座", (6, 21), (7, 22)),
    ("狮子座", (7, 23), (8, 22)),
    ("处女座", (8, 23), (9, 22)),
    ("天秤座", (9, 23), (10, 22)),
    ("天蝎座", (10, 23), (11, 21)),
    ("射手座", (11, 22), (12, 21)),
    ("摩羯座", (12, 22), (12, 31)),
]

# 星座性格词典
zodiac_traits = {
    "白羊座": "热情冲动，行动派🔥",
    "金牛座": "稳重踏实，爱好美食💎",
    "双子座": "聪明伶俐，社交达人🌀",
    "巨蟹座": "温柔顾家，情感丰富🌊",
    "狮子座": "自信霸气，领导范儿🔥",
    "处女座": "细致认真，追求完美🔍",
    "天秤座": "优雅公正，注重平衡⚖️",
    "天蝎座": "神秘强烈，直觉敏锐🦂",
    "射手座": "热爱自由，喜欢冒险🏹",
    "摩羯座": "脚踏实地，耐力强💼",
    "水瓶座": "思想前卫，特立独行🧠",
    "双鱼座": "感性浪漫，想象力丰富🎨",
}

# 支持多种输入映射
zodiac_map = {
    "白羊": "白羊座", "aries": "白羊座", "baiyang": "白羊座",
    "金牛": "金牛座", "taurus": "金牛座", "jinniu": "金牛座",
    "双子": "双子座", "gemini": "双子座", "shuangzi": "双子座",
    "巨蟹": "巨蟹座", "cancer": "巨蟹座", "juxie": "巨蟹座",
    "狮子": "狮子座", "leo": "狮子座", "shizi": "狮子座",
    "处女": "处女座", "virgo": "处女座", "chunv": "处女座",
    "天秤": "天秤座", "libra": "天秤座", "tiancheng": "天秤座",
    "天蝎": "天蝎座", "scorpio": "天蝎座", "tianxie": "天蝎座",
    "射手": "射手座", "sagittarius": "射手座", "sheshou": "射手座",
    "摩羯": "摩羯座", "capricorn": "摩羯座", "mojie": "摩羯座",
    "水瓶": "水瓶座", "aquarius": "水瓶座", "shuiping": "水瓶座",
    "双鱼": "双鱼座", "pisces": "双鱼座", "shuangyu": "双鱼座"
}

st.title("🔮 星座小助手 🔮")
st.markdown("✨ 支持 **生日转星座** 和 **星座查性格**，快来试试吧！")

# 分两栏
col1, col2 = st.columns(2)

# 左栏：生日转星座
with col1:
    st.header("🎂 输入生日")
    birthday_input = st.text_input("请输入你的生日（如：6/1，06-01，2025-06-01）")
    if birthday_input:
        birth = None
        for fmt in ("%Y-%m-%d", "%m-%d", "%m/%d"):
            try:
                birth = datetime.strptime(birthday_input, fmt)
                birth = birth.replace(year=2000)
                break
            except:
                continue
        if birth:
            month, day = birth.month, birth.day
            zodiac = None
            for sign, start, end in zodiac_dates:
                if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
                    zodiac = sign
                    break
            if zodiac:
                st.success(f"🌟 你的星座是：**{zodiac}**")
                st.info(f"📌 性格特点：{zodiac_traits.get(zodiac)}")
            else:
                st.error("🤔 没找到对应星座，请检查输入～")
        else:
            st.error("❌ 无法识别的日期格式，请重试～")

# 右栏：星座查性格
with col2:
    st.header("⭐ 输入星座")
    user_input = st.text_input("请输入星座（中文、英文、拼音都支持）")
    if user_input:
        key = user_input.strip().lower()
        zodiac = zodiac_map.get(key)
        if zodiac:
            trait = zodiac_traits.get(zodiac, "这个星座的描述还在编写中……")
            st.success(f"🎉 你的星座是：**{zodiac}**")
            st.info(f"📌 性格特点：{trait}")
        else:
            st.error("😭 没识别出星座，请确认拼写或格式～")
