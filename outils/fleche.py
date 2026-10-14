#!/usr/bin/env python3
"""Flèche d'une tablette en appui simple sous charge uniformément répartie.

Modèle : poutre sur deux appuis simples, section rectangulaire pleine.
    I = b h^3 / 12
    f = 5 q L^4 / (384 E I)
Avec fluage (charge permanente) : f_fin = f_inst * (1 + k_def)

Les valeurs par défaut sont des HYPOTHÈSES d'exemple : remplacez-les par
les dimensions réelles et le module E de la fiche technique du panneau.

Usage : python3 fleche.py --L 800 --b 300 --h 18 --E 3000 --masse 50 --kdef 2.25
"""
import argparse

G = 9.81  # m/s²


def fleche(L, b, h, E, masse_kg):
    """Retourne (I [mm^4], q [N/mm], f [mm]) ; unités : mm, MPa, kg."""
    I = b * h**3 / 12
    q = masse_kg * G / L
    f = 5 * q * L**4 / (384 * E * I)
    return I, q, f


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--L", type=float, default=800, help="portée entre appuis [mm]")
    p.add_argument("--b", type=float, default=300, help="profondeur de la tablette [mm]")
    p.add_argument("--h", type=float, default=18, help="épaisseur [mm]")
    p.add_argument("--E", type=float, default=3000, help="module d'élasticité en flexion [MPa]")
    p.add_argument("--masse", type=float, default=50, help="charge répartie totale [kg]")
    p.add_argument("--kdef", type=float, default=None, help="coefficient de fluage (Eurocode 5, à vérifier)")
    p.add_argument("--critere", type=float, default=250, help="critère de flèche L/n, donner n")
    a = p.parse_args()

    I, q, f = fleche(a.L, a.b, a.h, a.E, a.masse)
    lim = a.L / a.critere
    print(f"I          = {I:,.0f} mm^4".replace(",", " "))
    print(f"q          = {q:.3f} N/mm")
    print(f"f inst.    = {f:.2f} mm   (limite L/{a.critere:.0f} = {lim:.2f} mm) -> {'OK' if f <= lim else 'NON CONFORME'}")
    if a.kdef is not None:
        ff = f * (1 + a.kdef)
        print(f"f finale   = {ff:.2f} mm   avec k_def = {a.kdef}")
    # Charge admissible au critère, en flèche instantanée
    m_adm = a.masse * lim / f
    print(f"Charge admissible au critère (instantané) : {m_adm:.1f} kg")


if __name__ == "__main__":
    main()
