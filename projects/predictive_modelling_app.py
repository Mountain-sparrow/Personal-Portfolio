import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from io import StringIO
import warnings
warnings.filterwarnings('ignore')

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="OTT Predictive Modelling Tool",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    .main-header h1 { color: #e94560; font-size: 2.4rem; font-weight: 700; margin-bottom: 0.3rem; }
    .main-header p  { color: #a8b2d8; font-size: 1.05rem; }

    .metric-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        border: 1px solid #0f3460;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .metric-card .label { color: #a8b2d8; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }
    .metric-card .value { color: #e94560; font-size: 2rem; font-weight: 700; }
    .metric-card .sub   { color: #a8b2d8; font-size: 0.75rem; margin-top: 0.2rem; }

    .section-title {
        color: #e94560;
        font-size: 1.3rem;
        font-weight: 700;
        margin: 1.5rem 0 1rem 0;
        padding-left: 0.8rem;
        border-left: 4px solid #e94560;
    }

    .prediction-box {
        background: linear-gradient(135deg, #0f3460, #16213e);
        border: 2px solid #e94560;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin-top: 1rem;
    }
    .prediction-box .pred-label { color: #a8b2d8; font-size: 1rem; }
    .prediction-box .pred-value { color: #e94560; font-size: 3rem; font-weight: 700; }
    .prediction-box .pred-note  { color: #a8b2d8; font-size: 0.85rem; margin-top: 0.5rem; }

    .info-box {
        background: rgba(15, 52, 96, 0.3);
        border: 1px solid #0f3460;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        font-size: 0.9rem;
        color: #a8b2d8;
    }

    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        background-color: #16213e;
        color: #a8b2d8;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0f3460 !important;
        color: #e94560 !important;
    }

    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    div[data-testid="stSidebar"] .stMarkdown { color: #a8b2d8; }
    div[data-testid="stSidebar"] label { color: #a8b2d8 !important; }

    .stButton>button {
        background: linear-gradient(135deg, #e94560, #c73652);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.6rem 1.5rem;
        width: 100%;
    }
    .stButton>button:hover { opacity: 0.9; }

    .dataframe { font-size: 0.85rem; }
    .stDataFrame { border-radius: 10px; overflow: hidden; }

    .step-badge {
        display: inline-block;
        background: #e94560;
        color: white;
        border-radius: 50%;
        width: 28px; height: 28px;
        line-height: 28px;
        text-align: center;
        font-weight: 700;
        margin-right: 8px;
        font-size: 0.85rem;
    }
    .step-row {
        display: flex;
        align-items: center;
        padding: 0.5rem 0;
        color: #a8b2d8;
        font-size: 0.95rem;
    }
    .step-row.active { color: #e94560; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# ─── Helper: generate sample OTT data ───────────────────────────────────────
@st.cache_data
def generate_sample_data(n=500):
    np.random.seed(42)
    genres   = ['Action', 'Comedy', 'Drama', 'Thriller', 'Romance', 'Documentary']
    days     = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    seasons  = ['Spring','Summer','Fall','Winter']

    genre_w  = [0.25, 0.2, 0.2, 0.15, 0.12, 0.08]
    day_base = {'Monday':1.0,'Tuesday':0.9,'Wednesday':0.95,'Thursday':1.05,
                'Friday':1.3,'Saturday':1.5,'Sunday':1.4}
    season_w = {'Spring':1.0,'Summer':1.2,'Fall':1.1,'Winter':0.9}

    rows = []
    for _ in range(n):
        g  = np.random.choice(genres, p=genre_w)
        d  = np.random.choice(days)
        s  = np.random.choice(seasons)
        me = np.random.choice([0,1], p=[0.85, 0.15])

        visitors      = int(np.random.normal(50000, 10000) * day_base[d])
        ad_impressions= int(np.random.normal(200000, 40000))
        views_trailer = int(visitors * np.random.uniform(0.05, 0.2))
        views_content = int(
            views_trailer * np.random.uniform(1.5, 4.0)
            * season_w[s]
            * (1.3 if me else 1.0)
            + np.random.normal(0, 500)
        )
        views_content = max(views_content, 100)
        rows.append(dict(visitors=visitors, ad_impressions=ad_impressions,
                         views_trailer=views_trailer, genre=g,
                         dayofweek=d, season=s,
                         major_sports_event=me, views_content=views_content))
    return pd.DataFrame(rows)

# ─── Preprocessing pipeline ─────────────────────────────────────────────────
def preprocess_data(df):
    df = df.copy()
    df = df.drop_duplicates()

    # Outlier capping
    for col in ['visitors','ad_impressions','views_trailer','views_content']:
        if col in df.columns:
            Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
            IQR = Q3 - Q1
            lb, ub = Q1 - 1.5*IQR, Q3 + 1.5*IQR
            df[col] = np.clip(df[col], lb, ub)

    # Feature engineering
    df['total_promotional_impact'] = df['views_trailer'] * df['ad_impressions']
    df['content_to_trailer_ratio'] = df['views_content'] / df['views_trailer'].replace(0, np.nan)
    df['content_to_trailer_ratio'].fillna(df['content_to_trailer_ratio'].median(), inplace=True)

    return df

def encode_and_scale(df):
    cat_cols = ['genre','dayofweek','season']
    num_cols = ['visitors','ad_impressions','views_trailer','views_content',
                'total_promotional_impact','content_to_trailer_ratio']

    # Only use columns that exist
    cat_cols = [c for c in cat_cols if c in df.columns]
    num_cols = [c for c in num_cols if c in df.columns]

    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    enc_feat = encoder.fit_transform(df[cat_cols])
    enc_df   = pd.DataFrame(enc_feat, columns=encoder.get_feature_names_out(cat_cols), index=df.index)

    scaler  = StandardScaler()
    sc_feat = scaler.fit_transform(df[num_cols])
    sc_df   = pd.DataFrame(sc_feat, columns=num_cols, index=df.index)

    processed = pd.concat([sc_df, enc_df, df[['major_sports_event']]], axis=1)
    return processed, encoder, scaler, cat_cols, num_cols

# ─── Train model ─────────────────────────────────────────────────────────────
def train_model(df_processed):
    X = df_processed.drop('views_content', axis=1)
    y = df_processed['views_content']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    X_train_sm = sm.add_constant(X_train)
    X_test_sm  = sm.add_constant(X_test)

    model   = sm.OLS(y_train, X_train_sm).fit()
    y_pred  = model.predict(X_test_sm)

    r2   = r2_score(y_test, y_pred)
    mae  = mean_absolute_error(y_test, y_pred)
    mse  = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    return model, X_train, X_test, y_train, y_test, y_pred, r2, mae, rmse

# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📺 OTT Predict")
    st.markdown("---")

    st.markdown("### 📁 Data Source")
    data_source = st.radio("", ["Use Sample Data", "Upload CSV"], label_visibility="collapsed")

    df_raw = None
    if data_source == "Upload CSV":
        uploaded = st.file_uploader("Upload your ottdata.csv", type=['csv'])
        if uploaded:
            df_raw = pd.read_csv(uploaded)
            st.success(f"✅ {len(df_raw)} rows loaded")
        else:
            st.info("👆 Upload a CSV with columns: visitors, ad_impressions, views_trailer, genre, dayofweek, season, major_sports_event, views_content")
    else:
        df_raw = generate_sample_data(500)
        st.success("✅ 500 sample rows ready")

    st.markdown("---")
    st.markdown("### ⚙️ Model Settings")
    test_size_pct = st.slider("Test Set Size", 10, 40, 30, step=5, help="% of data used for testing")
    random_seed   = st.number_input("Random Seed", value=42, step=1)
    st.markdown("---")

    st.markdown("""
    <div style='color:#a8b2d8; font-size:0.8rem;'>
    <b>Pipeline:</b><br>
    <div class='step-row'>1. EDA & Visualizations</div>
    <div class='step-row'>2. Outlier Treatment</div>
    <div class='step-row'>3. Feature Engineering</div>
    <div class='step-row'>4. Encoding & Scaling</div>
    <div class='step-row'>5. OLS Regression</div>
    <div class='step-row'>6. Live Predictions</div>
    </div>
    """, unsafe_allow_html=True)

# ─── Main Content ─────────────────────────────────────────────────────────────
st.markdown("""
<div class='main-header'>
  <h1>📺 OTT Content Views Predictor</h1>
  <p>End-to-end predictive modelling — from raw data to live predictions</p>
</div>
""", unsafe_allow_html=True)

if df_raw is None:
    st.info("👈 Select a data source from the sidebar to get started.")
    st.stop()

# ─── Validate columns ─────────────────────────────────────────────────────────
required_cols = {'visitors','ad_impressions','views_trailer','genre',
                 'dayofweek','season','major_sports_event','views_content'}
missing = required_cols - set(df_raw.columns)
if missing:
    st.error(f"❌ Missing columns: {missing}. Please upload a dataset with all required columns.")
    st.stop()

# ─── Run pipeline ─────────────────────────────────────────────────────────────
df_clean    = preprocess_data(df_raw)
df_proc, encoder, scaler, cat_cols, num_cols = encode_and_scale(df_clean)
model, X_train, X_test, y_train, y_test, y_pred, r2, mae, rmse = train_model(df_proc)

# ─── Tabs ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Data Explorer", "🔍 EDA & Visuals", "🧪 Model Results",
    "📈 Diagnostics", "🎯 Live Predictor"
])

# ═══════════════════════ TAB 1: Data Explorer ══════════════════════════════
with tab1:
    st.markdown("<div class='section-title'>Dataset Overview</div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"<div class='metric-card'><div class='label'>Total Rows</div><div class='value'>{len(df_raw):,}</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-card'><div class='label'>Features</div><div class='value'>{df_raw.shape[1]-1}</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-card'><div class='label'>Missing Values</div><div class='value'>{df_raw.isnull().sum().sum()}</div></div>", unsafe_allow_html=True)
    with c4:
        dupes = df_raw.duplicated().sum()
        st.markdown(f"<div class='metric-card'><div class='label'>Duplicates</div><div class='value'>{dupes}</div></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Raw Data Preview</div>", unsafe_allow_html=True)
    st.dataframe(df_raw.head(20), use_container_width=True)

    st.markdown("<div class='section-title'>Descriptive Statistics</div>", unsafe_allow_html=True)
    st.dataframe(df_raw.describe().round(2), use_container_width=True)

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("<div class='section-title'>Categorical Breakdown</div>", unsafe_allow_html=True)
        for c in ['genre','dayofweek','season']:
            with st.expander(f"📋 {c} value counts"):
                st.dataframe(df_raw[c].value_counts().reset_index(), use_container_width=True)
    with col_r:
        st.markdown("<div class='section-title'>Data Types</div>", unsafe_allow_html=True)
        dtype_df = pd.DataFrame({'Column': df_raw.dtypes.index, 'Type': df_raw.dtypes.values,
                                  'Non-Null': df_raw.notnull().sum().values})
        st.dataframe(dtype_df, use_container_width=True)


# ═══════════════════════ TAB 2: EDA & Visuals ══════════════════════════════
with tab2:
    st.markdown("<div class='section-title'>Target Distribution — Views Content</div>", unsafe_allow_html=True)

    fig = make_subplots(rows=1, cols=2,
        subplot_titles=("Histogram (with KDE)", "Box Plot"))
    fig.add_trace(go.Histogram(x=df_raw['views_content'], nbinsx=40,
        marker_color='#e94560', opacity=0.75, name='Views Content'), row=1, col=1)
    fig.add_trace(go.Box(y=df_raw['views_content'], marker_color='#e94560',
        name='Views Content'), row=1, col=2)
    fig.update_layout(template='plotly_dark', height=350, showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<div class='section-title'>Numerical Feature Distributions</div>", unsafe_allow_html=True)
    num_feats = ['visitors','ad_impressions','views_trailer','views_content']
    fig2 = make_subplots(rows=2, cols=2, subplot_titles=num_feats)
    positions = [(1,1),(1,2),(2,1),(2,2)]
    colors = ['#e94560','#0f3460','#533483','#05c2c9']
    for feat, pos, clr in zip(num_feats, positions, colors):
        fig2.add_trace(go.Histogram(x=df_raw[feat], nbinsx=35,
            marker_color=clr, opacity=0.8, name=feat), row=pos[0], col=pos[1])
    fig2.update_layout(template='plotly_dark', height=500, showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)')
    st.plotly_chart(fig2, use_container_width=True)

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("<div class='section-title'>Views by Day of Week</div>", unsafe_allow_html=True)
        day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        day_med   = df_raw.groupby('dayofweek')['views_content'].median().reindex(day_order)
        fig3 = px.bar(x=day_med.index, y=day_med.values,
            labels={'x':'Day','y':'Median Views'},
            color=day_med.values, color_continuous_scale='reds', template='plotly_dark')
        fig3.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)',
            showlegend=False, coloraxis_showscale=False, height=320)
        st.plotly_chart(fig3, use_container_width=True)

    with col_r:
        st.markdown("<div class='section-title'>Views by Season</div>", unsafe_allow_html=True)
        season_order = ['Spring','Summer','Fall','Winter']
        seas_med = df_raw.groupby('season')['views_content'].median().reindex(season_order)
        fig4 = px.bar(x=seas_med.index, y=seas_med.values,
            labels={'x':'Season','y':'Median Views'},
            color=seas_med.values, color_continuous_scale='blues', template='plotly_dark')
        fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)',
            showlegend=False, coloraxis_showscale=False, height=320)
        st.plotly_chart(fig4, use_container_width=True)

    col_l2, col_r2 = st.columns(2)
    with col_l2:
        st.markdown("<div class='section-title'>Views by Genre</div>", unsafe_allow_html=True)
        genre_med = df_raw.groupby('genre')['views_content'].median().sort_values(ascending=True)
        fig5 = px.bar(x=genre_med.values, y=genre_med.index, orientation='h',
            labels={'x':'Median Views','y':'Genre'},
            color=genre_med.values, color_continuous_scale='sunset', template='plotly_dark')
        fig5.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)',
            showlegend=False, coloraxis_showscale=False, height=320)
        st.plotly_chart(fig5, use_container_width=True)

    with col_r2:
        st.markdown("<div class='section-title'>Trailer vs Content Views</div>", unsafe_allow_html=True)
        fig6 = px.scatter(df_raw, x='views_trailer', y='views_content',
            color='genre', template='plotly_dark',
            labels={'views_trailer':'Trailer Views','views_content':'Content Views'},
            opacity=0.65, trendline='ols')
        fig6.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)', height=320)
        st.plotly_chart(fig6, use_container_width=True)

    st.markdown("<div class='section-title'>Correlation Matrix</div>", unsafe_allow_html=True)
    corr = df_raw[num_feats].corr()
    fig7 = px.imshow(corr, text_auto='.2f', color_continuous_scale='RdBu_r',
        template='plotly_dark', aspect='auto')
    fig7.update_layout(paper_bgcolor='rgba(0,0,0,0)', height=380)
    st.plotly_chart(fig7, use_container_width=True)

    st.markdown("<div class='section-title'>Sports Event Impact</div>", unsafe_allow_html=True)
    event_data = df_raw.copy()
    event_data['Event'] = event_data['major_sports_event'].map({0:'No Event', 1:'Sports Event'})
    fig8 = px.box(event_data, x='Event', y='views_content', color='Event',
        color_discrete_map={'No Event':'#0f3460','Sports Event':'#e94560'},
        template='plotly_dark', labels={'views_content':'Views Content'})
    fig8.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)',
        showlegend=False, height=320)
    st.plotly_chart(fig8, use_container_width=True)


# ═══════════════════════ TAB 3: Model Results ══════════════════════════════
with tab3:
    st.markdown("<div class='section-title'>Model Performance Metrics</div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"<div class='metric-card'><div class='label'>R² Score</div><div class='value'>{r2:.4f}</div><div class='sub'>Variance Explained</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-card'><div class='label'>MAE</div><div class='value'>{mae:.3f}</div><div class='sub'>Mean Abs Error</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-card'><div class='label'>RMSE</div><div class='value'>{rmse:.3f}</div><div class='sub'>Root MSE</div></div>", unsafe_allow_html=True)
    with c4:
        adj_r2 = 1 - (1-r2)*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1)
        st.markdown(f"<div class='metric-card'><div class='label'>Adj R²</div><div class='value'>{adj_r2:.4f}</div><div class='sub'>Adjusted R²</div></div>", unsafe_allow_html=True)

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("<div class='section-title'>Actual vs Predicted</div>", unsafe_allow_html=True)
        actual_vals = y_test.values
        pred_vals   = y_pred.values if hasattr(y_pred, 'values') else np.array(y_pred)
        fig_avp = go.Figure()
        fig_avp.add_trace(go.Scatter(x=actual_vals, y=pred_vals, mode='markers',
            marker=dict(color='#e94560', opacity=0.6, size=6), name='Predictions'))
        mn, mx = min(actual_vals.min(), pred_vals.min()), max(actual_vals.max(), pred_vals.max())
        fig_avp.add_trace(go.Scatter(x=[mn, mx], y=[mn, mx], mode='lines',
            line=dict(color='white', dash='dash', width=1.5), name='Perfect Fit'))
        fig_avp.update_layout(template='plotly_dark', height=380,
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)',
            xaxis_title='Actual Views Content', yaxis_title='Predicted Views Content')
        st.plotly_chart(fig_avp, use_container_width=True)

    with col_r:
        st.markdown("<div class='section-title'>Prediction Error Distribution</div>", unsafe_allow_html=True)
        errors = actual_vals - pred_vals
        fig_err = go.Figure()
        fig_err.add_trace(go.Histogram(x=errors, nbinsx=40, marker_color='#0f3460',
            marker_line=dict(color='#e94560', width=0.5), name='Residuals'))
        fig_err.add_vline(x=0, line_dash='dash', line_color='#e94560', line_width=1.5)
        fig_err.update_layout(template='plotly_dark', height=380,
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)',
            xaxis_title='Prediction Error', yaxis_title='Count')
        st.plotly_chart(fig_err, use_container_width=True)

    st.markdown("<div class='section-title'>Feature Coefficients (Top 20 by Absolute Impact)</div>", unsafe_allow_html=True)
    coef_df = pd.DataFrame({
        'Feature': model.params.index,
        'Coefficient': model.params.values,
        'Std Error': model.bse.values,
        't-value': model.tvalues.values,
        'P-value': model.pvalues.values
    }).sort_values('Coefficient', key=abs, ascending=False).head(20)

    fig_coef = go.Figure(go.Bar(
        x=coef_df['Coefficient'],
        y=coef_df['Feature'],
        orientation='h',
        marker=dict(color=coef_df['Coefficient'],
                    colorscale=[[0,'#0f3460'],[0.5,'#533483'],[1,'#e94560']],
                    cmid=0)
    ))
    fig_coef.update_layout(template='plotly_dark', height=500,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)',
        xaxis_title='Coefficient Value', yaxis_title='Feature')
    st.plotly_chart(fig_coef, use_container_width=True)

    st.markdown("<div class='section-title'>Significant Features (p < 0.05)</div>", unsafe_allow_html=True)
    sig = coef_df[coef_df['P-value'] < 0.05].copy()
    sig['Significant'] = '✅'
    st.dataframe(sig.style.format({'Coefficient':'{:.4f}','Std Error':'{:.4f}',
        't-value':'{:.3f}','P-value':'{:.4f}'}), use_container_width=True)

    with st.expander("📄 Full OLS Summary"):
        st.text(model.summary().as_text())


