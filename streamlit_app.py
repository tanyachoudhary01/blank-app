import streamlit as st

# Set up clean, professional page configuration
st.set_page_config(
    page_title="Tanya Choudhary | E-Commerce Strategy & Category Leader",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom premium styling via CSS injector
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;&display=swap');
        
        /* Global Font Fixes */
        html, body, [class*="css"], .stMarkdown {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        
        /* Clean Metric Blocks */
        .metric-card {
            background-color: #ffffff;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #f1f5f9;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            text-align: center;
        }
        .metric-val {
            font-size: 28px;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 4px;
        }
        .metric-lbl {
            font-size: 12px;
            font-weight: 500;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        /* Simulator Display Block */
        .sim-display {
            background-color: #020617;
            padding: 24px;
            border-radius: 12px;
            border: 1px solid #1e293b;
        }
        .sim-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #1e293b;
            padding-bottom: 8px;
            margin-bottom: 12px;
        }
        
        /* Pill Badges */
        .pill {
            background-color: #fdf2f8;
            color: #db2777;
            font-size: 12px;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 9999px;
            display: inline-block;
        }
        .skill-badge {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            color: #334155;
            font-size: 12px;
            font-weight: 500;
            padding: 6px 12px;
            border-radius: 6px;
            display: inline-block;
            margin: 4px;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        }
    </style>
""", unsafe_allow_html=True)

# --- HERO HEADER SECTION ---
st.markdown('<span class="pill">Associate Category Manager @ Myntra</span>', unsafe_allow_html=True)
st.title("Scaling High-Growth E-Commerce Portfolios with Data-Driven Precision")

st.markdown("""
I optimize high-velocity retail portfolios, turn consumer analytics into P&L profitability, and deploy hyper-local supply chain initiatives. 
Currently managing 20Cr+ in monthly sales volume while driving rapid micro-fulfillment expansions.
""")

# Quick Contact Row
st.markdown("""
📩 **Email:** choudharytanya01@gmail.com &nbsp;|&nbsp; 📱 **Phone:** +91 7739039798 &nbsp;|&nbsp; 💼 **LinkedIn:** [in/tanyachoudhary1](https://linkedin.com/in/tanyachoudhary1)
""", unsafe_allow_html=True)

st.write("---")

# --- HIGH-IMPACT METRICS GRID ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><div class="metric-val">₹20 Cr+</div><div class="metric-lbl">Monthly Sales Managed</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="metric-val">10,000</div><div class="metric-lbl">SKU Scale-up Capacity</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div class="metric-val">Make It Happen</div><div class="metric-lbl">Myntra Award Winner</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div class="metric-val">8.5 CGPA</div><div class="metric-lbl">NIFT Kolkata Alumna</div></div>', unsafe_allow_html=True)

st.write("---")

# --- INTERACTIVE MYNTRA M-NOW SIMULATOR ---
st.subheader("💡 Interactive Project Blueprint: Strategic Assortment Expansion (Myntra M-Now)")
st.markdown("""
Adjust the slider below to re-simulate how mapping regional consumer search gaps to instant-delivery dark store depth drives scalable revenue performance expansion.
""")

sim_left, sim_right = st.columns([3, 2])

with sim_left:
    sku_input = st.slider(
        "Simulated Catalog Size (SKUs)",
        min_value=3000,
        max_value=10000,
        step=500,
        value=3000,
        help="Slide to increase SKU density mapped across targeted dark store regions."
    )
    
    st.info("""
    **Core Methodology:** Hyper-local Dark Store Gap Analysis. This models localized inventory replenishment factors 
    by checking localized out-of-stock metrics directly against incoming platform demand signals.
    """)

with sim_right:
    scale_factor = sku_input / 3000
    progress_fraction = (sku_input - 3000) / (10000 - 3000)
    calculated_lift = progress_fraction * 3.2
    
    st.markdown(f"""
    <div class="sim-display">
        <div class="sim-row">
            <span style="color: #94a3b8; font-size: 13px;">Catalog Scale Factor</span>
            <span style="color: #ffffff; font-family: monospace; font-weight: bold;">{scale_factor:.1f}x</span>
        </div>
        <div class="sim-row" style="border-bottom: none; margin-bottom: 0; padding-bottom: 0;">
            <span style="color: #94a3b8; font-size: 13px;">Est. Average Revenue Lift</span>
            <span style="color: #34d399; font-family: monospace; font-size: 20px; font-weight: bold;">+{calculated_lift:.1f}%</span>
        </div>
    </div>
    <div style="font-size: 11px; color: #64748b; font-style: italic; margin-top: 8px; text-align: right;">
        *Metrics correspond directly to revenue optimizations achieved across managed portfolio brands.
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- CAREER TIMELINE AND TRAJECTORY ---
st.subheader("💼 Professional Trajectory")

# Myntra
with st.container():
    st.markdown("#### **Associate Category Manager — Apparel, Beauty \& Personal Care (BPC)**")
    st.markdown("*Myntra (Flipkart Group) · Bangalore* | **Oct 2024 — Present**")
    st.markdown("""
    * Manage a large-scale commercial portfolio of 27 PPMP & Outright brands spanning Beauty, Personal Care, Hair Care, Perfumes, and Sanitary segments, consistently capturing over **20 Crore in Monthly Sales**.
    * Granted the platform's **'MAKE IT HAPPEN' Award** for exceptional proactiveness in preserving brand availability parameters and delivering prime commercial conversions during flagship June EORS and BFF cycles.
    * Generated **20% MoM growth** across premium skincare labels by optimizing premium banner placements and tailored promotions.
    * Exceeded target milestones by **30% during the End of Reason Sale (EORS)** through rigorous curated deals and hyper-optimized digital ad conversion paths.
    * **Strategic Assortment Expansion (Myntra M-Now):** Expanded high-demand catalog from 3k to 10k SKUs via data-driven dark store gap analysis, driving a 3.2% increase in average revenue across managed brands.
    """)

st.write("")

# FirstCry
with st.container():
    st.markdown("#### **Planning Executive — Retail Pricing \& Merchandising**")
    st.markdown("*FirstCry (BrainBees Solutions) · Pune* | **Sept 2023 — Oct 2024**")
    st.markdown("""
    * Modeled granular baseline margins, item costs, and historical elasticity indicators to implement dynamic retail pricing matrixes.
    * Maintained cross-functional category synergy across marketing, logistics, and design wings to maximize platform margins across complex seasonal shifts.
    """)

st.write("")

# CityMall
with st.container():
    st.markdown("#### **Category Associate — Home \& General Merchandise**")
    st.markdown("*CityMall · Gurgaon* | **May 2022 — Sept 2023**")
    st.markdown("""
    * Managed commercial supply pipelines for a base of 97–100 core strategic wholesale vendors.
    * **Doubled overall GMV targets (2X)** by designing structural vendor rewards structures and securing continuous shelf accessibility.
    * Onboarded 250+ unique digital merchants within a 90-day sprint cycle, expanding overall department net margin contribution margins.
    """)

st.write("---")

# --- EDUCATION & SKILLS HUB ---
ed_col, skill_col = st.columns(2)

with ed_col:
    st.subheader("🎓 Formal Education")
    st.markdown("##### **Bachelors in Fashion Technology (Apparel Production)**")
    st.markdown("*National Institute of Fashion Technology (NIFT), Kolkata*")
    st.markdown("🏆 **CGPA: 8.5 / 10.0**")
    st.caption("Specialized Core Focus: Retail Planning Operations, Supply Chain Logistics, and Quantitative Business Methods.")

with skill_col:
    st.subheader("🛠️ Technical Skill Matrix")
    skills = [
        "Advanced Microsoft Excel", "My SQL", "P&L Management", 
        "Dynamic Pricing", "Vendor Negotiation", "Auto CAD", 
        "WFX Apparel ERP", "Site Merchandising", "Inventory Modeling"
    ]
    for skill in skills:
        st.markdown(f'<div class="skill-badge">{skill}</div>', unsafe_allow_html=True)

# Footer Layout
st.markdown("""
<br><hr>
<div style="text-align: center; color: #94a3b8; font-size: 11px;">
    &copy; 2026 Tanya Choudhary. All Rights Reserved.
</div>
""", unsafe_allow_html=True)
