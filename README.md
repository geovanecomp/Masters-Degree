# Masters-Degree
This repo contains my ongoing code for my Masters in Computational Modeling at Rio de Janeiro State University.

## Here is the project summary (I still need to prepare a proper Readme, sorry 😇):

The description and reproduction of physical phenomena are a common challenge in the field of computational modeling. In the context of high-energy calorimetry, the particle energy produced from collisions is absorbed and sampled in the form of a digitized signal.

In a high event-rate and luminosity conditions, the signal pile-up effect may arise due to the high occupancy of the detector’s readout channels, causing the distortion of the expected signal. In this context, this work evaluates the performance of the method known as Matched Filter, by applying it in two distinct approaches called Deterministic Matched Filter and Stochastic Matched Filter.

These approaches will be compared to the current method applied in the ATLAS Tile Calorimeter (TileCal), known as Optimal Filter. For the efficiency analysis, a computational environment was created to contain simulated data considering different signal pile-up conditions in the TileCal. Furthermore, a hybrid environment was also created, consisting of signals whose amplitudes are previously known and added to different conditions of pile-up noise. For both analyses, different signal-noise ratio conditions were considered.

The results show that the Stochastic Matched Filter presented high accuracy in estimating the amplitude, becoming an alternative for the TileCal energy estimation task.
