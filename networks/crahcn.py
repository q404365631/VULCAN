"""CRAHCN(-O) reduced chemical reaction network definitions for VULCAN."""

CRAHCN_SPECIES = [
    "C", "CH", "CH2", "CH3", "CH4", "C2H", "C2H2", "C2H3", "C2H4", "C2H5", "C2H6",
    "C3H2", "C3H3", "C3H4", "C3H5", "C3H6", "C3H7", "C3H8",
    "C4H2", "C4H4", "C4H6", "C4H8",
    "H", "H2", "O", "O2", "OH", "H2O", "CO", "CO2", "N", "N2", "NH", "NH2", "NH3",
]

CRAHCN_O_SPECIES = CRAHCN_SPECIES + [
    "O3", "HO2", "H2O2", "NO", "NO2", "N2O", "CN", "HCN", "HNC", "HCO", "H2CO", "CH2O",
    "CH3OH", "C2H5OH",
]

CRAHCN_DEFAULT_TEMP = 150  # K
CRAHCN_DEFAULT_DENSITY = 1e4  # cm^-3
CRAHCN_DEFAULT_ZETA = 1.0  # cosmic ray ionization rate

NETWORK_NAME = "CRAHCN"
NETWORK_VERSION = "1.0"
NETWORK_REFERENCE = "Pearce et al. (reduced C/H/O/N network)"

def get_network_params():
    return {
        "name": NETWORK_NAME,
        "version": NETWORK_VERSION,
        "species": sorted(CRAHCN_SPECIES),
        "default_temp": CRAHCN_DEFAULT_TEMP,
        "default_density": CRAHCN_DEFAULT_DENSITY,
        "default_zeta": CRAHCN_DEFAULT_ZETA,
        "reference": NETWORK_REFERENCE,
    }

def get_oxygen_extended():
    return {
        "name": f"{NETWORK_NAME}-O",
        "species": sorted(CRAHCN_O_SPECIES),
        "extends": NETWORK_NAME,
        "extra_species": [s for s in CRAHCN_O_SPECIES if s not in CRAHCN_SPECIES],
    }
