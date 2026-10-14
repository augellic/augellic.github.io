---
title: "ModuBox — caissons modulaires sur mesure"
resume: "Caissons en MDF 18 mm conçus sous Siemens NX pour des espaces contraints : niches, sous-pentes, dessus d'électroménager. Contreventement intégré, plan de débit optimisé, premier meuble fabriqué."
date: 2026-09-01
weight: 10
vignetteAlt: "rendu NX ou photo du premier caisson installé"
cartouche:
  contexte: "Projet personnel"
  periode: "2026"
  role: "Conception, calcul, fabrication et essais (seul)"
  outils: ["Siemens NX", "Plan de débit", "Python"]
  materiau: "MDF 18 mm"
  statut: "1 meuble fabriqué — autres modules à l'étude"
  revision: "A"
---

## Problème

Les meubles standard laissent des volumes perdus dans les logements : niches entre deux murs, sous-pentes, espace au-dessus d'un réfrigérateur ou d'un lave-linge. Ces volumes ont des cotes irrégulières et des accès difficiles.

ModuBox est un système de caissons en MDF 18 mm dimensionnés au cas par cas, mais construits à partir des mêmes principes : mêmes assemblages, même contreventement, même logique de débit. J'ai conçu et fabriqué le premier meuble pour mon propre logement. Il n'y a pas de client : le cahier des charges reflète mes propres contraintes, que j'ai cherché à chiffrer.

{{< fig src="situation.jpg" n="1" legende="L'emplacement avant aménagement, avec ses cotes relevées." ratio="4/3" >}}

## Cahier des charges

{{< afaire >}}
Remplacer ce tableau par les exigences de votre cahier des charges v1 (Markdown). Gardez trois colonnes : exigence chiffrée, critère de vérification, résultat. Une exigence sans critère vérifiable va dans « Souhaits ».
{{< /afaire >}}

| Exigence | Critère de vérification | Résultat |
|---|---|---|
| S'insérer dans une niche de L × P × H mm, jeu ≤ … mm | Mesure après pose | … |
| Supporter … kg par tablette | Flèche ≤ L/250 sous charge (calcul + essai) | … |
| Rester stable sans fixation murale / avec fixation | Essai de poussée horizontale | … |
| Fabricable avec … (scie, perceuse…) | Gamme de fabrication réalisée | … |
| Matière : ≤ … panneaux de 2 800 × 2 070 mm | Plan de débit, taux de chute | … |
| Coût matière ≤ … € | Relevé des achats | … |

## Conception

Trois choix structurent le projet.

**Le contreventement intégré.** Un caisson rectangulaire assemblé par ses seuls côtés se déforme en parallélogramme sous un effort horizontal. Plutôt qu'une équerre rapportée, le contreventement est assuré par … (fond rainuré, traverse, panneau collé : à préciser). Il ne demande aucune pièce supplémentaire.

**Un module paramétré.** Le caisson est piloté dans NX par quelques expressions (largeur, hauteur, profondeur, nombre de tablettes). Un nouveau module se dérive d'une mise à jour des paramètres, sans remodéliser.

**Des assemblages adaptés à l'outillage disponible.**

{{< afaire >}}Préciser le type d'assemblage (vis, tourillons, excentriques…) et pourquoi ce choix plutôt qu'un autre.{{< /afaire >}}

{{< fig src="eclate.png" n="2" legende="Vue éclatée du caisson ; les repères correspondent à la nomenclature." ratio="4/3" >}}

### Nomenclature

| Rep. | Désignation | Matière | Dimensions (mm) | Qté |
|---|---|---|---|---|
| 1 | Côté | MDF 18 | … × … | 2 |
| 2 | Dessus / dessous | MDF 18 | … × … | 2 |
| 3 | Tablette | MDF 18 | … × … | … |
| 4 | Fond / contreventement | … | … × … | 1 |
| 5 | Vis d'assemblage | Acier | … | … |

## Calculs

### Flèche d'une tablette

La tablette est modélisée comme une poutre sur deux appuis simples, sous charge uniformément répartie. La section est rectangulaire pleine, de profondeur \(b\) et d'épaisseur \(h\) :

$$
I = \frac{b\,h^3}{12} \qquad f = \frac{5\,q\,L^4}{384\,E\,I}
$$

