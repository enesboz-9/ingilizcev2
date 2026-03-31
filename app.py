import streamlit as st

st.set_page_config(
    page_title="English Master",
    page_icon="🇬🇧",
    layout="wide",
    initial_sidebar_state="auto"
)

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
from data.oxford import OXFORD_3000
from data.vocabulary import VOCABULARY
from data.sentences import SENTENCE_PATTERNS
from data.adjectives import ADJECTIVES, VERBS, ADVERBS
from data.phrases import PHRASAL_VERBS, IDIOMS, DAILY_EXPRESSIONS

# ── Sidebar ──────────────────────────────────────────────────────────────────
# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-logo">🇬🇧 English<br><span>MASTER</span></div>', unsafe_allow_html=True)
    st.markdown("---")

    # Bu kısım içeride olmalı (4 boşluk veya 1 Tab)
    section = st.radio(
        "Navigate",
        ["🏠 Home", "📚 Vocabulary", "🎓 Oxford 3000", "🔤 Sentence Patterns", "🎨 Adjectives & More", "💬 Daily Expressions"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("**Filter by Level**")
    level_filter = st.multiselect(
        "Select levels",
        ["A1", "A2", "B1", "B2", "C1", "C2"],
        default=["A1", "A2", "B1", "B2", "C1", "C2"],
        label_visibility="collapsed"
    )
# ── HOME ─────────────────────────────────────────────────────────────────────
# ── HOME ─────────────────────────────────────────────────────────────────────
if section == "🏠 Home":
    st.markdown('<h1 class="hero-title">Master English.<br><span>From Zero to Fluent.</span></h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">Your complete reference guide — vocabulary, grammar patterns, adjectives, verbs, adverbs, idioms and more. All levels. All in one place.</p>', unsafe_allow_html=True)

    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        # Bu satırlar artık doğru şekilde içeride (indent edilmiş)
        oxford_count = sum(len(words) for words in OXFORD_3000.values())
        total_words = sum(len(v) for cat in VOCABULARY.values() for v in cat.values()) + oxford_count
        st.markdown(f'<div class="stat-card"><div class="stat-num">{total_words}+</div><div class="stat-label">Total Words</div></div>', unsafe_allow_html=True)
    
    with col2:
        total_patterns = sum(len(v) for v in SENTENCE_PATTERNS.values())
        st.markdown(f'<div class="stat-card"><div class="stat-num">{total_patterns}+</div><div class="stat-label">Sentence Patterns</div></div>', unsafe_allow_html=True)
    
    with col3:
        total_adj = len(ADJECTIVES) + len(VERBS) + len(ADVERBS)
        st.markdown(f'<div class="stat-card"><div class="stat-num">{total_adj}+</div><div class="stat-label">Adjectives, Verbs & Adverbs</div></div>', unsafe_allow_html=True)
    
    with col4:
        total_expr = len(PHRASAL_VERBS) + len(IDIOMS) + len(DAILY_EXPRESSIONS)
        st.markdown(f'<div class="stat-card"><div class="stat-num">{total_expr}+</div><div class="stat-label">Expressions & Idioms</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📖 What's Inside?")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <div class="feature-title">Vocabulary by Category</div>
            <div class="feature-desc">Food, travel, emotions, work, health, technology and many more — grouped by topic and sorted by level.</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔤</div>
            <div class="feature-title">Sentence Patterns</div>
            <div class="feature-desc">Essential grammar structures with real examples. Learn how native speakers actually build sentences.</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎨</div>
            <div class="feature-title">Adjectives, Verbs & Adverbs</div>
            <div class="feature-desc">The most commonly used describing words, action words, and modifiers — essential for natural speech.</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💬</div>
            <div class="feature-title">Daily Expressions</div>
            <div class="feature-desc">Phrasal verbs, idioms and everyday conversational phrases that make you sound like a native speaker.</div>
        </div>
        """, unsafe_allow_html=True)

# ── VOCABULARY ────────────────────────────────────────────────────────────────
elif section == "📚 Vocabulary":
    st.markdown('<h2 class="section-title">📚 Vocabulary</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-desc">Essential words organized by topic and difficulty level.</p>', unsafe_allow_html=True)

    search = st.text_input("🔍 Search a word or meaning...", placeholder="e.g. happy, mutlu, travel...")

    for category, levels in VOCABULARY.items():
        filtered_words = []
        for level, words in levels.items():
            if level in level_filter:
                for w in words:
                    if not search or search.lower() in w["word"].lower() or search.lower() in w["meaning"].lower():
                        filtered_words.append({**w, "level": level})

        if not filtered_words:
            continue

        with st.expander(f"**{category}** ({len(filtered_words)} words)", expanded=False):
            cols = st.columns([2, 3, 2, 1])
            cols[0].markdown("**Word**")
            cols[1].markdown("**Example Sentence**")
            cols[2].markdown("**Meaning (TR)**")
            cols[3].markdown("**Level**")
            st.markdown('<hr style="margin:4px 0 8px 0">', unsafe_allow_html=True)

            for w in filtered_words:
                cols = st.columns([2, 3, 2, 1])
                cols[0].markdown(f'<span class="word-text">{w["word"]}</span>', unsafe_allow_html=True)
                cols[1].markdown(f'<span class="example-text">{w["example"]}</span>', unsafe_allow_html=True)
                cols[2].markdown(f'<span class="meaning-text">{w["meaning"]}</span>', unsafe_allow_html=True)
                cols[3].markdown(f'<span class="badge badge-{w["level"]}">{w["level"]}</span>', unsafe_allow_html=True)
# ── OXFORD 3000 ──────────────────────────────────────────────────────────────
elif section == "🎓 Oxford 3000":
    st.markdown('<h2 class="section-title">🎓 Oxford 3000™ Core</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-desc">The most important words to learn in English, filtered by CEFR levels.</p>', unsafe_allow_html=True)

    ox_search = st.text_input("🔍 Search Oxford Core...", placeholder="Search word or meaning...", key="ox_search")

    # Seviyelere göre grupla
    for level in ["A1", "A2", "B1", "B2", "C1", "C2"]:
        if level in level_filter and level in OXFORD_3000:
            words = OXFORD_3000[level]
            
            # Arama filtresi
            filtered = [w for w in words if not ox_search or 
                        ox_search.lower() in w["word"].lower() or 
                        ox_search.lower() in w["meaning"].lower()]
            
            if not filtered:
                continue

            with st.expander(f"**Level {level}** ({len(filtered)} words)", expanded=(level == "A1")):
                cols = st.columns([2, 3, 2])
                cols[0].markdown("**Word**")
                cols[1].markdown("**Example Sentence**")
                cols[2].markdown("**Meaning (TR)**")
                st.markdown('<hr style="margin:4px 0 8px 0">', unsafe_allow_html=True)

                for w in filtered:
                    c = st.columns([2, 3, 2])
                    c[0].markdown(f'<span class="word-text" style="color:#1D4ED8;">{w["word"]}</span>', unsafe_allow_html=True)
                    c[1].markdown(f'<span class="example-text">{w["example"]}</span>', unsafe_allow_html=True)
                    c[2].markdown(f'<span class="meaning-text">{w["meaning"]}</span>', unsafe_allow_html=True)
# ── SENTENCE PATTERNS ─────────────────────────────────────────────────────────
elif section == "🔤 Sentence Patterns":
    st.markdown('<h2 class="section-title">🔤 Sentence Patterns</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-desc">Core grammar structures every English learner needs to master.</p>', unsafe_allow_html=True)

    for category, patterns in SENTENCE_PATTERNS.items():
        filtered = [p for p in patterns if p["level"] in level_filter]
        if not filtered:
            continue

        with st.expander(f"**{category}** ({len(filtered)} patterns)", expanded=False):
            for p in filtered:
                st.markdown(f"""
                <div class="pattern-card">
                    <div class="pattern-header">
                        <span class="pattern-name">{p['pattern']}</span>
                        <span class="badge badge-{p['level']}">{p['level']}</span>
                    </div>
                    <div class="pattern-formula">📐 {p['formula']}</div>
                    <div class="pattern-examples">
                        {''.join(f'<div class="pattern-ex">▸ {ex}</div>' for ex in p['examples'])}
                    </div>
                    <div class="pattern-note">💡 {p['note']}</div>
                </div>
                """, unsafe_allow_html=True)

# ── ADJECTIVES & MORE ─────────────────────────────────────────────────────────
elif section == "🎨 Adjectives & More":
    st.markdown('<h2 class="section-title">🎨 Adjectives, Verbs & Adverbs</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-desc">The building blocks of natural, expressive English.</p>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🎨 Adjectives", "⚡ Common Verbs", "🌀 Adverbs"])

    with tab1:
        search_adj = st.text_input("Search adjectives...", key="adj_search")
        for group, items in ADJECTIVES.items():
            filtered = [i for i in items if i["level"] in level_filter and
                        (not search_adj or search_adj.lower() in i["word"].lower() or search_adj.lower() in i["meaning"].lower())]
            if not filtered:
                continue
            with st.expander(f"**{group}**", expanded=False):
                cols = st.columns([2, 3, 2, 1])
                cols[0].markdown("**Adjective**"); cols[1].markdown("**Example**"); cols[2].markdown("**Meaning (TR)**"); cols[3].markdown("**Level**")
                st.markdown('<hr style="margin:4px 0 8px 0">', unsafe_allow_html=True)
                for i in filtered:
                    c = st.columns([2, 3, 2, 1])
                    c[0].markdown(f'<span class="word-text">{i["word"]}</span>', unsafe_allow_html=True)
                    c[1].markdown(f'<span class="example-text">{i["example"]}</span>', unsafe_allow_html=True)
                    c[2].markdown(f'<span class="meaning-text">{i["meaning"]}</span>', unsafe_allow_html=True)
                    c[3].markdown(f'<span class="badge badge-{i["level"]}">{i["level"]}</span>', unsafe_allow_html=True)

    with tab2:
        search_v = st.text_input("Search verbs...", key="verb_search")
        for group, items in VERBS.items():
            filtered = [i for i in items if i["level"] in level_filter and
                        (not search_v or search_v.lower() in i["word"].lower() or search_v.lower() in i["meaning"].lower())]
            if not filtered:
                continue
            with st.expander(f"**{group}**", expanded=False):
                cols = st.columns([2, 3, 2, 1])
                cols[0].markdown("**Verb**"); cols[1].markdown("**Example**"); cols[2].markdown("**Meaning (TR)**"); cols[3].markdown("**Level**")
                st.markdown('<hr style="margin:4px 0 8px 0">', unsafe_allow_html=True)
                for i in filtered:
                    c = st.columns([2, 3, 2, 1])
                    c[0].markdown(f'<span class="word-text">{i["word"]}</span>', unsafe_allow_html=True)
                    c[1].markdown(f'<span class="example-text">{i["example"]}</span>', unsafe_allow_html=True)
                    c[2].markdown(f'<span class="meaning-text">{i["meaning"]}</span>', unsafe_allow_html=True)
                    c[3].markdown(f'<span class="badge badge-{i["level"]}">{i["level"]}</span>', unsafe_allow_html=True)

    with tab3:
        search_adv = st.text_input("Search adverbs...", key="adv_search")
        filtered = [i for i in ADVERBS if i["level"] in level_filter and
                    (not search_adv or search_adv.lower() in i["word"].lower() or search_adv.lower() in i["meaning"].lower())]
        if filtered:
            cols = st.columns([2, 3, 2, 1])
            cols[0].markdown("**Adverb**"); cols[1].markdown("**Example**"); cols[2].markdown("**Meaning (TR)**"); cols[3].markdown("**Level**")
            st.markdown('<hr style="margin:4px 0 8px 0">', unsafe_allow_html=True)
            for i in filtered:
                c = st.columns([2, 3, 2, 1])
                c[0].markdown(f'<span class="word-text">{i["word"]}</span>', unsafe_allow_html=True)
                c[1].markdown(f'<span class="example-text">{i["example"]}</span>', unsafe_allow_html=True)
                c[2].markdown(f'<span class="meaning-text">{i["meaning"]}</span>', unsafe_allow_html=True)
                c[3].markdown(f'<span class="badge badge-{i["level"]}">{i["level"]}</span>', unsafe_allow_html=True)

# ── DAILY EXPRESSIONS ─────────────────────────────────────────────────────────
elif section == "💬 Daily Expressions":
    st.markdown('<h2 class="section-title">💬 Daily Expressions</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-desc">Sound like a native speaker with these essential phrases and expressions.</p>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🔗 Phrasal Verbs", "🌀 Idioms", "🗣️ Conversational Phrases"])

    with tab1:
        search_pv = st.text_input("Search phrasal verbs...", key="pv_search")
        filtered = [i for i in PHRASAL_VERBS if i["level"] in level_filter and
                    (not search_pv or search_pv.lower() in i["phrase"].lower() or search_pv.lower() in i["meaning"].lower())]
        if filtered:
            for i in filtered:
                st.markdown(f"""
                <div class="expr-card">
                    <div class="expr-header">
                        <span class="expr-phrase">{i['phrase']}</span>
                        <span class="badge badge-{i['level']}">{i['level']}</span>
                    </div>
                    <div class="expr-meaning">🇹🇷 {i['meaning']}</div>
                    <div class="expr-example">▸ {i['example']}</div>
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        search_id = st.text_input("Search idioms...", key="id_search")
        filtered = [i for i in IDIOMS if i["level"] in level_filter and
                    (not search_id or search_id.lower() in i["phrase"].lower() or search_id.lower() in i["meaning"].lower())]
        if filtered:
            for i in filtered:
                st.markdown(f"""
                <div class="expr-card idiom-card">
                    <div class="expr-header">
                        <span class="expr-phrase">{i['phrase']}</span>
                        <span class="badge badge-{i['level']}">{i['level']}</span>
                    </div>
                    <div class="expr-meaning">🇹🇷 {i['meaning']}</div>
                    <div class="expr-example">▸ {i['example']}</div>
                </div>
                """, unsafe_allow_html=True)

    with tab3:
        search_de = st.text_input("Search phrases...", key="de_search")
        for situation, phrases in DAILY_EXPRESSIONS.items():
            filtered = [i for i in phrases if not search_de or
                        search_de.lower() in i["phrase"].lower() or search_de.lower() in i["meaning"].lower()]
            if not filtered:
                continue
            with st.expander(f"**{situation}**", expanded=False):
                for i in filtered:
                    cols = st.columns([3, 3])
                    cols[0].markdown(f'<span class="expr-phrase-sm">🗣️ {i["phrase"]}</span>', unsafe_allow_html=True)
                    cols[1].markdown(f'<span class="meaning-text">🇹🇷 {i["meaning"]}</span>', unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="footer">🇬🇧 English Master · Built with Streamlit · All levels A1–C2</div>', unsafe_allow_html=True)
