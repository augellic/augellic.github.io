#!/usr/bin/env sh
# Télécharge les 7 fichiers de polices (licence SIL OFL) dans static/fonts/
# pour qu'elles soient servies par le site lui-même (aucun appel à Google : RGPD).
# À lancer une fois depuis la racine du dépôt : sh outils/telecharger-polices.sh
set -e
mkdir -p static/fonts
B="https://cdn.jsdelivr.net/npm/@fontsource"
for f in \
  "barlow-semi-condensed/files/barlow-semi-condensed-latin-500-normal.woff2" \
  "barlow-semi-condensed/files/barlow-semi-condensed-latin-600-normal.woff2" \
  "source-sans-3/files/source-sans-3-latin-400-normal.woff2" \
  "source-sans-3/files/source-sans-3-latin-400-italic.woff2" \
  "source-sans-3/files/source-sans-3-latin-600-normal.woff2" \
  "ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2" \
  "ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff2"
do
  curl -fsSL -o "static/fonts/$(basename "$f")" "$B/$f"
  echo "ok  $(basename "$f")"
done