# ═══════════════════════ TAB 4: Diagnostics ═══════════════════════════════
with tab4:
    residuals  = model.resid
    fitted_vals = model.fittedvalues

    st.markdown("<div class='section-title'>Residuals vs Fitted Values</div>", unsafe_allow_html=True)
    fig_rvf = go.Figure()
    fig_rvf.add_trace(go.Scatter(x=fitted_vals, y=residuals, mode='markers',
        marker=dict(color='#e94560', opacity=0.5, size=5), name='Residuals'))
    fig_rvf.add_hline(y=0, line_dash='dash', line_color='white', line_width=1.5)
    fig_rvf.update_layout(template='plotly_dark', height=380,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)',
        xaxis_title='Fitted Values', yaxis_title='Residuals')
    st.plotly_chart(fig_rvf, use_container_width=True)

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("<div class='section-title'>Q-Q Plot of Residuals</div>", unsafe_allow_html=True)
        from scipy import stats
        (osm, osr), (slope, intercept, r) = stats.probplot(residuals)
        fig_qq = go.Figure()
        fig_qq.add_trace(go.Scatter(x=osm, y=osr, mode='markers',
            marker=dict(color='#e94560', opacity=0.6, size=5), name='Residuals'))
        fig_qq.add_trace(go.Scatter(x=osm, y=slope*np.array(osm)+intercept,
            mode='lines', line=dict(color='white', dash='dash', width=1.5), name='Reference'))
        fig_qq.update_layout(template='plotly_dark', height=350,
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)',
            xaxis_title='Theoretical Quantiles', yaxis_title='Sample Quantiles')
        st.plotly_chart(fig_qq, use_container_width=True)

    with col_r:
        st.markdown("<div class='section-title'>Residual Distribution</div>", unsafe_allow_html=True)
        fig_rd = go.Figure()
        fig_rd.add_trace(go.Histogram(x=residuals, nbinsx=40, marker_color='#533483',
            marker_line=dict(color='#e94560', width=0.5), histnorm='probability density'))
        fig_rd.update_layout(template='plotly_dark', height=350,
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,52,96,0.2)',
            xaxis_title='Residuals', yaxis_title='Density')
        st.plotly_chart(fig_rd, use_container_width=True)

    # Model info box
    st.markdown("""
    <div class='info-box'>
    <b>📐 Model Diagnostics Guide</b><br><br>
    • <b>Residuals vs Fitted:</b> Should show random scatter around 0. Patterns indicate heteroscedasticity.<br>
    • <b>Q-Q Plot:</b> Residuals falling on the diagonal line suggest normality. Heavy tails indicate non-normality.<br>
    • <b>Residual Distribution:</b> Should be roughly bell-shaped and centered at 0 for a well-fitted OLS model.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Model Health Check</div>", unsafe_allow_html=True)
    checks = {
        'R² > 0.6 (Good fit)':          r2 > 0.6,
        'F-statistic significant':       model.f_pvalue < 0.05,
        'Condition Number < 1000':       model.condition_number < 1000,
        'AIC computed':                  model.aic is not None,
        'Residual mean ≈ 0':             abs(residuals.mean()) < 0.1,
    }
    for check, passed in checks.items():
        status = "✅" if passed else "⚠️"
        st.markdown(f"<div style='padding:6px 0; color:#a8b2d8;'>{status} {check}</div>", unsafe_allow_html=True)


# ═══════════════════════ TAB 5: Live Predictor ═══════════════════════════
with tab5:
    st.markdown("<div class='section-title'>🎯 Predict Content Views</div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'>Adjust the inputs below and hit <b>Predict Now</b> to get an estimated content view count in real time.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### 📊 Numerical Inputs")
        visitors_in    = st.slider("Visitors", 10000, 120000, 50000, step=1000,
            help="Number of unique visitors to the platform")
        ad_imp_in      = st.slider("Ad Impressions", 50000, 400000, 200000, step=5000,
            help="Number of ad impressions served")
        trailer_views  = st.slider("Trailer Views", 500, 20000, 5000, step=100,
            help="Number of trailer views for the content")
        sports_event   = st.selectbox("Major Sports Event Today?", ["No (0)", "Yes (1)"])
        sports_val     = 1 if "Yes" in sports_event else 0

    with col2:
        st.markdown("#### 🏷️ Categorical Inputs")
        genre_in   = st.selectbox("Content Genre", sorted(df_raw['genre'].unique()))
        day_in     = st.selectbox("Day of Week",
            ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
        season_in  = st.selectbox("Season", ['Spring','Summer','Fall','Winter'])

    st.markdown("")
    predict_btn = st.button("🚀 Predict Now")

    if predict_btn:
        # Build a single-row dataframe to mimic training features
        # We need a proxy for views_content to compute content_to_trailer_ratio
        # Use train median as stand-in for the ratio feature since we don't know it upfront
        median_ratio = df_clean['content_to_trailer_ratio'].median()
        total_promo  = trailer_views * ad_imp_in

        # Create raw-like row (we'll scale numerical + encode categorical)
        input_num = pd.DataFrame([[
            visitors_in, ad_imp_in, trailer_views,
            0,          # placeholder views_content (will be predicted)
            total_promo,
            median_ratio
        ]], columns=['visitors','ad_impressions','views_trailer','views_content',
                     'total_promotional_impact','content_to_trailer_ratio'])

        # Scale numerical using the same scaler
        num_cols_order = ['visitors','ad_impressions','views_trailer','views_content',
                          'total_promotional_impact','content_to_trailer_ratio']
        input_scaled = scaler.transform(input_num[num_cols_order])
        input_sc_df  = pd.DataFrame(input_scaled, columns=num_cols_order)

        # Encode categorical
        cat_input_df = pd.DataFrame([[genre_in, day_in, season_in]],
                                     columns=['genre','dayofweek','season'])
        cat_encoded  = encoder.transform(cat_input_df)
        cat_enc_df   = pd.DataFrame(cat_encoded, columns=encoder.get_feature_names_out(['genre','dayofweek','season']))

        # Assemble feature row (drop views_content from features)
        feature_row = pd.concat([input_sc_df.drop(columns=['views_content']), cat_enc_df,
                                  pd.DataFrame([[sports_val]], columns=['major_sports_event'])], axis=1)

        # Align columns with training
        expected_cols = X_train.columns.tolist()
        for c in expected_cols:
            if c not in feature_row.columns:
                feature_row[c] = 0
        feature_row = feature_row[expected_cols]

        feature_row_sm = sm.add_constant(feature_row, has_constant='add')
        # Ensure const column matches
        if 'const' not in feature_row_sm.columns:
            feature_row_sm.insert(0, 'const', 1.0)

        pred_scaled = model.predict(feature_row_sm)[0]

        # Convert back from scaled space
        # The scaler was fit on num_cols — views_content is at index 3
        vc_mean  = scaler.mean_[3]
        vc_std   = scaler.scale_[3]
        pred_raw = pred_scaled * vc_std + vc_mean
        pred_raw = max(int(pred_raw), 0)

        st.markdown(f"""
        <div class='prediction-box'>
          <div class='pred-label'>Estimated Content Views</div>
          <div class='pred-value'>{pred_raw:,}</div>
          <div class='pred-note'>
            Genre: {genre_in} &nbsp;|&nbsp; {day_in} &nbsp;|&nbsp; {season_in}
            &nbsp;|&nbsp; Sports: {"Yes ⚽" if sports_val else "No"}
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Gauge chart ─────────────────────────────────────────────────────
        max_vc = int(df_raw['views_content'].max())
        pct    = min(pred_raw / max_vc, 1.0) * 100

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=pred_raw,
            delta={'reference': int(df_raw['views_content'].median()), 'relative': False},
            title={'text': "vs Median Views", 'font': {'color': '#a8b2d8'}},
            gauge={
                'axis': {'range': [0, max_vc], 'tickcolor': '#a8b2d8'},
                'bar':  {'color': '#e94560'},
                'steps': [
                    {'range': [0, max_vc*0.33], 'color': '#16213e'},
                    {'range': [max_vc*0.33, max_vc*0.66], 'color': '#0f3460'},
                    {'range': [max_vc*0.66, max_vc], 'color': '#533483'},
                ],
                'threshold': {
                    'line': {'color': 'white', 'width': 3},
                    'thickness': 0.85,
                    'value': int(df_raw['views_content'].median())
                }
            }
        ))
        fig_gauge.update_layout(template='plotly_dark', height=320,
            paper_bgcolor='rgba(0,0,0,0)', font_color='#a8b2d8')
        st.plotly_chart(fig_gauge, use_container_width=True)

        # ── Context stats ─────────────────────────────────────────────────
        st.markdown("<div class='section-title'>Context: Similar Historical Records</div>", unsafe_allow_html=True)
        context = df_raw[
            (df_raw['genre'] == genre_in) &
            (df_raw['dayofweek'] == day_in)
        ]['views_content']
        if len(context) > 0:
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(f"<div class='metric-card'><div class='label'>Median (similar)</div><div class='value'>{int(context.median()):,}</div></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div class='metric-card'><div class='label'>Min</div><div class='value'>{int(context.min()):,}</div></div>", unsafe_allow_html=True)
            with c3:
                st.markdown(f"<div class='metric-card'><div class='label'>Max</div><div class='value'>{int(context.max()):,}</div></div>", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; color:#a8b2d8; font-size:0.75rem; margin-top:3rem; padding:1rem;
     border-top: 1px solid #0f3460;'>
  OTT Predictive Modelling Tool &nbsp;|&nbsp; OLS Regression &nbsp;|&nbsp; Built with Streamlit & Plotly
</div>
""", unsafe_allow_html=True)
