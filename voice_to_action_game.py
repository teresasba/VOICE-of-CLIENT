
import streamlit as st
import pandas as pd
from datetime import datetime

def voice_to_action_game():
    st.set_page_config(page_title="From Voice to Action Game", layout="centered")
    st.title("🚀 From Voice to Action – Lean Thinking Game")

    with st.expander("🌟 Why Voice of the Customer Matters"):
        st.markdown("""
        Every day, your work impacts someone else's life.

        **The Voice of the Customer (VOC)** is how people tell you — in their own words — what matters most to them.

        Your real role is to translate what they say into actions, standards, and measurable results.

        **Critical to Quality (CTQs)** turn needs into measurable quality.

        Listening is good.  
        Understanding is better.  
        Delivering is excellence.
        """)

    st.header("🎯 Your Mission:")
    st.markdown("""
Listen carefully to the Voice of the Customer.
Translate it into Critical to Quality (CTQ) requirements.
Identify the right Metric to monitor.
    """)

    player_name = st.text_input("👤 Enter your name or team:", key="player_name")

    level = st.radio("Choose your Level:", ["🍕 Level 1: Food & Beverage", "📞 Level 2: Service Processes"])

    if level == "🍕 Level 1: Food & Beverage":
        questions = [
            {
                "story": "You manage an online coffee delivery service. A client writes: 'I want my coffee to be hot when I receive it.'",
                "ctq_options": ["Deliver coffee within 10 minutes", "Coffee served at minimum 65°C", "Serve coffee in eco-friendly cups"],
                "correct_ctq": "Coffee served at minimum 65°C",
                "metric": "Coffee temperature at delivery",
                "feedback": "✅ Temperature ensures the sensory experience the customer expects."
            },
            {
                "story": "You manage a pizza delivery service. A customer writes: 'I want my pizza to arrive hot and fresh.'",
                "ctq_options": ["Deliver pizza within 20 minutes", "Pizza temperature at delivery above 60°C", "Pizza boxed in eco-friendly material"],
                "correct_ctq": "Pizza temperature at delivery above 60°C",
                "metric": "Temperature of pizza at arrival",
                "feedback": "✅ Temperature directly impacts freshness perception."
            }
        ]
    else:
        questions = [
            {
                "story": "You work in a customer service center. A customer writes: 'I want my issue resolved at the first contact.'",
                "ctq_options": ["Call wait time below 2 minutes", "First Contact Resolution Rate above 90%", "Average Handle Time under 5 minutes"],
                "correct_ctq": "First Contact Resolution Rate above 90%",
                "metric": "Percentage of cases resolved without escalation",
                "feedback": "✅ First Contact Resolution directly measures meeting the customer's expectation."
            },
            {
                "story": "You manage a reporting team. A client says: 'I need accurate reports delivered on time every week.'",
                "ctq_options": ["Reports delivered within 1 day", "0% errors in reports", "Use new reporting software"],
                "correct_ctq": "0% errors in reports",
                "metric": "Error rate in weekly reports",
                "feedback": "✅ Accuracy in reports directly matches the customer expectation for reliability."
            }
        ]

    st.subheader("🧩 Translate the Voice into Action")
    total_score = 0
    results = []

    for idx, q in enumerate(questions):
        st.markdown(f"**Scenario {idx+1}:**")
        st.info(q["story"])

        guess_ctq = st.radio(f"What is the correct CTQ?", q["ctq_options"], key=f"ctq_{idx}")
        metric_guess = st.text_input(f"Suggest a metric to monitor:", key=f"metric_{idx}")

        is_correct_ctq = (guess_ctq == q["correct_ctq"])
        results.append({
            "Player": player_name,
            "Scenario": q["story"],
            "Your CTQ Choice": guess_ctq,
            "Correct CTQ": q["correct_ctq"],
            "Metric Suggested": metric_guess,
            "Expected Metric": q["metric"],
            "Correct": is_correct_ctq
        })

        if is_correct_ctq:
            total_score += 2

    st.markdown("---")
    st.subheader("🏁 Final Score")
    st.markdown(f"### 🎯 Your total score is: **{total_score}** points!")

    if st.button("🔍 Show All Correct Answers"):
        st.subheader("✅ Here are the correct answers and explanations:")
        for q in questions:
            st.success(f"CTQ: {q['correct_ctq']} — Metric: {q['metric']}")
            st.caption(q['feedback'])

    if player_name.strip():
        df = pd.DataFrame(results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"voice_to_action_results_{player_name}_{timestamp}.csv"
        st.success("📥 Your results were saved!")
        st.download_button("⬇ Download your results", data=df.to_csv(index=False), file_name=filename, mime="text/csv")

    st.markdown("---")
    st.subheader("🌟 Final Reflection: Connect and Deliver")
    st.markdown("""
    ✨ Now, ask yourself:

    > **Are you truly listening to your Customers?**  
    > **Are you turning their words into actions, measurements, and improvements?**

    ➡️ Listen deeply.  
    ➡️ Translate wisely.  
    ➡️ Deliver excellently — with awareness, with purpose, with heart. 💖
    """)

voice_to_action_game()
