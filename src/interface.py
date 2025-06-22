import streamlit as st
import plotly.graph_objects as go
import json
import os

OUTPUT_DIR = "./output_results"

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def plot_history():
    data = load_json(os.path.join(OUTPUT_DIR, "history.json"))
    if not data:
        st.warning("Arquivo history.json não encontrado!")
        return

    frames = [item["id"] for item in data]
    counts = [item["count"] for item in data]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=frames,
        y=counts,
        mode='lines+markers',
        line=dict(
            color="#0571FF",
            width=3,
            shape='spline',
            smoothing=1.3
        ),
        marker=dict(
            size=6,
            color='white',
            line=dict(color="#0853F6", width=3),
            symbol='circle'
        ),
        fill='tonexty',
        fillcolor='rgba(102, 126, 234, 0.15)',
        hovertemplate='<b>Frame:</b> %{x}<br><b>Pessoas:</b> %{y}<extra></extra>',
        connectgaps=True
    ))

    fig.update_layout(
        title=dict(
            text="<b>Pessoas x Frame</b>",
            font=dict(size=28, color='#2C3E50'),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(
            title=dict(text="<b>Frames</b>", font=dict(size=16, color='#34495E')),
            gridcolor='rgba(52, 73, 94, 0.1)',
            showline=True,
            linecolor='#BDC3C7',
            linewidth=2,
            tickfont=dict(color='#2C3E50', size=12),
            ticks='outside',
            ticklen=5,
            tickcolor='#BDC3C7'
        ),
        yaxis=dict(
            title=dict(text="<b>Número de Pessoas</b>", font=dict(size=16, color='#34495E')),
            gridcolor='rgba(52, 73, 94, 0.1)',
            showline=True,
            linecolor='#BDC3C7',
            linewidth=2,
            tickfont=dict(color='#2C3E50', size=12),
            zeroline=True,
            zerolinecolor='rgba(52, 73, 94, 0.2)',
            ticks='outside',
            ticklen=5,
            tickcolor='#BDC3C7'
        ),
        plot_bgcolor='rgba(248, 249, 250, 0.8)',
        paper_bgcolor='white',
        font=dict(size=12, color="#2C3E50"),
        margin=dict(l=80, r=40, t=80, b=60),
        height=650,
        showlegend=False,
        dragmode=False,
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor="white",
            bordercolor="#667EEA",
            font_size=14,
            font_color="#2C3E50"
        )
    )

    config = {
        'modeBarButtonsToRemove': [
            'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d',
            'autoScale2d', 'hoverClosestCartesian', 'hoverCompareCartesian',
            'zoom2d', 'toggleSpikelines', 'toImage', 'resetScale2d'
        ],
        'displaylogo': False,
        'displayModeBar': True,
        'staticPlot': False
    }

    st.plotly_chart(fig, use_container_width=True, config=config)

def show_video():
    video_path = os.path.join(OUTPUT_DIR, "output_video.mp4")
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.error("Arquivo de vídeo não encontrado!")

def main():
    st.set_page_config(
        page_title="Detecção de Pessoas - Dashboard",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown("Processo Seletivo Metta", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### Vídeo Processado")
        show_video()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### Gráfico Pessoas x Frame")
        plot_history()

if __name__ == "__main__":
    main()