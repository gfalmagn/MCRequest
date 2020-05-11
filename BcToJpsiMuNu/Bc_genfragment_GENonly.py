import FWCore.ParameterSet.Config as cms

from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(5020.),
                         ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_Bc_2014.pdl'),
            list_forced_decays = cms.vstring('MyBc+',
                                             'MyBc-'),
            operates_on_particles = cms.vint32(541,-541,543,-543),
            use_default_decay = cms.untracked.bool(False),
            user_decay_embedded = cms.vstring(
"""
Particle B_c*+     6.34000 0.00000
Particle B_c+      6.27490 0.00000

Alias      MyBc+       B_c+
Alias      MyBc-       B_c-
ChargeConj MyBc-       MyBc+

Alias MyJpsi J/psi
ChargeConj MyJpsi MyJpsi

Decay B_c*+
  1.0 MyBc+  gamma   VSP_PWAVE;
Enddecay
CDecay B_c*-

Decay MyBc+
 1.000    MyJpsi      mu+   nu_mu        PHOTOS BC_VMN 2;
Enddecay
CDecay MyBc-

Decay MyJpsi
 1.0000  mu+        mu-                    PHOTOS VLL ;
Enddecay

End
"""
)
            ),
        parameterSets = cms.vstring('EvtGen130')
        ),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring('543:m0 = 6.34000',
                                        '543:tau0 = 0.',
                                        '543:mayDecay = off',
                                        #
                                        '541:m0 = 6.2749',
                                        '541:tau0 = 0.151995',
                                        '541:mayDecay = off',
                                        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
        )
                         )

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

ProductionFilterSequence = cms.Sequence(generator)
