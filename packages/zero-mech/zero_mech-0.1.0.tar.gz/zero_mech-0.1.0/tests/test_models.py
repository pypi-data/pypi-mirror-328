import zero_mech


def test_model():
    material = zero_mech.material.NeoHookean()
    mech_model = zero_mech.Model(
        material=material,
        compressibility=zero_mech.compressibility.Compressible1(),
        active=zero_mech.active.Passive(),
    )
    print(mech_model.variables())
    breakpoint()
