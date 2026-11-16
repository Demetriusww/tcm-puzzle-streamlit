# 古籍解谜·中医传承 Streamlit 部署版

这是一个 Streamlit 外壳页面，运行后会嵌入已经部署在 GitHub Pages 的网页版游戏。

## 本地运行

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Streamlit Community Cloud 配置

- Repository：上传本目录的 GitHub 仓库
- Branch：`main`
- Main file path：`streamlit_app.py`

游戏本体地址配置在 `streamlit_app.py` 的 `GAME_URL` 变量中。