{{< afaire >}}
Les valeurs ci-dessous sont des **hypothèses d'exemple**. Remplacez-les par la portée réelle, la charge visée et le module \(E\) de la fiche technique de votre panneau. Le script `outils/fleche.py` refait le calcul en une ligne.
{{< /afaire >}}

| Donnée | Valeur | Origine |
|---|---|---|
| Portée \(L\) | 800 mm | Hypothèse |
| Profondeur \(b\) × épaisseur \(h\) | 300 × 18 mm | Hypothèse |
| Module \(E\) (flexion) | 3 000 MPa | Hypothèse, à remplacer par la fiche technique |
| Charge | 50 kg répartis, soit \(q\) = 0,613 N/mm | Hypothèse |
| Critère | \(f \le L/250\) = 3,2 mm | Choix de conception |

Avec ces valeurs, \(I\) = 145 800 mm⁴ et la flèche instantanée vaut **7,5 mm**, plus du double du critère. La charge admissible au critère est d'environ 21 kg.

Le MDF flue sous charge permanente. L'Eurocode 5 (EN 1995-1-1) en tient compte par un coefficient \(k_{def}\) appliqué à la flèche : \(f_{fin} = f_{inst}\,(1 + k_{def})\). Pour le MDF, ce coefficient est élevé (à vérifier dans la norme). Pour une étagère chargée en permanence, c'est souvent le fluage, et non la résistance, qui dimensionne.

**Conséquence de conception.**

{{< afaire >}}Indiquer la décision prise (portée réduite, raidisseur sous la tablette, tablette doublée…) et le recalcul correspondant.{{< /afaire >}}

### Plan de débit

{{< afaire >}}
Donner le nombre de panneaux, le taux de chute avant et après optimisation, et l'outil utilisé. Ajouter l'image du plan de débit.
{{< /afaire >}}

{{< fig src="plan-de-debit.png" n="3" legende="Plan de débit optimisé sur panneau standard." ratio="3/2" >}}

## Fabrication

{{< afaire >}}
Décrire la gamme en étapes courtes : débit, chants, perçages, assemblage, pose. Ajouter 3 à 5 photos annotées, dont au moins une difficulté rencontrée et sa correction.
{{< /afaire >}}

{{< fig src="fabrication-assemblage.jpg" n="4" legende="Assemblage du caisson, contreventement en place." ratio="4/3" >}}

## Essais et résultats

### Essai de charge sur tablette

Protocole : charges connues (packs d'eau, sacs de 10 kg) posées par paliers et réparties sur la tablette. Flèche mesurée au milieu de la portée par rapport à une règle de référence. Mesure de la flèche résiduelle après déchargement, puis de la flèche à 24 h sous charge maintenue.

| Charge (kg) | Flèche calculée (mm) | Flèche mesurée (mm) |
|---|---|---|
| 10 | 1,5 | … |
| 20 | 3,0 | … |
| 30 | 4,5 | … |
| 40 | 6,0 | … |
| Résiduelle après déchargement | — | … |
| 24 h sous … kg | — | … |

{{< afaire >}}
Les flèches calculées ci-dessus découlent des hypothèses d'exemple. Une fois l'essai fait : tracer la courbe charge-flèche, en déduire le module \(E\) apparent, et commenter l'écart avec le calcul.
{{< /afaire >}}

### Essai de contreventement

{{< afaire >}}
Effort horizontal en haut du caisson (peson ou masse via poulie), déplacement mesuré en tête, avec et sans contreventement. Un tableau de deux lignes suffit.
{{< /afaire >}}

## Limites et leçons

{{< afaire >}}
Trois à cinq points concrets, par exemple : ce que le calcul a révélé, ce que l'essai a contredit, ce que vous changeriez au module suivant, ce qui n'a pas été vérifié (tenue à l'humidité, démontage répété…).
{{< /afaire >}}

## Fichiers

{{< fichiers >}}
modubox-cahier-des-charges.pdf | Cahier des charges v1
modubox-plan-ensemble.pdf | Mise en plan cotée, ensemble et nomenclature
modubox-plan-de-debit.pdf | Plan de débit
modubox-note-de-calcul.pdf | Note de calcul (flèche, fluage)
modubox-caisson.step | Modèle 3D du caisson (STEP, licence CC BY-NC 4.0)
{{< /fichiers >}}
