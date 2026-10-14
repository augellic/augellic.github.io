# Portfolio — Cristopher Augelli

Site statique [Hugo](https://gohugo.io) (version 0.147.9), publié gratuitement sur GitHub Pages.
Le contenu est en Markdown dans `content/`. Aucun domaine n'est nécessaire pour commencer :
le site vit à `https://augellic.github.io/` jusqu'à l'achat éventuel d'un domaine.

## Outils (Windows)

| Outil | Rôle | Installation |
|---|---|---|
| Git for Windows | Historique des versions, envoi vers GitHub (fournit Git Bash) | `winget install Git.Git` |
| GitHub CLI | Connexion à GitHub depuis le terminal | `winget install GitHub.cli` puis `gh auth login` |
| Hugo extended | Compile le site, aperçu local | `winget install Hugo.Hugo.Extended` |
| Python 3 | Scripts de calcul (`outils/fleche.py`) | `winget install Python.Python.3.12` |
| VS Code | Édition des fichiers, panneau Git intégré | déjà installé |

Emplacement du dépôt : `C:\Users\<vous>\Projets\augellic.github.io`, hors de tout dossier
synchronisé (OneDrive, Sync…). GitHub sert de sauvegarde. Les fichiers natifs NX et les photos
brutes restent dans un dossier à part ; seuls les exports (PNG, PDF, STEP) entrent dans le dépôt.

Cycle de travail :

```
hugo server          # aperçu sur http://localhost:1313 pendant que vous écrivez
git add -A
git commit -m "ModuBox : ajout du plan de débit"
git push             # le site en ligne se met à jour en 1 à 2 minutes
```

## Arborescence

```
config/_default/hugo.toml   réglages : nom, e-mail, liens, brouillon, noindex
config/preview/hugo.toml    variante pour un aperçu hors domaine
content/_index.md           accueil (accroche + cartouche profil)
content/projets/<projet>/   une fiche = un dossier : index.md + images + PDF + STEP
content/parcours.md         formation, expérience, compétences, langues
content/cv/                 index.md + les PDF du CV et du dossier
content/contact.md, content/mentions-legales.md
layouts/                    gabarits HTML (à ne modifier que pour la mise en forme)
assets/css/site.css         styles (couleurs et polices en tête de fichier)
outils/                     fleche.py, telecharger-polices.sh, cv-entete.tex
```

## Écrire une fiche

- Nouvelle fiche : `hugo new content projets/mon-projet/index.md` (trame déjà remplie).
- Images, PDF et STEP se déposent **dans le dossier de la fiche**.
- `{{< fig src="eclate.png" n="2" legende="Vue éclatée" >}}` : figure numérotée. Tant que le
  fichier manque, un cadre vide décrit l'image attendue.
- `{{< fichiers >}}nom.pdf | Description{{< /fichiers >}}` : un fichier absent s'affiche « à venir ».
- `{{< afaire >}}…{{< /afaire >}}` : bloc jaune « À compléter », masqué quand `brouillon = false`.
- Formules : `\( f \le L/250 \)` dans le texte, `$$ … $$` en bloc (LaTeX, converti en MathML).
- Vignette de carte : un fichier `vignette.jpg` (ou .png/.webp) dans le dossier de la fiche.

## Plan d'action

Chaque étape se termine par un livrable visible. Comptez 6 à 8 h par semaine.

### Étape 0 — Aperçu sur votre ordinateur (aujourd'hui, 30 min)

1. Installer Hugo **extended** 0.147.9 (Windows : `winget install Hugo.Hugo.Extended` ;
   macOS : `brew install hugo` ; Linux : paquet .deb des releases GitHub).
2. Dans ce dossier : `sh outils/telecharger-polices.sh` (polices hébergées sur le site, RGPD).
3. `hugo server` puis ouvrir http://localhost:1313 : chaque enregistrement d'un fichier
   recharge la page.

**Livrable :** le site tourne en local.

### Étape 1 — Site en ligne sans domaine (jour 1-2, 1 h)

1. Créer un compte GitHub au nom de `prenom-nom` (il apparaîtra dans l'adresse).
2. Créer un dépôt public nommé exactement `augellic.github.io`, y pousser ce dossier.
3. Settings > Pages > Source : **GitHub Actions**. Le workflow `.github/workflows/hugo.yml`
   compile et publie à chaque push.
4. Remplacer `augellic`, `email` et `linkedin` dans `config/_default/hugo.toml`.
   Pour l'e-mail, une adresse sobre de type prénom.nom suffit tant qu'il n'y a pas de domaine.

**Livrable :** URL publique, avec bandeau « version de travail » et `noindex` (non référencé).

### Étape 2 — ModuBox v1 (semaine 1)

1. Remplacer le tableau de cahier des charges par votre CdC v1.
2. Exporter de NX : mise en plan d'ensemble (PDF), vue éclatée et vignette (PNG),
   nomenclature, plan de débit. Les déposer dans `content/projets/modubox/`.
3. Envoyer les demandes d'accord à RD2 Innovate et au Dr Bravo Bénard (UDIATEM).

**Livrable :** fiche ModuBox avec plans, nomenclature et débit ; demandes envoyées.

### Étape 3 — Preuves d'ingénierie (semaine 2)

1. Refaire le calcul de flèche avec vos vraies valeurs : `python3 outils/fleche.py --L … --E …`.
2. Essai de charge par paliers, essai de contreventement, photos annotées.
3. Ajouter le lien et le QR code au CV LaTeX (`outils/cv-entete.tex`).

**Livrable :** ModuBox complet (calcul + essai + leçons) ; CV mis à jour. Vous pouvez candidater.

### Étape 4 — Autres fiches et dossier PDF (semaine 3)

1. Fiches RD2 et UDIATEM selon les réponses reçues ; page Parcours.
2. Dossier de réalisations PDF (4 pages, LaTeX) dans `content/cv/`.

**Livrable :** site complet, PDF prêt à joindre aux candidatures.

### Étape 5 — Lancement (semaine 4)

1. Relecture par un tiers, test sur téléphone.
2. Dans `hugo.toml` : `brouillon = false`, `noindex = false`, date `miseAJour`.
3. Google Search Console : déclarer le site, soumettre `sitemap.xml`.
4. LinkedIn (coordonnées, Sélection, post) et README de profil GitHub.
5. Optionnel : domaine `.fr`. Ajouter un fichier `static/CNAME` contenant le domaine, changer
   `baseURL`, déclarer le domaine dans Settings > Pages, puis l'e-mail (Cloudflare Email Routing).

**Livrable :** version 1.0 publique et référencée.

## Avant chaque publication

- Pas de cote, plan ou donnée d'entreprise sans accord écrit.
- Chaque chiffre est marqué : hypothèse, calcul ou mesure.
- `hugo` compile sans erreur ; vérifier le rendu sur téléphone.
