import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


GAME_URL = (
    "https://demetriusww.github.io/tcm-ancient-book-puzzle/"
    "?v=streamlit-20261117c"
)
PREVIEW_PATH = Path(__file__).parent / "assets" / "game-preview.png"
if PREVIEW_PATH.exists():
    PREVIEW_DATA = base64.b64encode(PREVIEW_PATH.read_bytes()).decode("ascii")
    PREVIEW_IMAGE = f"data:image/png;base64,{PREVIEW_DATA}"
else:
    PREVIEW_IMAGE = ""

st.set_page_config(
    page_title="古籍解谜·中医传承",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    f"""
    <style>
        :root {{
            --paper: #f3ecd8;
            --paper-deep: #e5d8b9;
            --ink: #2f2a23;
            --cinnabar: #963127;
            --jade: #336e53;
            --gold: #a98645;
        }}

        .stApp {{
            color: var(--ink);
            background:
                repeating-linear-gradient(
                    90deg,
                    rgba(77, 60, 38, 0.025) 0,
                    rgba(77, 60, 38, 0.025) 1px,
                    transparent 1px,
                    transparent 38px
                ),
                var(--paper);
        }}

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        footer {{
            display: none;
        }}

        .block-container {{
            max-width: 1120px;
            padding: 2.2rem 1.5rem 4rem;
        }}

        .hero {{
            position: relative;
            min-height: 520px;
            padding: 52px clamp(24px, 7vw, 88px) 44px;
            border: 1px solid rgba(255, 248, 233, 0.32);
            background:
                linear-gradient(
                    90deg,
                    rgba(25, 20, 15, 0.94) 0%,
                    rgba(25, 20, 15, 0.82) 44%,
                    rgba(25, 20, 15, 0.28) 78%,
                    rgba(25, 20, 15, 0.12) 100%
                ),
                url("{PREVIEW_IMAGE}") center / cover no-repeat;
            box-shadow: 0 22px 70px rgba(38, 25, 13, 0.28);
            overflow: hidden;
        }}

        .hero::before {{
            content: "";
            position: absolute;
            inset: 12px;
            border: 1px solid rgba(218, 193, 143, 0.40);
            pointer-events: none;
        }}

        .hero::after {{
            content: "修 卷";
            position: absolute;
            right: 28px;
            bottom: -34px;
            color: rgba(255, 248, 233, 0.08);
            font-family: "STKaiti", "KaiTi", serif;
            font-size: 150px;
            font-weight: 800;
            letter-spacing: 0.08em;
            white-space: nowrap;
            pointer-events: none;
        }}

        .seal {{
            display: inline-grid;
            place-items: center;
            width: 60px;
            height: 60px;
            margin-bottom: 18px;
            color: #fff8e9;
            background: var(--cinnabar);
            border: 2px solid rgba(255, 248, 233, 0.78);
            box-shadow: 0 0 0 6px rgba(150, 49, 39, 0.10);
            font-family: "STKaiti", "KaiTi", serif;
            font-size: 31px;
            font-weight: 800;
        }}

        .eyebrow {{
            margin: 0 0 10px;
            color: #d7b46b;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 0.22em;
        }}

        h1 {{
            margin: 0;
            color: #fff8e9;
            font-family: "STKaiti", "KaiTi", "Microsoft YaHei", serif;
            font-size: clamp(42px, 7vw, 82px);
            font-weight: 700;
            line-height: 1.04;
            letter-spacing: 0.02em;
        }}

        .subtitle {{
            max-width: 660px;
            margin: 20px 0 0;
            color: rgba(255, 248, 233, 0.84);
            font-size: clamp(16px, 2vw, 20px);
            line-height: 1.9;
        }}

        .launch-row {{
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 16px;
            margin-top: 30px;
        }}

        .launch-button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 214px;
            min-height: 58px;
            padding: 0 30px;
            color: #fff8e9 !important;
            background: var(--cinnabar);
            border: 2px solid #7c251e;
            box-shadow: 0 8px 0 #6f211b, 0 15px 24px rgba(74, 32, 21, 0.22);
            font-size: 20px;
            font-weight: 800;
            letter-spacing: 0.12em;
            text-decoration: none !important;
            transition: transform 120ms ease, box-shadow 120ms ease;
        }}

        .launch-button:hover {{
            color: #fff8e9 !important;
            transform: translateY(3px);
            box-shadow: 0 5px 0 #6f211b, 0 10px 18px rgba(74, 32, 21, 0.20);
        }}

        .launch-note {{
            color: rgba(255, 248, 233, 0.75);
            font-size: 14px;
            line-height: 1.7;
        }}

        .steps {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0;
            margin: 28px 0 20px;
            border-top: 1px solid rgba(111, 79, 42, 0.28);
            border-bottom: 1px solid rgba(111, 79, 42, 0.28);
        }}

        .step {{
            min-height: 100px;
            padding: 22px 20px;
            border-right: 1px solid rgba(111, 79, 42, 0.20);
        }}

        .step:last-child {{
            border-right: 0;
        }}

        .step b {{
            display: block;
            margin-bottom: 7px;
            color: var(--jade);
            font-size: 17px;
        }}

        .step span {{
            color: #776d5e;
            font-size: 14px;
            line-height: 1.7;
        }}

        .notice {{
            margin: 10px 0 22px;
            padding: 15px 18px;
            color: #584f43;
            background: rgba(229, 216, 185, 0.54);
            border-left: 4px solid var(--gold);
            font-size: 14px;
            line-height: 1.75;
        }}

        iframe {{
            display: block;
            border: 1px solid rgba(111, 79, 42, 0.30);
            background: #211b17;
        }}

        @media (max-width: 720px) {{
            .block-container {{
                padding: 1rem 0.8rem 2.5rem;
            }}

            .hero {{
                min-height: 0;
                padding: 36px 24px 34px;
                background:
                    linear-gradient(
                        180deg,
                        rgba(25, 20, 15, 0.86) 0%,
                        rgba(25, 20, 15, 0.93) 100%
                    ),
                    url("{PREVIEW_IMAGE}") center / cover no-repeat;
            }}

            .hero::after {{
                display: none;
            }}

            .launch-row {{
                align-items: flex-start;
                flex-direction: column;
            }}

            .launch-button {{
                width: 100%;
            }}

            .steps {{
                grid-template-columns: 1fr;
            }}

            .step {{
                min-height: 0;
                border-right: 0;
                border-bottom: 1px solid rgba(111, 79, 42, 0.20);
            }}

            .step:last-child {{
                border-bottom: 0;
            }}
        }}
    </style>

    <section class="hero">
        <div class="seal">卷</div>
        <p class="eyebrow">中医古籍互动解谜</p>
        <h1>古籍解谜<br>中医传承</h1>
        <p class="subtitle">
            残卷散落，墨迹隐去。循着药性、归经与方剂线索，
            修复五卷医书，寻回失落于纸页之间的医道传承。
        </p>
        <div class="launch-row">
            <a class="launch-button" href="{GAME_URL}" target="_blank" rel="noopener">
                开卷入局
            </a>
            <div class="launch-note">
                推荐使用新窗口全屏游玩<br>
                首次启动需载入网页运行核心，请留意页面中的进度条
            </div>
        </div>
    </section>

    <div class="steps">
        <div class="step">
            <b>壹 · 载入卷宗</b>
            <span>首次进入会下载约 9 MB 的 Python 网页运行核心。</span>
        </div>
        <div class="step">
            <b>贰 · 唤醒古籍</b>
            <span>核心载入后自动解压游戏内容，进度达到 100% 后稍候。</span>
        </div>
        <div class="step">
            <b>叁 · 落笔修卷</b>
            <span>出现姓名输入框即表示游戏已经启动，可以开始游玩。</span>
        </div>
    </div>

    <div class="notice">
        如果浏览器拦截了新窗口，请允许本站打开弹窗，或使用下方开关在当前页面加载。
        首次加载完成后，同一浏览器再次进入通常会快很多。
    </div>
    """,
    unsafe_allow_html=True,
)

show_embedded_game = st.toggle(
    "在当前页面内加载游戏",
    value=False,
    help="页内窗口会多一层浏览器容器，全屏新窗口的加载与操作体验更好。",
)

if show_embedded_game:
    components.iframe(GAME_URL, height=900, scrolling=False)
else:
    st.caption("尚未在页面内加载游戏资源。点击上方“开卷入局”即可开始。")
