
import streamlit as st
import pandas as pd
from datetime import datetime

def voice_to_action_game():
    st.set_page_config(page_title="Du Besoin Client à l'Action", layout="centered")
    st.title("🚀 Du Besoin Client à l'Action – Jeu Lean Thinking")

    with st.expander("🌟 Pourquoi la Voix du Client est-elle importante ?"):
        st.markdown("""
        Chaque jour, votre travail a un impact sur la vie de quelqu'un d'autre.

        **La Voix du Client (VOC)** est la façon dont les clients expriment, avec leurs propres mots, ce qui compte le plus pour eux.

        Votre rôle n'est pas seulement d'écouter, mais de traduire leurs besoins en actions, normes et résultats mesurables.

        **Les exigences critiques pour la qualité (CTQ)** transforment les besoins en qualité mesurable.

        Écouter est bien.  
        Comprendre est mieux.  
        Livrer, c'est l'excellence.
        """)

    st.header("🎯 Votre Mission :")
    st.markdown("""
Écoutez attentivement la Voix du Client.
Traduisez-la en exigences CTQ (Critical to Quality).
Identifiez la bonne métrique à suivre.
    """)

    player_name = st.text_input("👤 Entrez votre nom ou équipe :", key="player_name")

    level = st.radio("Choisissez votre Niveau :", ["🍕 Niveau 1 : Alimentation & Boissons", "📞 Niveau 2 : Services"])

    if level == "🍕 Niveau 1 : Alimentation & Boissons":
        questions = [
            {
                "story": "Vous gérez un service de livraison de café. Un client écrit : 'Je veux que mon café soit chaud à la livraison.'",
                "ctq_options": ["Livrer le café en moins de 10 minutes", "Café servi à au moins 65°C", "Utiliser des gobelets écologiques"],
                "correct_ctq": "Café servi à au moins 65°C",
                "metric": "Température du café à la livraison",
                "feedback": "✅ La température garantit l'expérience sensorielle attendue par le client."
            },
            {
                "story": "Vous gérez un service de livraison de pizza. Un client écrit : 'Je veux que ma pizza soit fraîche, comme tout juste sortie du four — ne la laissez pas attendre trop longtemps.'",
                "ctq_options": ["Livrer la pizza en moins de 20 minutes", "Température de la pizza supérieure à 60°C", "Boîte à pizza écologique"],
                "correct_ctq": "Livrer la pizza en moins de 20 minutes",
                "metric": "Temps moyen de livraison depuis la sortie du four",
                "feedback": "✅ Une livraison rapide garantit la fraîcheur du produit comme attendu par le client."
            },
            {
                "story": "Vous gérez un service de livraison de glaces. Un client écrit : 'Je veux que ma glace arrive congelée, pas fondue.'",
                "ctq_options": ["Livrer la glace en moins de 20 minutes", "Température de la glace maintenue en dessous de -10°C", "Utiliser des contenants écologiques"],
                "correct_ctq": "Température de la glace maintenue en dessous de -10°C",
                "metric": "Température de la glace à la livraison",
                "feedback": "✅ Pour les produits surgelés, maintenir une température basse est essentiel pour satisfaire les attentes du client."
            }
        ]
    else:
        questions = [
            {
                "story": "Vous travaillez dans un centre de service client. Un client écrit : 'Je veux que mon problème soit résolu au premier contact.'",
                "ctq_options": ["Temps d'attente inférieur à 2 minutes", "Taux de Résolution au Premier Contact supérieur à 90%", "Temps moyen de traitement inférieur à 5 minutes"],
                "correct_ctq": "Taux de Résolution au Premier Contact supérieur à 90%",
                "metric": "Pourcentage de cas résolus sans escalade",
                "feedback": "✅ La Résolution au Premier Contact mesure directement la satisfaction des attentes du client."
            },
            {
                "story": "Vous gérez une équipe de reporting. Un client dit : 'J'ai besoin de rapports exacts livrés à temps chaque semaine.'",
                "ctq_options": ["Rapports livrés sous 1 jour", "0% d'erreurs dans les rapports", "Utiliser un nouveau logiciel de reporting"],
                "correct_ctq": "0% d'erreurs dans les rapports",
                "metric": "Taux d'erreur dans les rapports hebdomadaires",
                "feedback": "✅ La précision des rapports correspond directement aux attentes du client en matière de fiabilité."
            },
            {
                "story": "Vous travaillez dans un centre de service RH. Un nouvel employé dit : 'Je veux que mes documents d'intégration soient prêts avant mon premier jour.'",
                "ctq_options": ["Accès au portail RH en 24 heures", "Tous les documents d'intégration prêts 48h avant la date d'entrée", "Le manager rencontre le nouvel employé le premier jour"],
                "correct_ctq": "Tous les documents d'intégration prêts 48h avant la date d'entrée",
                "metric": "Pourcentage de dossiers d'intégration prêts 2 jours avant l'entrée",
                "feedback": "✅ Avoir les documents prêts à l'avance garantit une intégration fluide et professionnelle."
            }
        ]

    st.subheader("🧩 Traduisez la Voix en Action")
    total_score = 0
    results = []

    for idx, q in enumerate(questions):
        st.markdown(f"**Scénario {idx+1} :**")
        st.info(q["story"])

        guess_ctq = st.radio(f"Quel est le bon CTQ ?", q["ctq_options"], key=f"ctq_{idx}")
        metric_guess = st.text_input(f"Suggérez une métrique à suivre :", key=f"metric_{idx}")

        is_correct_ctq = (guess_ctq == q["correct_ctq"])
        results.append({
            "Joueur": player_name,
            "Scénario": q["story"],
            "Votre choix CTQ": guess_ctq,
            "CTQ correct": q["correct_ctq"],
            "Métrique proposée": metric_guess,
            "Métrique attendue": q["metric"],
            "Correct": is_correct_ctq
        })

        if is_correct_ctq:
            total_score += 2

    st.markdown("---")
    st.subheader("🏁 Score Final")
    st.markdown(f"### 🎯 Votre score total est : **{total_score}** points!")

    if st.button("🔍 Afficher toutes les bonnes réponses"):
        st.subheader("✅ Voici les bonnes réponses et explications :")
        for q in questions:
            st.success(f"CTQ : {q['correct_ctq']} — Métrique : {q['metric']}")
            st.caption(q['feedback'])

    if player_name.strip():
        df = pd.DataFrame(results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"voice_to_action_results_FR_{player_name}_{timestamp}.csv"
        st.success("📥 Vos résultats ont été sauvegardés !")
        st.download_button("⬇ Télécharger vos résultats", data=df.to_csv(index=False), file_name=filename, mime="text/csv")

    st.markdown("---")
    st.subheader("🌟 Réflexion Finale : Connecter et Livrer")
    st.markdown("""
    ✨ Maintenant, posez-vous la question :

    > **Écoutez-vous vraiment vos Clients ?**  
    > **Transformez-vous vraiment leurs besoins en actions, mesures et améliorations ?**

    ➡️ Écoutez profondément.  
    ➡️ Traduisez avec sagesse.  
    ➡️ Livrez avec conscience, avec but, avec cœur. 💖
    """)

voice_to_action_game()
