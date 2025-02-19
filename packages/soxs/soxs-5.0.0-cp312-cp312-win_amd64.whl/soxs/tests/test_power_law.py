import os
import shutil
import tempfile

from numpy.random import RandomState

from soxs.events import write_spectrum
from soxs.instrument import instrument_simulator
from soxs.instrument_registry import make_simple_instrument
from soxs.simput import SimputCatalog, SimputPhotonList
from soxs.spatial import PointSourceModel
from soxs.spectra import Spectrum
from soxs.tests.utils import file_answer_testing, spectrum_answer_testing

make_simple_instrument("lynx_hdxi", "new_hdxi", 20.0, 1024)

prng = RandomState(69)


def test_power_law(answer_store):
    plaw_fit(1.1, answer_store)
    plaw_fit(0.8, answer_store)
    plaw_fit(1.0, answer_store)


def plaw_fit(alpha_sim, answer_store):
    tmpdir = tempfile.mkdtemp()
    curdir = os.getcwd()
    os.chdir(tmpdir)

    nH_sim = 0.02
    norm_sim = 1.0e-4
    redshift = 0.01

    exp_time = (50.0, "ks")
    area = 40000.0
    inst_name = "new_hdxi"

    spec = Spectrum.from_powerlaw(alpha_sim, redshift, norm_sim, 0.1, 10.0, 20000)
    spec.apply_foreground_absorption(nH_sim, model="tbabs")

    spectrum_answer_testing(spec, f"power_law_{alpha_sim}.h5", answer_store)

    pt_src_pos = PointSourceModel(30.0, 45.0)
    pt_src = SimputPhotonList.from_models(
        "plaw_model", spec, pt_src_pos, exp_time, area, prng=prng
    )
    SimputCatalog.from_source("plaw_model_simput.fits", pt_src, overwrite=True)

    instrument_simulator(
        "plaw_model_simput.fits",
        f"plaw_model_{alpha_sim}_evt.fits",
        exp_time,
        inst_name,
        [30.0, 45.0],
        instr_bkgnd=False,
        ptsrc_bkgnd=False,
        foreground=False,
        prng=prng,
    )

    write_spectrum(
        f"plaw_model_{alpha_sim}_evt.fits",
        f"plaw_model_{alpha_sim}_evt.pha",
        overwrite=True,
    )

    file_answer_testing(
        "EVENTS",
        f"plaw_model_{alpha_sim}_evt.fits",
        answer_store,
    )
    file_answer_testing(
        "SPECTRUM",
        f"plaw_model_{alpha_sim}_evt.pha",
        answer_store,
    )

    os.chdir(curdir)
    shutil.rmtree(tmpdir)
