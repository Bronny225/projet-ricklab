import os
import time
import numpy as np
import sounddevice as sd

from resemblyzer import VoiceEncoder, preprocess_wav


# ============================================================
# CONFIGURATION
# ============================================================

MIC_DEVICE = 1

MIC_SAMPLE_RATE = 48000

DUREE_ECOUTE = 5

VOIX_REFERENCE = "/home/pi/ricklab/voix_reference.wav"

SEUIL_RECONNAISSANCE = 0.75

MAX_TENTATIVES = 3


# ============================================================
# INITIALISATION
# ============================================================

print()
print("=" * 60)
print("       AUTHENTIFICATION VOCALE")
print("=" * 60)
print()


if not os.path.exists(VOIX_REFERENCE):

    print("ERREUR : voix de référence introuvable.")
    print()
    print("Fichier attendu :")
    print(VOIX_REFERENCE)

    exit()


print("Chargement de la voix de référence...")


encoder = VoiceEncoder()


voix_reference = preprocess_wav(
    VOIX_REFERENCE
)


empreinte_reference = encoder.embed_utterance(
    voix_reference
)


print("Voix de référence chargée.")
print()


# ============================================================
# AUTHENTIFICATION
# ============================================================

def authentification_vocale():

    print()
    print("=" * 60)
    print("AUTHENTIFICATION VOCALE")
    print("=" * 60)
    print()

    for tentative in range(
        1,
        MAX_TENTATIVES + 1
    ):

        print(
            f"TENTATIVE {tentative}/{MAX_TENTATIVES}"
        )

        print()
        print(
            "Parlez maintenant..."
        )

        try:

            audio = sd.rec(
                int(
                    DUREE_ECOUTE
                    * MIC_SAMPLE_RATE
                ),
                samplerate=MIC_SAMPLE_RATE,
                channels=1,
                dtype="float32",
                device=MIC_DEVICE
            )

            sd.wait()

        except Exception as erreur:

            print()
            print(
                "ERREUR MICRO :",
                erreur
            )

            return False


        # ----------------------------------------------------
        # PREPARATION DE LA VOIX
        # ----------------------------------------------------

        audio = audio.flatten()

        # Resemblyzer travaille avec des fichiers WAV
        # ou des signaux audio normalisés.

        try:

            voix_test = encoder.embed_utterance(
                audio
            )

        except Exception as erreur:

            print()
            print(
                "ERREUR ANALYSE VOCALE :",
                erreur
            )

            continue


        # ----------------------------------------------------
        # COMPARAISON DES VOIX
        # ----------------------------------------------------

        similarite = np.dot(
            empreinte_reference,
            voix_test
        ) / (
            np.linalg.norm(
                empreinte_reference
            )
            *
            np.linalg.norm(
                voix_test
            )
        )


        print()
        print(
            f"Similarité vocale : {similarite:.3f}"
        )


        # ----------------------------------------------------
        # DECISION
        # ----------------------------------------------------

        if similarite >= SEUIL_RECONNAISSANCE:

            print()
            print(
                "========================================"
            )

            print(
                "ACCÈS AUTORISÉ"
            )

            print(
                "Voix reconnue."
            )

            print(
                "========================================"
            )

            return True


        print()
        print(
            "ACCÈS REFUSÉ"
        )

        print()


        if tentative < MAX_TENTATIVES:

            time.sleep(1)


    # ========================================================
    # TROIS REFUS
    # ========================================================

    print()
    print(
        "========================================"
    )

    print(
        "INTRUSION DÉTECTÉE"
    )

    print(
        "Authentification vocale échouée."
    )

    print(
        "========================================"
    )

    return False


# ============================================================
# LANCEMENT
# ============================================================

resultat = authentification_vocale()


if resultat:

    print()
    print(
        "SYSTÈME DÉVERROUILLÉ."
    )

else:

    print()
    print(
        "SYSTÈME VERROUILLÉ."
    )
